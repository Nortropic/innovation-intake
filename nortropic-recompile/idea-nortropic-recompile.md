---
title: "Nortropic Recompile: the Kernel's first mission compiles Improvements into Concept/Constitution/Architecture/Roadmap"
type: idea-brief
status: idea
slug: nortropic-recompile
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: nortropic-recompile-full-chat.md
design_rationale: nortropic-recompile-design-rationale.md
intended_repo_path: nortropic-recompile/idea-nortropic-recompile.md
context_revision: 1
related: [nortropic-organization-os, brainstorming-arbetsfloden, project-corpus-intake, corpus-control-plane, korpusfrysning-och-syntesmetod]
---

# Idea brief: Nortropic Recompile

## 1. Summary
The post-Bootstrap synthesis shall not be done manually: once Autonomy Kernel v1 is
frozen, its first real mission is to assimilate the whole Improvements corpus plus
current repo reality and itself produce Nortropic Concept v1, Constitution v1,
Organization Architecture v1 and a dependency-ordered roadmap. The single most
important framing decision is the owner's "Kan inte kernel bygga allt detta?"
(← msg 11): the whole synthesis job — including building missing capabilities
mid-mission — moves to the Kernel; the humans supply vision, values, risk appetite and
a small decision queue.

## 2. Context you need
Months of Improvements chats hold ideas, decisions, rejections and supersessions that
must land in one canonical concept/plan once Bootstrap completes (← msg 6, 7). The
prerequisite corpus work is a separate idea (`project-corpus-intake`): intake sweeps
and normalizes Improvements first; the Kernel recompiles second (← msg 67). Recompile
consumes the sealed corpus + current authoritative repos and produces the constitutive
documents — it is compilation with owner judgment reduced to genuinely high-leverage
choices. Raw full chats are preserved so future, better models can recompile the
originals again (← msg 63; 64).

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
- A Kernel mission ("Nortropic Post-Bootstrap Rebaseline / Recompile") that
  assimilates: current authoritative repos, the complete raw Improvements corpus, the
  normalized intake corpus, current decisions/specs, external evidence — and derives
  what Nortropic now is, what remains valid, what is already solved, what is
  superseded, what is contradictory, and the minimal coherent architecture forward.
- Outputs: Nortropic Concept v1, Constitution v1 (order 10–20 strong rules — content
  is the mission's to derive, not pre-decided), Organization Architecture v1, a
  dependency-ordered roadmap, and a small owner decision queue holding only genuine
  judgment calls.
- Multi-pass compilation with inspectable intermediates and selective re-runs, never
  one giant prompt.
- When the first next build phase is unambiguously derived, verified and within
  authority: the Kernel continues autonomously instead of stopping at a plan.
- Choose architecture/decomposition/tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)
D1. Collect everything from all Improvements chats and land in the concept/plan
forward once Bootstrap completes — because the chats must stop being Nortropic's
long-term memory while nothing of what was learned is lost (← msg 6, 7; 8–10).
D2. The Kernel shall itself perform the synthesis ("Kan inte kernel bygga allt
detta?") — because having humans manually design the next system and feed the Kernel
small tasks would waste exactly what Bootstrap built; the assistant explicitly revised
its plan on this (← msg 11; revision 12).
D3. The post-Bootstrap working model is Recompile-first: freeze Kernel v1, then the
first real autonomous mission recompiles Improvements into
Concept/Constitution/Architecture/Roadmap before any next big build (← msg 63;
64).
D4. Sequencing: Intake cleans/sweeps Improvements first, then the Kernel works —
because Recompile must start from a closed, coverage-proven corpus (← msg 67; 68).
D5. The final intake/corpus cut happens after the Trust Kernel, as close to the
Recompile mission as possible — because the Kernel must not start from a stale
snapshot (← msg 75; 76).

R1. A manual "constituting synthesis" performed by Johnny/ChatGPT/Claude before the
Kernel (the assistant's original plan) — because it duplicates by hand what the Kernel
exists to do; overturned by the owner (← msg 11; 8–10).
R2. "One giant prompt with all the chats" as synthesis method — because it recreates
the context-dilution problem at larger scale; multi-pass compilation instead
(← msg 63; formulated 9, passes in 68).
R3. Letting "what we thought" automatically become "what we now build" — because a
good brainstorm contains much that must never be built; every idea passes a
disposition matrix (KEEP/ADAPT/ADD/SIMPLIFY/MERGE/DEFER/REJECT/SUPERSEDED/
NEEDS_EVIDENCE/FRONTIER_WATCH) against current reality (← msg 6; matrix 10, 64).

## 5. Acceptance criteria (v1)
AC1. WHEN Autonomy Kernel v1 is frozen and the mission starts, THE Kernel SHALL
assimilate the sealed Improvements corpus (raw + normalized) plus current repo reality
and produce verified Concept v1, Constitution v1, Organization Architecture v1 and a
dependency-ordered roadmap (← msg 11, 63; 12, 64).
AC2. WHEN compiling, THE mission SHALL run as multi-pass compilation (inventory →
atomic extraction → provenance → normalization → current-reality reconciliation →
cross-corpus synthesis → concept → architecture → roadmap) with inspectable
intermediates, never as one giant prompt (← msg 6, 63; 9, 68).
AC3. WHEN the Kernel lacks a needed capability mid-mission (e.g. cross-corpus
compilation), IT SHALL inventory existing tools, build/verify the minimal missing
capability, and continue the mission — no pre-built tool inventory is assumed
(← msg 11; 12, 66).
AC4. WHEN an old brainstorm conflicts with current verified repo reality, THE repo
SHALL win: the idea is dispositioned (e.g. SUPERSEDED/ALREADY_IMPLEMENTED) rather than
rebuilt, and only genuine owner-judgment questions reach a small decision queue
(← msg 11, 63; 64).
AC5. WHEN the constitutive documents and owner decisions are done, THE Kernel SHALL
continue autonomously into the first unambiguously derived build phase within its
authority, instead of writing a roadmap and waiting (← msg 11; 12, 64).

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)
Invariants pointer: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`); pointer only.
Suggestions from the source: authority hierarchy CURRENT VERIFIED REPO REALITY >
current owner decision > accepted concept/spec > derived knowledge > old brainstorm;
Recompile reads both raw chats and intake distillations (intake packages are inputs,
not the compilation's ontology — merge/split/supersede freely); old assistant
syntheses are DERIVED HISTORICAL SYNTHESIS, never auto-promoted ("do not learn from
output"); self-change stays inside the Kernel's authority/verification model
(spec → independent verification → behavioral evals → safe publication); the result
should be much smaller than the material (constitution ~10–20 rules, a handful of
first-class primitives); the owner supplies vision/values/risk boundaries — the
mission may not invent them.

## 7. Out of scope (v1)
- Building the intake sweep itself (separate brief `project-corpus-intake`).
- Building Recompile capability before Bootstrap — explicitly deferred until the
  Kernel exists (← msg 66; ratified by sequencing in 67).
- Organization OS / Digital Twin / Aquarium implementation — downstream of the roadmap.
- The assistant-only primitive catalog (msgs 13–62): comparator evidence for this
  mission, not packaged as decisions.
- Pre-deciding the constitution's content or the primitive set.

## 8. Verification (how we know it works)
From the record alone: the mission leaves Concept v1, Constitution v1, Architecture v1
and Roadmap v1 as verified artifacts with provenance into corpus sources; a
disposition table covering the corpus's extracted claims; a decision queue containing
only owner-judgment items (each with why-owner, recommendation, reversibility,
evidence); and an adversarial-review trail showing independent reviewers attacked the
synthesis before freeze.

## 9. Open questions (interview the owner before planning)
Q1. The constitution's actual content — the assistant's candidate 10–20 rules are
hypotheses, explicitly not pre-decided.
Q2. The example owner question: optimize initially as single-company internal OS vs
multi-customer platform (flagged as genuine owner judgment, unanswered).
Q3. When Kernel v1 actually freezes, and exactly which input snapshot ("Recompile
Source Cut") the mission receives.
Q4. Does Recompile become a recurring capability (the assistant's "recompilable
organization" — selective invalidation on new model generations / world shifts) — not
owner-decided.

## 10. Process for this brief
1. Clarify: first send a subagent to read `nortropic-recompile-design-rationale.md`
   (its rejection and unresolved sections cover most §9 rationale) and report back
   what bears on §9; only if the rationale lacks the needed evidence, exact source
   wording matters, or a conflict/ambiguity remains, have it read the targeted message
   ranges in the source conversation via the rationale's retrieval map — never the
   whole transcript, and keep both out of main context; then interview the owner on §9
   (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code ("address all notes, don't
   implement yet").
3. On explicit owner approval, persist the exact approved plan as
   `nortropic-recompile-approved-plan.md`, validate it
   (`scripts/plan_contract.py validate`), bind it into this frontmatter
   (`approved_plan` + `approved_plan_sha256` + `plan_version`) and only then set
   `status: planned`. Nothing is summarized away; a short execution prompt never
   replaces the plan file.
4. Implement in a fresh session, started from the approved plan:
   `plan_contract.py resume --slug nortropic-recompile --target-repo <repo>` proves
   the plan identity; reconcile the plan against current repository truth before
   continuing. After any compaction, re-read the plan from disk — never reconstruct it
   from memory; if it cannot be proven, STOP with `PLAN_IDENTITY_UNAVAILABLE`.
5. Adversarial review: fresh subagent checks the diff against this brief and the
   approved plan; report only gaps affecting correctness or stated requirements.
6. Traceability: commit messages cite this brief's slug.

## References
- Source conversation: `nortropic-recompile-full-chat.md` (same folder)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
