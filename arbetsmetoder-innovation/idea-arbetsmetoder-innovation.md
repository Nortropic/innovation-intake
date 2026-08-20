---
title: "Deep Brainstorm protocol: evidence-driven R&D mode as the standing default"
type: idea-brief
status: idea   # lifecycle: idea → clarified → planned → building → verified; terminal: superseded
slug: arbetsmetoder-innovation
owner: Johnny (Nortropic)
created: 2026-08-20
source_conversation: arbetsmetoder-innovation-full-chat.md   # reference only — this brief takes precedence
intended_repo_path: arbetsmetoder-innovation/idea-arbetsmetoder-innovation.md
related: [brainstorming-arbetsfloden]
---

# Idea brief: Deep Brainstorm protocol — evidence-driven R&D mode as the standing default

## 1. Summary

Replace the magic words ("Websearcha, best practices, think hard, iterate") with an
explicit, evidence-driven brainstorm protocol, and make the FULL version ("Deep
Brainstorm") the standing default for every brainstorm. The framing decision:
**iterate against an external definition of good, never against the model's own
satisfaction** — and always test whether the premise itself is wrong before building
on it. This is primarily a ChatGPT-side working protocol (already activated in that
context); the idea for Nortropic is to codify it wherever brainstorming happens
(skills, prompts, future Evolution Loop research agents).

## 2. Context you need

The researched basis: OpenAI and Anthropic both describe
problem → context/evidence → multiple hypotheses → critique → measurable quality bar
→ experiment → eval → iteration. OpenAI explicitly advises against "think step by
step"-style prompts for reasoning models — give a harder assignment instead. "Best
practices" alone anchors to what others already do; pair it with first-principles.
The protocol was activated as the default between Johnny and ChatGPT in this chat.
Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen
gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- The eight-step chain runs on every brainstorm: **Frame → Research (primary sources)
  → Diverge (best practice + first principles + unconventional) → Challenge
  (falsify own ideas, failure modes, second-order effects) → Synthesize → Quality
  bar/Eval → Smallest experiment → Iterate (on new evidence).**
- Epistemic labels keep claims honest: **FACT / EVIDENCE / INFERENCE / SPECULATION**
  — an exciting idea never becomes "truth" after five messages.
- Premise-challenging is mandatory: "is a research agent even the right solution?"
  precedes designing the research agent.
- The state machine QUESTION → FRAME → RESEARCH → HYPOTHESES → RED TEAM → SYNTHESIS →
  EVAL → EXPERIMENT gates entry to SPECIFICATION → BUILD.
- Where applicable in Nortropic (skills, agent prompts, Evolution Loop researchers),
  the same protocol is codified rather than re-invented per prompt.

Choose architecture/decomposition/tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

- D1. Deep Brainstorm (full process) is the standing DEFAULT for every brainstorm;
  only explicit "snabbt"/"ingen research"/"bara bolla kort" lightens it — because the
  owner shouldn't need to remember invocation words (← msg 7–8).
- D2. Iterate against an external definition of good (evals/quality bar), never until
  "the AI thinks it's good" (← msg 3–4).
- D3. Separate FACT/EVIDENCE/INFERENCE/SPECULATION in brainstorm output (← msg 6).
- D4. The assistant must not auto-accept the premise; testing whether the problem
  framing itself is wrong is part of the protocol (← msg 6, 8).
- R1 (REJECTED). "Think hard"-style prompting for reasoning models — replaced by
  harder assignments (e.g. "identify the three strongest hypotheses, then try to
  falsify each") (← msg 4).
- R2 (REJECTED). "Best practices" as a terminal criterion — always paired with
  first-principles re-derivation (← msg 4).

## 5. Acceptance criteria (v1 — if codified in Nortropic)

- AC1. WHEN a brainstorm is initiated, THE protocol SHALL run the full chain by
  default, and a lighter mode SHALL require an explicit owner request.
- AC2. WHEN brainstorm output makes claims, THE output SHALL label them
  FACT/EVIDENCE/INFERENCE/SPECULATION.
- AC3. WHEN a solution direction is proposed, THE record SHALL show a premise
  challenge preceded it.
- AC4. WHEN iteration happens, THE record SHALL name the external quality bar it
  iterates against.

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants: Nortropic's trust layer — constitution & rulebook (pointer, never a copy).
Codification candidates: the nortropic-intake brief template's open-questions
discipline already echoes this; the future Evolution Loop's hypothesis stage (see
`nortropic-frontier-delta`) is the natural home for the full state machine; a small
"brainstorm protocol" section in the knowledge repo could carry the canonical wording.

## 7. Out of scope (v1)

- Changing how the factory (build/verify) works — this governs the THINKING phase
  only.
- Retroactively re-labeling past brainstorms.

## 8. Verification (how we know it works)

From the record of one real brainstorm: the eight steps are identifiable, claims are
labeled, a premise challenge is present, and the iteration cites its quality bar
(AC1–AC4) — checkable by an independent reader of the transcript alone.

## 9. Open questions (interview the owner before planning)

- Q1. Should this protocol be codified in Nortropic artifacts (skill/knowledge repo/
  agent prompts), or remain a ChatGPT-side working agreement only?
- Q2. Does the Deep-default apply to Claude-side brainstorms too (Claude.ai/Claude
  Code plan-mode discussions)?
- Q3. Should `nortropic-intake` briefs record the FACT/EVIDENCE/INFERENCE/SPECULATION
  labels when the source chat used them?

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

- Source conversation: `arbetsmetoder-innovation-full-chat.md` (same folder)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
