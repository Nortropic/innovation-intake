---
title: "Nortropic Planning Wall — design rationale"
type: design-rationale
status: source-derived
slug: nortropic-planning-wall
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: nortropic-planning-wall-full-chat.md
execution_brief: idea-nortropic-planning-wall.md
authority: non-authoritative-rationale
fidelity: full
context_revision: 1
---

# Design rationale: Nortropic Planning Wall

## 1. Core thesis
"Det du saknar är inte kontrollrummet. Du saknar väggen framför kontrollrummet"
(← msg 6): Nortropic already has execution management (Factory Room, controller as
sole truth, `SNAPSHOT_WINS`); the missing layer is *work management* — what is
Nortropic doing as a whole, why, what waits, what's next. The Planning Wall is a view
above the existing state machine, built on the principle that a human may express
intention while the machine must prove reality — the philosophical inverse of
drag-a-card-to-DONE project tools (← msg 6).

## 2. Problem / current state / intended outcome
The owner's problem is separation and overview: "lättare hålla isär alltihop"
(← msg 1). Documentation gives memory/contracts; autonomous loops give execution;
between them there is no good visual panel for what is happening now (← msg 2,
ASSISTANT INFERENCE endorsed by the commission). The intended outcome (assistant
formulation): compress hundreds of thousands of lines of code, docs, verifications
and commits into five answerable questions — what are we trying to achieve, what's
happening, what's stuck, what needs me, what is proven done (← msg 2).

## 3. Reasoning chain
The first proposal (pre-inspection) was "Nortropic Mission Control": AI-native
scrum/kanban/Shape-Up/Linear hybrid on GitHub Projects, one datamodel with many
views, three clocks, Human Decision WIP (← msg 2). The owner's question "did you
actually inspect the repos?" (← msg 3) exposed that as designed against a
*conception* of Nortropic; the assistant conceded and defined the real analysis:
Nortropic today → coordination problems → what others solve well → what doesn't fit
AI-native development → native architecture (← msg 4). The owner ordered it ("gör
det", ← msg 5). Inspection then materially changed the design (← msg 6): (a)
Verkstadsgolvet/Factory Room already implements execution management (Maskinen plan,
`SNAPSHOT_WINS`, MaskinShell's IN→ARBETET→UT narrative); (b) the repo's own
contracts forbid a second task list (`tasks.spec.json`), read doneness from ATTEST
never state (taskval), and declare "Loggen är sanningen; SQLite är projektionen" —
so a classic board where dragging mints truth is philosophically opposed to
Nortropic; (c) hence Planning Wall as a *view*: five columns compressing the 11
canonical states, three zoom levels, Intent/Reality card split, and the discovery
that the needed swimlanes (SYSTEM_IMPROVEMENT / CUSTOMER_PRODUCTION) and the owner
attention state (`OWNER_ACTION_REQUIRED`) already exist. External sweeps (Plane,
OpenProject, Leantime, HumanLayer/12-factor-agents, OpenHands Agent Canvas) mostly
validated existing Nortropic decisions; OpenProject served as the negative reference
("we shall not build Jira") (← msg 6). A planes model emerged: Discovery
(innovation-intake) / Planning (owner intent) / Execution (controller) / Verification
(gates) / Evidence (attestation+Git) / Knowledge / Interface (← msg 6). After msg 6
the owner went silent; a daily watch automation was activated via UI widget and
msgs 8–15 grew the model with eight-plus architecture layers — all assistant-only,
unratified (← msg 7–15).

## 4. Design decisions and why
(D1–D3 are owner-backed; the elaborations are assistant design under those messages.)
D1. Ground the design in repo reality before deciding anything.
    Why: a scrum layer over an imagined Nortropic would duplicate the control room
    that already exists.
    Evidence: the recommendation flipped completely after inspection — from "build
    Mission Control" to "add a wall view".
    Source: (← msg 3, 5; 2 vs 6)
D2. Planning Wall as a view inside Verkstadsgolvet, columns as compression.
    Why: the finer state vocabulary already exists
    (RAW→PLANNING→NEEDS_SPEC→READY→QUEUED→WORKING→VERIFYING→REVIEWING→MERGING→DONE,
    plus STOPPED); five human-facing columns are a projection, so no second truth
    machine is created.
    Evidence: explicit mapping SHAPE=RAW·PLANNING·NEEDS_SPEC … PROVE=VERIFYING·
    REVIEWING·MERGING; "It is a view, not a new truth".
    Source: (← msg 5; 6)
D3. Intent/Reality split per card.
    Why: the human owns cycle/priority/initiative/desired outcome; the machine owns
    state/candidate/gate/attestation — traditional PM conflates them; Nortropic need
    not.
    Evidence: the two-plane card sketch; "FROZEN får helst inte sättas genom att
    Johnny drar ett kort med musen".
    Source: (← msg 5; 2, 6)
D4. Decoupled clocks; rituals become generated artifacts.
    Why: agents work event-driven in minutes; humans focus weekly; strategy moves in
    6–12 weeks — one calendar cannot serve all three. Sprint planning → short weekly
    goal choice; daily scrum → auto-generated owner briefing; review → what was
    actually verified/published; retro → flow analysis.
    Evidence: the three-clock section and ritual remapping.
    Source: (← msg 1, 5; 2, 6)
D5. Human Decision WIP as the scarcest-resource metric.
    Why: the binding constraint is the owner's attention/decision capacity, not
    tokens or CPU; `OWNER_ACTION_REQUIRED` already persists the needed state.
    Evidence: cap ~3 proposal; "15 samtidiga frågor = systemet har misslyckats".
    Source: (← msg 1, 5; 2, 6)
D6. Flow diagnostics, no story points.
    Why: task cost varies wildly across models and days; points would be misleading
    and metric-targets create Goodhart pressure — metrics stay diagnostic.
    Evidence: explicit metric list (age, blocked age, cycle time, throughput,
    verification fail rate, rework, intervention rate, autonomous completion rate).
    Source: (← msg 1; 2, 6)

## 5. Explicit rejections / anti-requirements
REJECTED: Classic Scrum verbatim (calendar sprints, story points, meetings).
WHY: agent execution is continuous/event-driven; estimates decay with model shifts.
FAILURE IT WOULD CREATE: agents idling for sprint boundaries; velocity theater.
SOURCE: (← msg 1; 2, 6)

REJECTED: Five separate boards / a new Mission Control system.
WHY: separate boards recreate fragmentation; the control room already exists —
duplicating it forks truth and maintenance.
FAILURE IT WOULD CREATE: a second dashboard/scheduler/trust system the repo contracts
explicitly forbid.
SOURCE: (← msg 5; 2, 6)

REJECTED: GitHub Projects as main UI / any UI minting runtime truth.
WHY: dragging a card mutates field values — the UI would author state; in Nortropic
the machine proves reality (ATTEST over state, log over projection).
FAILURE IT WOULD CREATE: a stale "done" contradicting reality with no mechanism to
notice; authority leaking into a display surface.
SOURCE: (← msg 5; 6)

REJECTED: R-rounds as their own cards.
WHY: R116…R120 are internal mechanics of one semantic work unit; the wall shows the
unit, the inspector shows the rounds.
FAILURE IT WOULD CREATE: a wall of internal mechanics again — the original problem.
SOURCE: (← msg 5; 6)

## 6. Explored but unresolved
All items below are ASSISTANT PROPOSALS with no owner response — never promote to
decisions without an owner delta:
- V1 board spec (columns, förvaltningar, fields, views, WIP rules, transitions) —
  proposed as next step, never commissioned (← msg 6).
- Watch-derived layers, msgs 8–15 (each anchored to an external pattern):
  Planning-Wall-commands-intent vs Factory-reports-reality (Symphony); Deliberation
  lane — discuss without acting (GitHub side-chat); append-only Plan Revisions at
  outcome barriers (OMA); approved-plan-as-anchor + honest-or-absent estimates
  (control-center); Steering Input as immutable operator-feedback objects (GitHub
  steering); `execution_origin` provenance (Codex thread-source); Admission
  Controller — READY ≠ wise to admit now, legitimate NO-OP (GitHub Issue Monster);
  Owner Attention as derived projection, question-only, bound to issuing context
  (control-center + Codex); Activity Evidence Overlay — Declared vs Observed,
  divergence is an alarm never a verdict (AgentTrail); Causal Trace Plane (W3C
  traceparent); foreground/background observation tiers (Claude Code 2.1.251);
  Hierarchical Resource Envelope — tree-wide budget (Codex 0.151); Tool Result Plane
  RAW→PROCESS→PRESENTED (Codex MCP interception); Trajectory Quality Plane +
  Factory Pattern Observatory (gh-aw graders); Context Revision ≠ Authorization
  Revision (Codex Guardian) (← msg 8–15).
- Cycle length (1 week) and Human Decision WIP cap (~3) — starting values only
  (← msg 2, 6).

## 7. Important trade-offs / tensions
- Human steerability vs machine truth: every added interaction surface (wall edits,
  steering, deliberation) is designed to carry zero authority — reasoning channel ≠
  authority channel (← msg 6, 8, 9).
- Visibility vs noise: more observability must not become 20 terminal streams or an
  attention firehose; compression and strict inclusion are the recurring answers
  (← msg 2, 12, 13).
- Standing on existing contracts vs new capability: nearly every need mapped to
  something already present (work domains, OWNER_ACTION_REQUIRED, snapshot
  authority) — the design repeatedly chooses projection over new machinery (← msg 6).

## 8. Metaphor / concept → technical principle
"Silicon Valley-väggen" (the war-room wall) → glanceable whole-org state compression →
MUST NOT be copied as a big screen that owns data (← msg 1, 2, 6).
"Väggen framför kontrollrummet" → planning is a layer in front of execution, not a
second control room → MUST NOT fork the state machine (← msg 6).
"Fabrikssensorer" (factory instrumentation, msg 11) → observed activity may inform,
never rewrite the production order or quality certificate → divergence signals are
diagnostics, never verdicts (← msg 11).

## 9. External evidence mentioned in the conversation
All MENTIONED IN SOURCE (assistant research); none INDEPENDENTLY VERIFIED during this
packaging run: Scrum Guide, Kanban flow metrics, Shape Up, Linear method, GitHub
Projects docs (← msg 2, 6); Plane, OpenProject (negative reference), Leantime,
HumanLayer/12-factor-agents, OpenHands Agent Canvas (← msg 6); OpenAI Symphony,
GitHub side-chat + /tasks, OMA adaptive recovery, Kandev (← msg 8); GitHub Agentic
Workflows steering PR #55171, Codex --thread-source PR #40161 (← msg 9); GitHub Issue
Monster admission pattern (← msg 10); AgentTrail (← msg 11); SamuelAlev/control-center,
gh-aw v0.87.8 cross-run clustering (← msg 12); Claude Code v2.1.251, Codex
question-only async attention + issuing-step approvals, Codex W3C traceparent
(← msg 13); Codex 0.151.0 tree-wide budgets + MCP result interception (← msg 14);
gh-aw v0.87.10 trajectory graders, Codex Guardian authorization revision (← msg 15).
In-repo files cited via chips (nortropic-control-room-plan-v1.md, MaskinShell,
tasks.spec.json, taskval, snapshot.ts) are repo references whose truth lives outside
this corpus.

## 10. Evolution / pivots
1. Mission Control on GitHub Projects → owner's inspection challenge → Planning Wall
   as a view inside Verkstadsgolvet (← msg 2 → 3–5 → 6).
2. "Nortropic needs Scrum" → "Nortropic needs a visual planning wall where human
   intention and machine-proven reality are strictly separated" (← msg 1 → 6).
3. Three-concept model (Intent/Reality/Deliberation) → five (adding Steering,
   Provenance) → the extended watch-derived stack — entirely assistant-side evolution
   awaiting ratification (← msg 8 → 9 → 10–15).

## 11. Retrieval map

| topic | message range |
|---|---|
| Owner's founding ask | 1 |
| Pre-inspection Mission Control proposal | 2 |
| Inspection challenge and commitment | 3–5 |
| Repo-grounded Planning Wall design (core) | 6 |
| Watch automation activated | 7 |
| Symphony / deliberation / plan revisions / Kandev | 8 |
| Steering input; execution-origin provenance | 9 |
| Admission Controller / legitimate NO-OP | 10 |
| Activity Evidence Overlay (Declared vs Observed) | 11 |
| Attention projection; Plan Studio; cross-run observatory | 12 |
| Observation tiers; question-only attention; trace plane | 13 |
| Resource envelope; Tool Result Plane | 14 |
| Trajectory Quality Plane; authorization revision | 15 |

## 12. What to load when
DEFAULT IMPLEMENTATION: read `idea-nortropic-planning-wall.md`.
IF DESIGN RATIONALE IS NEEDED: read this file.
IF EXACT SOURCE EVIDENCE IS NEEDED: read only the relevant message ranges in
`nortropic-planning-wall-full-chat.md` (use §11).
Do not preload the raw transcript into the main implementing context.
