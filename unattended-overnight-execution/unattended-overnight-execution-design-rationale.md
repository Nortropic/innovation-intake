---
title: "Unattended multi-agent execution — design rationale"
type: design-rationale
status: source-derived
slug: unattended-overnight-execution
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: unattended-overnight-execution-full-chat.md
execution_brief: idea-unattended-overnight-execution.md
authority: non-authoritative-rationale
fidelity: full
context_revision: 1
---

# Design rationale: Unattended multi-agent execution

## 1. Core thesis
Owner attention is the factory's scarcest resource, so the design converts every class
of avoidable owner stop into a bounded machine decision — while keeping exactly one
class human: changes to the system's ultimate mandate. Parallelism buys speed only
where lanes are independent; trust transitions must stay serial because two
simultaneous advances of the authoritative branch cannot both be "the" transition
(← msgs 27–33, 126–132).

## 2. Problem / current state / intended outcome
The owner works in Codex with gated rounds; each gate question costs a human wake-up
(← msgs 27, 29). Intended outcome: go to sleep, let it run — "tänkte gå och sova och
låta den arbeta på under natten" (← msg 29) — and later, remove needless standing
stops entirely: "varför ställer den frågor? den ska ju arbeta på autonomous"
(← msg 126). The counterweight, kept throughout: bounded windows, reviewed identities,
and a mandate the system can never rewrite (← msgs 32, 130–132).

## 3. Reasoning chain
- Speed demanded parallel agents (OWNER DECISION ← msg 27); parallelism forced a
  classification of what may run concurrently, giving PARALLEL_SAFE /
  SERIAL_TRUST_TRANSITION / DEPENDENCY_BLOCKED (assistant design ← msgs 28, 30, 33).
- Overnight running (← msg 29) meant no human approver exists at 03:00; the owner
  resolved it by delegating approval inside the window — "den får approva också"
  (← msg 32) — which made a written protocol necessary: Round A (no-ref candidates,
  remediation as a new child object, only reviewed READY identities run in confinement,
  authoritative branch advances exactly once) (assistant design ← msg 33; runs relayed
  ← msgs 40–48).
- Confinement questions during the runs produced A1b: temporal process-wide
  confinement where the sandbox may only *remove* forbidden capabilities, never change
  legitimate semantics — otherwise a green result proves the sandbox, not the product
  (assistant design ← msgs 45–48; recurring through ← msgs 51–86).
- Nested Seatbelt limits tempted a privileged native broker; rejected because a broker
  is a new trust root outside review (owner-relayed problem ← msg 123; ruling
  ← msgs 124–125).
- The H036 stop (← msg 126, relayed Codex log) showed that runtime/launcher authority
  layered into H034/H035 registries deadlocks: adding paths breaks current authority,
  omitting them breaks H036. Lesson: new authority classes need their own frozen gate
  beneath H032 (← msgs 126–130).
- Generalizing that stop, the assistant drafted two options; the owner took only the
  standing amendment (← msg 131): BOUNDED_PREREQUISITE_AUTHORITY_MIGRATION — the
  system may change implementation and bounded internal authority plumbing, never its
  ultimate mandate; extensible permission lists rejected in favor of exact two-state
  transitions (← msgs 128–132).
- Provider strategy: "vi har ju claude också" (← msg 106) split the workforce — Codex
  on the trust-critical path, Claude as independent/adversarial reviewer — because
  cross-provider review has different blind spots (assistant elaboration ← msgs
  107–111).

## 4. Design decisions and why
D2/D3 (overnight + bounded autonomous approval). Why: no approver exists at night; an
    unbounded delegation would rewrite the trust model, so the delegation is scoped to
    the window and to reviewed identities. Evidence: (← msgs 29, 32; protocol msg 33).
D4 (ask the agent). Why: process-list forensics guesses; the agent reports. Evidence:
    "kan jag inte bara fråga codex i min terminal?" (← msg 55).
D9 (standing amendment only). Why: the one-off was already dispatched; the owner wants
    the durable class-level fix — "jag vill bara ha det som löser framtida onödiga
    ägarstopp". Evidence: (← msg 131; drafts msgs 130, 132).
D7 (two-provider split). Why: independent failure modes in review. Evidence:
    (← msg 106; ← msgs 107–111). ASSISTANT INFERENCE labelled: the exact lane
    assignments are assistant-proposed.

## 5. Explicit rejections / anti-requirements
REJECTED: Privileged native broker for nested Seatbelt.
WHY: it would hold capabilities no gate reviews.
FAILURE IT WOULD CREATE: a permanent unauditable trust root under every sandbox.
SOURCE: (← msgs 123–125).

REJECTED: Extensible permission lists for delegation.
WHY: lists invite silent growth; each addition is an unreviewed authority expansion.
FAILURE IT WOULD CREATE: authority creep with no single reviewable diff.
SOURCE: (← msgs 128–132, owner choice ← msg 131).

## 6. Explored but unresolved
- Standing vs expired: does the msg-32 approval mandate survive beyond that window?
  PENDING OWNER REVIEW — it relaxes the "AI makes no authority decisions" family of
  principles for the bootstrap orchestrator; the analysis flags it for explicit owner
  confirmation, and this rationale keeps it unresolved (← msgs 32, 131).
- Ceremony ablation: which R128-level controls are bootstrap scaffolding vs permanent
  (assistant raises ← msgs 64, 76); resolution needs a steady-state cost/risk review.
- Ratification of the Round A directives: owner turns in msgs 40–48 are largely pasted
  agent output; which directives are owner law is unresolved (← msgs 40–48).

## 7. Important trade-offs / tensions
- Autonomy vs auditability: fewer stops (← msgs 29, 32, 126) vs every transition
  leaving a reviewable record (← msgs 33, 130–132).
- Parallel speed vs serial trust: lanes parallelize, the authoritative branch advances
  once (← msgs 27–33).
- Confinement strength vs result validity: A1b exists because an over-strong sandbox
  falsifies green results (← msgs 45–48).

## 8. Metaphor / concept → technical principle
- "Fabrik med nattskift" → bounded unattended window with checkpoint reporting → do NOT
  copy: a human foreman; the checkpoint is the foreman (← msgs 29–33).
- "Kompetensutveckling av medarbetarna" → workforce competency subsystem → do NOT copy:
  HR processes; it is capability measurement and training (← msgs 83–84).

## 9. External evidence mentioned in the conversation
- Codex usage/quota mechanics and session limits — MENTIONED IN SOURCE (← msgs 104,
  106–111).
- macOS Seatbelt nesting behavior — MENTIONED IN SOURCE via relayed Codex logs
  (← msgs 123–125). Nothing independently verified during intake.

## 10. Evolution / pivots
- "Fler agenter för fart" → classified lanes with serialized trust (← msgs 27 → 33).
- Overnight run → delegation of approval → written Round A protocol (← msgs 29 → 32 →
  33–48).
- Broker temptation → A1b confinement doctrine instead (← msgs 123–125 vs 45–48).
- Per-incident owner stop (H036) → class-level standing amendment (← msgs 126 → 131).

## 11. Retrieval map
| topic | message range |
|---|---|
| parallel agents mandate; lane classification | 27–28, 30, 33 |
| overnight mandate; autonomous approval | 29–33 |
| Round A protocol and runs | 33, 40–48 |
| A1b temporal confinement | 45–48, 51–61 |
| ask-the-agent status | 55 |
| workforce competency subsystem | 83–84 |
| name stays Nortropic | 87–88 |
| two-provider split | 104–111 |
| broker rejection (nested Seatbelt) | 123–125 |
| H036 layering stop; standing amendment | 126–132 |
| ceremony ablation question | 64, 76 |

## 12. What to load when
DEFAULT IMPLEMENTATION: read `idea-unattended-overnight-execution.md`.
IF DESIGN RATIONALE IS NEEDED: read this file.
IF EXACT SOURCE EVIDENCE IS NEEDED: read only the relevant message ranges in
`unattended-overnight-execution-full-chat.md` (use §11).
Do not preload the raw transcript into the main implementing context.
