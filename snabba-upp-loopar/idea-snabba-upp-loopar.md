---
title: "Middle-out loop compression: faster Nortropic loops without touching trust"
type: idea-brief
status: idea   # lifecycle: idea → clarified → planned → building → verified; terminal: superseded
slug: snabba-upp-loopar
owner: Johnny (Nortropic)
created: 2026-08-20
source_conversation: snabba-upp-loopar-full-chat.md   # reference only — this brief takes precedence
intended_repo_path: snabba-upp-loopar/idea-snabba-upp-loopar.md
related: [build-fast-path, nortropic-frontier-delta, workflow-orkestrering, brainstorma-nortropic-engineering, bevaka-frontier-ai-engineering]
---

# Idea brief: Middle-out loop compression — faster Nortropic loops without touching trust

## 1. Summary

Make Nortropic's autopilots/loops dramatically faster in wall-clock time while keeping
frozen gates, reviewer separation, candidate binding and owner authority exactly as
strong. The framing decision (Silicon Valley's "middle-out compression" as architecture
metaphor): **keep the small serial trust backbone untouched; compress information
inward to it (task capsules, deterministic control plane); parallelize safe work
outward from it (read-only scouts, post-freeze verification lanes)** — and pay
frontier-model reasoning only where code cannot decide.

## 2. Context you need

Nortropic's loop today: frozen authority → builder → immutable candidate → independent
reviewer → owner final gate → merge. Frozen gates are authority; agent roles are
workflow. The loop is deliberately serial and evidence-heavy, so wall-clock cost comes
from repeated model round-trips, context copying, prose handoffs and serialized
verification — not from the trust requirements themselves. This chat researched
OpenAI/Codex, Anthropic, Lovable and several GitHub loop projects; all converge on
"state in code/filesystem, deterministic coordination, agents only where judgment is
needed, worktrees for isolation, gates for truth".
Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen
gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- Loop telemetry exists (timestamps per phase; counts of model turns, tool calls,
  process starts, context size) — measured baseline before any behavior change.
- A deterministic "compiler" produces a minimal **task capsule** (task, SHAs, allowed
  writes, frozen hashes, required gates, references-not-copies of authority docs) and a
  `nortropic inspect --json`-style command replaces multi-command LLM state probing.
- Coordination that needs no judgment (scheduling, routing, retries, SHA binding,
  allowed-write checks, exit classification, state transitions) runs as controller
  code, not model reasoning.
- Read-only discovery fan-out: many scouts, **one writer**.
- After candidate freeze, all verification lanes (frozen gate, invariants, review
  lanes) run in parallel against the immutable SHA; owner final gate converges them.
- Machine-to-machine handoffs are content-addressed structured artifacts
  (manifest/evidence/test-results/findings JSON), with human reports rendered from them.
- Loop speed is scored as LOOP_COMPRESSION_RATIO with a hard companion invariant
  EVIDENCE_EQUIVALENCE=YES (same gates, binding, proofs, reviewer requirement, owner
  authority).

Choose architecture/decomposition/tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

The chat has a single owner message (the commission); the roadmap is the assistant's
proposal. Treat as **proposals with provenance, not owner decisions** — except the
quality bar itself, which Johnny set in the commission:

- D1. Speed must never be bought by weakening quality — "utan att tumma på kvaliteten"
  is the task's own constraint — because the whole point is same-or-stronger evidence
  at lower wall-clock (← msg 1).
- P1. Don't touch the trust backbone; rebuild everything around it — because the
  backbone is small and the latency lives in the periphery (← msg 5).
- P2. Loop speed beats model speed as leverage: fewer serialized agent turns and less
  context copying, before any model swap (← msg 4).
- P3. Fast mode over model downgrade for trust-critical roles; any model DOWNGRADE
  must first prove itself on Nortropic's own replay evals (← msg 5).
- P4. Speculative Build (two isolated builder hypotheses in parallel) is an
  experiment for high-variance task classes only, never a default (← msg 5).
- P5 (REJECTED path). Importing trust policies from the surveyed GitHub loops
  (e.g. Architect-loop's no-human-gates model) — rejected because their authority
  models are weaker than Nortropic's (← msg 5).
- P6 (warning). Harness logic must not become "a museum of past model weaknesses":
  periodically re-ask whether an LLM phase is a security invariant or an obsolete
  workaround (← msg 5).

## 5. Acceptance criteria (v1)

- AC1. WHEN a loop run completes, THE system SHALL emit per-phase timestamps and
  counts (model turns, tool calls, process starts) sufficient to compute the critical
  path.
- AC2. WHEN an agent needs task/candidate state, THE controller SHALL provide it as
  one structured deterministic result (capsule/inspect), and the agent SHALL NOT need
  free-form shell probing for it.
- AC3. WHEN a candidate is frozen, THE verification lanes SHALL run in parallel
  against the same immutable SHA, and THE owner final gate SHALL still require all of
  them.
- AC4. WHEN any speed optimization is enabled, THE run SHALL still produce evidence
  satisfying EVIDENCE_EQUIVALENCE (same frozen gates, candidate binding, allowed-write
  proof, reviewer requirement, owner authority) — verified from the record.
- AC5. WHEN scouts explore, THE system SHALL enforce read-only for them and exactly
  one writer per candidate.

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants: Nortropic's trust layer — constitution & rulebook (pointer, never a copy).
Suggestions from the chat: follow the proposed 9-step order (measure → capsule/inspect
→ deterministic control plane → scout fan-out → parallel post-freeze verification →
artifact handoffs → Fast mode on critical roles → eval-gated model routing →
Speculative Build last); keep a stable prompt prefix / variable suffix for cache hits;
append-only model-visible history; targeted fast inner loop with the full trust chain
only at the candidate freeze boundary.

## 7. Out of scope (v1)

- Any change to frozen gates, reviewer separation, candidate binding or owner
  authority (the backbone is explicitly untouchable).
- Importing external loop projects' trust/approval policies (rejected, P5).
- Model downgrades without replay-eval proof (P3).
- Speculative Build as default behavior (P4).
- Site-factory build speed (template repo + Content-phase split) — that is the
  separate related brief `build-fast-path`.

## 8. Verification (how we know it works)

End-to-end: run the same benchmark task class before and after adoption. The record
alone must show LOOP_COMPRESSION_RATIO > 1 (fewer critical-path model round-trips,
lower wall-clock) AND an EVIDENCE_EQUIVALENCE=YES checklist where each item (gates,
binding, proofs, reviewer, owner gate) is confirmed identical — "faster and it feels
as good" is not acceptance.

## 9. Open questions (interview the owner before planning)

- Q1. Which of the 9 proposed steps do you adopt now vs defer? (Only D1 is yours;
  P1–P6 await your triage.)
- Q2. What is the benchmark task class and baseline window for LOOP_COMPRESSION_RATIO?
- Q3. Fast mode costs extra credits (e.g. 2.5× on some models) — what budget bound
  applies, and on which roles?
- Q4. Where does the task-capsule compiler live relative to the existing controller
  (nortropic-system), and is building it in scope before the current slice completes?
- Q5. Does parallel post-freeze verification require rulebook changes (gates currently
  specified as sequential?), or is ordering already unspecified?

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

- Source conversation: `snabba-upp-loopar-full-chat.md` (same folder)
- Related brief: `build-fast-path/idea-build-fast-path.md` (site-factory speed; same theme, different subsystem)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
