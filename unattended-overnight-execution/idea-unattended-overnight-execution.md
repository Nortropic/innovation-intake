---
title: "Unattended multi-agent execution: overnight mandate, Round A trust protocol, bounded delegation"
type: idea-brief
status: idea
slug: unattended-overnight-execution
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: unattended-overnight-execution-full-chat.md
design_rationale: unattended-overnight-execution-design-rationale.md
intended_repo_path: unattended-overnight-execution/idea-unattended-overnight-execution.md
related: [bootstrap-closeout-rebaseline, snabba-upp-loopar]
---

# Idea brief: Unattended multi-agent execution

## 1. Summary
An operating model for running the Nortropic factory unattended: multiple named
parallel lanes, an overnight mandate where the orchestrator may approve and publish
autonomously within a bounded window, the Round A trust protocol (remediation is always
a new child object, the authoritative branch advances exactly once), temporal
process-wide confinement, and a standing rule that lets the system clear bounded
prerequisite/authority migrations without waking the owner. The key framing decision:
parallelize discovery and falsification, but serialize every exact trust transition.

## 2. Context you need
The bootstrap runs through Codex with owner-gated trust transitions; every gate stop
costs a human round-trip, which makes overnight progress impossible. This brief covers
only msgs 27–48, 55, 83–88, 104–111 and 123–135 of the source conversation (the
unattended-execution operating model); the same thread's Digitalförvaltningen design
sprint, Foundation Repair Gate campaign, cockpit redesign and Frontier Delta reports
are separate briefs/packages.

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
- Named parallel lanes classified PARALLEL_SAFE / SERIAL_TRUST_TRANSITION /
  DEPENDENCY_BLOCKED; discovery and falsification run in parallel, exact trust
  transitions serialize.
- The Round A protocol: no-ref candidates; remediation as a new child object, never a
  mutation; only reviewed READY identities run in confinement; the authoritative branch
  advances exactly once per round.
- Temporal process-wide confinement (A1b): the sandbox may only remove forbidden
  capabilities, never change legitimate semantics.
- OVERNIGHT_CHECKPOINT reporting with required fields; "never invent busywork".
- The four-states-of-reality model: workspace → candidate → reviewed → canonical.
- The standing BOUNDED_PREREQUISITE_AUTHORITY_MIGRATION amendment: the system may
  change implementation and bounded internal authority plumbing, never its ultimate
  mandate; OWNER_DECISION_REQUIRED becomes an internal orchestrator signal for exactly
  that class.
- Two-provider workforce: Codex on the trust-critical path, Claude in independent /
  adversarial reviewer lanes.
Choose architecture, decomposition and tooling yourself, within §6's constraints.

## 4. Decisions already made (do not relitigate silently)
D1. Multiple parallel agents is the established working model — because speed:
    "vi vill ha flera pararella agenter igång för att det ska fortare" (← msg 27).
D2. The factory runs unattended overnight — because the owner sleeps while it works
    (← msg 29).
D3. Within the bounded overnight window the orchestrator may approve and publish
    autonomously — "den får approva också, vi låter den köra oss framåt" (← msg 32).
    NOTE: whether this is standing or expired with that window is §9 Q1 and awaits
    owner review.
D4. Ask Codex directly for its own status instead of process-list forensics — because
    the agent is the cheapest reliable source about itself (← msg 55).
D5. Workforce competency development becomes its own subsystem — because factory
    workers' "kompetensutveckling" matters long-term (← msg 83).
D6. Keep the name Nortropic; no rename-proofing during bootstrap — because renaming is
    not on the table: "nejdå, vi ska inte byta" (← msg 87).
D7. Two-provider split: "vi har ju claude också" — Codex keeps the trust-critical path,
    Claude takes independent/adversarial review lanes — because provider diversity
    catches what same-provider review misses (← msg 106).
D8. Remove unnecessary owner stops — "varför ställer den frågor? den ska ju arbeta på
    autonomous" (← msg 126).
D9. Adopt only the standing delegation amendment, not the combined one-off
    authorization — because the owner had already sent the other prompt and wants the
    durable fix for future needless stops (← msg 131).

R1. A privileged native broker as fix for nested Seatbelt limits — because it would
    itself become a new unreviewed trust root (← msg 123, owner-relayed problem;
    assistant ruling ← msgs 124–125).
R2. Extensible permission lists for delegation — because open-ended lists grow silently;
    replaced by exact two-state authority transitions under the standing amendment
    (← msg 131; design detail ← msgs 128–132).

## 5. Acceptance criteria (v1)
AC1. WHEN an overnight window starts, THE system SHALL run named lanes classified
     PARALLEL_SAFE / SERIAL_TRUST_TRANSITION / DEPENDENCY_BLOCKED and SHALL serialize
     every exact trust transition (← msgs 27, 29; protocol detail in assistant msg 33).
AC2. WHEN a lane reaches an approval point inside the bounded window, THE orchestrator
     SHALL approve and publish autonomously within the window's bounds instead of
     stopping for the owner (← msg 32).
AC3. WHEN the overnight run ends, THE system SHALL emit an OVERNIGHT_CHECKPOINT with
     its required fields and SHALL NOT invent busywork to appear productive (← msg 29;
     checkpoint contract in assistant msgs 30, 33).
AC4. WHEN a reviewed candidate needs remediation, THE system SHALL create a new child
     object and SHALL NOT mutate the reviewed candidate; the authoritative branch
     advances exactly once per round (← msg 32, owner mandate; Round A protocol in
     assistant msg 33, exercised ← msgs 40–48).
AC5. WHEN a bounded prerequisite/authority migration blocks progress, THE system SHALL
     treat OWNER_DECISION_REQUIRED as an internal orchestrator signal under the
     standing amendment and SHALL NOT expand its ultimate mandate (← msgs 126, 131;
     amendment text in assistant msgs 130, 132).

## 6. Constraints & implementation notes (suggestions, not orders)
Invariants: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`). Pointer only.
- A1b temporal confinement: sandboxing may remove forbidden capabilities only — it must
  never alter the semantics of legitimate operations (assistant design, msgs 45–48).
- The H036 lesson: runtime/launcher authority needs its own frozen gate beneath H032 —
  layering authority into an existing gate is what caused the stop (← msgs 126–132).
- Prefer asking the agent (D4) over host forensics for liveness/status.

## 7. Out of scope (v1)
- The Digitalförvaltningen design sprint (msgs 136–231), Foundation Repair Gate
  campaign (msgs 232–336), Verkstadsgolvet v2 cockpit (msgs 118–122, 135), Frontier
  Delta monitoring reports (msgs 11–13, 44) — separate briefs/packages.
- Renaming/rename-proofing (D6); privileged broker (R1); extensible permission lists
  (R2).

## 8. Verification (how we know it works)
End-to-end: one bounded unattended window on a non-production task set, producing an
OVERNIGHT_CHECKPOINT whose lane classifications, single authoritative advance, and
zero owner interruptions an independent reviewer can confirm from the record alone.

## 9. Open questions (interview the owner before planning)
Q1. Is the msg-32 autonomous-approval mandate a standing rule or did it expire with
    that overnight window? PENDING OWNER REVIEW — flagged as a possible relaxation of
    the standing "AI makes no authority decisions" principle (msgs 32, 131); do not
    treat as settled either way.
Q2. Which parts of the R128-level ceremony are bootstrap scaffolding to ablate in
    steady state (raised in assistant msgs 64, 76)?
Q3. Owner participation in the Round A runs is largely relay of agent-authored
    directives (msgs 40–48); which of those directives does the owner ratify as
    standing protocol?

## 10. Process for this brief
1. Clarify: first send a subagent to read
   `unattended-overnight-execution-design-rationale.md` and report what bears on §9;
   only if evidence is missing there, read the targeted message ranges via the
   rationale's retrieval map — never the whole transcript, and keep both out of main
   context; then interview the owner on §9 (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code.
3. On explicit owner approval, persist the approved plan as
   `unattended-overnight-execution-approved-plan.md`, validate and bind it in the
   frontmatter, then set `status: planned`.
4. Implement in a fresh session started from the approved plan; after any compaction
   re-read the plan from disk.
5. Adversarial review: fresh subagent checks the diff against this brief and the plan.
6. Traceability: commit messages cite this brief's slug.

## References
- Source conversation: `unattended-overnight-execution-full-chat.md` (same folder)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
