---
title: "Verkstadsgolvet v2: executive cockpit with representational compression"
type: idea-brief
status: idea
slug: verkstadsgolvet-v2-cockpit
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: verkstadsgolvet-v2-cockpit-full-chat.md
design_rationale: verkstadsgolvet-v2-cockpit-design-rationale.md
intended_repo_path: verkstadsgolvet-v2-cockpit/idea-verkstadsgolvet-v2-cockpit.md
related: [workflow-orkestrering, nortropic-planning-wall]
---

# Idea brief: Verkstadsgolvet v2 — executive cockpit

## 1. Summary
Redesign of the operator portal after the owner found the current UI overwhelming: an
executive cockpit on top of the existing technical factory, not a simplified version of
the trust system. The key framing decision: UI simplification must be representational
compression, never loss of underlying evidence or control — three information depths
(Executive / Operations / Engineering-Forensics), exception-first with NEEDS-YOU as the
most important component, project-first rather than agent-first, and an explicit ban on
fabricated metrics.

## 2. Context you need
Verkstadsgolvet today exposes the factory's full technical surface; with growing agent
counts the owner is overwhelmed by it. The redesign was assigned to the already-running
Claude terminal via a commissioned prompt, and Claude produced a COCKPIT-00..07 sliced
plan. This brief covers only msgs 118–122 and 135 of the source conversation; the rest
of that thread (Digitalförvaltningen sprint, unattended execution, Foundation Repair
Gate, Frontier Delta reports) belongs to other briefs/packages.

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
- Three information depths: Executive (calm, compressed) → Operations →
  Engineering/Forensics; the existing `/loop` layer stays as technology/forensics.
- Exception-first: NEEDS-YOU is the most important component, including the distinction
  "nothing needs you" vs "the factory is not connected".
- Project/workstream-first presentation, not agent-first; a Factory Pulse; an Ask
  Nortropic command surface.
- Design bar: 100 agents / 25 projects must still compress to one calm paragraph.
- Only real existing data; unavailable states shown as unavailable — never fabricated
  metrics.
Choose architecture, decomposition and tooling yourself, within §6's constraints.

## 4. Decisions already made (do not relitigate silently)
D1. Verkstadsgolvet needs a genuinely modern interface — because "nu är det alldeles
    för mycket, man blir överväldigat" (← msg 118).
D2. The work is assigned to the existing Claude terminal via a commissioned prompt —
    because that terminal already works in this codebase: "vi har ju en Claude terminal
    som arbetar med detta" (← msg 121).

R1. Simplifying by hiding or removing underlying evidence or control — because the
    cockpit must compress representation, not capability; a simpler UI that amputates
    forensics or control would gut the trust system (← msg 121, owner commission;
    boundary authored in assistant msg 122).

## 5. Acceptance criteria (v1)
AC1. WHEN the operator opens the portal, THE system SHALL default to an executive view
     whose primary component is exception-first NEEDS-YOU, distinguishing "nothing
     needs you" from "factory not connected" (← msg 118; design in assistant msgs 122,
     135).
AC2. WHEN underlying data is missing, THE UI SHALL show an explicit unavailable state
     and SHALL NOT fabricate metrics (← msg 118 commission; ban authored in assistant
     msg 122).
AC3. WHEN 100 agents across 25 projects are active, THE executive view SHALL still
     compress status to one calm summary with drill-down to Operations and Forensics
     depths (← msg 118; depth model in assistant msg 122).
AC4. WHEN the cockpit ships, THE existing `/loop` technical/forensic layer SHALL remain
     reachable and functionally intact (← msg 121 commission; preserved in the plan per
     assistant msg 135).

## 6. Constraints & implementation notes (suggestions, not orders)
Invariants: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`). Pointer only.
- Build new routes before replacing the old start page/navigation; remove dead weight
  last (pattern endorsed in the Claude plan, per assistant msg 135).
- Representational compression only: every number shown must trace to real underlying
  data.

## 7. Out of scope (v1)
- Changing the trust system, gates or `/loop` contracts themselves.
- The same thread's other ideas: Digitalförvaltningen (msgs 136–231), unattended
  execution (msgs 27–135 excl. this range), Foundation Repair Gate (msgs 232–336).
- Any overlap resolution with the claude-design-watch package (see §9 Q2).

## 8. Verification (how we know it works)
End-to-end: with the factory in a known state (including at least one genuine NEEDS-YOU
item and one disconnected data source), open the executive view and confirm from the
record alone that every displayed value traces to real data, the NEEDS-YOU item and the
disconnected state render distinctly, and Operations/Forensics drill-downs reach the
same underlying evidence as before.

## 9. Open questions (interview the owner before planning)
Q1. Owner approval of the Claude-produced COCKPIT-00..07 plan is not visible in the
    transcript — msg 135 is the ChatGPT assistant recommending "1. Yes" with no
    preceding owner turn captured. Did the owner actually approve, and is that plan
    still the intended baseline?
Q2. Relation to the claude-design-watch package's Visual Intent work is UNCERTAIN and
    PENDING OWNER REVIEW — overlap unclear; deliberately not recorded as a related
    link here.

## 10. Process for this brief
1. Clarify: first send a subagent to read
   `verkstadsgolvet-v2-cockpit-design-rationale.md` and report what bears on §9; only
   if evidence is missing there, read the targeted message ranges via the rationale's
   retrieval map — never the whole transcript, and keep both out of main context; then
   interview the owner on §9 (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code.
3. On explicit owner approval, persist the approved plan as
   `verkstadsgolvet-v2-cockpit-approved-plan.md`, validate and bind it in the
   frontmatter, then set `status: planned`.
4. Implement in a fresh session started from the approved plan; after any compaction
   re-read the plan from disk.
5. Adversarial review: fresh subagent checks the diff against this brief and the plan.
6. Traceability: commit messages cite this brief's slug.

## References
- Source conversation: `verkstadsgolvet-v2-cockpit-full-chat.md` (same folder)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
