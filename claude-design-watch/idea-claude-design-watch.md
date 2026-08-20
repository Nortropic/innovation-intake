---
title: "Visual Intent: a frozen visual decision step before code, powered by Claude /design"
type: idea-brief
status: idea   # lifecycle: idea → clarified → planned → building → verified; terminal: superseded
slug: claude-design-watch
owner: Johnny (Nortropic)
created: 2026-08-20
source_conversation: claude-design-watch-full-chat.md   # reference only — this brief takes precedence
intended_repo_path: claude-design-watch/idea-claude-design-watch.md
related: [build-fast-path]
---

# Idea brief: Visual Intent — a frozen visual decision step before code, powered by Claude /design

## 1. Summary

Claude Code's new `/design` command (research preview: editable UI artboards inside
Claude Code) could give Nortropic the missing visual link between idea/specification
and implementation. The framing decision: the value is **a visual decision step
BEFORE code** — "code is expensive to think with"; the first built version otherwise
becomes an anchor the architecture bends around. The proposed concept is **Visual
Intent**: Need → UX intent → `/design` exploration (several genuinely different
directions) → choose/remix → freeze APPROVED_VISUAL_INTENT → only then Builder →
separate verification. A weekly watch automation is active to track `/design`
maturity before it touches any core workflow.

## 2. Context you need

`/design` is a research-preview skill: Claude Code sketches UIs as editable
artboards, the human picks/adjusts a direction, and hands the chosen design back for
implementation. Figma's canvas argument matches: seeing multiple solutions
side-by-side enables divergent thinking before locking direction. Nortropic's current
risk pattern: idea → prompt → Claude Code builds → first UI anchors iteration. The
watch automation (activated in this chat, weekly) reports only meaningful changes:
preview status, `/design-sync`, handoff quality, API/automation support, maturity.
Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen
gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- Design-sensitive tasks (site builds, Verkstadsgolvet views) run:
  **brief first** (goals, users, content, hierarchy, constraints, existing
  components) → **diverge** with ~6 genuinely different directions (conservative /
  structurally different / radical) → **choose/remix before code** ("B's IA + D's
  hero + F's nav") → **freeze Visual Intent** (artboard + explicit responsiveness,
  states, interactions, component mapping, accessibility) → Builder implements the
  frozen intent → verification stays separate (real runtime, responsive, a11y,
  visual regressions).
- `/design` maturity is tracked by the weekly watch; adoption into core workflow
  waits for evidence, not novelty.

Choose architecture/decomposition/tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

- D1. A weekly "Claude /design Watch" automation is ACTIVE, reporting only meaningful
  changes (preview status, design-sync, handoff quality, API/automation, maturity)
  (← msg 5).
- P1 (proposal). Visual Intent as a first-class frozen artifact between spec and
  build — because the first coded version otherwise anchors everything (← msg 4).
- P2 (proposal). Diverge-then-remix: never ask for "one good page"; generate multiple
  genuinely different directions and combine the best (← msg 4).
- P3 (caution). `/design` is research preview — not for the core workflow until the
  watch shows maturity (← msg 3–5).

## 5. Acceptance criteria (v1 — if adopted)

- AC1. WHEN a design-sensitive task starts, THE flow SHALL produce multiple visual
  directions before any production code.
- AC2. WHEN a direction is chosen, THE frozen Visual Intent SHALL specify states,
  responsiveness, component mapping and accessibility — not just an image.
- AC3. WHEN the Builder implements, THE implementation SHALL be verified against the
  frozen intent by the separate verification step, not by the builder's judgment.
- AC4. WHEN the watch reports a material `/design` change, THE record SHALL show a
  triage decision (adopt-experiment/watch/ignore).

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants: Nortropic's trust layer — constitution & rulebook (pointer, never a copy).
Suggestions: pilot on a Verkstadsgolvet view or one site build, not the core
pipeline; the frozen-intent concept works even WITHOUT `/design` (any artboard/mockup
source) — the tool is fungible, the decision step is the idea; connects naturally to
the Design stage of the site pipeline (`build-fast-path`).

## 7. Out of scope (v1)

- Making `/design` (research preview) a dependency of any frozen gate or core
  workflow (P3).
- General design-system work — this is about the decision step, not a component
  library.

## 8. Verification (how we know it works)

Run one pilot task both ways (with and without the Visual Intent step) and compare
from the record: number of post-build direction changes, rework rounds, and whether
the frozen intent's requirements (states/a11y/responsive) survived into verification
(AC1–AC3).

## 9. Open questions (interview the owner before planning)

- Q1. First pilot: a customer site build or a Verkstadsgolvet view?
- Q2. Where does APPROVED_VISUAL_INTENT live as an artifact (task folder, spec,
  corpus), and what exactly does "frozen" mean for it (hash? owner sign-off?)?
- Q3. Is the weekly watch's triage output feeding the same backlog as Frontier
  Delta's recommendations (shared ladder), or is design watched separately?
- Q4. This chat is a LIVE weekly feed — same re-harvest question as the other watch
  chats.

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

- Source conversation: `claude-design-watch-full-chat.md` (same folder)
- Related brief: `build-fast-path/` (site pipeline stages; Visual Intent slots into its Design stage)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
