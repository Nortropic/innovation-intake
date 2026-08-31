---
title: "Provider failover: Claude takes over the bootstrap from Codex at the usage cap, under the same Nortropic work-form"
type: idea-brief
status: idea
slug: claude-bootstrap-takeover-protocol
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: claude-bootstrap-takeover-protocol-full-chat.md
design_rationale: claude-bootstrap-takeover-protocol-design-rationale.md
intended_repo_path: claude-bootstrap-takeover-protocol/idea-claude-bootstrap-takeover-protocol.md
context_revision: 1
related: [bootstrap-closeout-rebaseline, nortropic-organization-os, agent-harness-priorities]
---

# Idea brief: Claude Bootstrap Takeover Protocol

## 1. Summary
If Codex usage runs out before the bootstrap is finished, Claude shall continue
working exactly the way Codex works now — the same autonomous supervisor loop, not "in
its own way" (← msg 38). The durable idea is a standing provider-failover protocol:
transfer authority, epistemology, exact mechanically verified state and the
supervisor work-form, via a Codex-produced machine-verifiable checkpoint from which
the Claude prompt is built. The framing conviction: the autonomy difference is mostly
the Nortropic harness/mandate, not the model — institutional state lives in Nortropic,
not in any model's context.

## 2. Context you need
The source chat is a standing Bootstrap status/control thread. The owner asked why
Codex works so much more autonomously than Claude Code did (← msg 35); the assistant's
analysis: Codex inherited a much better Nortropic (authority, worktrees, immutable
candidates, adversarial reviewers, supervisor form), got an explicit mandate, and
internalized Nortropic's epistemology — Claude given the same rails would likely look
dramatically more autonomous (← msg 36–37, assistant analysis). At the time of the
conversation Codex was working locally ahead of published main (H035-R15 lane,
published authority PR #175), which makes a careless mid-round provider switch
genuinely dangerous. Protocol details are largely assistant-authored; the intention
and trigger procedure are owner-backed.

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
- A standing Claude Bootstrap Takeover Protocol so a Codex usage cap becomes a
  provider switch, not a work stop: Codex and Claude Code as interchangeable
  executors under the same Nortropic work-form.
- Four transfer objects: (1) authority — same mandate to build, spawn
  reviewers/subagents, mutation-test, commit, push, PR, merge, stopping only at a
  proven owner boundary; (2) epistemology — structural green ≠ executable proof, own
  review ≠ independent review, working tree ≠ immutable reviewed candidate, git clean
  ≠ physical exactness, claimed blocker ≠ blocker until tested; (3) exact current
  state — start from repo artifacts (handoff doc, decision log, git/worktree status,
  latest checkpoint) and mechanically verify claims before continuing; (4) the
  supervisor work-form — keep the main goal, parallelize bounded questions, don't
  bounce control back to the owner.
- A two-prompt handoff: first a prompt to Codex producing a safe machine-verifiable
  checkpoint; then a Claude prompt built from exactly those bytes plus current GitHub
  truth — never a generic "continue the bootstrap" prompt.
- Symmetric switching (Claude → Codex → Claude) so institutional state lives in
  Nortropic.
- Choose the concrete protocol form/artifacts yourself, within §6.

## 4. Decisions already made (do not relitigate silently)
D1. Claude shall continue working the same way Codex does if Codex usage runs out
before the bootstrap is done on the current usage cap — because the work-form
(autonomous loop under Nortropic authority) is the asset; a provider switch must not
change it (← msg 38; elaboration 39).
D2. Trigger procedure: Johnny says when usage starts running low; then a handoff
prompt to Codex is prepared for the handover so Claude continues the same way —
because the checkpoint must be produced by the outgoing worker at a safe boundary,
then turned into the incoming worker's prompt from actual bytes (← msg 40; 41).

R1. IMPLICIT (via the requirement "fortsätta på samma sätt"): Claude taking over the
project in its own style, or a provider switch meaning restart with manual
reconstruction of state and orchestration — because that forfeits the institutional
state and re-introduces the human as reconstruction layer (← msg 38, 40; 39, 41).

## 5. Acceptance criteria (v1)
AC1. WHEN the owner signals that Codex usage is running low, THE prepared Codex
handoff prompt SHALL make Codex finish or safely stop the current atomic step, start
no new slice, and report authoritative main/HEAD/worktree/branch/dirty state,
published authority vs unpublished candidates/evidence, active task/phase/blockers,
parallel lanes and verdicts, and an exact resume boundary for Claude (← msg 40; 41).
AC2. WHEN Claude takes over, IT SHALL operate under the same authority and
epistemology as the outgoing Codex loop and SHALL mechanically verify the checkpoint's
claims against the repo before continuing — never treating the checkpoint as a
TODO-list to check off from text (← msg 38; 39).
AC3. WHEN taking over, Claude SHALL inspect before mutation: never switch branches or
"clean" in an existing Codex worktree with unpublished work until its git status,
HEAD, branch, untracked files and relation to authoritative main are documented;
uncommitted work is preserved and identified, never discarded (← msg 38; fail-safe
rule 39).
AC4. WHEN Claude usage in turn runs out, THE same protocol SHALL work symmetrically
(Claude → Codex), with no bootstrap-institutional state living solely in either
model's context (← msg 38; 39).
Caveat: AC1's checkpoint fields and AC3–AC4 rest on assistant elaboration (msgs 39,
41) after the owner's adoption messages; confirm details in the §9 interview.

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)
Invariants pointer: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`); pointer only.
Suggestions from the source: state transfer starts from repo artifacts
(`docs/agentoverlamning.md`, tail of `docs/05-beslutslogg.md`, git/worktree status,
latest checkpoint), not from a narrative of what we think happened; if Codex leaves a
clean immutable commit, Claude creates its own fresh worktree from it; the takeover
prompt is composed from the actual Codex handoff output plus verified GitHub truth;
no rushed model switch — check where the bootstrap actually stands first; align with
bootstrap-closeout-rebaseline's provider-neutral SUB-1 direction and respect its
phase-A deferral of "Claude migration mid-run" (see Q4).

## 7. Out of scope (v1)
- Executing the takeover now (contingency only — triggered by the owner's signal).
- The Codex-vs-Claude A/B comparison after bootstrap (assistant proposal, not a
  decided experiment — §9).
- Making provider-survivability an Autonomy Kernel v1 requirement (assistant
  proposal, unconfirmed — §9).
- General per-role model routing in Organization OS (related idea, other packages).
- The bootstrap execution log itself (the surrounding thread's status reporting is
  not brainstorm truth).

## 8. Verification (how we know it works)
From the record alone: a dry-run (or the real event) leaves (a) a Codex checkpoint
whose claims are each mechanically checkable (SHAs, branch states, lane verdicts),
(b) a takeover prompt provably built from those bytes plus verified GitHub truth, and
(c) a Claude session log showing verification-before-continuation and untouched
pre-existing worktrees — an independent reviewer can confirm no work was lost and no
unpublished bytes were mutated across the switch.

## 9. Open questions (interview the owner before planning)
Q1. The protocol's concrete content (four transfer objects, inspect-before-mutation,
checkpoint format, Claude↔Codex symmetry) is assistant-proposed and never
owner-ratified point by point — ratify or amend.
Q2. What threshold counts as "usage starting to run out"? Owner signals manually; no
mechanical trigger is defined.
Q3. Should provider-survivability of the bootstrap be an explicit Autonomy Kernel v1
requirement (assistant proposal, msg 39)?
Q4. Reconciliation with `bootstrap-closeout-rebaseline`, whose phase A defers "Claude
migration mid-run": is the usage-cap failover exempt from that deferral?
Q5. Is the post-bootstrap A/B comparison Codex vs Claude (assistant, msg 37) wanted
at all? The owner asked the comparative question (msg 35) but never decided an
experiment.

## 10. Process for this brief
1. Clarify: first send a subagent to read
   `claude-bootstrap-takeover-protocol-design-rationale.md` (its rejection and
   unresolved sections cover most §9 rationale) and report back what bears on §9;
   only if the rationale lacks the needed evidence, exact source wording matters, or
   a conflict/ambiguity remains, have it read the targeted message ranges in the
   source conversation via the rationale's retrieval map — never the whole
   transcript, and keep both out of main context; then interview the owner on §9
   (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code ("address all notes, don't
   implement yet").
3. On explicit owner approval, persist the exact approved plan as
   `claude-bootstrap-takeover-protocol-approved-plan.md`, validate it
   (`scripts/plan_contract.py validate`), bind it into this frontmatter
   (`approved_plan` + `approved_plan_sha256` + `plan_version`) and only then set
   `status: planned`. Nothing is summarized away; a short execution prompt never
   replaces the plan file.
4. Implement in a fresh session, started from the approved plan:
   `plan_contract.py resume --slug claude-bootstrap-takeover-protocol --target-repo
   <repo>` proves the plan identity; reconcile the plan against current repository
   truth before continuing. After any compaction, re-read the plan from disk — never
   reconstruct it from memory; if it cannot be proven, STOP with
   `PLAN_IDENTITY_UNAVAILABLE`.
5. Adversarial review: fresh subagent checks the diff against this brief and the
   approved plan; report only gaps affecting correctness or stated requirements.
6. Traceability: commit messages cite this brief's slug.

## References
- Source conversation: `claude-bootstrap-takeover-protocol-full-chat.md` (same folder)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
