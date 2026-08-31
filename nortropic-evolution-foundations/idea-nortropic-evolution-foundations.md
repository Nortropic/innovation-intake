---
title: "Nortropic Evolution Foundations — semantic registry, causal lineage, principal identity, assumption expiry and the Evolution Loop"
type: idea-brief
status: idea
slug: nortropic-evolution-foundations
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: nortropic-evolution-foundations-full-chat.md
design_rationale: nortropic-evolution-foundations-design-rationale.md
intended_repo_path: nortropic-evolution-foundations/idea-nortropic-evolution-foundations.md
context_revision: 1
related: [bevaka-frontier-ai-engineering, nortropic-organization-os]
---

# Idea brief: Nortropic Evolution Foundations

## 1. Summary

Cross-cutting foundations Organization OS / Digital Twin must own for any projection (including Aquarium) to ever be true, from an owner-ordered gap + frontier scan: a versioned Semantic Registry, temporal semantics, causal lineage ("every story must have a proof path"), first-class Principal Identity, explicit epistemic state, process-mining readiness, Assumption Expiry, experience→eval, attention as an OS resource, an ECONOMICS overlay, interoperability awareness, quarantined simulation — and above them an institutional Evolution Loop (outside-in frontier learning + inside-out operational learning). The key framing decision: these are **mandatory design questions for the future Organization OS design phase, not additions to the current implementation** — and this scope must never become a parallel Organization OS.

## 2. Context you need

This idea is the second scope of the "Nortropic Aquarium" chat (source: `nortropic-evolution-foundations-full-chat.md`, msgs 9–18; msgs 1–8 and 14–17 carry the Aquarium scope, packaged as `nortropic-aquarium`). The owner's directive (msg 9) asked for a further substantial watch plus "what are we missing, for now and the future — brainstorma, think hard". The scan found no catastrophic missing pillar — the append-only-log-is-truth principle is unusually well positioned — but several things are not yet explicit first-class concepts. The weekly Wednesday condition-watch "Nortropic Evolution Radar" was set up in this chat; msg 18 is its first material report (DTC framework, OCEL 2.1, OTel GenAI), arriving after the owner's last message — evidence input, not owner decision.

This brief is the primary intake artifact for execution. Deeper design logic lives in the linked design rationale; the full chat is raw evidence — read targeted message ranges only if the rationale is insufficient. Current canonical repository authority beats all intake artifacts; within the intake package this brief wins over rationale and transcript. Once an owner-approved plan is bound (see the frontmatter), it carries execution order above this brief and below current repository authority.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook (`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- The five mandatory design questions answered in the future Organization OS/Digital Twin design phase: (1) Semantic Registry — versioned organizational vocabulary, "no organizational concept without observable evidence"; (2) temporal + causal lineage — when it happened, who did it, why events belong together; (3) Principal Identity — initiator/authority/orchestrator/executor/model/verifier as distinct roles; (4) process-mining readiness — canonical history can reconstruct how the organization actually works (designed vs observed conformance); (5) assumption lifecycle — assumptions as versioned hypotheses with retest triggers.
- Epistemic state separated from operational state: UNKNOWN and STALE are real states; INFERRED never looks like OBSERVED.
- An Evolution Loop as institution: frontier signal → which assumption? → IGNORE or EXPERIMENT → evidence → reject/adopt → semantics change → new evals/gates; in parallel, operational experience becomes regression cases and evals.
- Later horizons kept later: projection compatibility and conformance; then city-scale semantic zoom, economics overlay, external-agent federation (A2A/MCP awareness only), strictly separated forecasting/simulation.
- The quality formula extended to TRUE + BEAUTIFUL + CURRENT + LEARNING.

Choose architecture, decomposition and tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

D1. Continuous co-evolution/currency is a system requirement — parts must stay in relation as the system evolves; a design true at release and false a year later is also untruth ("Jag håller med") (← msg 9; msgs 6, 8).
D2. Set up an additional substantial watch — the weekly Wednesday "Nortropic Evolution Radar" condition-watch hunting structural developments (digital twins, process mining, event sourcing/replay, provenance/lineage, ontologies, agent identity, observability/evals, calm HCI, privacy, interoperability) that could age Nortropic's assumptions — not duplicating the Frontier or Aquarium watches (← msg 9; setup msg 13).
D3. Proceed to planning via nortropic-intake — the chat holds two scopes that must NOT become one giant brief, and this scope must be corpus-checked against `nortropic-organization-os` (related vs addition), never creating a parallel Organization OS (← msg 14; msg 17).

R1. Adopting external standards as canonical schema (OCEL as the canonical log, OTel Development-status fields shaping our schema, DTC simulation gates taken literally) — because canonical Nortropic truth comes first; standards become projections/exports/adapters (← msg 14 carrying the msg 13 stance into planning; deepened msg 18, which postdates the owner's last message — see Q5).
R2. "AI rewrites its own code when it wants" self-improvement — because the Evolution Loop is evidence-gated: challenge a named assumption, experiment, adopt only on evidence (← msg 14; msg 13).
R3. Scope-creeping these foundations into the current implementation — classic scope creep; they enter as mandatory questions when the Organization OS design phase starts (← msg 14; msg 13).

## 5. Acceptance criteria (v1)

AC1. WHEN the Organization OS/Digital Twin design phase begins, THE design SHALL answer the five mandatory questions (semantic registry; temporal + causal lineage; principal identity; process-mining readiness; assumption lifecycle) before the architecture freezes (← msg 14; msg 13).
AC2. WHEN any state is projected, THE system SHALL carry epistemic state separately from operational state: UNKNOWN and STALE are real states; INFERRED never looks identical to OBSERVED (← msg 9; msg 13 §7).
AC3. WHEN an architecture assumption ("models cannot reliably do X") is recorded, THE system SHALL store it as a versioned hypothesis with evidence, introduced/last-challenged dates and retest triggers (← msg 9; msg 13 §5).
AC4. WHEN the Evolution Radar or operational experience produces a material signal, THE Evolution Loop SHALL route it against a named assumption to IGNORE or EXPERIMENT, adopting only on evidence, flowing into semantics change and new evals/gates (← msg 9; msg 13).
AC5. WHEN a causal question is asked of any projected story, THE system SHALL walk visual object → twin state → semantic transition → canonical event → evidence — a proof path, not chronology alone (← msg 9; msg 13 §3).
AC6. WHEN simulation/forecasting is ever added, THE system SHALL quarantine it in a distinct epistemic category, never sharing LIVE/REPLAY's visual space (← msg 14; msg 13 §12).

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants this must not violate: Nortropic's trust layer — constitution & rulebook (`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`). Pointer only — never copied here.
Suggestions: keep the append-only-log-is-truth / SQLite-as-projection separation as the base; distinguish event_time / observed_time / recorded_time plus causation; ensure events carry enough object identity and qualified relations that an OCEL-style export loses nothing; treat OTel GenAI as a future interoperability projection ("no attribute without a real signal" is a good registry rule); carry msg 18's design-review inputs (Context/Semantics as its own layer; decision vs actuation as distinct authority domains; object-centric exportability); attention-budget metrics as future OS resources.

## 7. Out of scope (v1)

- The Aquarium scope (msgs 1–8, 14–17) — see `nortropic-aquarium`.
- Implementing any foundation now; changing the current build.
- Adopting A2A/MCP or any external standard — awareness and non-obstruction only.
- Building process mining, the economics overlay, city-scale zoom or simulation now — "sedan"/"långt senare" horizons.
- A parallel Organization OS in any form.

## 8. Verification (how we know it works)

At the future design-phase gate: an independent reviewer can confirm from the frozen Organization OS design record that each mandatory question has an explicit answer (or owner-accepted deferral), that epistemic-state and assumption-expiry semantics appear in the canonical contracts, and that the Evolution Loop routes radar findings to named assumptions with an IGNORE/EXPERIMENT disposition trail. For this capture stage: coverage gate passes; every D/R/AC resolves to its cited owner message.

## 9. Open questions (interview the owner before planning)

Q1. Package identity — separate related brief (this package) or addition/episode under `nortropic-organization-os`? Deferred to the corpus dedup check; never a parallel Organization OS (← msg 17).
Q2. Naming: `nortropic-organization-intelligence` vs `nortropic-evolution-foundations`? (← msg 17)
Q3. Which mandatory design questions enter Organization OS V0 versus later (← msg 13)?
Q4. Does the Wednesday Evolution Radar later consolidate with the other watches (the corpus-control-plane idea proposes a Radar lane)?
Q5. Caveat to ratify: msg 18 (first radar report, with "inference for Nortropic" recommendations) postdates the owner's last message; it is treated here as evidence input for the future design review, not as decisions. Does the owner endorse that?
Q6. The chat's attachment "Inklistrad markdown.md" was not captured (likely the msg 1 checkpoint, Aquarium scope) — confirm nothing load-bearing for this scope is lost.

## 10. Process for this brief

1. Clarify: first send a subagent to read `nortropic-evolution-foundations-design-rationale.md` (its rejection and unresolved sections cover most §9 rationale) and report back what bears on §9; only if the rationale lacks the needed evidence, exact source wording matters, or a conflict/ambiguity remains, have it read the targeted message ranges in the source conversation via the rationale's retrieval map — never the whole transcript, and keep both out of main context; then interview the owner on §9 (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code ("address all notes, don't implement yet").
3. On explicit owner approval, persist the exact approved plan as `nortropic-evolution-foundations-approved-plan.md`, validate it (`scripts/plan_contract.py validate`), bind it into this frontmatter and only then set `status: planned`.
4. Implement in a fresh session started from the approved plan: `plan_contract.py resume --slug nortropic-evolution-foundations --target-repo <repo>`; reconcile against current repository truth; after any compaction re-read the plan from disk; if it cannot be proven, STOP with `PLAN_IDENTITY_UNAVAILABLE`.
5. Adversarial review: fresh subagent checks the diff against this brief and the approved plan.
6. Traceability: commit messages cite this brief's slug.

## References

- Source conversation: `nortropic-evolution-foundations-full-chat.md` (idea content msgs 9–18; msgs 1–8 belong to `nortropic-aquarium`)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
