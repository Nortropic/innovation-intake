---
title: "Bootstrap closeout and rebaseline: finish narrow, observe, rebaseline, continue"
type: idea-brief
status: idea   # lifecycle: idea → clarified → planned → building → verified; terminal: superseded
slug: bootstrap-closeout-rebaseline
owner: Johnny (Nortropic)
created: 2026-08-20
source_conversation: bootstrap-closeout-rebaseline-full-chat.md   # reference only — this brief takes precedence
intended_repo_path: bootstrap-closeout-rebaseline/idea-bootstrap-closeout-rebaseline.md
---

# Idea brief: Bootstrap closeout and rebaseline — finish narrow, observe, rebaseline, continue

## 1. Summary

The strategy for taking on Nortropic's remaining work: **let Codex finish the running
bootstrap untouched, but define "klart bootstrap" narrowly** — the self-hosting
checkpoint (supervisor resumes, a real agent launches, work passes the mechanical
trust boundaries, evidence survives the process), NOT all ~18 roadmap slices. At
first-real-launch, pause at a deliberate checkpoint: **BOOTSTRAP → OBSERVE →
REBASELINE → CONTINUE** — using the harvested chat corpus as an R&D corpus whose
synthesis classifies every major concept as **KEEP / SIMPLIFY / ADD / DEFER**, flowing
full-chat → knowledge/research → synthesized architecture delta → owner decision →
nortropic-system (never chat → agent → production). Meanwhile Claude Code prepares
the next phase in parallel via the nortropic-intake campaign. This chat is the
campaign's own origin and in-flight decision log.

## 2. Context you need

Codex's estimate at the time: ~18 functional slices left, 38–42 handoffs, 150–300
agent hours, 3–6 weeks (6–10 with quota pauses). The two-layer distinction: the
**Bootstrap Kernel** being built now (authority → task → isolated execution →
candidate → mechanical verification → persisted evidence → safe resume) vs the
**Nortropic Engineering Platform** (the next phase where the slices belong). The
provider-neutral direction is already owner-authorized: SUB-1 refrozen as
AgentProvider + ClaudeCodeProvider (default) + CodexProvider; H032 is kept as the
Codex adapter/security boundary, not discarded. Messages 12–22 record the ingestion
campaign's operational decisions (Plan Mode first, manifest home in
`~/nortropic/intake-campaigns/`, authorized fetch+rebase without push, manual
approval, one chat at a time with manifest as canonical state).
Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen
gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- Phase A (now): Codex finishes the current chain to first real autonomous launch —
  no new Frontier Delta agent, no new documentation architecture, no speed
  mechanisms, no Claude migration mid-run (nothing that grows the state space while
  proving the bootstrap).
- Phase B (Bootstrap Closeout): at first-real-launch, freeze a reproducible
  checkpoint.
- Then the rebaseline: synthesize the full idea corpus into an architecture delta
  where each major concept is KEEP (proven fundamentally right) / SIMPLIFY
  (overbuilt vs what provider harnesses now do) / ADD (genuinely missing) / DEFER
  (good but off critical path) — decided by the owner, then executed through
  nortropic-system's normal authority.
- The ingestion campaign (this one) completes the corpus so the rebaseline has all
  material with provenance.

Choose architecture/decomposition/tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

- D1. Do NOT touch the running bootstrap; Codex continues exactly where it is ("den
  arbetar ju just nu så den arbetar på") (← msg 5–6).
- D2. "Klart bootstrap" = the self-hosting checkpoint, NOT SUB-1–4 + S2 + S4–S13 + L
  — that is the next phase (← msg 7).
- D3. At first-real-launch: deliberate pause — BOOTSTRAP → OBSERVE → REBASELINE →
  CONTINUE; the chat corpus is an R&D corpus, never a direct agent feed into
  production (← msg 7).
- D4. Claude Code prepares the next phase in parallel NOW via nortropic-intake,
  fully separated from nortropic-system; the skill's fail-closed rules are not
  weakened for batch convenience (← msg 8–11).
- D5. Campaign operational decisions: Plan Mode first; manifest in
  `~/nortropic/intake-campaigns/` (process ≠ result); fetch+rebase authorized, no
  push; one chat at a time with the manifest as sole canonical workflow state
  (← msg 12–20).
- D6 (from the Codex side, owner-endorsed): SUB-1 refrozen to AgentProvider +
  ClaudeCodeProvider (default) + CodexProvider; H032 kept as adapter boundary
  (← msg 1, 7).
- R1 (REJECTED). Letting "bootstrap" swell to the full roadmap; feeding hundreds of
  brainstorm pages directly to agents; changing production from chat content —
  because each would grow the state space mid-proof or bypass the authority chain
  (← msg 7).

## 5. Acceptance criteria (v1)

- AC1. WHEN the bootstrap reaches first real autonomous launch, THE checkpoint SHALL
  be frozen reproducibly before roadmap execution continues.
- AC2. WHEN the rebaseline runs, THE synthesis SHALL classify each major corpus
  concept as KEEP/SIMPLIFY/ADD/DEFER with provenance to briefs/transcripts, and SHALL
  produce owner decisions before any nortropic-system change.
- AC3. WHEN campaign/preparation work runs (this campaign included), THE record SHALL
  show zero writes to nortropic-system and no disturbance of the running chain.
- AC4. WHEN the corpus is used for synthesis, THE inputs SHALL be the delivered
  briefs (with transcripts as evidence), never raw chat dumps.

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants: Nortropic's trust layer — constitution & rulebook (pointer, never a copy).
Suggestions: the synthesis output contract already drafted in the campaign README
(grouping categories + KEEP/SIMPLIFY/ADD/DEFER/REJECT/NEEDS EVIDENCE) implements D3;
proposed home for the synthesis is nortropic-knowledge (non-normative); the pending
OWNER_CLASSIFICATION items in the campaign manifest are prerequisites for a complete
rebaseline input set.

## 7. Out of scope (v1)

- Executing the rebaseline (a separate owner-initiated step after closeout).
- Any of the deferred tracks during Phase A (Frontier Delta agent build,
  documentation architecture, speed mechanisms, Claude migration).
- Modifying the intake skill's safety model.

## 8. Verification (how we know it works)

From the record: the frozen checkpoint exists and is reproducible (AC1); the
rebaseline document classifies with provenance and carries explicit owner decisions
(AC2); campaign separation proofs show nortropic-system untouched throughout (AC3).

## 9. Open questions (interview the owner before planning)

- Q1. What exactly constitutes the frozen closeout checkpoint artifact (tag? evidence
  bundle? both)?
- Q2. Who performs the rebaseline synthesis (fresh Claude session per the campaign
  contract?) and what is its deliverable format in nortropic-knowledge?
- Q3. The OBSERVE step: how long/what evidence from the first autonomous runs before
  rebaselining?
- Q4. After rebaseline: does the phase plan (B onward, msg 7's five phases) become a
  canonical roadmap document in nortropic-system through the normal authority chain?

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

- Source conversation: `bootstrap-closeout-rebaseline-full-chat.md` (same folder)
- Campaign this chat commissioned: `~/nortropic/intake-campaigns/improvements-2026-08/`
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
