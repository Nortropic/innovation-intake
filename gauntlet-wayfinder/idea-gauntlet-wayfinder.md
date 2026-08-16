---
title: "Gauntlet quality layer inside the Nortropic trust loop"
type: idea-brief
status: ready-for-clarification
slug: gauntlet-wayfinder
owner: Johnny (Nortropic)
created: 2026-08-16
source_conversation: gauntlet-wayfinder-full-chat.md
intended_repo_path: gauntlet-wayfinder/idea-gauntlet-wayfinder.md
---

# Idea brief: Gauntlet quality layer inside the Nortropic trust loop

## 1. Summary

Give Nortropic a quality-optimization layer (a "Gauntlet") without ever letting it touch
trust: agents propose, build, criticize and improve; the environment supplies evidence;
deterministic mechanisms establish trust. The single most important framing decision:
**Nortropic does not become a Gauntlet loop — it contains one**, as an advisory quality
layer inside the stricter verification/trust loop, and the full chain is
**Wayfinding → Specification → precommitted Verification → Build → Verify →
Quality Gauntlet → Empirical → Promotion**.

## 2. Context you need

Nortropic is a provider-neutral trust-kernel system: frozen owner contracts, exact
candidate SHAs, deterministic graders first, independent falsification, attestation,
promotion. Its contracts already state `DETERMINISTIC_GRADERS_FIRST=YES`,
`LLM_EVALUATOR_IS_ROOT_OF_TRUST=NO`, `CODEX_ROLE_SEPARATION_IS_SECURITY_BOUNDARY=NO`.
The roadmap already reserves S10 (Markdown intake / Task IR), S11 (verifier-author +
challenger + kernel freeze) and S12/h-025 (evaluator adapter). What is missing is making
the separation between **quality optimization** and **trust verification** first-class,
and the pre-build chain (wayfinding, specification, precommitted checks) explicit.
This idea is captured as Innovation issue #4 (Area=VERIFICATION, INBOX).

Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.

## 3. Destination (goal, not implementation plan)

- The three-loop model is explicit in Nortropic's governing docs: inner provider loop
  (Ralph-like persistence, owned by the provider harness), middle Quality Gauntlet
  (advisory optimizer), outer Nortropic trust loop (root of trust).
- S10's Task IR distinguishes epistemic categories: DECIDED REQUIREMENT, UNKNOWN
  DECISION, ASSUMPTION, CONSTRAINT, REFERENCE, EXAMPLE, OUT-OF-SCOPE, SUCCESS CRITERION
  — and building is blocked while semantics depend on an unresolved unknown.
- Verification is designed claim-first before build (claim → how could it be false →
  check), then frozen; quality bars are concrete, versioned artifacts frozen before
  optimization.
- S12/h-025 is a narrow evaluator adapter whose results are findings/evidence/
  uncertainties/abstentions — never a promotion verdict.
- Requirements traceability: every important check can answer "why does this check
  exist" back through requirement → decision → owner intent.

Choose architecture, decomposition and tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

- D1. Nortropic contains a Gauntlet; it does not become one — because replacing frozen
  gates with "critic says looks good → merge" is an architectural step backwards.
- D2. Three loops never share stop conditions: persistence (provider), quality
  (Gauntlet), trust (Nortropic) — because they solve three different problems.
- D3. Critic ≠ grader ≠ trust authority; evaluator output is advisory findings, and the
  evaluator result contract contains no `approved=true` — because LLM judgment is input,
  never authorization.
- D4. Quality bars must be concrete, external and versioned before optimization; the
  builder may not move goalposts mid-run — because "make it amazing" is not a bar.
- D5. Gauntlet optimizes inside an authorized space; it never invents the space —
  because a reference product smuggles in thousands of requirements, and without one the
  agent invents both the problem and the answer key (perfect PASS against an
  unauthorized requirement).
- D6. Checks are first-class objects derived claim-first before build — because when
  critics/checks are the lead agent's spontaneous thoughts, product, evaluator,
  orchestration and specification failures become indistinguishable.
- D7. Critics falsify, they do not prescribe: observations + evidence + severity, root
  cause belongs to the builder — because Shumer's critics misdiagnosed root cause and
  following their prescriptions made results worse.
- D8. Parallelize falsification aggressively (reviewer fan-out on the same immutable
  SHA); parallelize builders only on proven-independent write surfaces — because
  parallel builders on coupled systems degraded results.
- D9. Critics may say UNKNOWN and must themselves be falsifiable; order-unstable A/B →
  EVALUATOR_UNSTABLE → abstain — because self-preference and position bias are measured
  phenomena.
- D10. `MAX_ROUNDS reached = QUALITY_BUDGET_EXHAUSTED`, never `= PASS` — because budgets
  are fail-stops, not proofs of correctness.
- D11. Capability/quality evals (hill to climb) are separate from regression gates
  (nearly always green); Gauntlet pushes QUALITY, frozen gates protect HARD.
- D12. Missed real failures become regressions: failure → minimal reproducer →
  verifier-author → challenger → kernel freeze — the system self-proposes stronger
  measurements; authority freezes them; no self-modification.
- D13. ASSUMPTION ≠ REQUIREMENT; discovered unknowns route backwards through
  wayfinding/owner decision, never sideways into implementation — because an agent
  quietly filling an unknown later reads as authority.
- D14. REJECTED: a separate "Gauntlet framework"/engine (`debate.py`, `swarm.py`, …) —
  because the Harness Substitution Contract says use provider-native capabilities, don't
  build a parallel agent harness without its own trust function.
- D15. REJECTED: hardcoded "Claude and Codex debate 5 rounds, take the best" — because
  cross-provider diversity is diversity, not authority, and "best according to what?"
  stays unanswered.
- D16. REJECTED: heavy critic fan-out on every change — because evaluators pay off at
  the capability edge; elsewhere they are token overhead.

## 5. Acceptance criteria (v1)

- AC1. WHEN the principles are adopted, THE governing docs SHALL state the three-loop
  separation and decisions D1–D13 in versioned form.
- AC2. WHEN an evaluator (h-025) produces a result, THE result contract SHALL contain
  findings/evidence/uncertainties/abstentions and SHALL contain no promotion verdict.
- AC3. WHEN a quality run starts, THE system SHALL reference a quality profile frozen
  and versioned before the run.
- AC4. WHEN a quality budget is exhausted, THE run record SHALL state
  QUALITY_BUDGET_EXHAUSTED and SHALL NOT convert it to PASS.
- AC5. WHEN an A/B comparison flips under order permutation, THE system SHALL record
  EVALUATOR_UNSTABLE and abstain.
- AC6. WHEN a finding falls outside frozen requirements, THE system SHALL route it as a
  requirement proposal (wayfinding/owner), not to the builder.
- AC7. WHEN a missed real failure is confirmed, THE system SHALL produce reproducer →
  new verifier → challenger pass → freeze, yielding a new regression.

## 6. Constraints & implementation notes (suggestions, not orders)

- Do not change the control plane mid-bootstrap; land principles as roadmap/contract
  text first, mechanics with S10–S12.
- Reuse provider-native reviewer/subagent capabilities (per Harness Substitution
  Contract); evaluator adapter stays thin (EvaluationRequest/EvaluationResult sketch in
  the source conversation).
- Existing anchors to build on: detached reviewer worktrees, exact BASE_SHA/CANDIDATE_SHA
  locking, frozen task gates, `MAX_ARCHITECT_ROUNDS`/`EMPIRICAL_MAX_ROUNDS` as budgets.

## 7. Out of scope (v1)

- The conversation-archiving / chat-capture track from the same chat (otaliptus
  exporter, Innovation Intake v2 artifact binding) — separate neighboring idea.
- Building any Gauntlet engine or new agent framework (D14).
- Changing the Nortropic Innovation Project schema or current bootstrap/gate chain.
- Replacing deterministic verification with quality scoring anywhere.

## 8. Verification (how we know it works)

One end-to-end record: a task run whose artifacts show (from the record alone) a frozen
versioned quality profile, evaluator findings without any verdict field, a
budget-exhaustion or bar-met stop reason, at least one out-of-requirements finding routed
backwards as a proposal, and promotion decided solely by the deterministic trust chain.

## 9. Open questions (interview the owner before planning)

- Q1. First slice: land D1–D13 as a frozen contract document now (like the Harness
  Substitution Contract), or as roadmap guidance folded into S10–S12 planning?
- Q2. Where do versioned quality profiles live — inside the task contract, or as a
  separate registry with their own freeze step?
- Q3. Does Wayfinding get tooling in the near-term roadmap (S10 extension), or stay a
  manual owner+chat process for now?
- Q4. Should h-025's EvaluationRequest/EvaluationResult sketch be adopted as the design
  baseline for S12, or redesigned fresh at build time?

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

- Source conversation: `gauntlet-wayfinder-full-chat.md` (same folder)
- Innovation issue #4 — "Wayfinding → Specification → Verification → Quality Gauntlet"
  (Area=VERIFICATION)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
