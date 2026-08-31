---
title: "Verkstadsgolvet v2: executive cockpit — design rationale"
type: design-rationale
status: source-derived
slug: verkstadsgolvet-v2-cockpit
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: verkstadsgolvet-v2-cockpit-full-chat.md
execution_brief: idea-verkstadsgolvet-v2-cockpit.md
authority: non-authoritative-rationale
fidelity: full
context_revision: 1
---

# Design rationale: Verkstadsgolvet v2 — executive cockpit

## 1. Core thesis
The portal's problem is representational, not informational: the factory's evidence is
right, but showing all of it makes the operator the bottleneck. The model adopted: a
chief's cockpit layered *above* the technical factory — compress the representation,
keep every byte of evidence and every control reachable underneath (owner problem
statement ← msg 118; layered design in the commissioned prompt ← msgs 121–122).

## 2. Problem / current state / intended outcome
Current state: Verkstadsgolvet shows the machine's full surface; the owner: "nu är det
alldeles för mycket, man blir överväldigat" (← msg 118). Intended outcome: a genuinely
modern interface (← msg 118) built by the Claude terminal already working on this
(← msg 121), where the owner sees at a glance what needs him — even at 100 agents / 25
projects — and can still descend to full forensics (design ← msg 122).

## 3. Reasoning chain
- "Överväldigad" is a signal-to-noise failure, so the fix is depth-stratification:
  Executive → Operations → Engineering/Forensics, each depth a compression of the one
  below (← msgs 118, 122).
- Because the scarce resource is owner attention, the top depth is exception-first:
  NEEDS-YOU is the most important component, and "nothing needs you" must be
  distinguishable from "the factory is not connected" — silence from a dead system
  must never read as calm (← msg 122; endorsed ← msg 135).
- The owner thinks in projects/customers, not in agent processes — so presentation is
  project-first, with agents as a resource view (← msg 122).
- Compression invites cheating, hence the load-bearing boundary: simplification must be
  representational compression, not loss of underlying evidence or control, with an
  explicit ban on fabricated metrics and mandatory unavailable-states (← msg 122).
- Delivery went through the standing pattern: owner commissions a prompt (← msg 121),
  Claude produces a sliced plan (COCKPIT-00..07, separate review/visual review/gated
  publication per slice, new routes before old ones are replaced, dead weight removed
  last), the ChatGPT assistant reviews it and recommends approval (← msg 135).

## 4. Design decisions and why
D1 (modern cockpit, not more dashboard). Why: the current surface scales with the
    factory, the owner's attention does not. Evidence: (← msg 118).
D2 (assign to the existing Claude terminal). Why: it already holds the codebase
    context; a prompt is the transfer artifact. Evidence: (← msg 121).
Three-depth model, NEEDS-YOU primacy, project-first, Factory Pulse, Ask Nortropic
    (ASSISTANT PROPOSALS inside the commissioned prompt). Why: each converts raw state
    into decisions the owner can act on. Evidence: (← msg 122; plan review ← msg 135).

## 5. Explicit rejections / anti-requirements
REJECTED: Simplifying by hiding/removing underlying evidence or control.
WHY: the cockpit sits above a trust system; amputating evidence to look calm destroys
the very auditability the factory exists to provide.
FAILURE IT WOULD CREATE: a pretty UI the owner cannot trust in an incident — forensics
gone exactly when needed. ASSISTANT-STATED boundary in the owner-commissioned prompt.
SOURCE: (← msgs 121–122).

REJECTED (within the same boundary): fabricated/placeholder metrics.
WHY: an invented number is worse than a visible gap.
FAILURE IT WOULD CREATE: decisions taken on fiction; "connected" and "healthy" become
indistinguishable. SOURCE: (← msg 122; reaffirmed in plan review ← msg 135).

## 6. Explored but unresolved
- Owner approval of the COCKPIT-00..07 plan: msg 135 is the assistant recommending
  "1. Yes"; no owner approval turn is captured in this conversation. OPEN — the
  approval state must be established from repository/terminal truth (← msg 135).
- Relation to the claude-design-watch package's Visual Intent work: UNCERTAIN, PENDING
  OWNER REVIEW; kept out of related-links deliberately.

## 7. Important trade-offs / tensions
- Calm vs completeness: one calm paragraph at the top vs full forensics below — solved
  by depth, not deletion (← msgs 118, 122).
- Speed of redesign vs safety of migration: new routes built before the old start
  page/navigation is replaced; dead weight removed last (← msg 135).

## 8. Metaphor / concept → technical principle
- "Chefscockpit" → an exception-first executive layer over unchanged instruments → do
  NOT copy: pilot-style controls; the principle is compression with drill-down, not a
  new control surface replacing the old one (← msgs 122, 135).
- "Factory Pulse" → a single liveness/health rhythm indicator → do NOT copy: a vanity
  activity feed (← msg 122).

## 9. External evidence mentioned in the conversation
None in this range. The COCKPIT-00..07 plan itself is referenced as a Claude-terminal
artifact reviewed in (← msg 135) — MENTIONED IN SOURCE; the plan document is not part
of this package.

## 10. Evolution / pivots
- "För mycket, överväldigad" → depth-stratified cockpit (← msgs 118 → 122).
- Prompt commissioned → Claude plan → assistant endorsement; approval state itself not
  captured (← msgs 121 → 122 → 135).

## 11. Retrieval map
| topic | message range |
|---|---|
| owner problem statement (overwhelming UI) | 118 |
| assignment to Claude terminal | 121 |
| commissioned prompt: depths, NEEDS-YOU, bans | 122 |
| plan review, COCKPIT-00..07, endorsement | 135 |

## 12. What to load when
DEFAULT IMPLEMENTATION: read `idea-verkstadsgolvet-v2-cockpit.md`.
IF DESIGN RATIONALE IS NEEDED: read this file.
IF EXACT SOURCE EVIDENCE IS NEEDED: read only the relevant message ranges in
`verkstadsgolvet-v2-cockpit-full-chat.md` (use §11).
Do not preload the raw transcript into the main implementing context.
