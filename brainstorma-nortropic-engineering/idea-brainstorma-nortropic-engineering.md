---
title: "The Nortropic engineering stack: layer taxonomy, memory model and the missing layers"
type: idea-brief
status: idea   # lifecycle: idea → clarified → planned → building → verified; terminal: superseded
slug: brainstorma-nortropic-engineering
owner: Johnny (Nortropic)
created: 2026-08-20
source_conversation: brainstorma-nortropic-engineering-full-chat.md   # reference only — this brief takes precedence
intended_repo_path: brainstorma-nortropic-engineering/idea-brainstorma-nortropic-engineering.md
related: [workflow-orkestrering, nortropic-frontier-delta, snabba-upp-loopar, bevaka-frontier-ai-engineering]
---

# Idea brief: The Nortropic engineering stack — layer taxonomy, memory model and the missing layers

## 1. Summary

A self-assessment of Nortropic against the frontier vocabulary (context / memory /
harness engineering) that produces a fuller map: Nortropic is **already strong on
harness and exceptional on trust engineering** (a fourth layer the standard
taxonomies lack — a provider-neutral trust kernel), has a good context foundation,
but **memory engineering is the largest untapped layer**. Two layers are missing as
first-class concepts: **Objective & Specification Engineering** (the bridge from vague
intent to executable TaskContract) and **Evolution Engineering**. The load-bearing
principle: **"Memory may influence reasoning. Memory may never manufacture
authority."** This brief is primarily a MAP — prime input for the coming cross-chat
rebaseline — plus two concrete build ideas (Context Compiler, the memory model).

## 2. Context you need

Assessment grounded in `nortropic-system@main` (e56edc08): the autopilot chain and
`harness-substitution-contract-v1` (provider owns sessions/reasoning/tool loops;
Nortropic owns TaskContract, containment, candidate SHA, gates, attestation,
recovery, promotion) map directly onto OpenAI's harness-engineering description;
`AGENTS.md` is already "router, not rulebook" (context routing by convention);
`nortropic-knowledge` is "context, never trust authority" with provenance rules — a
safety foundation for memory but not yet an active operational memory. The full
proposed stack: 0 Product/Intent → 1 Objective & Specification → 2 Memory/Knowledge
→ 3 Context → 4 Capability/Tool → 5 Harness/Runtime → 6 Evaluation → 7
Trust/Governance → 8 Promotion → 9 Evolution, crossed by observability,
identity/security/containment, provenance, and cost/latency planes.
Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen
gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- The layer taxonomy is adopted as the shared vocabulary for architecture
  discussions and the coming rebaseline (which briefs/components live in which
  layer; where the gaps are).
- **Nortropic Context Compiler**: `task + role + base SHA` → a reproducible
  `ContextPack` (authority refs, contract, allowed_write, relevant architecture/code
  surface/failures/decisions, capabilities, verification target) — progressive
  disclosure, not RAG-everything. (Same concept family as workflow-orkestrering's
  Context Manifest and snabba-upp-loopar's Task Capsule — one implementation should
  serve all three.)
- **Nortropic Memory Model**: five memory types (working / episodic / semantic /
  procedural / normative) where normative state is NEVER memory; memory is advisory
  input to the Context Engine only.
- **Objective & Specification Engineering** becomes a named layer: vague intent →
  problem framing → constraints → success criteria → quality bar → acceptance →
  TaskContract (the Wayfinding→Specification→Verification→Gauntlet chain as four
  epistemic functions, not necessarily four agents).
- Capability/Tool engineering is tracked separately from harness (what the agent CAN
  do vs how it works) — infrastructure configuration alone moves benchmarks.

Choose architecture/decomposition/tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

Exploratory chat; owner commissioned the mapping — the map itself is proposal:

- P1. The gap assessment: harness 🟢, trust 🟢 (exceptional), eval 🟢, context 🟡,
  memory 🟠 — don't "start doing harness engineering"; Nortropic largely IS a
  harness-engineering project (← msg 3–5).
- P2. "Memory may influence reasoning. Memory may never manufacture authority" — and
  the strict provenance/authority separation is also the defense against persistent
  memory poisoning (← msg 5).
- P3. The 10-layer stack with 4 cross-cutting planes; Objective/Specification and
  Evolution engineering added as first-class layers — because something must answer
  "what are we trying to achieve and how do we know we succeeded" before any agent
  runs, and improvement itself needs an owned layer (← msg 8–9).
- P4. Architecture ≠ implementation: parts of the substitution contract's components
  are not yet built; claims must stay tied to actual main-state (← msg 5).

## 5. Acceptance criteria (v1 — for adopting the map)

- AC1. WHEN the rebaseline runs, THE synthesis SHALL classify existing
  briefs/components against the 10-layer stack and mark each layer's maturity with
  evidence.
- AC2. WHEN a ContextPack is produced, THE pack SHALL be reproducible (same task/
  role/SHA → same pack hash) and SHALL contain references, not copied authority.
- AC3. WHEN memory influences an agent, THE record SHALL show it entered as advisory
  context — never as a source of permission or gate-relaxation.
- AC4. WHEN a task is authored, THE Objective/Specification layer's outputs (success
  criteria, quality bar, acceptance) SHALL exist before the harness dispatches it.

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants: Nortropic's trust layer — constitution & rulebook (pointer, never a copy).
Suggestions: unify ContextPack/Context Manifest/Task Capsule into ONE concept at
rebaseline time (three chats named the same thing); the memory model's episodic store
maps onto the Experience Store ideas in `nortropic-frontier-delta`; treat the planes
(observability, identity, provenance, cost) as requirements on every layer rather
than separate components.

## 7. Out of scope (v1)

- Building the Evolution layer (owned by `nortropic-frontier-delta`).
- The operator portal/UX (owned by `workflow-orkestrering`).
- Any change to trust-layer mechanics (the map celebrates them; it does not touch
  them).

## 8. Verification (how we know it works)

From the record: the rebaseline document uses the taxonomy with per-layer evidence
(AC1); one generated ContextPack regenerates bit-identically from the same inputs
(AC2); one traced run shows memory entering as advisory only (AC3).

## 9. Open questions (interview the owner before planning)

- Q1. Adopt the 10-layer stack as the rebaseline's organizing structure?
- Q2. ContextPack vs Context Manifest vs Task Capsule — one name, and which chat's
  field list wins as v1?
- Q3. Should Objective & Specification Engineering become a real pipeline stage now
  (task authoring discipline), or wait for the rebaseline?
- Q4. Where does the episodic memory store live physically (knowledge repo?
  controller state? new store), given "advisory only" and the poisoning risk?

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

- Source conversation: `brainstorma-nortropic-engineering-full-chat.md` (same folder)
- Related briefs: `workflow-orkestrering/` (Context Manifest, knowledge model),
  `nortropic-frontier-delta/` (Evolution layer), `snabba-upp-loopar/` (Task Capsule)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
