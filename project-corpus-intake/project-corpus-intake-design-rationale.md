---
title: "Nortropic Intake v3: Project Corpus Intake — design rationale"
type: design-rationale
status: source-derived
slug: project-corpus-intake
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: project-corpus-intake-full-chat.md
execution_brief: idea-project-corpus-intake.md
authority: non-authoritative-rationale
fidelity: full
context_revision: 1
---

# Design rationale: Nortropic Intake v3 — Project Corpus Intake + proving-run iteration

## 1. Core thesis
A whole ChatGPT project is not "a folder of chats" — it is a source container whose
membership must first be enumerated and sealed before anything is interpreted
(← msg 78, 80). Therefore the intake skill grew a second, explicitly separate job:
PROJECT_SWEEP, unattended corpus ingest that produces a lossless,
coverage-verified, normalized R&D corpus — so the Autonomy Kernel's first real mission
(Recompile) starts from proven raw material instead of import doubt (← msg 67, 68).
The corpus is delivered by two runs, not one: today's sweep is a proving run that lets
reality attack the architecture; the sealing "corpus cut" happens as close to
Recompile as possible (← msg 75, 76).

## 2. Problem / current state / intended outcome
Improvements had become Nortropic's de facto R&D corpus — vision, methods, rejections,
external comparisons — living only as ChatGPT chat history (← msg 63, 64). Intake v2.1
handled exactly one brainstorm at a time and carried two honestly documented residual
risks: role-blind provenance and non-persisted approval strength (← msg 65). The
intended outcome: every Improvements conversation preserved verbatim under a stable
source identity, ideas routed project-globally, coverage mechanically provable, and a
sealed corpus the Kernel can trust (← msg 67, 68, 72).

## 3. Reasoning chain
The owner asked how to work after Bootstrap (← msg 63); the assistant proposed
"Improvements Recompile" as the Kernel's first mission (← msg 64). Seeing the v2.1
status report (← msg 65), the assistant first recommended only a minimal v2.2
hardening, leaving corpus capability for the Kernel to build mid-mission (← msg 66).
The owner overturned that: rebuild intake now, sweep all chats, then let the Kernel
work (← msg 67). That reordering is load-bearing because a Kernel that must first
build a browser mass-importer and prove its own coverage wastes its highest-value
mission on plumbing (← msg 68). The rebuild made the two dormant v2.1 risks mandatory:
compiling *all* chats makes "who said it" (owner vs assistant) and "how strong was
that approval" load-bearing rather than theoretical (← msg 68). Sweeping many
historical chats forbids per-chat interviews, so the mode had to be non-interactive
with a review queue, while capture integrity stays fail-closed (← msg 68, 70). The
owner then ordered the master prompt (← msg 69), which was delivered as a build-only
contract — build, verify, freeze, but do not sweep — so the tool would be proven before
meeting production (← msg 70). The STOP REPORT (owner-relayed machine evidence) showed
v3.0 built and frozen 2026-08-30 (← msg 71); the assistant accepted it and produced
the separate production sweep prompt, adding one operative change: the owner-authorized
Claude session (not the skill runtime) may publish the finished corpus (← msg 72). The
owner started the sweep (← msg 73) and then reframed the run as a proving run with a
later optimized final intake after the Trust Kernel (← msg 75), which the assistant
expanded into four phases (test sweep → iterate → clean → final incremental cut) plus
daily reports as their own evidence class (← msg 76). Reality immediately tested the
design: the project page exposed Chattar vs Källor surfaces (← msg 77, 78), Projects
research sharpened the model ("a Project URL is not a chat source", ← msg 80), and the
shipped discovery adapter's count==total assumption met cursor pagination — resolved
not by remodeling but by owner confirmation of the 27-conversation inventory
(← msg 81–84).

## 4. Design decisions and why
D1. Intake sweeps first; Kernel recompiles second.
    Why: separates "clean the corpus" (mechanical, provable) from "synthesize the
    future" (judgment, Kernel's job); the Kernel gets a closed input.
    Evidence: owner's explicit sequencing; assistant's MESSY HUMAN R&D → TRUSTWORTHY
    CORPUS → Recompile split.
    Source: (← msg 67; 68, 70, 72)
D2. PROJECT_SWEEP is a new mode on top of v2.1, never a replacement.
    Why: the single-brainstorm intake was already good; the new orchestrator must not
    make single mode ambiguous — mode is explicit and testable.
    Evidence: master prompt's binding principle 10; STOP REPORT confirms SINGLE flow
    untouched.
    Source: (← msg 68, 70, 71)
D3. Source identity before idea identity; raw source survives.
    Why: a conversation is not an idea (one chat → many ideas; one idea → many chats);
    future, better models must be able to recompile the originals.
    Evidence: binding principles 1–2 and 8 in the owner-approved prompt.
    Source: (← msg 68, 70)
D4. Coverage must be mechanically provable; enumeration is fail-closed.
    Why: "Claude thinks it read everything" is not acceptance; a hard capture gap may
    never be rounded to "complete with review".
    Evidence: manifest lifecycle DISCOVERED→…→COMPLETE, PROJECT_ENUMERATION_UNVERIFIED
    fallback, and the real 27-conversation verification via three converging signals
    plus owner confirmation.
    Source: (← msg 68, 70; 81–84)
D5. Proving run now, corpus cut later.
    Why: sealing now would hand the Kernel a stale snapshot; real failures (pagination,
    lazy loading, dedup, role provenance) are cheapest to fix before the final cut;
    v3's idempotent revision model makes the final sweep incremental.
    Evidence: owner's reframing and the assistant's four-phase plan with an
    eval-generator loop (observed failure → reproducer → permanent eval → fix → rerun).
    Source: (← msg 75; 76)
D6. Daily reports are a distinct source class.
    Why: a daily report is derived external/environment evidence — not a brainstorm,
    not owner instruction, not repo truth; it powers temporal supersession analysis.
    Evidence: source-class schema (CONVERSATION / DAILY RESEARCH REPORT / REPO STATE /
    OWNER DECISION / EXTERNAL PRIMARY SOURCE) — ASSISTANT INFERENCE under the owner's
    "dagliga rapporter... ta hänsyn till".
    Source: (← msg 75; 76)

## 5. Explicit rejections / anti-requirements
REJECTED: Minimal v2.2 hardening only; Kernel builds corpus capability itself later.
WHY: owner overturned it — intake shall clean Improvements before the Kernel works.
FAILURE IT WOULD CREATE: Kernel's first mission consumed by import tooling and
unprovable coverage; synthesis built on uncertain raw material.
SOURCE: (← msg 66, 67)

REJECTED: Owner interview / plan mode / approved plans per historical chat in sweep mode.
WHY: unattended ingest dies if every chat needs dialogue; historical chats are corpus,
not IMPLEMENT_NOW.
FAILURE IT WOULD CREATE: sweep stalls after two hours; hundreds of junk plans minted
from history.
SOURCE: (← msg 68, 69, 70)

REJECTED: Sealing Improvements as the final corpus now.
WHY: material keeps arriving until the Kernel is ready; the cut must be fresh.
FAILURE IT WOULD CREATE: Kernel recompiles from a weeks-old snapshot missing the
latest decisions and world evidence.
SOURCE: (← msg 75, 76)

REJECTED: Mid-run remodeling of the frozen skill (including "improve a little while
you're there").
WHY: observations go to the residual report; reopen only via the freeze policy.
FAILURE IT WOULD CREATE: unfalsifiable proving run — the contract under test changes
under the test.
SOURCE: (← msg 72, 81, 82, 84)

REJECTED: Faking enumeration completeness (or title-based identity, screenshots/OCR
capture, vector DBs, a giant Projects crawler).
WHY: honesty beats false 100 % — declare PROJECT_ENUMERATION_UNVERIFIED instead;
titles are metadata, never primary keys; files/Git-first until observed need.
FAILURE IT WOULD CREATE: silent corpus gaps poisoning every downstream synthesis.
SOURCE: (← msg 70, 78, 80)

## 6. Explored but unresolved
- The v3.1 candidate list — enumeration receipt, Källor-tab intake, conversation
  lineage/branches, project-config snapshot, saved-response content equivalence,
  cross-oracle coverage via account export, live adapter fixture — explicitly parked
  until the proving run confirms need (assistant proposals) (← msg 80).
- Classification of the Källor tab and daily reports in the final sweep; the proposed
  Chats=laboratory / Sources=reference-shelf semantics are untested (← msg 78, 80).
- Project-only memory for Improvements — flagged as a genuine owner architecture
  question, unanswered (← msg 80).
- The sweep's own outcome — the transcript ends mid-run (← msg 84).

## 7. Important trade-offs / tensions
- Unattended throughput vs owner authority: semantic ambiguity queues and continues;
  capture/coverage integrity fails closed — two different failure classes on purpose
  (← msg 68, 70, 74).
- Lossless preservation vs usable corpus: raw bytes are immutable evidence; all
  understanding is derived and replaceable (← msg 68, 70).
- Freshness vs sealing: an early seal is reproducible but stale; the corpus cut
  resolves this by sealing late with an exact input snapshot (← msg 75, 76).
- Skill invariant vs practical publication: the runtime never commits/pushes, yet the
  finished corpus needs a stable Git object — resolved by owner-authorized session
  publication, distinct from the skill (← msg 71, 72).

## 8. Metaphor / concept → technical principle
"Rensa" (clean up) → remove chaos from the working representation without losing
originals → MUST NOT be implemented as deletion of raw sources (← msg 68, 76).
"Proving run" → let reality falsify the frozen contract, harvest regression tests →
MUST NOT become continuous mid-run tinkering (← msg 75, 76, 82).

## 9. External evidence mentioned in the conversation
- OpenAI documentation on ChatGPT Projects (Chats/Sources tabs, project instructions,
  memory modes) — MENTIONED IN SOURCE (assistant web research, msg 80).
- ICM / incremental-compilation ideas invoked as "do not learn from output" rationale —
  MENTIONED IN SOURCE (← msg 68).
- The v3.0 STOP REPORT and the in-run Claude enumeration question — owner-transported
  machine evidence quoted in owner messages, not owner-authored prose (← msg 65, 71, 81).
None of these were INDEPENDENTLY VERIFIED during this packaging run.

## 10. Evolution / pivots
1. Kernel-builds-intake-itself → owner's "gör om intake … sedan låter vi Kernel
   arbeta" → intake-first sequencing (← msg 66 → 67 → 68).
2. v2.2 patch framing → "owner architecture change" → v3.0 Project Corpus Intake with
   both trust risks closed as mandatory (← msg 66 → 67 → 68, 70).
3. "Now we seal the corpus" → proving run + later corpus cut with daily reports
   admitted (← msg 72 → 75 → 76).
4. count==total discovery assumption → observed cursor pagination → owner-confirmed
   verified enumeration + regression candidate for later (← msg 70 → 81 → 82–84).

## 11. Retrieval map

| topic | message range |
|---|---|
| Improvements as R&D corpus; recompile framing | 63–64 |
| v2.1 status report (owner-relayed) | 65 |
| Rejected v2.2-only path | 66 |
| Owner decision: rebuild + sweep + then Kernel | 67 |
| PROJECT_SWEEP design (source corpus, queue, coverage) | 68 |
| Master build prompt (binding principles, DoD) | 69–70 |
| STOP REPORT v3.0 (frozen identities) | 71 |
| Production sweep prompt + publication authorization | 72 |
| Sweep start; what to watch | 73–74 |
| Proving run decision; daily reports; corpus cut | 75–76 |
| Project page reality; Chattar vs Källor | 77–78 |
| Projects research; v3.1 candidates; Project-only memory | 79–80 |
| Enumeration verification "27 stämmer" | 81–84 |

## 12. What to load when
DEFAULT IMPLEMENTATION: read `idea-project-corpus-intake.md`.
IF DESIGN RATIONALE IS NEEDED: read this file.
IF EXACT SOURCE EVIDENCE IS NEEDED: read only the relevant message ranges in
`project-corpus-intake-full-chat.md` (use §11).
Do not preload the raw transcript into the main implementing context.
