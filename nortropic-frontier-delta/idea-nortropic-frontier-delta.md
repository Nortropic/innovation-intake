---
title: "Nortropic Evolution Loop: autonomous frontier monitoring and self-improvement without touching trust"
type: idea-brief
status: superseded   # ägarbeslut 2026-08-20: ersatt av bevaka-frontier-ai-engineering (Observatory)
superseded_by: bevaka-frontier-ai-engineering
slug: nortropic-frontier-delta
owner: Johnny (Nortropic)
created: 2026-08-20
source_conversation: nortropic-frontier-delta-full-chat.md   # reference only — this brief takes precedence
intended_repo_path: nortropic-frontier-delta/idea-nortropic-frontier-delta.md
related: [agent-harness-priorities, snabba-upp-loopar, workflow-orkestrering, brainstorma-nortropic-engineering]
---

# Idea brief: Nortropic Evolution Loop — autonomous frontier monitoring and self-improvement without touching trust

## 1. Summary

Keep Nortropic self-improving autonomously by adding a **separate meta-loop on top of
the existing trust/control plane** — never by letting the builder that writes the
system decide how the system improves. The framing decision: **"multi-agent to
understand the world; strict Nortropic chain to change Nortropic"** — world research is
step one in hypothesis → local reproduction → eval → independent falsification →
promotion, and external claims can never become truth for Nortropic without local
proof. A daily monitoring automation ("Nortropic Frontier Delta") is already live.

## 2. Context you need

Nortropic's operating model: builder is not its own trust authority; frozen gates
cannot be rewritten to fit an implementation; candidates are reviewed independently
before the owner's final gate. The bootstrap (S3→S13, ending in an empirical unattended
run) is in progress and must not be interrupted by a self-modifying meta-agent. This
chat designed the meta-loop architecture and activated the first piece: a daily
surveillance report. The transcript also contains four dated delta reports (Aug 16–20)
whose specific findings (Claude Code 2.1.234–2.1.237, Codex 0.148/0.149, papers) are
time-sensitive signals, not part of the core idea.
Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen
gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- **Four loops**: Execution (minutes — today's factory), Quality (daily — mine
  Nortropic's own traces for waste/recurring failures), Frontier (daily delta + weekly
  deep analysis of OpenAI/Anthropic/papers/GitHub), Evolution (weekly/on major release
  — isolated experiments, baseline vs candidate under equal budget, falsification
  before promotion).
- A **research team, not one agent**: Frontier Lead → short-lived source scouts →
  separate Citation/Verification Agent → **Nortropic Mapper** that converts findings to
  structured claims (source tier, claim, affected component, local hypothesis,
  measurable outcome, risk, next action: IGNORE/WATCH/REPRODUCE/EXPERIMENT/
  CREATE_CANONICAL_TASK).
- An **evidence ladder** for external claims: OBSERVED → CORROBORATED →
  LOCALLY_REPLICATED → LOCALLY_PROVEN → ADOPTED (or REJECTED/SUPERSEDED/STALE). An
  Anthropic blog post is never PROVEN for Nortropic by itself.
- **Three eval surfaces**: dev evals (visible), adversarial evals, and held-out evals
  invisible to the optimizer/builder — the improvement agent must never see the final
  judge.
- A **Harness Ablation Agent** whose job is removal: candidate vs baseline where
  correctness/safety/held-out hold while latency/tokens/failure surface shrink.
- A versioned **SOURCE_REGISTRY** with evidence tiers and freshness; weak signals may
  say "investigate", never "change Nortropic".
- An **Evolution view** in Verkstadsgolvet (frontier signals, hypotheses, experiments,
  locally proven, awaiting authority — and a REMOVED counter so the dashboard doesn't
  reward expansion).
- Accepted findings convert into the same canonical Task IR/backlog as all other work —
  **no shadow backlog**; the controller keeps owning work and state.

Choose architecture/decomposition/tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

- D1. The daily **Nortropic Frontier Delta** automation is ACTIVE (first run ~Aug 16):
  it monitors OpenAI/Codex, Anthropic/Claude Code, papers and GitHub, reports only
  material deltas, may analyze and recommend (IGNORE/WATCH/REPRODUCE/EXPERIMENT/
  CREATE_CANONICAL_TASK) but may NOT change Nortropic, create commits/tasks, or make
  authority decisions — because monitoring must exist during bootstrap without gaining
  execution power (← msg 4–5).
- D2. Autonomous world-monitoring toward "world-leading and constantly better" is a
  standing owner goal — it is the commission itself (← msg 1).
- P1 (proposal). Do not interrupt S3→S13; sequence the meta-loop as S14–S20 after the
  empirical unattended run (Research Radar → Trace Ingestion → Hypothesis/Eval Author →
  Evolution Lab → Hidden Holdout → Ablation → Gated Meta-Promotion) (← msg 4).
- P2 (proposal). Keep core evals code-native and reproducible in Nortropic's own
  control plane — OpenAI's hosted Evals API platform is being retired in 2026; provider
  scheduled-agent features are workers/triggers, never trust roots (← msg 4).
- P3 (proposal, later-corroborated). Evolution experiments need multi-run variance
  measurement, shuffled task ordering, held-out evals and an independent evidence
  reviewer — single good runs are not proof (← msg 8).
- P4 (proposal). Add a **Strategy Reconsideration Gate**: after N failed experiments /
  marginal gains / repeated failure class, stop local search, restate objective and
  competing strategies, branch a genuinely different strategy family — because agents
  empirically lock strategy early and only optimize execution (← msg 9).
- R1 (REJECTED). "A research agent that reads the internet and then improves Nortropic"
  — rejected because the improver must never be its own trust authority (← msg 4).
- R2 (REJECTED). Borrowing AutoResearch's broad permissions or single scalar objective
  — only its experiment discipline (small mutation surface, fixed budget, keep/discard)
  is borrowed (← msg 4).

## 5. Acceptance criteria (v1)

- AC1. WHEN the Frontier loop reports a finding, THE system SHALL record it as a
  structured claim with source tier, affected component, measurable outcome and a next
  action from the fixed vocabulary.
- AC2. WHEN an external claim lacks local reproduction, THE system SHALL NOT allow it
  to justify any change to Nortropic (ladder state below LOCALLY_PROVEN blocks
  adoption).
- AC3. WHEN an improvement candidate is evaluated, THE evaluation SHALL include
  multiple independent runs, shuffled task ordering and held-out evals the optimizer
  cannot read.
- AC4. WHEN an ablation candidate passes (correctness ≥ baseline, safety invariants
  preserved, held-out non-regressing, latency/tokens down), THE system SHALL record the
  removal in the Evolution view's REMOVED ledger.
- AC5. WHEN the monitoring automation runs, THE run SHALL produce zero writes to
  Nortropic repos, tasks or authority state — verifiable from the record.

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants: Nortropic's trust layer — constitution & rulebook (pointer, never a copy).
Suggestions from the chat: held-out evals must not be readable by repo-wide-read agents
(storage/access design matters); bind benchmark runs to model, reasoning level, harness
version, environment and budget so "more compute" is not mistaken for a better loop;
event-driven wakeups (e.g. notify-when-idle patterns) may signal the controller but
durable controller state decides truth; a per-run Resource Envelope (tokens, calls,
spend, wall-clock, retries) with atomic reservation and fail-closed stop suits
unattended runs.

## 7. Out of scope (v1)

- Any change to the current bootstrap chain S3→S13 (explicitly deferred until after the
  empirical unattended run).
- Acting on the dated delta-report findings in the transcript (Claude Code 2.1.23x
  reproductions, Codex 0.148/0.149 watches, etc.) — those are monitoring outputs to be
  triaged through the ladder, not part of this idea's build.
- Letting the monitoring automation gain any write/task/authority capability (D1
  boundary).
- Provider-hosted eval platforms as the eval backbone (P2).

## 8. Verification (how we know it works)

End-to-end: take one real frontier signal through the full ladder — structured claim
(AC1) → local reproduction attempt → Evolution Lab experiment with multi-run/shuffled/
held-out protocol (AC3) → falsification pass → promotion through the existing authority
chain — and separately demonstrate one ablation landing in the REMOVED ledger (AC4).
An independent reviewer must be able to confirm every transition from the record alone,
including that the monitoring runs wrote nothing (AC5).

## 9. Open questions (interview the owner before planning)

- Q1. Do you adopt the S14–S20 sequencing (P1) as the post-bootstrap roadmap, and what
  triggers its start — the empirical unattended run alone, or an explicit go?
- Q2. Who/what triages the daily Frontier Delta recommendations today (the WATCH/
  REPRODUCE backlog is already accumulating in the transcript) — and where does that
  triage state live until S14 exists?
- Q3. How should held-out evals be stored so a repo-wide-read agent cannot see them
  (separate repo? encrypted? controller-only runner)?
- Q4. This chat is a LIVE daily feed — what is the re-harvest policy (periodic
  re-capture superseding this transcript, or per-report ingestion), and does the same
  policy cover the sibling monitoring chats?
- Q5. How does the Evolution Loop relate to the Gauntlet quality layer
  (`gauntlet-wayfinder`) — same lab, adjacent lanes, or merged concept?
- Q6. P3/P4 rest on preprints — do you want them held at NEEDS-EVIDENCE until locally
  replicated, per the ladder's own rule?

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

- Source conversation: `nortropic-frontier-delta-full-chat.md` (same folder)
- Related briefs: `agent-harness-priorities/` (sibling surveillance feed),
  `snabba-upp-loopar/` (the chat explicitly ties harness ablation to loop compression)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
