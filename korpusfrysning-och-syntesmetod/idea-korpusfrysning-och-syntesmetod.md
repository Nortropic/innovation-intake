---
title: "Corpus freeze and synthesis method: evidence grading, authority attribution, two-tier verification"
type: idea-brief
status: idea
slug: korpusfrysning-och-syntesmetod
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: korpusfrysning-och-syntesmetod-full-chat.md
design_rationale: korpusfrysning-och-syntesmetod-design-rationale.md
intended_repo_path: korpusfrysning-och-syntesmetod/idea-korpusfrysning-och-syntesmetod.md
related: [project-corpus-intake, nortropic-recompile, bootstrap-closeout-rebaseline]
---

# Idea brief: Corpus freeze and synthesis method

## 1. Summary
Durable R&D-corpus methodology that emerged while executing the closeout campaign: a
corpus durability protocol ending in ONE atomic campaign commit whose SHA becomes the
canonical downstream input identity, plus a synthesis method with evidence grading,
authority attribution and two-tier verification. The key framing decision: mechanical
coverage proof and semantic correctness are different things — an independent semantic
reviewer is a required gate before any freeze, because coherence is not evidence and
repetition is not truth.

## 2. Context you need
The improvements-corpus campaign (15 chats → 13+ idea packages) reached closeout, and
Phase 2 cross-chat synthesis ran in nortropic-knowledge. The method that carried both —
QA gates, freeze semantics, grading vocabulary — is worth extracting as standing
procedure. This brief covers only msgs 23–56 of the source conversation; the
autonomy/provider doctrine (msgs 74–128) is the sibling brief
`autonomi-utan-sjalvcertifiering`. Caveat: most owner-role turns here are pasted agent
reports; decisions rest on the owner's own routing acts and ratification-by-action,
marked where relayed.

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
- Corpus durability protocol: independent rubric-QA gate → supersede resolution →
  read-only consistency audit → ONE atomic campaign commit → frozen corpus SHA as the
  canonical input identity for the next phase.
- Live-watch re-harvest policy: chat snapshot → immutable intake; a new intake only on
  materially new decisions; daily reports route to the Observatory flow, not the idea
  corpus.
- Evidence-grading vocabulary: INDEPENDENT_CONVERGENCE / DEPENDENT_REFINEMENT /
  SHARED_PRIOR_CONTEXT / UNKNOWN — with the guard rails COHERENCE_IS_NOT_EVIDENCE,
  ELEGANCE_IS_NOT_AUTHORITY, REPETITION_IS_NOT_TRUTH, RECENCY_IS_NOT_SUPERSESSION,
  ASSISTANT_SPECIFICITY_IS_NOT_OWNER_INTENT.
- Authority attribution separating "idea present in chat" from "direction the owner
  chose": owner decision / assistant proposal / ratified-by-action / inference.
- Two-tier verification: mechanical coverage proof (Pass E class) plus an independent
  semantic reviewer, both required before freezing; bounded remediation in between.
- Artifact conventions: English synthesis with verbatim Swedish owner quotes, rfcs/
  with status: proposed and authority: none, corpus SHA as canonical_sources; pointer
  discipline — the git identity of a committed artifact is the durable pointer.
Choose architecture, decomposition and tooling yourself, within §6's constraints.

## 4. Decisions already made (do not relitigate silently)
D1. Closeout waits for the independent rubric-QA reviewer — "Ska vi invänta detta
    först?" routed the campaign through the fresh no-context reviewer before closing
    (← msg 26).
D2. Surgical fixes are autonomous; length trimming is an owner call — because
    shortening risks substance; executed exactly so ("Ingen nedkortning gjord, enligt
    beslut") (← msgs 28, 30; pasted-report framing with owner adoption).
D3. Closeout = supersede verkställd + read-only audit + ONE atomic commit + push;
    corpus frozen at 62e9fd4 as canonical Phase-3 input identity (← msg 30, owner-run
    execution report). NOTE on the push: see §9 Q3.
D4. Synthesis artifact language is English (Swedish owner quotes verbatim) and it
    lives in rfcs/ with status: proposed — ratified by the delivered artifact
    (← msgs 34, 36 routing; result confirmed ← msg 40).
D5. Phase 2 freezes and pushes only after verified remediation — Pass E green AND
    independent semantic review, remediation 4/4 fixed, frozen at 5c8a811
    (← msgs 47, 53).

R1. The Task Capsule ⊃ Context Manifest unification hypothesis — because the corpus
    falsified it: the transcripts support synonyms, not the layered hierarchy, and the
    chronology was inverted; canonical naming left OWNER_CHOICE_REQUIRED (← msg 40,
    owner-run report: "transkripten stödjer synonymer, inte din skiktade hypotes";
    analysis msgs 25, 33, 43, 46).
R2. Memory pointers on synthesis artifacts — because the git identity of a committed
    artifact is the durable pointer; the memory note was skipped and never replaced
    (← msg 40, owner-run report; assistant ruling msg 41).

## 5. Acceptance criteria (v1)
AC1. WHEN a corpus campaign closes, THE system SHALL pass an independent rubric-QA
     gate and a read-only consistency audit, then land as ONE atomic commit whose SHA
     becomes the canonical downstream input identity (← msgs 26, 30).
AC2. WHEN a synthesis claim is recorded, THE system SHALL grade its evidence
     (INDEPENDENT_CONVERGENCE / DEPENDENT_REFINEMENT / SHARED_PRIOR_CONTEXT / UNKNOWN)
     and attribute its authority (owner decision vs assistant proposal vs
     ratified-by-action) (← msgs 40, 47; vocabulary in assistant msg 43).
AC3. WHEN a synthesis artifact is candidate-complete, THE system SHALL require both
     the mechanical coverage proof and an independent semantic review, with bounded
     remediation, before freezing (← msgs 40, 47, 53).
AC4. WHEN a live-watch chat is re-captured, THE system SHALL treat the prior snapshot
     as immutable, open a new intake only on materially new decisions, and route
     daily/weekly reports to the Observatory flow (← msg 30 execution of the policy;
     policy authored in assistant msg 25).
AC5. WHEN a frozen artifact must be referenced later, THE reference SHALL be its git
     identity (repo@SHA), not a memory note or prose pointer (← msgs 40, 53; ruling in
     assistant msg 41).

## 6. Constraints & implementation notes (suggestions, not orders)
Invariants: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`). Pointer only.
- The semantic reviewer must be genuinely independent (fresh context, no authorship of
  the reviewed artifact) — the verifier's own two real bugs were caught this way
  (← msg 40).
- Synthesis artifacts carry authority: none until owner decisions promote them.
- Keep verbatim Swedish owner quotes inside English artifacts — translation is
  interpretation.

## 7. Out of scope (v1)
- The autonomy/provider doctrine (msgs 74–128) — sibling brief.
- Phase 3 rebaseline itself (reserved questions listed in the RFC's §14; awaits the
  bootstrap checkpoint).
- Resolving the ContextPack/Context Manifest/Task Capsule naming (explicitly
  OWNER_CHOICE_REQUIRED — §9 Q1).

## 8. Verification (how we know it works)
End-to-end: run one small corpus campaign (or a dry-run replay) through the full
protocol — rubric QA, audit, ONE commit, graded synthesis, Pass E + independent
semantic review — and confirm from the record alone that every claim carries a grade
and an authority attribution and that the freeze SHA is the only pointer downstream
artifacts use.

## 9. Open questions (interview the owner before planning)
Q1. Final states of the three msg-23 pending owner decisions: post-14 supersede
    handling (resolved in-thread at msg 30), live-chat re-harvest cadence, and the
    ContextPack/Context Manifest/Task Capsule canonical name (left
    OWNER_CHOICE_REQUIRED at msgs 40, 43, 46).
Q2. Should this method be folded back into the nortropic-intake skill /
    openai-anthropic-workflow package as the canonical procedure?
Q3. PENDING OWNER REVIEW: the closeout and Phase-2 pushes (← msgs 30, 53) are flagged
    against the closeout brief's D5 ("fetch+rebase authorized, no push"). The analysis
    reads them as the reserved owner decision being exercised at closeout — recorded
    for the record, not judged; confirm that reading.

## 10. Process for this brief
1. Clarify: first send a subagent to read
   `korpusfrysning-och-syntesmetod-design-rationale.md` and report what bears on §9;
   only if evidence is missing there, read the targeted message ranges via the
   rationale's retrieval map — never the whole transcript, and keep both out of main
   context; then interview the owner on §9 (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code.
3. On explicit owner approval, persist the approved plan as
   `korpusfrysning-och-syntesmetod-approved-plan.md`, validate and bind it in the
   frontmatter, then set `status: planned`.
4. Implement in a fresh session started from the approved plan; after any compaction
   re-read the plan from disk.
5. Adversarial review: fresh subagent checks the diff against this brief and the plan.
6. Traceability: commit messages cite this brief's slug.

## References
- Source conversation: `korpusfrysning-och-syntesmetod-full-chat.md` (same folder)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
