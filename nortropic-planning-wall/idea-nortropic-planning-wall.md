---
title: "Nortropic Planning Wall: AI-native scrum/planning layer on top of Factory Room"
type: idea-brief
status: idea
slug: nortropic-planning-wall
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: nortropic-planning-wall-full-chat.md
source_conversation_2: nortropic-planning-wall-full-chat-CHAT-002.md
design_rationale: nortropic-planning-wall-design-rationale.md
intended_repo_path: nortropic-planning-wall/idea-nortropic-planning-wall.md
context_revision: 1
related: [workflow-orkestrering, nortropic-organization-os, innovation-inbox-idehantering, bevaka-frontier-ai-engineering, bootstrap-closeout-rebaseline, nortropic-aquarium, verkstadsgolvet-v2-cockpit]
---

# Idea brief: Nortropic Planning Wall

## 1. Summary
The owner wants a scrum-like layer "för att lättare hålla isär alltihop" (← msg 1) and
steered the design to actual repo grounding ("gör det", ← msg 5). The repo inspection
flipped the recommendation: do NOT build a new Mission Control —
Verkstadsgolvet/Factory Room is already execution management; what is missing is work
management. The Planning Wall is therefore a VIEW inside Verkstadsgolvet: five columns
(SHAPE/READY/BUILD/PROVE/DONE) as pure compression of the existing canonical task
states, with human intent and machine-proven reality strictly separated ("FROZEN is
never set with the mouse").

## 2. Context you need
Nortropic already has execution management: Factory Room / MaskinShell with the
controller as sole truth authority, `SNAPSHOT_WINS`, doneness read from ATTEST never
from state, and two locked work domains (SYSTEM_IMPROVEMENT, CUSTOMER_PRODUCTION)
(in-source repo inspection, msg 6). The missing layer answers "what is Nortropic doing
as a whole, why, what's next?" — work management above execution management. Important
caveat: the owner has not ratified any architecture detail after msg 5; the concrete
Planning Wall model is the assistant's repo-grounded proposal, and msgs 8–15 are
assistant-only watch reinforcements (unratified proposals, held in the rationale).

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
- A Planning Wall view inside Verkstadsgolvet/Factory Room: an abstraction layer above
  the existing state machine, per work domain (swimlanes already exist), giving three
  zoom levels: Planning Wall → Factory Room → Task Inspector.
- Intent/Reality split per card: the human owns cycle, priority, initiative, desired
  outcome; the machine owns state, PASS, attestation, candidate identity, "done".
- Decoupled clocks: ~1-week human cycle, event-driven continuous agent execution, a
  6–12-week strategic clock; scrum rituals become owner briefings/reviews generated
  from reality, not meetings.
- Human Decision WIP as a first-class measure (initial cap ~3 concurrent owner
  decisions — assistant starting value).
- Flow metrics as diagnostics (age, blocked age, cycle time, throughput, verification
  fail rate, intervention rate) — no story points, no metric the agent optimizes.
- Choose architecture/decomposition yourself, within §6.

## 4. Decisions already made (do not relitigate silently)
D1. Nortropic needs a scrum-like layer to keep the work apart — "arbeta innovativt med
en scrum skulle också vara hjälpsamt … Brainstorma kring detta" — because the owner
should not have to carry the system's complexity in his head to understand the state
(← msg 1; 2).
D2. The design must be grounded in actual inspection, not in an imagined Nortropic —
the owner's challenge "Jag antar du kollade igenom repos på Github för inspiration?"
exposed that no repo inspection had happened — because designing a scrum layer on a
mental model of Nortropic risks duplicating what already exists (← msg 3; 4).
D3. "gör det" — perform the review of Nortropic's own repos plus two external GitHub
sweeps (PM systems; agent-orchestration repos) before deciding board, states or
implementation — because that analysis level precedes any board decision (← msg 5; 6).

R1. Classic Scrum verbatim (calendar sprints, story points, five separate boards) —
because agent feedback loops are event-driven and model capability shifts make
point estimates misleading; separate boards recreate the fragmentation the idea is
meant to fix (← msg 1; rejections 2, 6).
R2. Building a new Mission Control system — because repo inspection showed
Verkstadsgolvet/Factory Room already is the control room; what's missing is the wall
in front of it, not another system (← msg 5; 6).
R3. GitHub Projects as the main UI — because dragging a card mutates field values,
i.e. the UI would mint runtime truth; GitHub Projects may at most be a secondary
planning/portfolio mirror that never owns runtime state, gate verdicts, attestation or
"done" (← msg 5; 6).

## 5. Acceptance criteria (v1)
AC1. WHEN the Planning Wall renders work, human intent (cycle/priority/initiative) and
machine-proven reality (state/candidate/gate/attestation) SHALL be visibly separate,
and no wall interaction SHALL be able to change machine-owned truth (← msg 1, 5; 6).
AC2. WHEN the wall's columns are computed, THEY SHALL be a pure view-compression of
the existing canonical task states (SHAPE/READY/BUILD/PROVE/DONE + interrupt) — no new
controller states are created (← msg 5; 6).
AC3. WHEN the owner opens the wall, HE SHALL be able to answer at a glance: what are
we trying to achieve, what is happening, what is stuck, what needs me, what is proven
done — with drill-down Wall → Factory Room → Task Inspector (← msg 1, 5; 2, 6).
AC4. WHEN owner decisions queue up, THE wall SHALL show Human Decision WIP against its
cap and the system SHALL prefer agent-safe work over generating further owner
decisions when the cap is reached (← msg 1, 5; 2, 6).
Caveat: AC1–AC4 rest on assistant elaboration (msgs 2, 6) after the owner's adoption
messages; details are unratified — confirm in the §9 interview.

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)
Invariants pointer: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`); pointer only.
Suggestions from the source: build on what exists (work domains, canonical states,
`SNAPSHOT_WINS`, `OWNER_ACTION_REQUIRED` in taskval — the attention queue is not new
machinery); R-rounds (R116…R120) live inside a card's timeline/inspector, never as
separate cards; internal review mechanics must not become a wall of cards; metrics are
diagnostics, never targets (Goodhart); the org-os brief's R5 (UI/board as source of
truth is REJECTED) binds this design; consistency with "Loggen är sanningen; SQLite är
projektionen".

## 7. Out of scope (v1)
- All watch-derived layers (msgs 8–15, assistant-only, unratified): Admission
  Controller, Owner Attention projection, append-only Plan Revisions, Activity
  Evidence Overlay, Causal Trace Plane, Hierarchical Resource Envelope, Tool Result
  Plane, Trajectory Quality Plane, Deliberation lane, Steering Input,
  execution-origin provenance — rationale material for the architecture phase.
- The Aquarium track (CONV-005) — boundary between Planning Wall, Factory Room and
  Aquarium is an open review question.
- GitHub Projects mirroring (at most secondary, later).
- Building a standalone PM product or replacing the controller/state machine.

## 8. Verification (how we know it works)
From the record alone: a review of the delivered view proves (a) every wall column
value is derivable from canonical controller state with a documented mapping and no
new states; (b) attempted mutation of machine-owned fields through the wall is
rejected and logged; (c) a walkthrough shows the five owner questions answerable with
three zoom levels; (d) Human Decision WIP is computed from persisted
owner-action-required state, not manually curated.

## 9. Open questions (interview the owner before planning)
Q1. The owner has taken no position on any architecture detail after msg 5 — confirm
or amend the Planning Wall model itself (columns, Intent/Reality split, zoom levels,
clocks) before planning.
Q2. Commission the V1 board spec (columns, förvaltningar, fields, views, WIP rules,
agent-state transitions)? Proposed as next step, never ordered.
Q3. Boundary against the Aquarium track (CONV-005) and explicit alignment with the
org-os brief's R5 ("UI/board as source of truth" rejected) — make the relations
explicit at packaging/planning time.
Q4. Cycle length (1 week proposed) and Human Decision WIP cap (~3) are assistant
starting values — set them.

## 10. Process for this brief
1. Clarify: first send a subagent to read
   `nortropic-planning-wall-design-rationale.md` (its rejection and unresolved
   sections cover most §9 rationale) and report back what bears on §9; only if the
   rationale lacks the needed evidence, exact source wording matters, or a
   conflict/ambiguity remains, have it read the targeted message ranges in the source
   conversation via the rationale's retrieval map — never the whole transcript, and
   keep both out of main context; then interview the owner on §9 (AskUserQuestion);
   append answers here.
2. Plan in plan mode; owner reviews before any code ("address all notes, don't
   implement yet").
3. On explicit owner approval, persist the exact approved plan as
   `nortropic-planning-wall-approved-plan.md`, validate it
   (`scripts/plan_contract.py validate`), bind it into this frontmatter
   (`approved_plan` + `approved_plan_sha256` + `plan_version`) and only then set
   `status: planned`. Nothing is summarized away; a short execution prompt never
   replaces the plan file.
4. Implement in a fresh session, started from the approved plan:
   `plan_contract.py resume --slug nortropic-planning-wall --target-repo <repo>`
   proves the plan identity; reconcile the plan against current repository truth
   before continuing. After any compaction, re-read the plan from disk — never
   reconstruct it from memory; if it cannot be proven, STOP with
   `PLAN_IDENTITY_UNAVAILABLE`.
5. Adversarial review: fresh subagent checks the diff against this brief and the
   approved plan; report only gaps affecting correctness or stated requirements.
6. Traceability: commit messages cite this brief's slug.

## References
- Source conversation: `nortropic-planning-wall-full-chat.md` (same folder)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

## Episode 2 (CHAT-002, captured 2026-09-01)

`nortropic-planning-wall-full-chat-CHAT-002.md` is the same conversation (Improvements
sweep CONV-006) at revision 2: one new message (← CHAT-002 msg 16), an assistant watch
report dated 1 sep 2026. EXTERNAL EVIDENCE + PROPOSAL (assistant synthesis — the owner
has not ratified it in-thread):

- Trigger: OpenAI Codex 0.152.0 (2026-09-01) built automatic reconnection for
  app-server sessions with a strict safety semantics — no user operation is ever
  auto-retried; uncertain pre-drop input is quarantined; completions from a dead
  connection generation may not trigger new actions (← CHAT-002 msg 16).
- Proposed new Factory Room principle: **observability recovery ≠ mutation recovery**.
  On connection loss: LIVE → DEGRADED/READ-ONLY (keep last authoritative snapshot,
  quarantine unconfirmed commands, ignore old-generation completions, never
  auto-replay mutations) → RECONCILE (resume authoritative thread, resolve every
  uncertain command_id, verify connection generation) → WRITE PLANE RESTORED. Bind to
  `command_id + issued_against_watermark + connection_generation`; an uncertain
  command outcome presents as `UNCERTAIN`, never "failed"/"not sent", and is never
  auto-resent (← CHAT-002 msg 16).

Treat as a design-input candidate for activation: it extends §3's degraded-mode
thinking but is not an owner decision.
