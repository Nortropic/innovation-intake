---
title: "Nortropic as a municipality: central governance, shared infrastructure, autonomous förvaltningar"
type: idea-brief
status: idea   # lifecycle: idea → clarified → planned → building → verified; terminal: superseded
slug: nortropic-som-kommun
owner: Johnny (Nortropic)
created: 2026-08-20
source_conversation: nortropic-som-kommun-full-chat.md   # reference only — this brief takes precedence
intended_repo_path: nortropic-som-kommun/idea-nortropic-som-kommun.md
---

# Idea brief: Nortropic as a municipality — central governance, shared infrastructure, autonomous förvaltningar

## 1. Summary

An organizational mental model: **Nortropic is the municipality; the web agency is
merely its first förvaltning (administration).** Central governance (control plane,
policy, identity, evidence, economy, innovation, monitoring) plus shared
infrastructure (Factory, Verkstadsgolvet, agent identities, evidence, knowledge)
support multiple self-governing business areas that each own their domain model,
backlog, workflows and KPIs — so new areas (Sales, Finance, Research, …) can be added
without rebuilding the core. The key caveat is the framing decision: **copy the
separation (mandate → responsibility → domain → shared governance), never the
municipality's bureaucratic slowness** — a "digital, agentic municipality" where
förvaltningar execute autonomously within delegated mandates.

## 2. Context you need

Nortropic today is mostly one business (web production) plus the system that builds
systems. Without an explicit organizational model, "Nortropic" and "the web factory"
blur together. The chat's analogy table maps: kommunfullmäktige = owner/constitution;
kommunstyrelse = strategic control plane; nämnd = per-area governance; förvaltning =
e.g. Web Production; delegationsordning = capabilities/permissions; ärende = task;
diarium = event/evidence/audit trail; beslut = authority transition; internrevision =
reviewer/Quality Gauntlet. This aligns with the existing trust architecture: roles
organize work; frozen gates and actually delegated authority decide what may happen.
This is a single-exchange concept chat — one owner proposal, one confirming
elaboration; no execution decisions were made.
Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen
gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

If adopted as the naming/architecture frame:

- Nortropic's central layer is explicitly the "kommunledning": governance, policy,
  identity/permissions, evidence, prioritization, shared data, innovation, world
  monitoring.
- The Factory, Verkstadsgolvet, agent runtime, evidence and knowledge systems are
  explicitly **shared infrastructure**, not properties of the web business.
- Web Production becomes the first named förvaltning with its own mandate: intake →
  specification → design → build → verification → delivery → monitoring →
  improvement, run autonomously within its delegation.
- The central layer intervenes only on: new policy, new budget, new capability, risk
  transitions, strategic choices, exceptions.
- New förvaltningar can be chartered later without core rebuilds, sharing identity,
  authority, knowledge, audit, task infrastructure, agent runtime, observability,
  governance and continuous improvement.

Choose architecture/decomposition/tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

- D1. The framing itself is Johnny's proposal, confirmed and extended in-chat:
  "Nortropic är kommunen; webbyrån är bara en av dess första förvaltningar" — because
  the architecture can then carry businesses that don't yet exist (← msg 1–2).
- P1 (proposal). Factory ≠ webbförvaltningen: the factory is shared production/
  administration infrastructure usable by several förvaltningar — because tying it
  to one business would force a rebuild for every new verksamhetsområde (← msg 2).
- R1 (REJECTED). Copying municipal inertia — committee meetings, silos, long decision
  paths; only the separation of mandate/responsibility/domain/governance is wanted
  (← msg 2).

## 5. Acceptance criteria (v1 — if the model is adopted)

- AC1. WHEN the model is adopted, THE documentation SHALL name the central layer, the
  shared infrastructure and each förvaltning explicitly, with the analogy table's
  mappings anchored to real components.
- AC2. WHEN a förvaltning acts within its delegated mandate, THE central layer SHALL
  NOT be in its execution path (only in its audit trail).
- AC3. WHEN an action crosses a mandate boundary (policy, budget, capability, risk,
  strategy, exception), THE system SHALL require the central/owner path.
- AC4. WHEN a new förvaltning is chartered, THE core (identity, authority, evidence,
  task infrastructure) SHALL be reused without modification.

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants: Nortropic's trust layer — constitution & rulebook (pointer, never a copy).
This is primarily a naming/structuring lens: apply it first in documentation and the
knowledge repo's architecture sections; only later (if at all) in code-level
boundaries. The delegation concept maps naturally onto existing capabilities/
allowed_write mechanisms — prefer anchoring the metaphor in those rather than
inventing parallel constructs.

## 7. Out of scope (v1)

- Building any new förvaltning beyond web production.
- Reorganizing repos or code to match the metaphor before it has proven useful in
  documentation.
- Municipal process theater (boards, meetings, formalism) — explicitly rejected (R1).

## 8. Verification (how we know it works)

From the record alone: the architecture documentation names the three layers and maps
them to real components (AC1); one traced task shows the central layer absent from a
mandate-internal execution path (AC2) and present in one boundary-crossing decision
(AC3).

## 9. Open questions (interview the owner before planning)

- Q1. Is this the official organizational frame for documentation/knowledge-repo
  architecture sections, or a thinking lens only?
- Q2. Should "Web Production" be formally chartered as förvaltning #1 with an explicit
  written mandate (delegationsordning)?
- Q3. Which existing components get the "shared infrastructure" label first —
  Factory, Verkstadsgolvet, evidence, knowledge — and does anything currently sit in
  the wrong layer?
- Q4. What is the second förvaltning candidate, and when would chartering one become
  worth the overhead?

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

- Source conversation: `nortropic-som-kommun-full-chat.md` (same folder)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
