---
title: "Context & orchestration contract: kill copy/paste handoffs, operator portal, learning fabric"
type: idea-brief
status: idea   # lifecycle: idea → clarified → planned → building → verified; terminal: superseded
slug: workflow-orkestrering
owner: Johnny (Nortropic)
created: 2026-08-20
source_conversation: workflow-orkestrering-full-chat.md   # reference only — this brief takes precedence
intended_repo_path: workflow-orkestrering/idea-workflow-orkestrering.md
related: [nortropic-frontier-delta, snabba-upp-loopar, innovation-inbox-idehantering, dokumentation-repo-struktur, brainstorming-arbetsfloden, brainstorma-nortropic-engineering, bevaka-frontier-ai-engineering]
---

# Idea brief: Context & orchestration contract — kill copy/paste handoffs, operator portal, learning fabric

## 1. Summary

Replace the human/chat copy-paste transport of context between ChatGPT, Johnny, Codex
and Claude Code with a repository-native contract: decisions compile into **canonical
work orders**, agents start from `TASK_ID + ROLE + RUN_ID` and reconstruct their own
context, Verkstadsgolvet becomes an **operator portal / digital twin** over canonical
state, and a **Learning Fabric** (Engelbart's A/B/C loops) sits on top — all while the
existing trust architecture stays untouched. The framing decision: **"keep our trust
architecture; replace our context-transport architecture."** This chat also produced
the decided step order and the SYSTEM ARCHAEOLOGY mission that appears to have started
the current bootstrap.

## 2. Context you need

Nortropic already has frozen specs/gates, allowed_write, candidate identity,
builder/reviewer separation, evidence contracts and an owner final gate. The failure
mode is above that layer: context historically traveled as giant prompts, chat history
and manual evidence pasting — every hop risking context loss, drift, stale state and
wrong SHAs. OpenAI/Anthropic/GitHub have converged on repo-native knowledge +
executable plans + small agent contexts + persistent external state. NOTE: the final
section of this chat (a read-only SYSTEM ARCHAEOLOGY inventory mission for Claude Code,
Aug 15) appears to be the origin of the currently running bootstrap — at pull time,
re-check which parts of this brief are already operationalized in `nortropic-system`.
Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen
gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- **Canonical work orders**: a brainstorm ends at a compilation boundary — task_id,
  goal, context refs, constraints, non-goals, acceptance criteria, decisions, evidence
  requirements — written into existing canonical stores (tasks.spec, plans/ExecPlan
  bound to existing task IDs; **no parallel backlog**).
- **Context Resolver → Context Manifest**: per task/role/run, a deterministic,
  hash-identified minimal context package (authority refs, decisions/ADRs, relevant
  docs, prior findings). Context identity becomes reproducible like candidate identity.
- **Knowledge model in four lanes**: stable knowledge (AGENTS.md as short router;
  CLAUDE.md imports `@AGENTS.md` + Claude specifics), decision memory (ADR-style with
  alternatives/why/supersedes), task context (refs, not the whole library), runtime
  state/evidence (never in docs). Handoffs become **generated recovery snapshots**;
  canonical state wins on conflict.
- **Verkstadsgolvet = operator portal / digital twin**: e-service UX ("Mina ärenden",
  start/follow/decide), typed Operator API/MCP (intake.submit, inspect, run.start/pause,
  owner.decide), conversational frontend (ChatKit and/or a ChatGPT MCP app) — multiple
  frontends over one control plane; the portal owns no state.
- **Learning Fabric** (later, on top of a working factory): A-loop does work, B-loop
  mines runs and proposes improvements, C-loop improves the learning process itself; a
  Dynamic Knowledge Repository; external sources enter via
  source → principle → hypothesis → experiment → evidence → decision — never straight
  to authority; an Acceleration Firewall keeps authority transitions explicit and
  evidence-driven no matter how fast intelligence scales.

Choose architecture/decomposition/tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

- D1. ChatGPT is NOT Nortropic's runtime orchestrator — it is the thinking partner;
  the controller orchestrates machines — because every human/chat transport hop loses
  context and the S3-handoff pattern is a recovery mechanism, not a normal transport
  (← msg 5, 21).
- D2. Step order validated by Johnny: inventory current state first → establish
  workflow + documentation/context model → build task by task through the existing
  trust chain — because measuring reality precedes designing on top of it (← msg 20–21).
- D3. Claude Code gets mission 1: a strictly read-only SYSTEM ARCHAEOLOGY inventory
  (full prompt preserved in msg 25), then a FRESH context does architecture/migration,
  then the factory builds slice by slice — because an agent must not both interpret
  and mutate the current state (← msg 22–25).
- D4. No parallel sources of truth: no tasks-v2, no ChatGPT-state.md; ExecPlans bind
  to existing canonical task IDs (← msg 5).
- D5 (REJECTED). Building on OpenAI Agent Builder — rejected because OpenAI is
  retiring it (announced Jun 3 2026, shutdown Nov 30 2026); ChatKit + own server-side
  implementation is the recommended path (← msg 10).
- D6 (REJECTED). One giant NORTROPIC_CONTEXT.md / monolithic AGENTS.md — rejected
  because oversized instruction files go stale and crowd out the task (← msg 5, 13).
- D7 (REJECTED). "Big rewrite from a finished future architecture" — rejected in favor
  of incremental fail-closed slices (← msg 21).
- P1 (proposal). Typed transition kernel: lifecycle states as types
  (merge(OwnerApprovedCandidate), never merge(Candidate)); functional core /
  imperative shell for the controller (← msg 17, 19).
- P2 (proposal). Learning principle: experience may PROPOSE learning; it may never
  itself change authority; owner gate may be a deliberate trust constraint — "eliminate
  the bottleneck" must never resolve to "eliminate Johnny" (← msg 15, 19).

## 5. Acceptance criteria (v1)

- AC1. WHEN a decided idea becomes work, THE system SHALL produce a canonical work
  order bound to an existing task ID, and no agent SHALL need the chat log afterwards.
- AC2. WHEN a worker starts, THE controller SHALL hand it `TASK_ID + ROLE + RUN_ID`
  plus a hash-identified Context Manifest, and THE record SHALL show exactly which
  sources the agent received.
- AC3. WHEN a ChatGPT/Claude/Codex session dies or the machine restarts, THE task's
  state (run state, decisions, SHAs, evidence, next legal transitions) SHALL survive
  and be reconstructible without human retelling.
- AC4. WHEN Claude Code and Codex load repository instructions, THEY SHALL consume
  the same authority (CLAUDE.md importing AGENTS.md), with only agent-specific deltas.
- AC5. WHEN the operator portal or any chat frontend requests an action, THE action
  SHALL pass through the typed Operator API into the controller — UI ≠ capability,
  chat ≠ authority.

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants: Nortropic's trust layer — constitution & rulebook (pointer, never a copy).
Suggestions from the chat: fresh context is a feature — reviewers see diff + criteria,
never the builder's life story; machine-to-machine handoffs as structured artifacts
with human reports rendered on top; portal knowledge section built on provenance-aware
knowledge objects (authority_class, superseded_by, content_hash) so agents can do
"software archaeology"; evidence-first UX (never "SYSTEM HEALTH: 98%"); Goodhart-guard
the learning metrics with opposing signals.

## 7. Out of scope (v1)

- Any redesign of the existing trust architecture (explicitly preserved, D1/§2).
- OpenAI Agent Builder (rejected, D5); retraining/fine-tuning models as the learning
  mechanism (the system learns, not the weights — fine-tuning is a possible later
  stage only).
- Building Learning Fabric before the factory + context layer works (ordering, D2).
- A parallel backlog or second source of truth (D4).
- Loop-speed mechanics (Task Capsule overlap) — covered by related brief
  `snabba-upp-loopar`; external monitoring/Evolution Loop — covered by related brief
  `nortropic-frontier-delta`.
- Explored-but-unresolved side threads from the chat's book section — capability
  zones (empirical model/task routing) and the wider book-synthesis reading list —
  parked here, not decisions; capability zones are carried forward in
  `brainstorma-nortropic-engineering` (Capability Map).

## 8. Verification (how we know it works)

End-to-end: take one real idea from a ChatGPT session through the full chain — compile
to canonical work order (AC1) → controller dispatches a worker with task-ID + manifest
(AC2) → kill the originating chat session mid-run and show the run completes and is
auditable from the record alone (AC3) → the same run inspected via the operator API
(AC5). An independent reviewer confirms every step from the record, including that no
step required pasting chat content between agents.

## 9. Open questions (interview the owner before planning)

- Q1. This chat spans three sizeable ideas (context/orchestration contract; operator
  portal; learning fabric). Keep as one brief or split into separate corpus ideas?
- Q2. Which parts are already operationalized by the running bootstrap (the msg-25
  archaeology mission and its successors), and what does that make this brief's
  remaining scope?
- Q3. Operator API surface: MCP-only, HTTP+MCP, or controller-CLI first? And is
  ChatKit actually wanted for v1 of the portal?
- Q4. Where do ADRs live relative to the existing beslutslogg — new docs/decisions/
  structure or evolve the current one?
- Q5. Is the typed transition kernel (P1) a target for the controller now, or a
  NEEDS-EVIDENCE experiment after the context layer lands?
- Q6. Who authors the Context Resolver's source-of-truth map (which docs are
  authority vs reference) — owner-curated or inventory-derived?

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

- Source conversation: `workflow-orkestrering-full-chat.md` (same folder; msg 25 holds
  the full SYSTEM ARCHAEOLOGY mission prompt)
- Related briefs: `nortropic-frontier-delta/` (Evolution Loop — sibling meta-loop
  design), `snabba-upp-loopar/` (Task Capsule ≈ Context Manifest concept family)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
