---
title: "Owner attention ≠ owner stop — design rationale"
type: design-rationale
status: source-derived
slug: owner-attention-inte-owner-stop
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: owner-attention-inte-owner-stop-full-chat.md
execution_brief: idea-owner-attention-inte-owner-stop.md
authority: non-authoritative-rationale
fidelity: full
context_revision: 1
---

# Design rationale: Owner attention ≠ owner stop

## 1. Core thesis
"Owner must approve" had quietly become a general safety mechanism when it should be
an escalation mechanism for real risk or irreversibility (← msg 4). Three different
things were conflated — work may not continue, work should take another path, Johnny
should know — and disentangling them yields a delegation order where hard stop is
defined by effect and mandate, never by an agent feeling uncertain: uncertainty
normally produces evidence + attention, not stop (← msg 7). The maturity step is not
less safety but less synchronous owner involvement (← msg 3, 7).

## 2. Problem / current state / intended outcome
The owner observes trust-worthy autonomy being throttled by built-in owner stops,
most acutely in webbförvaltningen (← msg 3). In-source repo inspection located the
mechanism: owner logic has grown into the verification/exit harness
(h-032-owner-live-call, h-031-exit, task spec), `/nortropic-plan` makes all
intervention outcomes except `NY SAJT` a `STRATEGISK` open question, and
`nortropic-autobygg` stops on every remaining `STRATEGISK` question — with a
mechanical check requiring the coupling (← msg 5, 11). Intended outcome: "Nortropic
asks for attention often, permission rarely, and stops only when continuing would
exceed authority, create an unacceptable irreversible effect, or make a claim/action
it cannot substantiate" (← msg 7); the owner works with exceptions, not with the
workflow (← msg 7).

## 3. Reasoning chain
The owner's observation (← msg 3) led to separating hard authority boundaries from
owner-attention events (← msg 4), then to the sharper insight that STOPP and FRÅGA
ÄGAREN are two different things — a flow can correctly conclude "don't build a new
site" and re-route *without waiting* (← msg 6). Msg 7 generalized: three conflated
outcomes; a five-level delegation order (AUTONOMOUS / ATTENTION /
ATTENTION-BEFORE-BOUNDARY / DELEGATION-BOUNDARY / HARD STOP); bounded trust (a
standing mandate for a decision class, with the system collecting evidence — "47
times, 46 uncorrected" — and *proposing* delegation moves that only the owner enacts);
and exception-based management with the Aquarium as its display surface ("13
autonomous decisions · 4 owner-attention · 1 waiting · 0 hard stops"). The owner's
"Är det här nåt vi kan justera nu direkt?" (← msg 8) turned philosophy into a slice:
the coupling proved local (← msg 9–11), so the patch introduces four outcomes,
remaps the intervention cases (NY SAJT → CONTINUE; the rest → ROUTE + attention;
scope-nej → ROUTE + attention), and breaks `STRATEGISK = stop` by requiring an
explicit blocking classification, with unclassified failing closed (← msg 11). The
owner commissioned the prompt (← msg 12), delivered as a complete Claude Code
document with a 15-point verification matrix and a 13-flag Definition of Done proving
both directions (← msg 13). The next day's scheduled delta report independently
corroborated the distinction: OpenAI's Hugging Face incident response adopts safe
stopping and tiered responses — monitoring/alert first, pause/shutdown only for
severe levels (← msg 14).

## 4. Design decisions and why
D1. Four machine outcomes: CONTINUE / ATTENTION_CONTINUE / ROUTE / HARD_STOP.
    Why: they encode the three-way separation plus the normal case; ROUTE is a
    workflow outcome, not an authority error — correctly ending a lane requires no
    human unlock.
    Evidence: the remapping of all current intervention cases onto the taxonomy.
    Source: (← msg 6, 7; 11, 13)
D2. Hard stop defined by effect and mandate, not by uncertainty.
    Why: otherwise every insecure agent becomes a mutex on the owner; uncertainty
    should yield evidence + attention.
    Evidence: the delegation order's "viktigaste regeln".
    Source: (← msg 7)
D3. Blocking is a separate machine-readable classification; unclassified fails closed.
    Why: the label STRATEGISK must not decide; the actual authority/effect risk
    decides — and the change must not flip "everything stops" into "everything
    continues".
    Evidence: patch §4's invariants (ATTENTION_CONTINUE default only within existing
    mandate; explicit blocking → HARD_STOP; schema errors fail closed).
    Source: (← msg 11; 13)
D4. Attention events as first-class structured output.
    Why: "call my attention" must be concrete: severity / decision / reason /
    evidence / actionTaken / ownerActionRequired, with ownerActionRequired=false the
    new important value; consumable by future Aquarium/observability.
    Evidence: patch §6 and the OWNER ATTENTION report example.
    Source: (← msg 3; 11, 13)
D5. Surgical slice, frozen boundaries.
    Why: this is a small webbförvaltning delegation change, not an H036-style
    authority project; legal, capability, CRITICAL, provenance, deploy and
    bootstrap/controller authority stops stay untouched.
    Evidence: patch §7's preserved-stop list and §12's scope.
    Source: (← msg 8, 12; 10, 11, 13)
D6. Verification proves both directions, adversarially.
    Why: the risk of this patch is symmetric — unnecessary blocking OR a permeable
    real boundary; tests are mutated (HARD_STOP treated as continue, ROUTE leaking
    into build, missing disposition read as continue) to prove they catch inversions.
    Evidence: patch §9's 15 checks and the mutation instruction.
    Source: (← msg 12; 11, 13)

## 5. Explicit rejections / anti-requirements
REJECTED: Removing owner stops one by one.
WHY: becomes another long series of point fixes; the systematic Owner-Stop Audit
classifies each stop (must work stop? must Johnny decide? safe default? reversible?
mandate exists? first truly irreversible boundary?) into keep / re-route / convert.
FAILURE IT WOULD CREATE: unprincipled deletions — some real boundaries weakened, most
false stops surviving.
SOURCE: (← msg 3, 7)

REJECTED: General fail-open.
WHY: the patch explicitly freezes the real stops (legal, missing capability,
remaining CRITICAL, broken fix/provenance contract, deploy, bootstrap authority).
FAILURE IT WOULD CREATE: the exact catastrophe the fail-closed philosophy exists to
prevent, introduced under the banner of autonomy.
SOURCE: (← msg 10, 11, 12; 13)

REJECTED: STRATEGISK label as automatic stop.
WHY: strategic significance ≠ stop condition; a separate blocking classification
decides, and unknown classification must fail closed rather than silently continue.
FAILURE IT WOULD CREATE: either the owner as mutex (today) or silent continuation on
unclassified questions (the naive fix).
SOURCE: (← msg 11, 12; 13)

REJECTED: Fixing the Input Gate in this slice.
WHY: phone/USP is a "what is minimally necessary input" question — a different
semantic problem than attention-vs-blocking; releasing input through is not the fix.
FAILURE IT WOULD CREATE: scope creep redefining research validity under a delegation
patch.
SOURCE: (← msg 11, 12; 13)

## 6. Explored but unresolved
- Owner-Stop Audit across all of Nortropic — proposed with a predicted three-way
  outcome (real authority stops / routing stops mislabeled as owner stops /
  uncertainty stops convertible to ATTENTION+continue), not commissioned (← msg 7).
- Mandate-based split of deploy (standing deploy mandate + green gates + rollback +
  in-scope diff → autonomous; domain/DNS/paid services behind mandate boundary) and
  legal (escalate on material unresolved question, not on node existence) —
  explicitly later (← msg 7; 10, 13).
- Trust-calibration mechanics: evidence-based delegation-move proposals
  (ATTENTION → AUTONOMOUS) that only the owner enacts — direction stated, mechanism
  undesigned (← msg 7).
- Whether the prompt was executed and the patch landed — outside the source.

## 7. Important trade-offs / tensions
- Autonomy vs safety: resolved as an asymmetric contract — more autonomy for
  reversible in-mandate work, unchanged hardness at real boundaries; verification
  must prove both simultaneously (← msg 7, 11, 13).
- Attention volume vs attention value: attention must not become a second notification
  firehose; ownerActionRequired distinguishes "know this" from "answer this"
  (← msg 7, 11).
- Fail-closed heritage vs fail-open risk in migration: old artifacts without the new
  classification must not gain authority by absence of a field (← msg 13 §10).

## 8. Metaphor / concept → technical principle
"Kommunens delegationsordning" (municipal delegation order) → standing mandates per
decision class with escalation only for principal/unusual/large questions → MUST NOT
be copied as literal municipal process or committee structure (← msg 7).
"Mänsklig mutex" (human mutex) → the owner as a lock every flow must acquire → the
anti-pattern the patch removes; MUST NOT be reintroduced via attention events that
block (← msg 7, 13).

## 9. External evidence mentioned in the conversation
- OpenAI's Hugging Face incident report (26 Aug 2026): safe stopping, tiered
  responses, agents trained to keep original task/permissions despite peer
  instructions; harness+system prompt reduced compromise propensity >100× — cited
  in-source as independent corroboration of the ATTENTION/ROUTE/HARD_STOP
  distinction — EXTERNAL CLAIM MENTIONED IN SOURCE (← msg 14).
- Repo artifacts cited via file-chips during inspection (`/nortropic-plan`,
  `nortropic-autobygg.js`, `check-planner-routing.mjs`, taskval/h-032/h-031
  surfaces) — SOURCE-DERIVED FACTs about the repo as read in-chat; the repo itself is
  the authority (← msg 5, 7, 11).
- The surrounding scheduled delta reports (msgs 1–2, 14–18) are automated assistant
  monitoring, not part of this idea's decisions.
None of these were INDEPENDENTLY VERIFIED during this packaging run.

## 10. Evolution / pivots
1. "Too many owner stops" feeling → three-way separation and delegation order
   (← msg 3 → 6–7).
2. Philosophy → immediate surgical slice, once inspection showed the coupling is
   local and mechanically enforced (← msg 8 → 9–11).
3. Point-fix instinct → systematic audit framing, webbförvaltningen first
   (← msg 3 → 7).
4. Freshly formulated taxonomy → external corroboration by OpenAI's incident
   response the following day (← msg 11–13 → 14).

## 11. Retrieval map

| topic | message range |
|---|---|
| Owner's founding observation | 3 |
| Attention vs hard boundary; STOP ≠ ASK | 4–6 |
| Delegation order, bounded trust, exception management, audit | 7 |
| "Adjust now?" and locality finding | 8–10 |
| Four outcomes, case remapping, frozen stops | 11 |
| Prompt commissioned | 12 |
| Full patch prompt (taxonomy, events, tests, DoD) | 13 |
| HF-incident corroboration (safe stopping, tiered responses) | 14 |

## 12. What to load when
DEFAULT IMPLEMENTATION: read `idea-owner-attention-inte-owner-stop.md`.
IF DESIGN RATIONALE IS NEEDED: read this file.
IF EXACT SOURCE EVIDENCE IS NEEDED: read only the relevant message ranges in
`owner-attention-inte-owner-stop-full-chat.md` (use §11) — the verbatim patch prompt
is msg 13.
Do not preload the raw transcript into the main implementing context.
