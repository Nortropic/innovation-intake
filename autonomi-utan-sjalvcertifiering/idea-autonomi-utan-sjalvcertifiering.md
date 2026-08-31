---
title: "Autonomy without self-certification: hard-stop taxonomy, owner-authority invariant, provider confinement"
type: idea-brief
status: idea
slug: autonomi-utan-sjalvcertifiering
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: autonomi-utan-sjalvcertifiering-full-chat.md
design_rationale: autonomi-utan-sjalvcertifiering-design-rationale.md
intended_repo_path: autonomi-utan-sjalvcertifiering/idea-autonomi-utan-sjalvcertifiering.md
related: [bootstrap-closeout-rebaseline, agent-harness-priorities]
---

# Idea brief: Autonomy without self-certification

## 1. Summary
A doctrine cluster that outgrew the bootstrap-closeout brief: autonomy redesigned so a
NORMAL_WORKFLOW_TRANSITION is never a human stop while an explicit hard-stop taxonomy
keeps the genuinely dangerous cases human. The key framing decision, the
owner-authority invariant: an agent may autonomously fix defects but may never expand
its own trust authority — every expansion requires owner review of the exact
allowlist/inventory/design diff. Around it: PREVENTION>RECOVERY provider confinement,
immutable failed candidates, atomic no-overwrite publication, provider handoff via
Git/effect evidence, and safe/speculative parallelism under one coordinator.

## 2. Context you need
The bootstrap campaign commissioned by the closeout brief ran into Codex quota
exhaustion; the owner moved execution to Claude Code inside nortropic-system, rounds
R112–R122 unfolded with real security defects found by cross-provider review, and the
autonomy/authority doctrine crystallized under pressure. This brief covers only msgs
74–128 of the source conversation; the corpus-closeout/synthesis method (msgs 23–56)
is the sibling brief `korpusfrysning-och-syntesmetod`. Caveat: many owner-role turns
in this range are pasted agent reports/menus; decisions below rest on the owner's own
words or his explicit relays, marked where relayed.

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
- Hard-stop taxonomy: NORMAL_WORKFLOW_TRANSITION ≠ HUMAN_STOP; autonomy does not mean
  self-certification — review stays independent.
- The owner-authority invariant with reviewable exact diffs for any authority
  expansion; least-authority source-form freezing (freeze the exact call form, with
  negative controls); authority retirement (drop unused frozen authority); the
  measurability hard stop (if the sandbox cannot express the exact capability, stop —
  never approximate or broaden).
- PREVENTION>RECOVERY provider confinement replacing cleanup-as-security (cleanup =
  defense-in-depth only); PROVIDER_RETURNED ≠ PROVIDER_ATTEMPT_FINISHED
  (owned-process-family quiescence on all terminal paths).
- Atomic no-overwrite publication (CREATE_IF_ABSENT / NEVER_OVERWRITE); the
  candidate-materialization trust boundary (candidate = deterministic function of
  authoritative base + validated result + frozen contract; provider scratch is never
  authority); immutable failed candidates.
- Provider-handoff doctrine via Git/effect evidence, never model memory;
  review-independence taxonomy (context-isolated-same-provider ≠ cross-provider);
  safe/speculative parallelism (N independent builders on one frozen task, adversarial
  comparison, pick not merge) with model/effort routing by epistemic risk.
Choose architecture, decomposition and tooling yourself, within §6's constraints.

## 4. Decisions already made (do not relitigate silently)
D1. When Codex quota ran out, Claude Code continues the bootstrap inside
    nortropic-system — because idle quota must not stall the campaign: "Vi fick slut
    usage, kan du kolla av git och se om vi kan arbeta vidare med Claude code
    istället?" (← msg 78; anticipated ← msg 74). NOTE: this contradicts the closeout
    brief's D1/D4 separation and awaits owner ratification — see §9 Q1.
D2. The handoff prompt includes the end goal so the agent understands direction —
    "behöver vi även nämna slutmålet? så claude förstår vars vi arbetar mot?"
    (← msg 83).
D3. Autonomy redesign commissioned — "why is it stopping? i want it to work autonomous
    towards the end goal" (← msg 89, owner question appended to a pasted report).
D4. Returned Codex quota is reserved rather than switched to immediately — "Vi har
    codex usage igen som vi använder senare när claude är klar" (← msg 92).
D5. The R115 trust-authority expansion goes review-first: the exact
    allowlist/inventory diff and design are presented for approval before any mutation
    — ratified by the executed review flow (← msgs 96, 98; msg 96 is a pasted option
    menu, the routing itself is the owner act).
D6. Primary provider switches back to Codex before token reset to maximize usage —
    "jag vill maxa usage där innan reset … Kan vi återgå till Codex jobba klart"
    (← msg 108). Provider assignment is thereby operationally fluid — §9 Q1.
D7. One canonical coordinator terminal; the coordinator spawns agents itself — because
    the owner confirmed single-terminal operation and observed "Den kunde starta
    själv" (← msgs 118, 121, 123).

R1. Cleanup-as-security-boundary — because a provider that can outrace cleanup owns
    the race; replaced by provider confinement (Option A) plus the kernel no-overwrite
    fix; "Option B avslås som ofullständig" (← msg 106, owner relay of the Codex
    ruling; defect analysis in msgs 102, 105, 107).
R2. Patching a failed candidate in place — because a failed candidate is forensic
    evidence; "e167fc0 och R115 förblir immutable", fresh round from authoritative
    main (← msg 106, owner relay; practice msgs 86, 89; design msgs 88, 95).
R3. Agent Teams for parallelism — because the chosen model is one coordinator with
    fresh context-isolated reviewer subagents (← msg 121; design msgs 91, 95, 117).
R4. Retaining R115's dirfd-unlink authority once confinement removes the need —
    "ingen generell dirfd- eller TMPDIR-auktoritet" (← msg 106, owner relay; authority
    retirement analysis msg 105).

## 5. Acceptance criteria (v1)
AC1. WHEN a workflow reaches a NORMAL_WORKFLOW_TRANSITION, THE system SHALL continue
     autonomously toward the end goal; only taxonomized hard stops halt for the owner
     (← msg 89; taxonomy in assistant msgs 91, 95).
AC2. WHEN an agent's work would expand its own trust authority, THE system SHALL stop
     and present the exact allowlist/inventory/design diff for owner review before any
     mutation (← msgs 96, 98, 102).
AC3. WHEN a candidate fails review, THE system SHALL freeze it as immutable forensic
     evidence and start a fresh round from authoritative main (← msg 106 relay;
     practice msgs 86, 89).
AC4. WHEN work hands off between providers, THE receiving provider SHALL reconstruct
     state from Git and effect evidence only, never from model memory (← msgs 78, 108
     ratified-by-action; doctrine in assistant msgs 82, 95, 117).
AC5. WHEN a result publishes, THE system SHALL use atomic CREATE_IF_ABSENT /
     NEVER_OVERWRITE semantics — a concurrently created canonical object is never
     overwritten (← msg 106 relay contract; defect #5 in msg 102).

## 6. Constraints & implementation notes (suggestions, not orders)
Invariants: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`). Pointer only.
- Measurability hard stop: if the sandbox cannot express the exact capability, stop;
  never approximate or broaden (assistant doctrine, msgs 95, 105, 107).
- Review independence: context-isolated-same-provider review is weaker than
  cross-provider review — the R115 defects were caught only cross-provider (← msg 102).
- Route model/effort by epistemic risk; speculative parallelism picks one winner, it
  never merges candidates (assistant design msgs 117–128, owner steering ← msgs 118,
  121, 123, 127).

## 7. Out of scope (v1)
- The corpus-freeze/synthesis method (msgs 23–56) — sibling brief
  `korpusfrysning-och-syntesmetod`.
- The closeout campaign's own phase plan and "klart bootstrap" definition (existing
  package bootstrap-closeout-rebaseline).
- Agent Teams (R3); any general dirfd/TMPDIR authority (R4).

## 8. Verification (how we know it works)
End-to-end: one bounded round in which (a) a normal transition proceeds without a
human stop, (b) a deliberate authority-expansion attempt hard-stops with the exact
diff presented, and (c) a deliberately failed candidate stays immutable while a fresh
round succeeds — all provable from Git/effect evidence alone by an independent
reviewer.

## 9. Open questions (interview the owner before planning)
Q1. PENDING OWNER REVIEW: D1 and D6 are flagged reversal candidates against the
    closeout brief's D1 ("do not touch the running bootstrap") and D4 ("fully
    separated") — owner-initiated under quota pressure, but not yet ratified as a
    standing provider-fluidity policy. Do not treat either position as settled.
Q2. Is the Codex-authored R116 contract that ChatGPT declared "binding owner-contract"
    (msg 107) owner-ratified? Only the owner relay in msg 106 is visible.
Q3. What is the standing status of the bounded host-execution authorization pattern
    (msgs 78, 82, 85, 95)?
Q4. The bootstrap checkpoint was still unreached at thread end (R122, H032 148/4) —
    where do these doctrines get frozen?

## 10. Process for this brief
1. Clarify: first send a subagent to read
   `autonomi-utan-sjalvcertifiering-design-rationale.md` and report what bears on §9;
   only if evidence is missing there, read the targeted message ranges via the
   rationale's retrieval map — never the whole transcript, and keep both out of main
   context; then interview the owner on §9 (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code.
3. On explicit owner approval, persist the approved plan as
   `autonomi-utan-sjalvcertifiering-approved-plan.md`, validate and bind it in the
   frontmatter, then set `status: planned`.
4. Implement in a fresh session started from the approved plan; after any compaction
   re-read the plan from disk.
5. Adversarial review: fresh subagent checks the diff against this brief and the plan.
6. Traceability: commit messages cite this brief's slug.

## References
- Source conversation: `autonomi-utan-sjalvcertifiering-full-chat.md` (same folder)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
