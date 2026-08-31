---
title: "Owner attention ≠ owner stop: Nortropic delegation order + surgical web-management patch"
type: idea-brief
status: idea
slug: owner-attention-inte-owner-stop
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: owner-attention-inte-owner-stop-full-chat.md
design_rationale: owner-attention-inte-owner-stop-design-rationale.md
intended_repo_path: owner-attention-inte-owner-stop/idea-owner-attention-inte-owner-stop.md
context_revision: 1
related: [bevaka-frontier-ai-engineering]
---

# Idea brief: Owner attention ≠ owner stop

## 1. Summary
Nortropic has accumulated unnecessary owner stops — especially in the web management
lane — and the owner wants trust-based attention escalation instead of concrete stops
(← msg 3). The design separates three conflated things (work may not continue / work
should be re-routed / Johnny should know) into four machine outcomes
(CONTINUE / ATTENTION_CONTINUE / ROUTE / HARD_STOP), with the governing rule that a
hard stop is defined by effect and mandate — never by an agent feeling uncertain. The
deliverable is a surgical Claude Code patch for webbförvaltningen (prompt in msg 13),
commissioned by the owner (← msg 12).

## 2. Context you need
Today `/nortropic-plan` turns every intervention outcome except `NY SAJT` into a
`STRATEGISK` open question, and `nortropic-autobygg` stops on every remaining
`STRATEGISK` question; a mechanical check enforces exactly that coupling — the
behavior is deliberate, and local (per the assistant's in-source repo inspection,
msg 11). The result: correct routing decisions ("improve existing site") wait for
owner approval they don't need. The wider frame is a Nortropic delegation order
(AUTONOMOUS / ATTENTION / ATTENTION-BEFORE-BOUNDARY / DELEGATION-BOUNDARY /
HARD STOP) with bounded trust: the system gathers evidence and proposes delegation
moves; only the owner changes delegation (← msg 3; 7).

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
- Webbförvaltningen decisions carry an explicit taxonomy: CONTINUE /
  ATTENTION_CONTINUE / ROUTE / HARD_STOP; the coupling "STRATEGISK = stop" is broken
  in favor of a separate machine-readable blocking classification.
- Owner attention becomes a first-class outcome: structured attention events
  (severity, decision, reason, evidence, actionTaken, ownerActionRequired), where
  ownerActionRequired=false is the important new possibility.
- Genuine authority/safety stops are preserved untouched: unresolved legal, required
  but unbuilt capability, remaining CRITICAL, broken fix/provenance contract,
  deploy/external irreversible effects, bootstrap/controller authority.
- Verification proves both directions: no unnecessary owner blocking, and no real
  boundary made permeable.
- Choose architecture/representation yourself, within §6; the msg 13 prompt is the
  intended contract, retrievable verbatim from the transcript.

## 4. Decisions already made (do not relitigate silently)
D1. Replace unnecessary owner stops with calling the owner's attention — trust-based;
the problem is currently frequent in webbförvaltningen — because many small normal
decisions are blocking autonomy where escalation should be reserved for real risk or
irreversibility (← msg 3; 4–7).
D2. Adjust this now, directly — not as a later architecture phase — because the
coupling is local in current code and a small, surgical delegation slice suffices
(← msg 8; 9–11).
D3. The implementation prompt for the surgical patch was commissioned ("ge mig
prompten för det") — because the analysis had converged on a bounded, verifiable
change (← msg 12; prompt 13).

R1. Removing owner stops one by one as point fixes — because it becomes another long
series of patches; replaced by a systematic Owner-Stop Audit with webbförvaltningen
first (assistant proposal within the owner's direction) (← msg 3; 7).
R2. A general fail-open change — because legal, capability, CRITICAL, provenance,
deploy and bootstrap-authority stops are explicitly frozen in place by the patch
(← msg 12; 10–11, 13).
R3. "STRATEGISK open question = automatic stop" — because strategic significance is
not per se a stop condition; a separate machine-readable blocking classification
decides, and unclassified must not silently become CONTINUE (← msg 12; 11).
R4. Touching the Input Gate in the same slice — because the phone/USP deviation is a
separate semantic question (what is minimally necessary input), not an
attention-vs-blocking question (← msg 12; 11, 13).

## 5. Acceptance criteria (v1)
AC1. WHEN the intervention decision is other than `NY SAJT` (FÖRBÄTTRA BEFINTLIG /
ICKE-SAJT-ÅTGÄRD / AVRÅD) or a scope-nej occurs, THE workflow SHALL route or close the
lane correctly and register an attention event with ownerActionRequired=false, without
waiting for owner approval — while never building the wrong product (← msg 3, 12; 11,
13).
AC2. WHEN a `STRATEGISK` open question lacks an explicit blocking classification, THE
system SHALL treat it as ATTENTION_CONTINUE; an explicitly blocking
strategic/authority question SHALL stop; an unclassified/invalid disposition SHALL
fail closed, never silently continue (← msg 12; 11, 13).
AC3. WHEN attention is raised, THE result SHALL carry machine-readable events
(severity, decision, reason, evidence, actionTaken, ownerActionRequired) visible in
the final report in a form future observability (Aquarium) can consume (← msg 3, 12;
11, 13).
AC4. WHEN real hard-stop conditions occur (unresolved material legal question,
required but unbuilt capability, remaining CRITICAL after the allowed autonomous fix
loop, broken fix/provenance contract), THE system SHALL still stop, and deploy SHALL
still never happen from autobygg — proven by mechanical tests mutated adversarially in
both directions (← msg 12; 11, 13).

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)
Invariants pointer: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`); pointer only.
Suggestions from the source: expected primary surfaces are
`agents/project-planner.md`, `skills/nortropic-plan/SKILL.md`,
`workflows/nortropic-autobygg.js`, `scripts/check-planner-routing.mjs` plus bound
tests/docs — change fewer files if that suffices; old artifacts without the new
classification must not gain authority by absence of a field (schema/version
detection, migration, or fail-closed); document the principle in ONE canonical place;
smallest diff, no broad refactoring, no new general authority architecture, no
notification infrastructure in this slice; ROUTE must never accidentally become
CONTINUE, HARD_STOP never degrade to attention.

## 7. Out of scope (v1)
- Owner-Stop Audit across all of Nortropic (proposed, not decided — §9).
- Splitting deploy and legal nodes into mandate-based autonomy (explicitly deferred).
- Input Gate parameterization (separate question).
- Trust-calibration mechanics (evidence-based delegation proposals ATTENTION →
  AUTONOMOUS) — future design.
- Slack/email notification infrastructure.

## 8. Verification (how we know it works)
From the record alone: the patch's Definition-of-Done gate shows PASS on both
directions — OWNER_ATTENTION_NE_OWNER_APPROVAL, NONBLOCKING_STRATEGIC_CONTINUES,
INTERVENTION_NON_NEW_SITE_DOES_NOT_BUILD / _DOES_NOT_WAIT_FOR_OWNER,
SCOPE_NEJ_ROUTES_WITHOUT_BYPASS, UNCLASSIFIED_DECISION_FAILS_CLOSED, and the five
*_HARD_STOP_PRESERVED / DEPLOY_AUTHORITY_UNCHANGED / BOOTSTRAP_AUTHORITY_UNCHANGED
checks — with adversarial mutations proving the tests catch inversions (← msg 13).

## 9. Open questions (interview the owner before planning)
Q1. Owner-Stop Audit over all of Nortropic (beyond webbförvaltningen) — proposed as
separate work; commission it?
Q2. Splitting the deploy and legal nodes into mandate-based autonomy — explicitly
deferred; when?
Q3. Input Gate parameterization (minimally necessary input) — separate question;
schedule it?
Q4. Design of the trust-calibration mechanism (system proposes delegation moves with
evidence; owner decides) — not yet designed.
Q5. Outcome: was the msg 13 prompt run, and did the patch land? Outside this source.

## 10. Process for this brief
1. Clarify: first send a subagent to read
   `owner-attention-inte-owner-stop-design-rationale.md` (its rejection and unresolved
   sections cover most §9 rationale) and report back what bears on §9; only if the
   rationale lacks the needed evidence, exact source wording matters, or a
   conflict/ambiguity remains, have it read the targeted message ranges in the source
   conversation via the rationale's retrieval map — never the whole transcript, and
   keep both out of main context; then interview the owner on §9 (AskUserQuestion);
   append answers here.
2. Plan in plan mode; owner reviews before any code ("address all notes, don't
   implement yet").
3. On explicit owner approval, persist the exact approved plan as
   `owner-attention-inte-owner-stop-approved-plan.md`, validate it
   (`scripts/plan_contract.py validate`), bind it into this frontmatter
   (`approved_plan` + `approved_plan_sha256` + `plan_version`) and only then set
   `status: planned`. Nothing is summarized away; a short execution prompt never
   replaces the plan file.
4. Implement in a fresh session, started from the approved plan:
   `plan_contract.py resume --slug owner-attention-inte-owner-stop --target-repo
   <repo>` proves the plan identity; reconcile the plan against current repository
   truth before continuing. After any compaction, re-read the plan from disk — never
   reconstruct it from memory; if it cannot be proven, STOP with
   `PLAN_IDENTITY_UNAVAILABLE`.
5. Adversarial review: fresh subagent checks the diff against this brief and the
   approved plan; report only gaps affecting correctness or stated requirements.
6. Traceability: commit messages cite this brief's slug.

## References
- Source conversation: `owner-attention-inte-owner-stop-full-chat.md` (same folder)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
