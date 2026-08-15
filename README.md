# Nortropic Innovation Intake v1

A minimal, deterministic bridge that captures innovation ideas as GitHub
issues and automatically synchronizes them into the existing GitHub Project
**Nortropic Innovation** with `Status = INBOX`.

This is a **Discovery Plane intake tool**. It is intentionally not part of
Nortropic's Control Plane, and an intake issue is a **raw innovation record**
— never an implementation task. Nothing here creates executable Factory work.

## How it works

```text
ChatGPT (or a human)
   ↓  creates an issue in this repository using the v1 contract below
GitHub Actions (.github/workflows/innovation-intake.yml)
   ↓  on issues: opened / edited / reopened
scripts/sync_innovation.py
   ↓  parses + validates the contract (fail closed — no mutation on invalid input)
GitHub Projects v2 GraphQL API
   ↓
Nortropic Innovation:  Status=INBOX, Area, Source / Context, Why it matters
```

Properties:

* **Idempotent** — re-running for the same issue updates its existing Project
  item; it never creates duplicates. Edits to the issue body re-synchronize
  the same item.
* **Fail closed** — malformed bodies, unknown Area values, wrong schema
  versions, and Project schema drift all abort with a clear error before any
  Project mutation.
* **Isolated** — the synchronizer only ever touches the Project item backing
  the triggering issue. It never scans, edits, or deletes other items, and it
  never alters Project fields or options.

## ChatGPT Intake Contract

The **issue title** is the innovation title. The **issue body** must follow
this exact v1 format (heading case and spacing around `/` are tolerated;
everything else is strict):

```markdown
<!-- nortropic-innovation-intake:v1 -->

## Area
<exactly one allowed Area value>

## Source / Context
<where the idea came from — conversation, tool, date>

## Why it matters
<one sentence explaining the value>
```

Allowed `Area` values (choose exactly one, no invention of new values):

```text
CONTROL PLANE
FACTORY / AGENTS
VERIFICATION
UX / VERKSTADSGOLVET
RESEARCH / SELF-IMPROVEMENT
PERFORMANCE / THROUGHPUT
PRODUCT / BUSINESS
OTHER
```

Rules:

* the marker comment `<!-- nortropic-innovation-intake:v1 -->` is required;
* all three sections are required and non-empty;
* only these three `##` headings may appear — unknown or duplicate headings
  are rejected;
* an unknown `Area` is rejected, never guessed;
* multi-line text in `Source / Context` / `Why it matters` is collapsed to a
  single line in the Project fields (the issue itself remains the lossless
  record).

### Canonical example

Title: `Continuous self-improvement discovery loop`

```markdown
<!-- nortropic-innovation-intake:v1 -->

## Area
RESEARCH / SELF-IMPROVEMENT

## Source / Context
ChatGPT – Workflow och Orkestrering – 2026-08-15

## Why it matters
Could let Nortropic continuously discover and evaluate system improvements without interrupting active implementation.
```

### Intended ChatGPT behavior

```text
USER:  "Spara den här idén."

CHATGPT:
1. infer a concise title;
2. choose exactly one allowed Area;
3. summarize source/context;
4. explain Why it matters in one sentence;
5. create the issue in this repository (innovation-intake);
6. automation synchronizes the Project;
7. reply with the issue identity and "Sparad i INBOX".
```

## Configuration

`scripts/intake_config.json` holds the target Project owner, title, number,
field names, and the allowed option values. The synchronizer resolves the
Project and its fields **by name on every run** and verifies they match this
expected model, so renamed or deleted fields/options fail visibly instead of
silently mis-filing ideas. If `project_number` is set, the Project is looked
up by number and its title is verified. Single-select option names are
matched case-insensitively: the live Status options are `Inbox`, `Shaping`, …
while the intake model spells them `INBOX`, `SHAPING`, … — same options; the
Project schema is never modified to force a case match.

## Authentication

The workflow needs one repository secret:

* **`PROJECT_TOKEN`** — a fine-grained personal access token with the minimum
  viable footprint:
  * Resource owner: the organization that owns the Project (`Nortropic`);
  * Organization permissions → **Projects: Read and write**;
  * Repository access: **only this repository** → **Issues: Read-only**
    (needed so the token may attach the private intake issue to the Project).

No other permissions are required. The default Actions `GITHUB_TOKEN` cannot
write organization Projects v2, which is why this secret exists. No
credentials live in the source tree.

Set it with:

```bash
gh secret set PROJECT_TOKEN --repo <owner>/innovation-intake
```

## Tests

Pure unit tests (parser + sync logic against a fake GraphQL transport — no
network, no live Project access):

```bash
python3 -m unittest discover -s tests -v
```

CI runs the same suite on every push and pull request.

## Scope of v1

v1 is **lossless idea capture only**. Deliberately out of scope: semantic
deduplication, research/shaping agents, prioritization, and any Factory
integration. An INBOX item never automatically becomes executable work.
