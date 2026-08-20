---
title: "Agent harness priorities: reviewer isolation, provenance, bounded multi-agent patterns"
type: idea-brief
status: idea   # lifecycle: idea → clarified → planned → building → verified; terminal: superseded
slug: agent-harness-priorities
owner: Johnny (Nortropic)
created: 2026-08-20
source_conversation: agent-harness-priorities-full-chat.md   # reference only — this brief takes precedence
intended_repo_path: agent-harness-priorities/idea-agent-harness-priorities.md
related: [nortropic-frontier-delta, bevaka-frontier-ai-engineering]   # bevakningsfamiljen; frontier-delta ersatt av Observatory-briefen
---

# Idea brief: Agent harness priorities — reviewer isolation, provenance, bounded multi-agent patterns

## 1. Summary

A scheduled monitoring chat (two automated digest reports, Aug 10–20 2026) scanned
Anthropic/OpenAI harness developments and distilled implications for Nortropic. The
central recommendation: Nortropic's next harness innovation is **not more debating
models but harder reviewer isolation plus lineage/provenance** — a future
"Operating Model v2" — while the current S1 plan stays unchanged. **Important framing:
this chat contains zero owner messages; nothing here is an owner decision.** Everything
below is monitored evidence plus assistant recommendations awaiting owner triage.

## 2. Context you need

Nortropic runs a builder → reviewer → owner loop where deterministic mechanisms (frozen
gates, mechanical verification) establish trust and model agents act as workers or
challengers, never as root-of-trust. This chat is an automated surveillance feed watching
what Anthropic (Claude Code) and OpenAI (Codex) ship in the same problem space, so
Nortropic can adopt validated patterns instead of inventing in the dark.
Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen
gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

If the owner adopts these recommendations, the end state is:

- An **Operating Model v2** evidence contract carrying lineage/provenance fields
  (e.g. `root_run_id`/`ROOT_RUN_ID`, `agent_path`, `role`, `model`,
  `environment_profile_id`, immutable `candidate_sha`).
- A mechanized reviewer profile: non-interactive (`approval=never`), read-only
  execution intersected with parent permissions, empty extension/plugin registry by
  default, no nested reviewer-of-reviewer, identity bound to `candidate_sha` +
  environment profile.
- A **single controller-owned privileged-action pipeline** for push, merge, permission
  expansion, network escalation and promotion — no per-tool escalation logic; model
  risk scores may request MORE verification but can never skip frozen gates.
- Backlog experiments, measured against the mechanical verifier before touching
  promotion: (a) asymmetric challenger — Codex builder → Claude adversarial reviewer →
  targeted repair; (b) parallel independent read-only specialist review lanes →
  aggregator.
- Forward-tests per skill (can builder-skill touch a frozen gate? can reviewer-skill
  write? can test-author implement?).

Choose architecture/decomposition/tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

**None by the owner.** This conversation has no user turns (scheduled task; the visible
chat is two assistant reports — see transcript metadata). The strongest standing
recommendation, repeated in both reports, is:

- R1. Do NOT change the current S1 plan — because fresh signals validate the existing
  direction (controller-owned containment, frozen verifier authority, bounded retries),
  not a pivot (← msg 1–2).
- R2. Prefer asymmetric challenger over symmetric multi-model debate — because the only
  cited empirical study (116 tasks) showed Claude-review-of-Codex improved results while
  Codex-review-of-Claude worsened them (← msg 1).
- R3. Multi-model consensus must carry degraded-mode honesty (`provider`, `model`,
  `input_sha`, `candidate_sha`, `verdict`, `fallback_for`, `degraded`); a fallback never
  counts as independent consensus, and consensus never creates attestation (← msg 1).

Treat R1–R3 as recommendations with provenance, not owner decisions.

## 5. Acceptance criteria (v1 — if/when the owner pulls this to build)

- AC1. WHEN a reviewer session is spawned, THE harness SHALL run it non-interactive,
  read-only, with an empty extension registry, and SHALL deny (not escalate) permission
  requests.
- AC2. WHEN any agent turn is recorded as evidence, THE evidence record SHALL carry
  root-run id, agent path, role, model and immutable candidate sha.
- AC3. WHEN any privileged action (push, merge, permission/network escalation,
  promotion) is requested, THE controller SHALL route it through the single
  privileged-action pipeline; no other code path SHALL perform it.
- AC4. WHEN a model-based risk score is produced, THE system SHALL be able to add
  verification steps but SHALL NOT be able to skip or weaken a frozen gate.
- AC5. WHEN a reviewer is forked from a builder context, THE reviewer SHALL NOT inherit
  the builder's role instructions.

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants: Nortropic's trust layer — constitution & rulebook (pointer, never a copy).
Suggestions from the monitored sources: model whatever is adopted on the cited
OpenAI/Codex mechanisms (Guardian reviewer isolation, root_turn_id lineage, common
approval pipeline) rather than inventing parallel vocabulary; keep challenger/review
experiments advisory until measured on Nortropic's own task suite; shadow-mode any
future skill router before it steers production.

## 7. Out of scope (v1)

- Changing anything in the current S1 slice or any frozen gate (explicitly recommended
  against in both reports).
- Symmetric "five-round model debate" designs (recommended against, R2).
- A smart skill router now (only worth it with many skills; shadow-mode first).
- MCP/stateless control-plane work for S13/Verkstadsgolvet (noted as low-priority
  future signal only).

## 8. Verification (how we know it works)

End-to-end: spawn a builder run producing a candidate, then a reviewer session against
it. From the record alone an independent reviewer confirms: the reviewer ran
non-interactive/read-only/extension-free (AC1), every turn's evidence carries the
lineage fields (AC2), a deliberately attempted privileged action outside the pipeline
was refused (AC3), and a forked reviewer's transcript shows no builder role text (AC5).

## 9. Open questions (interview the owner before planning)

- Q1. Which recommendations (R1–R3, §3 items) do you adopt, defer, or reject? Nothing
  was decided in the chat.
- Q2. Is "Operating Model v2" (lineage + reviewer isolation) actually the next priority
  after S1, ahead of the challenger experiments?
- Q3. Should the asymmetric challenger experiment (Codex builder → Claude reviewer) run
  on the existing task suite, and what metric gates its adoption?
- Q4. Do the proposed evidence fields fit the current evidence contract, or does this
  wait for a contract revision?
- Q5. This is a recurring surveillance chat — should future digests be re-harvested
  into this same brief (superseding it), or is this a one-time snapshot?

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

- Source conversation: `agent-harness-priorities-full-chat.md` (same folder)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
