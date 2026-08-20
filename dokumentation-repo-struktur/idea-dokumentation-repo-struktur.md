---
title: "Thin authoritative core, thick knowledge base: the nortropic-knowledge split"
type: idea-brief
status: idea   # lifecycle: idea → clarified → planned → building → verified; terminal: superseded
slug: dokumentation-repo-struktur
owner: Johnny (Nortropic)
created: 2026-08-20
source_conversation: dokumentation-repo-struktur-full-chat.md   # reference only — this brief takes precedence
intended_repo_path: dokumentation-repo-struktur/idea-dokumentation-repo-struktur.md
related: [workflow-orkestrering]
---

# Idea brief: Thin authoritative core, thick knowledge base — the nortropic-knowledge split

## 1. Summary

Split Nortropic's documentation by lifecycle, not by weight: everything that must be
versioned atomically with the code (constitution, rulebook, frozen contracts, gates,
AGENTS.md) stays in `nortropic-system`; everything that explains, teaches, explores or
preserves knowledge moves to a dedicated `nortropic-knowledge` repo that is **never
execution authority**. The framing decision: **"move documentation when it does not
need atomic versioning with the code — not because it is heavy."** Phase 0 (the
foundation repo, 21 files, governance flags) was built and owner-gated in this chat
and is now live; the remaining idea is the MIGRATION and the ongoing conventions.

## 2. Context you need

`nortropic-knowledge` exists (Phase 0 committed as `e764eb4`) with the governing
boundary flags (`NORTROPIC_KNOWLEDGE_IS_EXECUTION_AUTHORITY=NO`,
`SOURCE_REPOSITORY_WRITES_FROM_KNOWLEDGE_TASKS=FORBIDDEN`, …), 13 sections
(architecture/decisions/rfcs/research/learnings/handoffs/operations/postmortems/
product/references/reports/archive/templates) and an inspected-snapshot model where
canonical identity is always `Nortropic/<repo>@<commit>`. The research base: OpenAI
keeps agent instructions and version-bound docs near code but general docs elsewhere
(AGENTS.md ~32KiB cap); Anthropic recommends CLAUDE.md under ~200 lines with
specialized knowledge loaded on demand; Kubernetes/GitHub/GitLab split knowledge
lifecycles across repos. Phase 0 deliberately migrated NOTHING — heavy documents still
live in `nortropic-system` and `verkstadsgolvet` (which was found 57 commits behind
its remote during inventory).
Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen
gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- The heavy, non-authoritative knowledge mass (architecture explanations, research,
  design exploration, Verkstadsgolvet/UX concepts, learnings, postmortems, historical
  handoffs) lives in `nortropic-knowledge`, classified per section with frontmatter
  (`authority: none | informational` only) and provenance.
- `nortropic-system` keeps only the thin core: constitution, rulebook, frozen task
  contracts, gates/verifiers, AGENTS.md router — small, precise, local, normative.
- Migration happens through owner-gated, fail-closed batches (the Phase 0 discipline:
  exact file manifests, source repos untouched, evidence bundles for owner review,
  commit only after owner gate).
- Knowledge documents point to authority (`Nortropic/<repo>@<commit>` + path); they
  never copy or restate it as a second source of truth.
- Agents can find what is current: navigable hierarchy, supersession recorded,
  always-on context stays small while knowledge is fetched on demand.

Choose architecture/decomposition/tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

- D1. Split rule: documentation moves out when it does NOT need atomic versioning with
  the code — because the naive "move it because it's heavy" breaks version-bound docs
  (API/behavior docs, agent instructions) that must live beside code (← msg 8).
- D2. The split itself: thin authoritative core in `nortropic-system`; thick knowledge
  base in a new dedicated repo — because always-on agent context must stay small while
  knowledge can be large and on-demand (← msg 2–3, 8).
- D3. `nortropic-knowledge` is never execution authority and knowledge tasks may never
  write to source repositories — a standing rule, encoded as governance flags in the
  repo itself (← msg 25–35; now in GOVERNANCE.md).
- D4. Phase 0 scope: foundation only — 21 exactly-manifested files, no migration, no
  remote/commit/push until the owner gate passed (← msg 24).
- D5. Proof discipline: exact relative-path manifests beat file counts; claim
  "Git-visible state identical", never "byte-for-byte"; frontmatter verified
  mechanically; fail closed if the target path already exists (← msg 24).
- D6. Remote-tracking refs (`refs/remotes/**`) are observed external state, not an
  invariant — source repos may evolve through their own processes during knowledge
  work (← msg 35).
- Precedent worth keeping: the entire Phase 0 ran as plan-mode iterations with owner
  "No, keep planning" corrections before any file was written (← msg 10–24).

## 5. Acceptance criteria (v1 — for the migration phases)

- AC1. WHEN a document is migrated, THE batch SHALL carry an exact expected/actual
  manifest diff (empty = pass) and the source repos' Git-visible state SHALL be
  unchanged by the knowledge task.
- AC2. WHEN a knowledge document lands, THE frontmatter SHALL validate mechanically
  (delimiters, required fields, authority ∈ {none, informational}).
- AC3. WHEN a knowledge document references canonical material, THE reference SHALL be
  `Nortropic/<repo>@<commit>` + path — never a copied normative text.
- AC4. WHEN a migration batch completes, THE owner SHALL receive a reviewable evidence
  bundle before any commit, and commits SHALL happen only after explicit owner
  authorization.
- AC5. WHEN documentation is superseded, THE supersession SHALL be recorded so an
  agent can determine what is current without reading history.

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants: Nortropic's trust layer — constitution & rulebook (pointer, never a copy).
Suggestions from the chat/research: keep CLAUDE.md/AGENTS.md short (Anthropic's
<200-line guidance; Codex's 32KiB combined cap argues the same); path-scoped rules and
on-demand loading for specialized knowledge; consider a docs-drift check (OpenAI's
docs-sync pattern) for version-bound docs that stay in the code repo; the
Verkstadsgolvet repo's 57-commit remote lag found in inventory needs its own owner
attention before its docs are classified.

## 7. Out of scope (v1)

- Moving anything from the authoritative core (constitution, rulebook, contracts,
  gates, AGENTS.md) — it stays with the code by design (D2).
- Making nortropic-knowledge a runtime or verification dependency (forbidden by its
  own governance flags).
- The knowledge-plane/context-manifest MACHINERY — that is the related
  `workflow-orkestrering` brief; this brief owns the repo split and migration.
- Re-doing Phase 0 (done and committed).

## 8. Verification (how we know it works)

End-to-end: run one migration batch of real documents. From the record alone an
independent reviewer confirms: empty manifest diff (AC1), mechanical frontmatter pass
(AC2), pointer-not-copy spot-checks (AC3), owner evidence bundle + explicit commit
authorization in sequence (AC4), and that `nortropic-system`/`verkstadsgolvet`
Git-visible state was untouched by the batch.

## 9. Open questions (interview the owner before planning)

- Q1. What migrates first — historical handoffs, architecture explanations, or the
  Verkstadsgolvet document family?
- Q2. Verkstadsgolvet's 57-commit remote lag: sync it before classifying its docs, and
  who owns that sync?
- Q3. Should the idébank (`innovation-intake`) stay a separate repo, or does the
  knowledge repo's rfcs/research sections eventually absorb parts of it? (The future
  Improvements synthesis is slated for nortropic-knowledge — same question.)
- Q4. Does the migration wait until the current bootstrap completes, or can batches
  run in parallel since knowledge tasks never write to source repos?
- Q5. Which documents in nortropic-system today are secretly load-bearing (read by
  agents/gates) and must be identified before anything moves?

## 10. Process for this brief

1. Clarify: first send a subagent to read the source conversation and report back the
   rationale relevant to §9 (keeps the transcript out of main context); then interview
   the owner on §9 (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code ("address all notes, don't implement yet").
3. Implement in a fresh session from the approved plan.
4. Adversarial review: fresh subagent checks the diff against this brief; report only
   gaps affecting correctness or stated requirements.
5. Traceability: commit messages cite this brief's slug.

## References

- Source conversation: `dokumentation-repo-struktur-full-chat.md` (same folder)
- The live result: `~/nortropic/nortropic-knowledge` @ e764eb4 (Phase 0 foundation)
- Related brief: `workflow-orkestrering/` (knowledge model, context manifests)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
