"""Unit tests for the Innovation Intake v1 parser and synchronizer.

Pure unit tests: no network, no live GitHub calls, no Project mutation.
Run with:  python3 -m unittest discover -s tests -v
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import sync_innovation as si  # noqa: E402

CONFIG = si.load_config()

VALID_BODY = """\
<!-- nortropic-innovation-intake:v1 -->

## Area
RESEARCH / SELF-IMPROVEMENT

## Source / Context
ChatGPT – Workflow och Orkestrering – 2026-08-15

## Why it matters
Could let Nortropic continuously discover and evaluate system improvements without interrupting active implementation.
"""


def make_body(area="OTHER", source="ChatGPT test", why="Because it matters."):
    return (
        "<!-- nortropic-innovation-intake:v1 -->\n\n"
        f"## Area\n{area}\n\n"
        f"## Source / Context\n{source}\n\n"
        f"## Why it matters\n{why}\n"
    )


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------

class TestParserValid(unittest.TestCase):
    def test_valid_v1_intake(self):
        record = si.parse_intake_body(VALID_BODY, CONFIG)
        self.assertEqual(record.area, "RESEARCH / SELF-IMPROVEMENT")
        self.assertEqual(
            record.source_context, "ChatGPT – Workflow och Orkestrering – 2026-08-15"
        )
        self.assertTrue(record.why_it_matters.startswith("Could let Nortropic"))

    def test_all_valid_area_values(self):
        for area in CONFIG["allowed_areas"]:
            with self.subTest(area=area):
                record = si.parse_intake_body(make_body(area=area), CONFIG)
                self.assertEqual(record.area, area)

    def test_area_case_and_slash_spacing_tolerated(self):
        for variant in ("factory/agents", "FACTORY /AGENTS", "  Factory / Agents  "):
            with self.subTest(variant=variant):
                record = si.parse_intake_body(make_body(area=variant), CONFIG)
                self.assertEqual(record.area, "FACTORY / AGENTS")

    def test_whitespace_tolerance(self):
        body = (
            "   <!--  nortropic-innovation-intake:v1   -->  \r\n\r\n"
            "##   Area   \r\n   OTHER   \r\n\r\n"
            "##  Source /Context\r\n  padded source  \r\n\r\n"
            "## Why it matters   ##\r\n  padded why  \r\n"
        )
        record = si.parse_intake_body(body, CONFIG)
        self.assertEqual(record.area, "OTHER")
        self.assertEqual(record.source_context, "padded source")
        self.assertEqual(record.why_it_matters, "padded why")

    def test_multiline_text_sections_collapse_to_single_line(self):
        record = si.parse_intake_body(
            make_body(why="Line one.\nLine two."), CONFIG
        )
        self.assertEqual(record.why_it_matters, "Line one. Line two.")

    def test_preamble_free_text_before_first_heading_is_ignored(self):
        body = "Some intro chatter.\n\n" + VALID_BODY
        record = si.parse_intake_body(body, CONFIG)
        self.assertEqual(record.area, "RESEARCH / SELF-IMPROVEMENT")


class TestParserRejections(unittest.TestCase):
    def assert_rejected(self, body, fragment):
        with self.assertRaises(si.IntakeValidationError) as ctx:
            si.parse_intake_body(body, CONFIG)
        self.assertIn(fragment, "; ".join(ctx.exception.problems))

    def test_unknown_area_rejected(self):
        self.assert_rejected(make_body(area="MARKETING"), "unknown Area")

    def test_no_guessing_of_close_area_values(self):
        self.assert_rejected(make_body(area="FACTORY"), "unknown Area")

    def test_missing_area_rejected(self):
        body = (
            "<!-- nortropic-innovation-intake:v1 -->\n"
            "## Source / Context\nx\n## Why it matters\ny\n"
        )
        self.assert_rejected(body, "missing required section '## Area'")

    def test_empty_area_rejected(self):
        self.assert_rejected(make_body(area=""), "'## Area' is empty")

    def test_multivalue_area_rejected(self):
        self.assert_rejected(make_body(area="OTHER\nVERIFICATION"), "exactly one value")

    def test_missing_source_context_rejected(self):
        body = (
            "<!-- nortropic-innovation-intake:v1 -->\n"
            "## Area\nOTHER\n## Why it matters\ny\n"
        )
        self.assert_rejected(body, "missing required section '## Source / Context'")

    def test_empty_source_context_rejected(self):
        self.assert_rejected(make_body(source=""), "'## Source / Context' is empty")

    def test_missing_why_it_matters_rejected(self):
        body = (
            "<!-- nortropic-innovation-intake:v1 -->\n"
            "## Area\nOTHER\n## Source / Context\nx\n"
        )
        self.assert_rejected(body, "missing required section '## Why it matters'")

    def test_empty_why_it_matters_rejected(self):
        self.assert_rejected(make_body(why=""), "'## Why it matters' is empty")

    def test_wrong_schema_version_rejected(self):
        body = VALID_BODY.replace("intake:v1", "intake:v2")
        self.assert_rejected(body, "unsupported schema version 'v2'")

    def test_missing_marker_rejected(self):
        body = VALID_BODY.replace("<!-- nortropic-innovation-intake:v1 -->", "")
        self.assert_rejected(body, "missing schema marker")

    def test_unknown_heading_rejected(self):
        self.assert_rejected(VALID_BODY + "\n## Priority\nhigh\n", "unknown section heading")

    def test_duplicate_heading_rejected(self):
        self.assert_rejected(VALID_BODY + "\n## Area\nOTHER\n", "duplicate section")

    def test_empty_body_rejected(self):
        self.assert_rejected("", "missing schema marker")
        self.assert_rejected(None, "missing schema marker")

    def test_all_problems_reported_together(self):
        body = "<!-- nortropic-innovation-intake:v1 -->\n## Area\nNOPE\n"
        with self.assertRaises(si.IntakeValidationError) as ctx:
            si.parse_intake_body(body, CONFIG)
        joined = "; ".join(ctx.exception.problems)
        self.assertIn("unknown Area", joined)
        self.assertIn("Source / Context", joined)
        self.assertIn("Why it matters", joined)


# ---------------------------------------------------------------------------
# Synchronizer (fake GraphQL transport — no network)
# ---------------------------------------------------------------------------

PROJECT_ID = "PVT_proj"
ISSUE_ID = "I_issue"
ITEM_ID = "PVTI_item"


def project_fields_response(drop_status_option=None):
    statuses = [s for s in CONFIG["expected_statuses"] if s != drop_status_option]
    return {
        "node": {
            "fields": {
                "nodes": [
                    # The live project's Status options are Title-case
                    # ('Inbox', not 'INBOX'); matching must tolerate that.
                    {"id": "F_status", "name": "Status", "dataType": "SINGLE_SELECT",
                     "options": [{"id": f"OPT_S_{s}", "name": s.capitalize()}
                                 for s in statuses]},
                    {"id": "F_area", "name": "Area", "dataType": "SINGLE_SELECT",
                     "options": [{"id": f"OPT_A_{a}", "name": a}
                                 for a in CONFIG["allowed_areas"]]},
                    {"id": "F_source", "name": "Source / Context", "dataType": "TEXT"},
                    {"id": "F_why", "name": "Why it matters", "dataType": "TEXT"},
                    {"id": "F_title", "name": "Title", "dataType": "TITLE"},
                ]
            }
        }
    }


class FakeClient:
    """Replays canned responses and records every mutation."""

    def __init__(self, existing_item=None, drop_status_option=None):
        self.existing_item = existing_item
        self.drop_status_option = drop_status_option
        self.mutations = []
        self.calls = 0

    def execute(self, query, variables):
        self.calls += 1
        if "projectsV2(first: 50)" in query:
            return {"organization": {"projectsV2": {"nodes": [
                {"id": PROJECT_ID, "number": 7,
                 "title": CONFIG["project_title"], "closed": False},
                {"id": "PVT_other", "number": 9, "title": "Unrelated", "closed": False},
            ]}}}
        if "projectV2(number:" in query:
            return {"organization": {"projectV2": {
                "id": PROJECT_ID, "number": variables["number"],
                "title": CONFIG["project_title"], "closed": False}}}
        if "fields(first: 50)" in query:
            return project_fields_response(self.drop_status_option)
        if "projectItems" in query:
            nodes = []
            if self.existing_item:
                nodes.append({"id": self.existing_item,
                              "project": {"id": PROJECT_ID}})
            # An item in some other project must never be reused.
            nodes.append({"id": "PVTI_foreign", "project": {"id": "PVT_other"}})
            return {"node": {"projectItems": {"nodes": nodes}}}
        if "addProjectV2ItemById" in query:
            self.mutations.append(("add", dict(variables)))
            return {"addProjectV2ItemById": {"item": {"id": ITEM_ID}}}
        if "updateProjectV2ItemFieldValue" in query:
            self.mutations.append(("update", dict(variables)))
            return {"updateProjectV2ItemFieldValue": {"projectV2Item": {"id": variables["itemId"]}}}
        raise AssertionError(f"unexpected query: {query[:80]}")


class TestSync(unittest.TestCase):
    def test_new_issue_added_and_all_fields_set(self):
        client = FakeClient()
        summary = si.sync_issue(client, CONFIG, ISSUE_ID, "My idea", VALID_BODY)
        self.assertTrue(summary["created"])
        self.assertEqual(summary["item_id"], ITEM_ID)
        adds = [m for m in client.mutations if m[0] == "add"]
        updates = [m for m in client.mutations if m[0] == "update"]
        self.assertEqual(len(adds), 1)
        self.assertEqual(adds[0][1]["contentId"], ISSUE_ID)
        self.assertEqual(len(updates), 4)
        by_field = {u[1]["fieldId"]: u[1] for u in updates}
        self.assertEqual(by_field["F_status"]["optionId"], "OPT_S_INBOX")
        self.assertEqual(
            by_field["F_area"]["optionId"], "OPT_A_RESEARCH / SELF-IMPROVEMENT"
        )
        self.assertEqual(
            by_field["F_source"]["text"],
            "ChatGPT – Workflow och Orkestrering – 2026-08-15",
        )
        self.assertIn("Could let Nortropic", by_field["F_why"]["text"])
        # Every mutation targets only the resolved item in the target project.
        for _, vars_ in updates:
            self.assertEqual(vars_["itemId"], ITEM_ID)
            self.assertEqual(vars_["projectId"], PROJECT_ID)

    def test_existing_item_updated_not_duplicated(self):
        client = FakeClient(existing_item=ITEM_ID)
        summary = si.sync_issue(client, CONFIG, ISSUE_ID, "My idea", VALID_BODY)
        self.assertFalse(summary["created"])
        self.assertEqual(summary["item_id"], ITEM_ID)
        self.assertEqual([m[0] for m in client.mutations], ["update"] * 4)

    def test_edited_issue_updates_same_item_with_new_value(self):
        client = FakeClient(existing_item=ITEM_ID)
        edited = VALID_BODY.replace(
            "Could let Nortropic continuously discover and evaluate system "
            "improvements without interrupting active implementation.",
            "Updated reasoning.",
        )
        summary = si.sync_issue(client, CONFIG, ISSUE_ID, "My idea", edited)
        self.assertEqual(summary["item_id"], ITEM_ID)
        self.assertEqual(summary["why_it_matters"], "Updated reasoning.")
        self.assertEqual([m[0] for m in client.mutations], ["update"] * 4)

    def test_repeated_sync_is_idempotent(self):
        first = FakeClient()
        si.sync_issue(first, CONFIG, ISSUE_ID, "My idea", VALID_BODY)
        second = FakeClient(existing_item=ITEM_ID)
        si.sync_issue(second, CONFIG, ISSUE_ID, "My idea", VALID_BODY)
        self.assertEqual(len([m for m in second.mutations if m[0] == "add"]), 0)

    def test_item_in_unrelated_project_is_never_reused(self):
        client = FakeClient(existing_item=None)
        summary = si.sync_issue(client, CONFIG, ISSUE_ID, "My idea", VALID_BODY)
        self.assertTrue(summary["created"])
        for _, vars_ in client.mutations:
            self.assertNotEqual(vars_.get("itemId"), "PVTI_foreign")

    def test_validation_failure_makes_no_project_calls(self):
        client = FakeClient()
        with self.assertRaises(si.IntakeValidationError):
            si.sync_issue(client, CONFIG, ISSUE_ID, "Bad", "not an intake body")
        self.assertEqual(client.calls, 0)
        self.assertEqual(client.mutations, [])

    def test_missing_expected_status_option_fails_before_mutation(self):
        client = FakeClient(drop_status_option="INBOX")
        with self.assertRaises(si.ProjectContractError) as ctx:
            si.sync_issue(client, CONFIG, ISSUE_ID, "My idea", VALID_BODY)
        self.assertIn("INBOX", str(ctx.exception))
        self.assertEqual(client.mutations, [])

    def test_ambiguous_project_title_fails_closed(self):
        cfg = dict(CONFIG, project_number=None)  # force title-based resolution

        class AmbiguousClient(FakeClient):
            def execute(self, query, variables):
                if "projectsV2(first: 50)" in query:
                    node = {"id": PROJECT_ID, "number": 7,
                            "title": CONFIG["project_title"], "closed": False}
                    return {"organization": {"projectsV2": {"nodes": [node, dict(node)]}}}
                return super().execute(query, variables)

        client = AmbiguousClient()
        with self.assertRaises(si.ProjectContractError):
            si.sync_issue(client, cfg, ISSUE_ID, "My idea", VALID_BODY)
        self.assertEqual(client.mutations, [])

    def test_configured_project_number_with_wrong_title_fails_closed(self):
        cfg = dict(CONFIG, project_number=7, project_title="Nortropic Innovation")

        class WrongTitleClient(FakeClient):
            def execute(self, query, variables):
                if "projectV2(number:" in query:
                    return {"organization": {"projectV2": {
                        "id": PROJECT_ID, "number": 7,
                        "title": "Something Else", "closed": False}}}
                return super().execute(query, variables)

        client = WrongTitleClient()
        with self.assertRaises(si.ProjectContractError):
            si.sync_issue(client, cfg, ISSUE_ID, "My idea", VALID_BODY)
        self.assertEqual(client.mutations, [])


if __name__ == "__main__":
    unittest.main()
