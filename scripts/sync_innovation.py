#!/usr/bin/env python3
"""Nortropic Innovation Intake v1 — deterministic issue → Project synchronizer.

Reads a GitHub issue (from the Actions event payload), validates the v1 intake
contract in the issue body, and synchronizes the issue into the existing
GitHub Project "Nortropic Innovation":

    Status          = INBOX
    Area            = <parsed Area>
    Source / Context = <parsed Source / Context>
    Why it matters  = <parsed Why it matters>

Guarantees:
  * fail closed: no Project mutation if validation fails;
  * idempotent: re-running for the same issue updates the existing Project
    item, never creates a duplicate;
  * never touches unrelated Project items and never alters the Project schema;
  * fails visibly if expected fields/options are missing or have changed.

Only Python stdlib is used. Authentication comes from the PROJECT_TOKEN
environment variable (a narrowly scoped credential able to read intake issues
and write the target org Project). The token is never printed.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

GRAPHQL_ENDPOINT = "https://api.github.com/graphql"
SCHEMA_MARKER_RE = re.compile(
    r"<!--\s*nortropic-innovation-intake:([A-Za-z0-9.\-]+)\s*-->"
)
H2_RE = re.compile(r"^ {0,3}##(?!#)\s*(.+?)\s*#*\s*$")

CONFIG_PATH = Path(__file__).resolve().parent / "intake_config.json"


class IntakeValidationError(Exception):
    """Raised when the issue body does not satisfy the v1 intake contract."""

    def __init__(self, problems: list[str]):
        self.problems = problems
        super().__init__("; ".join(problems))


class ProjectContractError(Exception):
    """Raised when the live Project does not match the expected contract."""


@dataclass(frozen=True)
class IntakeRecord:
    area: str
    source_context: str
    why_it_matters: str


def load_config(path: Path = CONFIG_PATH) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------------------
# Parsing / validation
# ---------------------------------------------------------------------------

def _normalize_key(text: str) -> str:
    """Normalize a heading or Area value for tolerant-but-strict matching:
    collapse whitespace runs, normalize spacing around '/', casefold."""
    text = re.sub(r"\s+", " ", text.strip())
    text = re.sub(r"\s*/\s*", " / ", text)
    return text.casefold()


def _normalize_text_value(text: str) -> str:
    """Collapse all whitespace (including newlines) to single spaces."""
    return re.sub(r"\s+", " ", text.strip())


def parse_intake_body(body: str | None, config: dict) -> IntakeRecord:
    """Parse and validate an intake issue body against the v1 contract.

    Raises IntakeValidationError listing every problem found. Never guesses:
    unknown Area values, unknown sections, duplicate sections, and missing
    required sections are all hard failures.
    """
    problems: list[str] = []
    body = (body or "").replace("\r\n", "\n").replace("\r", "\n")

    expected_version = config["schema_version"]
    markers = SCHEMA_MARKER_RE.findall(body)
    if not markers:
        raise IntakeValidationError(
            [
                "missing schema marker: the issue body must contain "
                f"'<!-- nortropic-innovation-intake:{expected_version} -->'"
            ]
        )
    if len(markers) > 1:
        problems.append("multiple schema markers found; exactly one is required")
    if markers[0] != expected_version:
        raise IntakeValidationError(
            [
                f"unsupported schema version '{markers[0]}': this synchronizer "
                f"only accepts '{expected_version}'"
            ]
        )

    known_sections = {
        "area": "Area",
        "source / context": "Source / Context",
        "why it matters": "Why it matters",
    }

    sections: dict[str, str] = {}
    current: str | None = None
    buffers: dict[str, list[str]] = {}
    for line in body.split("\n"):
        m = H2_RE.match(line)
        if m:
            key = _normalize_key(m.group(1))
            if key not in known_sections:
                problems.append(
                    f"unknown section heading '## {m.group(1)}': allowed headings "
                    "are '## Area', '## Source / Context', '## Why it matters'"
                )
                current = None
                continue
            if key in buffers:
                problems.append(f"duplicate section '## {known_sections[key]}'")
                current = None
                continue
            buffers[key] = []
            current = key
        elif current is not None:
            buffers[current].append(line)

    for key, lines in buffers.items():
        sections[key] = "\n".join(lines).strip()

    # Area ------------------------------------------------------------------
    area: str | None = None
    if "area" not in sections:
        problems.append("missing required section '## Area'")
    else:
        raw = sections["area"]
        if not raw:
            problems.append("section '## Area' is empty")
        elif len(raw.splitlines()) > 1:
            problems.append(
                "section '## Area' must contain exactly one value on one line"
            )
        else:
            normalized = _normalize_key(raw)
            allowed = {_normalize_key(a): a for a in config["allowed_areas"]}
            if normalized in allowed:
                area = allowed[normalized]
            else:
                problems.append(
                    f"unknown Area '{raw.strip()}': allowed values are "
                    + ", ".join(config["allowed_areas"])
                )

    # Source / Context ------------------------------------------------------
    source_context: str | None = None
    if "source / context" not in sections:
        problems.append("missing required section '## Source / Context'")
    elif not sections["source / context"]:
        problems.append("section '## Source / Context' is empty")
    else:
        source_context = _normalize_text_value(sections["source / context"])

    # Why it matters --------------------------------------------------------
    why_it_matters: str | None = None
    if "why it matters" not in sections:
        problems.append("missing required section '## Why it matters'")
    elif not sections["why it matters"]:
        problems.append("section '## Why it matters' is empty")
    else:
        why_it_matters = _normalize_text_value(sections["why it matters"])

    if problems:
        raise IntakeValidationError(problems)

    assert area is not None and source_context is not None and why_it_matters is not None
    return IntakeRecord(area, source_context, why_it_matters)


# ---------------------------------------------------------------------------
# GraphQL client
# ---------------------------------------------------------------------------

class GraphQLClient:
    """Minimal GitHub GraphQL client (stdlib only). User content is always
    passed via GraphQL variables, never interpolated into query text."""

    def __init__(self, token: str):
        self._token = token

    def execute(self, query: str, variables: dict) -> dict:
        payload = json.dumps({"query": query, "variables": variables}).encode()
        req = urllib.request.Request(
            GRAPHQL_ENDPOINT,
            data=payload,
            headers={
                "Authorization": f"Bearer {self._token}",
                "Content-Type": "application/json",
                "User-Agent": "nortropic-innovation-intake/1.0",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode())
        except urllib.error.HTTPError as exc:
            raise ProjectContractError(
                f"GitHub GraphQL request failed with HTTP {exc.code}. "
                "Check that the PROJECT_TOKEN secret is valid and has "
                "organization Projects read/write plus intake-repo Issues read."
            ) from exc
        if data.get("errors"):
            messages = "; ".join(
                e.get("message", "unknown error") for e in data["errors"]
            )
            raise ProjectContractError(f"GitHub GraphQL error: {messages}")
        return data["data"]


# ---------------------------------------------------------------------------
# Project resolution (by name, fail closed on drift)
# ---------------------------------------------------------------------------

PROJECT_BY_NUMBER_QUERY = """
query($owner: String!, $number: Int!) {
  organization(login: $owner) {
    projectV2(number: $number) { id number title closed }
  }
}
"""

PROJECTS_BY_TITLE_QUERY = """
query($owner: String!) {
  organization(login: $owner) {
    projectsV2(first: 50) {
      nodes { id number title closed }
    }
  }
}
"""

FIELDS_QUERY = """
query($projectId: ID!) {
  node(id: $projectId) {
    ... on ProjectV2 {
      fields(first: 50) {
        nodes {
          ... on ProjectV2FieldCommon { id name dataType }
          ... on ProjectV2SingleSelectField {
            id name dataType
            options { id name }
          }
        }
      }
    }
  }
}
"""

ISSUE_PROJECT_ITEMS_QUERY = """
query($issueId: ID!) {
  node(id: $issueId) {
    ... on Issue {
      projectItems(first: 50, includeArchived: true) {
        nodes { id project { id } }
      }
    }
  }
}
"""

ADD_ITEM_MUTATION = """
mutation($projectId: ID!, $contentId: ID!) {
  addProjectV2ItemById(input: {projectId: $projectId, contentId: $contentId}) {
    item { id }
  }
}
"""

UPDATE_TEXT_MUTATION = """
mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $text: String!) {
  updateProjectV2ItemFieldValue(
    input: {projectId: $projectId, itemId: $itemId, fieldId: $fieldId,
            value: {text: $text}}
  ) { projectV2Item { id } }
}
"""

UPDATE_SINGLE_SELECT_MUTATION = """
mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $optionId: String!) {
  updateProjectV2ItemFieldValue(
    input: {projectId: $projectId, itemId: $itemId, fieldId: $fieldId,
            value: {singleSelectOptionId: $optionId}}
  ) { projectV2Item { id } }
}
"""


def resolve_project(client: GraphQLClient, config: dict) -> dict:
    """Resolve the target Project by configured number, or by exact title.

    Returns {"id": ..., "number": ..., "title": ...}. Fails closed if the
    project cannot be found unambiguously or its title does not match.
    """
    owner = config["project_owner"]
    title = config["project_title"]
    number = config.get("project_number")

    if number is not None:
        data = client.execute(PROJECT_BY_NUMBER_QUERY, {"owner": owner, "number": number})
        project = (data.get("organization") or {}).get("projectV2")
        if project is None:
            raise ProjectContractError(
                f"Project number {number} not found under organization '{owner}'"
            )
        if project["title"] != title:
            raise ProjectContractError(
                f"Project number {number} is titled '{project['title']}', "
                f"expected '{title}' — refusing to touch it"
            )
        return project

    data = client.execute(PROJECTS_BY_TITLE_QUERY, {"owner": owner})
    nodes = ((data.get("organization") or {}).get("projectsV2") or {}).get("nodes") or []
    matches = [p for p in nodes if p and p["title"] == title and not p["closed"]]
    if len(matches) != 1:
        raise ProjectContractError(
            f"expected exactly one open project titled '{title}' under "
            f"'{owner}', found {len(matches)}"
        )
    return matches[0]


def resolve_fields(client: GraphQLClient, project_id: str, config: dict) -> dict:
    """Resolve the four contract fields by exact name and validate their
    types/options against the expected model. Fails closed on any drift."""
    data = client.execute(FIELDS_QUERY, {"projectId": project_id})
    nodes = ((data.get("node") or {}).get("fields") or {}).get("nodes") or []
    by_name = {n["name"]: n for n in nodes if n and "name" in n}

    problems: list[str] = []
    resolved: dict = {}

    def require(field_key: str, expected_type: str) -> dict | None:
        name = config["fields"][field_key]
        field = by_name.get(name)
        if field is None:
            problems.append(f"Project field '{name}' not found")
            return None
        if field.get("dataType") != expected_type:
            problems.append(
                f"Project field '{name}' has type {field.get('dataType')}, "
                f"expected {expected_type}"
            )
            return None
        return field

    status = require("status", "SINGLE_SELECT")
    if status is not None:
        options = {o["name"]: o["id"] for o in status.get("options", [])}
        missing = [s for s in config["expected_statuses"] if s not in options]
        if missing:
            problems.append(
                f"Status field is missing expected options: {', '.join(missing)}"
            )
        else:
            resolved["status"] = {
                "field_id": status["id"],
                "inbox_option_id": options[config["status_inbox"]],
            }

    area = require("area", "SINGLE_SELECT")
    if area is not None:
        options = {o["name"]: o["id"] for o in area.get("options", [])}
        missing = [a for a in config["allowed_areas"] if a not in options]
        if missing:
            problems.append(
                f"Area field is missing expected options: {', '.join(missing)}"
            )
        else:
            resolved["area"] = {"field_id": area["id"], "options": options}

    source = require("source_context", "TEXT")
    if source is not None:
        resolved["source_context"] = {"field_id": source["id"]}

    why = require("why_it_matters", "TEXT")
    if why is not None:
        resolved["why_it_matters"] = {"field_id": why["id"]}

    if problems:
        raise ProjectContractError(
            "the live Project no longer matches the expected contract — "
            "refusing to mutate anything: " + "; ".join(problems)
        )
    return resolved


def find_existing_item(client: GraphQLClient, issue_node_id: str, project_id: str) -> str | None:
    """Return the Project item id for this issue in the target project, if any.
    Looks only at this issue's own project items — never scans the Project."""
    data = client.execute(ISSUE_PROJECT_ITEMS_QUERY, {"issueId": issue_node_id})
    nodes = ((data.get("node") or {}).get("projectItems") or {}).get("nodes") or []
    for item in nodes:
        if item and (item.get("project") or {}).get("id") == project_id:
            return item["id"]
    return None


def sync_issue(client: GraphQLClient, config: dict, issue_node_id: str,
               issue_title: str, issue_body: str) -> dict:
    """Validate the intake body, then create-or-update this issue's Project
    item. Validation happens BEFORE any Project call. Returns a summary dict.
    """
    record = parse_intake_body(issue_body, config)  # raises before any mutation

    project = resolve_project(client, config)
    fields = resolve_fields(client, project["id"], config)

    item_id = find_existing_item(client, issue_node_id, project["id"])
    created = False
    if item_id is None:
        # addProjectV2ItemById is idempotent server-side: if a concurrent run
        # already added this issue, GitHub returns the existing item.
        data = client.execute(
            ADD_ITEM_MUTATION,
            {"projectId": project["id"], "contentId": issue_node_id},
        )
        item_id = data["addProjectV2ItemById"]["item"]["id"]
        created = True

    client.execute(UPDATE_SINGLE_SELECT_MUTATION, {
        "projectId": project["id"], "itemId": item_id,
        "fieldId": fields["status"]["field_id"],
        "optionId": fields["status"]["inbox_option_id"],
    })
    client.execute(UPDATE_SINGLE_SELECT_MUTATION, {
        "projectId": project["id"], "itemId": item_id,
        "fieldId": fields["area"]["field_id"],
        "optionId": fields["area"]["options"][record.area],
    })
    client.execute(UPDATE_TEXT_MUTATION, {
        "projectId": project["id"], "itemId": item_id,
        "fieldId": fields["source_context"]["field_id"],
        "text": record.source_context,
    })
    client.execute(UPDATE_TEXT_MUTATION, {
        "projectId": project["id"], "itemId": item_id,
        "fieldId": fields["why_it_matters"]["field_id"],
        "text": record.why_it_matters,
    })

    return {
        "project_number": project["number"],
        "item_id": item_id,
        "created": created,
        "title": issue_title,
        "status": config["status_inbox"],
        "area": record.area,
        "source_context": record.source_context,
        "why_it_matters": record.why_it_matters,
    }


# ---------------------------------------------------------------------------
# GitHub Actions entrypoint
# ---------------------------------------------------------------------------

def _error(title: str, message: str) -> None:
    # Single-line GitHub Actions error annotation (newlines are escaped).
    escaped = message.replace("%", "%25").replace("\n", "%0A")
    print(f"::error title={title}::{escaped}")


def main() -> int:
    token = os.environ.get("PROJECT_TOKEN")
    if not token:
        _error(
            "PROJECT_TOKEN missing",
            "The PROJECT_TOKEN repository secret is not configured. Create a "
            "fine-grained PAT (resource owner: the Project's organization; "
            "org permission Projects: read/write; this repo's Issues: read) "
            "and store it: gh secret set PROJECT_TOKEN",
        )
        return 1

    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        _error("no event payload", "GITHUB_EVENT_PATH is not set; this script "
               "must run inside a GitHub Actions issues workflow")
        return 1
    with open(event_path, encoding="utf-8") as fh:
        event = json.load(fh)

    issue = event.get("issue")
    if not issue or "pull_request" in issue:
        print("Not an issue event; nothing to do.")
        return 0

    config = load_config()
    client = GraphQLClient(token)
    try:
        summary = sync_issue(
            client, config,
            issue_node_id=issue["node_id"],
            issue_title=issue["title"],
            issue_body=issue.get("body") or "",
        )
    except IntakeValidationError as exc:
        _error(
            f"intake contract violation in issue #{issue.get('number')}",
            "The issue body does not satisfy the "
            f"nortropic-innovation-intake:{config['schema_version']} contract. "
            "No Project changes were made.\nProblems:\n- "
            + "\n- ".join(exc.problems)
            + "\nSee README.md → 'ChatGPT Intake Contract' for the exact format.",
        )
        return 1
    except ProjectContractError as exc:
        _error("project synchronization failed", str(exc))
        return 1

    action = "added to" if summary["created"] else "updated in"
    print(
        f"Issue #{issue.get('number')} ('{summary['title']}') {action} "
        f"project #{summary['project_number']} as item {summary['item_id']}\n"
        f"  Status = {summary['status']}\n"
        f"  Area = {summary['area']}\n"
        f"  Source / Context = {summary['source_context']}\n"
        f"  Why it matters = {summary['why_it_matters']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
