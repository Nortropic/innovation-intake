---
title: "Webbförvaltningen Capability Assurance — post-build reconciliation & completeness audit"
type: idea-brief
status: idea
slug: webbforvaltningen-capability-assurance
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: webbforvaltningen-capability-assurance-full-chat.md
design_rationale: webbforvaltningen-capability-assurance-design-rationale.md
intended_repo_path: webbforvaltningen-capability-assurance/idea-webbforvaltningen-capability-assurance.md
context_revision: 1
related: [gauntlet-wayfinder]
---

# Idea brief: Webbförvaltningen Capability Assurance

## 1. Summary

A read-only, evidence-bound Capability Assurance campaign that proves what the finished Webbförvaltning can actually do: atomic reconciliation of the historical 100-day plan (D001–D100) and the DESIGN-FROZEN masterplan against the final built system, plus outside-in comparison against literature, practitioners, agencies, OpenAI and Anthropic, plus a Web Excellence & Design Intelligence audit. Load-bearing framing: **capture and design the method now; run the evaluation only at `WEBBFÖRVALTNINGEN_BUILD_COMPLETE` against a frozen final SHA** — never against the moving build.

## 2. Context you need

The 100-day backlog (2026-07-29) is no longer the active execution plan — the DESIGN-FROZEN masterplan and current repo reality govern HOW — but the full D001–D100 walk showed it is three things: a first third absorbed by the Trust Kernel, a mixed middle (design intelligence D35–40, CI/CodeQL D21–24/30, framework policy D47 still real), and a surprisingly current last third (migration, fact approval, human user testing, Care/Growth, v1 proof). The system's own registers say `VALIDATING`, not `PROVEN`. The audit generalizes into a repeatable completeness institution: assurance claims with evidence + defeaters + freshness, dispositions separated from maturity, gap types including REALITY_GAP/EVIDENCE_GAP, a Supersession/Rejection Ledger with semantic-zombie protection, mission coverage UNDERSTAND→…→EXIT, comparator council, counterfactual/minimality, agency economics, tacit-dependency audit, four independent verdicts. Two campaigns: Assurance (read-only), then Implementation Intake for accepted gaps only.

This brief is the primary intake artifact for execution. Deeper design logic lives in the linked design rationale; the full chat is raw evidence — read targeted message ranges only if the rationale is insufficient. Current canonical repository authority beats all intake artifacts; within the intake package this brief wins over rationale and transcript. Once an owner-approved plan is bound (see the frontmatter), it carries execution order above this brief and below current repository authority.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook (`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- Stage A (now): only the assurance method/campaign contract and its self-guards — no evaluation of the moving build, no product changes.
- Stage B (triggered by `WEBBFÖRVALTNINGEN_BUILD_COMPLETE`): freeze final SHAs, add final report/current reality as new source episodes, do fresh comparator research, then run the read-only campaign.
- Outputs, small and decidable: atomic coverage matrix; assurance claims with evidence/defeaters/freshness; mission coverage; modern gap map incl. removal candidates; Supersession/Rejection Ledger with forbidden semantic roles and selective tripwires; Web Excellence & Design Intelligence report; a short list of fitness-function candidates. 100 historical points should compile down to a few modern gaps.
- Owner triage afterwards; only accepted gaps become implementation candidates via Intake.

Choose architecture, decomposition and tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

D1. Finish the ongoing Webbförvaltning first; then run the comparison via Nortropic Intake with a comparative prompt — because injecting the old manual mid-build would make Claude "solve" things already solved better (← msg 5; two-round model msg 14).
D2. The audit must also compare outside-in — persons of interest, web agencies, literature, OpenAI, Anthropic — not only Nortropic-vs-Nortropic — because both internal plans can share blind spots (← msg 11; comparator council msg 12).
D3. "Kontroll över alla variabler": sites must be built per what literature and professionals say AND with the extracted Emil Kowalski/Taste/Impeccable/popular-GitHub skills — non-AI-slop, superb quality — because objective goodness and craft/distinction must never substitute for each other (← msg 15; msg 16).
D4. Stop broad brainstorming and plan the implementation of the assurance framework — Stage A now (method only), Stage B at BUILD_COMPLETE (← msg 17; staging and prompt msg 18).
D5. Procedural: the deep brainstorm was explicitly invited and continued by the owner before freezing direction (← msgs 7, 9).

R1. Running the audit now against a moving `main` — because a mid-build audit produces stale conclusions; the SHA under review changed within hours during the chat (← msgs 5, 15, 17 accepting msg 14).
R2. A composite completeness score ("93.7% complete") — because it is instant Goodhart; use counts and named critical risks instead (← msg 17; msg 10 §25).
R3. Treating the 100-day manual as active execution plan — because it becomes the coverage/requirements oracle while the DESIGN-FROZEN masterplan + current repo govern HOW (← msg 5; msgs 2, 4).
R4. The assurance campaign implementing its own findings — because read-only + owner triage is what separates assurance from scope creep; explicit no-build contract (← msg 17; msg 14).
R5. Filename/component-presence matching ("does `FACT-LEDGER.json` exist?") — because the question is always "is the problem solved?", never "does the same-named file exist?" (← msg 17; msgs 6, 10 §2).

## 5. Acceptance criteria (v1)

AC1. WHEN Stage B runs against the frozen final SHA, THE campaign SHALL give 100% of the atomized D001–D100 and binding masterplan parts a disposition (`SATISFIED/SUPERSEDED/PARTIAL/STILL_REQUIRED/TRUST_KERNEL_OWNED/TRIGGER_ONLY/REJECT/UNKNOWN`) on a separate axis from maturity (`DECLARED/BUILT/VALIDATING/PROVEN`) — every `SATISFIED` with concrete evidence, every `SUPERSEDED` with a named replacement (← msg 5; msgs 6, 8, 18).
AC2. WHEN the campaign executes, THE campaign SHALL honor the no-build contract: read-only target repos, no implemented findings, no gate/baseline/capability-status changes, no new runtime authority (← msg 17; msgs 14, 18).
AC3. WHEN a claim rests only on synthetic evidence, THE campaign SHALL never mark it `PROVEN`, recording a REALITY_GAP (or EVIDENCE_GAP) with the observation needed instead of generated code (← msg 15; msgs 10 §15–16, 18 fixture 4).
AC4. WHEN external comparator lenses produce fresh findings, THE campaign SHALL route them through Knowledge Lane as candidates — never as direct authority over the build (← msg 11; msgs 12 §, 14, 18).
AC5. WHEN the Web Excellence & Design Intelligence audit runs, THE campaign SHALL verify the Nortropic Web Standard × Project Visual Intent separation, distill the eight external design skills into owned principles with source-authority classes, and detect both classic AI-slop and "anti-slop slop"/sibling convergence — four independent verdicts (Integrity / Experience / Craft & Distinction / Outcome), none averaged away (← msg 15; msg 16).
AC6. WHEN the campaign's analysis completes, THE campaign SHALL pass its planted falsification fixtures (superseded-not-missing; file-present-behavior-absent; atomization; synthetic-never-proven; untraced complexity; route-out-not-gap; reject-plus-tripwire) before findings are presented (← msg 17; msgs 8, 10, 18).

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants this must not violate: Nortropic's trust layer — constitution & rulebook (`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`). Pointer only — never copied here.
Suggestions: atomize on problem/outcome level with stable IDs (`D038-R01`…); bidirectional traceability with orphan and untraced-complexity detection; claims carry defeaters and invalidation surfaces so evidence goes `STALE` when owner surfaces change (enabling incremental re-audit); challengers (Coverage, Simplification, Real Customer); findings resolve to `ADD/CHANGE/REMOVE/PROVE/OBSERVE/ROUTE/DO_NOTHING`; a stop rule so v1 is never held hostage — "completeness = capability coverage + truthful boundaries", current scope as zero point.

## 7. Out of scope (v1)

- Running the evaluation before `WEBBFÖRVALTNINGEN_BUILD_COMPLETE`; any change to the ongoing build.
- Implementing findings (Campaign 2 territory, owner-gated).
- Importing GOV.UK/SRE/DORA/etc. as standards rather than challenger lenses; comparator tooling beyond the campaign's needs.
- Aquarium visualization of assurance state (future; separate track).
- Generalizing into every-förvaltning institution machinery beyond what this first campaign needs.

## 8. Verification (how we know it works)

Stage A: the campaign contract's self-guards pass on the planted falsification set (AC6) and the no-build contract is mechanically confirmable. Stage B: the coverage-matrix completeness checks pass (all source sections consumed, all D001–D100 represented, no atom without source pointer, no `SATISFIED` without evidence, no high-risk `UNKNOWN` without owner) and the challengers fail to break the classification — all from the record alone.

## 9. Open questions (interview the owner before planning)

Q1. Exact definitions and split of `BUILD_COMPLETE` vs `CAPABILITY_COMPLETE` vs `ASSURANCE_COMPLETE` vs `PROVEN` (assistant proposal msg 14 — needs owner ratification).
Q2. Which ~12 comparator lenses become audit canon (msg 14 shortlist)?
Q3. Does design-canon distillation (old D038; the eight-skill inventory) run inside this campaign or separately?
Q4. How is human taste calibration institutionalized (blind A/B against premium references; which judges)?
Q5. How deep do the agency-economics and tacit-dependency lenses go in the first campaign?
Q6. The load-bearing attachment `Nortropic_100_dagar_manual_v2.3_verified.pdf` was NOT captured in the sweep — it is the source of D001–D100 and must be captured before planning.
Q7. Relation to `gauntlet-wayfinder`: linked as related; the deeper merge question (the challengers and falsification fixtures echo the Gauntlet quality layer) is pending owner review.

## 10. Process for this brief

1. Clarify: first send a subagent to read `webbforvaltningen-capability-assurance-design-rationale.md` (its rejection and unresolved sections cover most §9 rationale) and report back what bears on §9; only if the rationale lacks the needed evidence, exact source wording matters, or a conflict/ambiguity remains, have it read the targeted message ranges in the source conversation via the rationale's retrieval map — never the whole transcript, and keep both out of main context; then interview the owner on §9 (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code ("address all notes, don't implement yet").
3. On explicit owner approval, persist the exact approved plan as `webbforvaltningen-capability-assurance-approved-plan.md`, validate it (`scripts/plan_contract.py validate`), bind it into this frontmatter and only then set `status: planned`.
4. Implement in a fresh session started from the approved plan: `plan_contract.py resume --slug webbforvaltningen-capability-assurance --target-repo <repo>`; reconcile against current repository truth; after any compaction re-read the plan from disk; if it cannot be proven, STOP with `PLAN_IDENTITY_UNAVAILABLE`.
5. Adversarial review: fresh subagent checks the diff against this brief and the approved plan.
6. Traceability: commit messages cite this brief's slug.

## References

- Source conversation: `webbforvaltningen-capability-assurance-full-chat.md` (same folder; 18 messages)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
