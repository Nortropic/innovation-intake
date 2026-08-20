---
title: "Conversation compiler: BUILD IR, repo reconciliation and evals-before-code after intake"
type: idea-brief
status: idea   # lifecycle: idea → clarified → planned → building → verified; terminal: superseded
slug: brainstorming-arbetsfloden
owner: Johnny (Nortropic)
created: 2026-08-20
source_conversation: brainstorming-arbetsfloden-full-chat.md   # reference only — this brief takes precedence
intended_repo_path: brainstorming-arbetsfloden/idea-brainstorming-arbetsfloden.md
related: [workflow-orkestrering, arbetsmetoder-innovation, openai-anthropic-workflow]
---

# Idea brief: Conversation compiler — BUILD IR, repo reconciliation and evals-before-code after intake

## 1. Summary

With the intake skill already solving transport (chat → Claude Code), the interesting
problem moves downstream: **what happens when the chat lands**. The proposal: a
12-step chain where the chat is compiled — like source code to an intermediate
representation — into a semantic **BUILD IR**, reconciled against the repo's actual
state, specified, designed with explicit alternatives, given acceptance evals BEFORE
any code, planned, tasked, built, verified and finally mined for lessons. The framing
decision: **the chat is source of intent, never source of truth** — spec, repo, plan,
tests and Git each own their own truth. This refines the compile boundary of the
related `workflow-orkestrering` brief from the intake side; neither supersedes the
other.

## 2. Context you need

The chain: Brainstorm (high entropy, unconstrained) → Transfer (the skill carries the
RAW conversation for provenance) → **Compile** (BUILD IR: intent, problem,
current/desired state, user/business value, decisions, open questions, rejected
ideas, constraints, assumptions, research, risks, success criteria — a semantic
compilation, not a summary) → **Repo reconciliation** ("conversation says X,
repository does Y, therefore actual change is Z") → Specification (WHAT/WHY, Spec-Kit
style) → Architecture (options A/B/C, tradeoffs, SELECTED + WHY + REJECTED) →
**Evals/acceptance before code** → ExecPlan (self-contained, agent-followable without
chat memory) → Tasks (input, expected change, files, constraints, AC, dependencies,
verification) → Build → Verify (per milestone, not one big end run) → **Learn** (what
was wrong, which docs went stale, should CLAUDE.md/skills/evals change). Three
worlds: Thinking (ChatGPT/Claude chat) / Engineering (compilation→plan) / Execution
(builders, reviewers, gauntlet).
Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen
gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- The intake skill's delivery becomes the START of an engineering pipeline: after the
  brief+transcript land, a conversation-compilation step produces the BUILD IR, and a
  reconciliation step produces the DELTA against repo reality, before any spec/plan.
- "Claude Code session start ≠ implementation start" is normalized: research,
  reconciliation, specification, architecture, evals and planning all precede the
  first production-file edit.
- Acceptance evals exist before the builder builds (SPEC → ACCEPTANCE TESTS →
  IMPLEMENTATION, never "does it look good?").
- Every completed implementation runs the Learn step and can propose updates to
  CLAUDE.md, skills and evals.
- The sources-of-truth ladder is documented and observed: chat=intent, spec=desired
  behavior, repo=current reality, plan=intended change, tests=success, Git=history.

Choose architecture/decomposition/tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

The chat is exploratory; Johnny's one confirmed premise plus the assistant's
proposals:

- D1. Transport is solved and stays solved by the intake skill; the raw conversation
  is preserved unedited for provenance (← msg 4–6).
- P1. Compile, don't summarize: the BUILD IR's 13 sections are a semantic
  compilation of the discussion (← msg 6).
- P2. Repo reconciliation is the almost-always-missed step: desired state (chat) vs
  actual state (repo) → explicit DELTA before spec (← msg 6).
- P3. Evals/acceptance criteria precede implementation — because the definition of
  good must exist before the builder builds; "does it look good?" is not a gate
  (← msg 6).
- P4. End every build with a Learn step feeding persistent context
  (CLAUDE.md/skills/evals) — because that turns the system self-improving, not just
  self-building (← msg 6).
- P5 (REJECTED). "Brainstorm → send chat → Claude Code builds" as the workflow — and
  the "one giant master document" as source of truth — because chats carry dead ends
  an agent may faithfully build, and a monolith rots; each truth belongs in its own
  artifact (← msg 6).

## 5. Acceptance criteria (v1)

- AC1. WHEN an intake delivery is pulled to build, THE pipeline SHALL produce a BUILD
  IR artifact whose sections are populated or explicitly marked empty — before any
  spec is written.
- AC2. WHEN the IR exists, THE reconciliation SHALL output "conversation says X /
  repository does Y / change is Z" grounded in actual repo reads.
- AC3. WHEN implementation starts, THE record SHALL already contain acceptance
  evals/tests derived from the spec.
- AC4. WHEN a build completes, THE Learn step SHALL run and its proposals SHALL be
  recorded (even if the answer is "no changes").
- AC5. WHEN any downstream artifact conflicts with the chat, THE artifact SHALL win
  (chat is intent, not truth).

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants: Nortropic's trust layer — constitution & rulebook (pointer, never a copy).
Suggestions: the BUILD IR overlaps heavily with the nortropic-intake brief template
(decisions, rejected, open questions, constraints, ACs) — extend that template or add
a compile step to the implement-now route rather than inventing a parallel format;
Spec-Kit's specify→clarify→plan→tasks→implement is a reference shape; the Learn step
connects to the Quality Loop in `nortropic-frontier-delta`.

## 7. Out of scope (v1)

- Rebuilding intake/transport (solved by the skill).
- The operator portal and context-manifest machinery (owned by
  `workflow-orkestrering`).
- Brainstorm-phase methodology (owned by `arbetsmetoder-innovation`).

## 8. Verification (how we know it works)

End-to-end: pull one stored idébank brief through the full chain and show, from the
record alone: IR artifact (AC1), reconciliation delta with repo citations (AC2),
acceptance tests dated before the first implementation commit (AC3), and a Learn
record (AC4).

## 9. Open questions (interview the owner before planning)

- Q1. Should the BUILD IR be merged INTO the nortropic-intake brief template (one
  artifact), or be a separate compile artifact produced at pull-to-build time?
- Q2. Where does the "conversation compiler" run — as a phase of the intake skill's
  implement-now route, or as a separate skill/step in the factory?
- Q3. Reconciliation scope: whole-repo read or bounded to the areas the IR names?
- Q4. Does the Learn step feed the (future) Evolution Loop's Quality Loop, or write
  directly to CLAUDE.md/skills via owner review?
- Q5. The chat ended mid-thread ("exactly which transformation steps should the skill
  initiate") — continue that design conversation before planning?

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

- Source conversation: `brainstorming-arbetsfloden-full-chat.md` (same folder)
- Related briefs: `workflow-orkestrering/` (compile boundary, canonical work orders),
  `arbetsmetoder-innovation/` (brainstorm-phase protocol),
  `openai-anthropic-workflow/` (the transfer/harvest ancestry)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
