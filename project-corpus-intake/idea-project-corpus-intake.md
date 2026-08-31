---
title: "Nortropic Intake v3: Project Corpus Intake (PROJECT_SWEEP) + proving-run iteration"
type: idea-brief
status: idea
slug: project-corpus-intake
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: project-corpus-intake-full-chat.md
design_rationale: project-corpus-intake-design-rationale.md
intended_repo_path: project-corpus-intake/idea-project-corpus-intake.md
context_revision: 1
related: [openai-anthropic-workflow, innovation-inbox-idehantering, nortropic-recompile, corpus-control-plane, korpusfrysning-och-syntesmetod]
---

# Idea brief: Nortropic Intake v3 — Project Corpus Intake + proving-run iteration

## 1. Summary
Owner-decided rebuild of `nortropic-intake` from single-brainstorm v2.1 to v3.0 with an
explicit PROJECT_SWEEP mode: sweep a whole ChatGPT project losslessly into a
coverage-verified, normalized R&D corpus, run it on all of Improvements, and hand a
sealed corpus to the Autonomy Kernel. The build was EXECUTED inside the source chat
(v3.0 frozen 2026-08-30; sweep started; enumeration owner-verified at 27
conversations). The durable remaining content is the framing decision that this run is
a **proving run** — iterate on observed failures, clean up, and run an optimized final
intake ("corpus cut") only when the Trust Kernel is done.

## 2. Context you need
`nortropic-intake` v2.1 captured one brainstorm at a time (routing, interview, plan
mode, exact approval). The owner decided the Improvements project — the whole R&D
history — must be swept into a trustworthy corpus *before* the Kernel's first Recompile
mission, so the Kernel does not spend its first mission building a browser
mass-importer (← msg 67; design 68). v3.0 exists and is frozen: SINGLE mode preserves
v2.1; PROJECT_SWEEP is explicit-invocation-only corpus ingest (STOP REPORT relayed in
msg 71 — owner-transported machine evidence, frozen identities
SKILL_MAIN=7ddb9a53…, final main c586ae4f…, FREEZE_DATE=2026-08-30). The transcript
ends mid-sweep; the sweep outcome is outside this source.

This brief is the primary intake artifact for execution. Deeper design logic lives in
the linked design rationale; the full chat is raw evidence — read targeted message
ranges only if the rationale is insufficient. Current canonical repository authority
beats all intake artifacts; within the intake package this brief wins over rationale
and transcript. Once an owner-approved plan is bound (see the frontmatter), it carries
execution order above this brief and below current repository authority.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts,
frozen gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)
- The current Improvements sweep treated as a real-world proving run: observe real
  failures, convert each into a minimal reproducer + permanent regression test +
  smallest fix + refreeze — never mid-run remodeling.
- A final optimized intake ("corpus cut") run fresh and incrementally as close to the
  Recompile mission as possible, only after the Trust Kernel is done, with daily
  reports admitted as their own evidence class (never as owner instruction or repo
  truth).
- A sealed, mechanically coverage-verified Improvements corpus
  (SOURCE_COVERAGE_COMPLETE / PROCESSING_COMPLETE / AUDIT_CURRENT / review items
  resolved or explicitly accepted) as the Kernel's Recompile input.
- Choose architecture, decomposition and tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)
D1. Rebuild intake so it can sweep/clean all current chats; then run it on the whole
Improvements project, and only then let the Kernel work — because the Kernel should
receive a closed, lossless, mechanically coverage-verified corpus instead of spending
its first mission on mass-import and coverage doubt (← msg 67; detail 68).
D2. Build v3 per the commissioned master prompt ("ge mig prompten för att göra om
intake enligt det du beskriver") — because the owner ratified the described design:
raw source survives, source identity before idea identity, role-aware provenance,
approval strength survives, non-interactive sweep, provable coverage,
idempotent/resumable, one idea many episodes, sweep never defines final ontology,
v2.1 single mode survives (← msg 69; prompt text 70).
D3. The real sweep was started with the approved production prompt — because the tool
was first built, frozen and mechanically verified, and the sweep is a separate
owner-authorized run (← msg 73; prompt 72).
D4. The current run is a proving run: test, iterate, clean; the optimized final intake
runs after the Trust Kernel, and daily reports shall be taken into account — because
sealing now would hand the Kernel a stale snapshot, and real failures are cheapest to
fix before the final cut (← msg 75; phases 76).
D5. No remodeling of intake mid-run ("tillbaka till intake körningen nu innan vi
modellerar om den") — because observations belong in the residual report and the frozen
v3.0 contract must meet reality unchanged (← msg 81; reinforced 82, 84).
D6. Owner verification of the source inventory: "27 stämmer" → enumeration declared
verified (--method data-layer --verified) — because three independent mechanical
signals plus owner visual confirmation converged on the same membership (← msg 83;
context 81–82, 84).

R1. Only minimal v2.2 hardening now, letting the Kernel build corpus/recompile
capability itself later — because that wastes the Kernel's first mission on tooling and
unprovable coverage; superseded by the owner's decision to build v3 first (← msg 67;
prior recommendation 66).
R2. Sealing Improvements as the final corpus already now — because new brainstorms,
decisions and reports keep arriving; replaced by proving run + corpus cut near
Recompile (← msg 75; 76).
R3. Owner interview / plan mode per historical chat in sweep mode — because the
process would die after two hours; PROJECT_SWEEP is unattended corpus ingest, never
IMPLEMENT_NOW — a binding rule of the owner-approved prompt (← msg 69; principle 68,
prompt 70).

## 5. Acceptance criteria (v1)
AC1. WHEN a project sweep is invoked, THE skill SHALL run it as non-interactive corpus
ingest — no owner interview, no plan mode, no approved plans — recording ambiguities to
a persistent review queue and continuing (← msg 67, 69; 70).
AC2. WHEN a conversation cannot be captured/verified or enumeration cannot be proven
exhausted, THE sweep SHALL fail closed (hard gap / PROJECT_ENUMERATION_UNVERIFIED)
rather than claim completeness; owner confirmation may close enumeration exactly as in
the 27-conversation verification (← msg 83; 81–82).
AC3. WHEN the proving run observes a real failure (e.g. cursor pagination where the
adapter expected count==total), THE process SHALL record it as an observation /
regression candidate for post-run iteration and SHALL NOT reopen the frozen skill
architecture mid-run (← msg 81; 82, 84).
AC4. WHEN the Trust Kernel is done, THE final optimized intake SHALL run as a fresh
incremental sweep (unchanged sources reused by verified bytes) including daily reports
as a distinct evidence class, and seal a reproducible Recompile Source Cut (← msg 75;
76).

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)
Invariants pointer: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`); pointer only.
Suggestions from the source: keep the system files/Git-first (no vector DB, no giant
crawler framework); iterate only on observed/material problems, each with a permanent
regression test before the fix; daily reports enter as DERIVED_RESEARCH_EVIDENCE with
observed_at/freshness/sources, hydratable back to primary sources; the skill runtime
never commits/pushes — publication is a separate owner-authorized session step.

## 7. Out of scope (v1)
- Nortropic Recompile itself (Concept/Constitution/Architecture/Roadmap) — Kernel's
  mission, separate brief `nortropic-recompile`.
- The Gold Extraction working mode (separate brief `gold-extraction-overlay`) and the
  assistant-only primitive catalog (msgs 13–62, not packaged).
- Källor-tab intake and all v3.1 candidates until proving-run evidence exists.
- Any architecture change to the frozen v3.0 skill outside its own reopen policy.

## 8. Verification (how we know it works)
From the record alone: the final sweep STOP REPORT plus the corpus repo show
SOURCE_COVERAGE_COMPLETE=YES, PROCESSING_COMPLETE=YES, AUDIT_CURRENT=YES, review items
resolved or explicitly owner-accepted, a published corpus SHA/tree, raw sources
retained per revision, and an independent sweep audit round that attempted — and
failed — to falsify completeness.

## 9. Open questions (interview the owner before planning)
Q1. Which v3.1 candidates (enumeration receipt, Källor-tab intake, conversation
lineage, project-config snapshot, content equivalence, cross-oracle coverage, live
adapter fixture — assistant proposals, msg 80) become real work items after the
proving run?
Q2. How are daily reports and the Källor tab classified in the final sweep (the
assistant's source-class schema is untested)?
Q3. Should Improvements switch to Project-only memory (flagged as a genuine owner
architecture question, msg 80)?
Q4. What was the outcome of the ongoing sweep — the transcript ends mid-run (msg 84)?

## 10. Process for this brief
1. Clarify: first send a subagent to read `project-corpus-intake-design-rationale.md`
   (its rejection and unresolved sections cover most §9 rationale) and report back
   what bears on §9; only if the rationale lacks the needed evidence, exact source
   wording matters, or a conflict/ambiguity remains, have it read the targeted message
   ranges in the source conversation via the rationale's retrieval map — never the
   whole transcript, and keep both out of main context; then interview the owner on §9
   (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code ("address all notes, don't
   implement yet").
3. On explicit owner approval, persist the exact approved plan as
   `project-corpus-intake-approved-plan.md`, validate it
   (`scripts/plan_contract.py validate`), bind it into this frontmatter
   (`approved_plan` + `approved_plan_sha256` + `plan_version`) and only then set
   `status: planned`. Nothing is summarized away; a short execution prompt never
   replaces the plan file.
4. Implement in a fresh session, started from the approved plan:
   `plan_contract.py resume --slug project-corpus-intake --target-repo <repo>` proves
   the plan identity; reconcile the plan against current repository truth before
   continuing. After any compaction, re-read the plan from disk — never reconstruct it
   from memory; if it cannot be proven, STOP with `PLAN_IDENTITY_UNAVAILABLE`.
5. Adversarial review: fresh subagent checks the diff against this brief and the
   approved plan; report only gaps affecting correctness or stated requirements.
6. Traceability: commit messages cite this brief's slug.

## References
- Source conversation: `project-corpus-intake-full-chat.md` (same folder)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
