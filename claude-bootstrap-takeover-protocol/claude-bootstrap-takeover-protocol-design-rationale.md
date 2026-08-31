---
title: "Claude Bootstrap Takeover Protocol — design rationale"
type: design-rationale
status: source-derived
slug: claude-bootstrap-takeover-protocol
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: claude-bootstrap-takeover-protocol-full-chat.md
execution_brief: idea-claude-bootstrap-takeover-protocol.md
authority: non-authoritative-rationale
fidelity: full
context_revision: 1
---

# Design rationale: Claude Bootstrap Takeover Protocol

## 1. Core thesis
"Modellen är en replaceable worker; authority, evidence, state och process tillhör
Nortropic" (← msg 39). What looks like "Codex is autonomous, Claude wasn't" is mostly
Codex inheriting a finished Nortropic operating system, an explicit mandate, and
internalized Nortropic epistemology (← msg 37). Therefore a usage cap should trigger a
provider switch, not a work stop: Claude continues the exact autonomous loop from a
machine-verifiable checkpoint — and the switch is symmetric (← msg 38–41).

## 2. Problem / current state / intended outcome
The owner observed a stark autonomy difference between the earlier Claude Code phase
and the current Codex phase and asked why (← msg 35). The practical risk: Codex works
under a usage cap, locally ahead of published main (H035-R15 TEST_AUTHOR lane;
published authority PR #175); if the cap hits mid-adversarial-round, a naive takeover
could lose or corrupt unpublished work (← msg 39). Intended outcome: a standing
protocol where cap-exhaustion produces a safe checkpoint, a byte-grounded takeover
prompt, and seamless continuation of the same supervisor loop (← msg 38–41).

## 3. Reasoning chain
The assistant decomposed the autonomy difference into five factors (← msg 37): Codex
inherited the built Nortropic ("Claude helped build the railway; Codex drives the
train on it"); the Codex product is optimized for multi-agent long-running work; the
mandate is explicit ("you have authority to build, review, push, merge — a claimed
owner stop must be mechanically proven"); the interaction pattern shifted from
human↔agent to supervisor↔workers; and the bootstrap itself has "trained" the agent
into Nortropic's epistemology (claim ≠ proof, structural green ≠ runtime green,
same-author review ≠ independent review). Conclusion: given the same rails, today's
Claude Code would likely look dramatically more autonomous — with one possibly real
Codex edge (keeping a long technical goal alive with self-spawned parallel tracks),
only decidable by a fair post-bootstrap A/B (← msg 37, ASSISTANT INFERENCE). The
owner then stated the durable intention: Claude continues the same way if Codex usage
runs out mid-bootstrap (← msg 38). The assistant converted it into transfer design
(← msg 39): four objects (authority, epistemology, exact state, supervisor form);
state read from repo artifacts and mechanically re-verified, because narrative
handoffs rot; the fail-safe "inspect before mutation" rule protecting Codex worktrees
with unpublished work; a standing protocol prepared *before* the cap hits; symmetry
Claude↔Codex; and the suggestion to make provider-survivability an explicit Kernel v1
requirement. The owner adopted the operational plan — he signals when usage runs low,
then the Codex handoff prompt is prepared (← msg 40) — and the assistant specified
the checkpoint contract the Codex prompt must produce, and that the final Claude
prompt is built from Codex's actual handoff output plus current GitHub truth, never a
generic continuation prompt (← msg 41).

## 4. Design decisions and why
D1. Same work-form across providers ("fortsätta på samma sätt").
    Why: the loop (build → falsify → review → freeze → publish → continue, stop only
    at proven owner boundaries) is Nortropic's asset; letting the incoming model
    improvise forfeits it.
    Evidence: owner's explicit wording; the eliminated anti-pattern "Claude → finds
    question → asks Johnny → waits".
    Source: (← msg 38; 39)
D2. Checkpoint produced by the outgoing worker at a safe boundary.
    Why: only Codex knows its lanes/verdicts/uncommitted state; the checkpoint must
    complete or safely stop the atomic step, start nothing new, and enumerate
    published vs unpublished vs uncommitted bytes.
    Evidence: the ten-point Codex handoff prompt contract.
    Source: (← msg 40; 41)
D3. Mechanical verification before continuation.
    Why: "the checkpoint is claims, not proof" — Claude must verify main/HEAD/
    worktrees/candidates against the repo, not execute the text as a TODO list.
    Evidence: "Claude skulle inte få tolka detta som en TODO-lista … verifiera att
    det fortfarande är sant och därefter fortsätta".
    Source: (← msg 38; 39)
D4. Inspect before mutation — never touch a Codex worktree with unpublished work.
    Why: named prior incident class (branch switching in a shared working copy);
    clean immutable commit → new own worktree; uncommitted work → preserve and
    identify, never "clean up".
    Evidence: the explicit fail-safe first rule of the handoff.
    Source: (← msg 38; 39)
D5. Symmetric, repeatable switching.
    Why: Claude → Codex → Claude → Codex without institutional state living in either
    model's context is the instantiation of model-as-replaceable-worker.
    Evidence: the symmetry paragraph and its principle statement.
    Source: (← msg 38; 39)

## 5. Explicit rejections / anti-requirements
REJECTED: Claude taking over "på sitt eget sätt" (its own way).
WHY: implicit in the owner's requirement; the work-form, not the model's preference,
defines the loop.
FAILURE IT WOULD CREATE: a mid-bootstrap methodology fork — different review
discipline, different stop behavior — invalidating the accumulated process trust.
SOURCE: (← msg 38, 40; 39)

REJECTED: Provider switch as restart with manual state reconstruction.
WHY: the human as reconstruction layer is exactly what Nortropic exists to remove;
state lives in repo artifacts and is re-verified mechanically.
FAILURE IT WOULD CREATE: lost lanes/evidence, re-done inventory, thrown-away Codex
work, days of owner archaeology.
SOURCE: (← msg 40; 39, 41)

REJECTED: A generic "continue the bootstrap" prompt for Claude.
WHY: the prompt must be built from the exact bytes and trust-transition Codex leaves
behind plus verified GitHub truth.
FAILURE IT WOULD CREATE: Claude acting on stale assumptions about which candidate/
authority state is current.
SOURCE: (← msg 40; 41)

REJECTED: Hasty model switch at the cap moment.
WHY: first check where the bootstrap actually stands; then the two-prompt sequence.
FAILURE IT WOULD CREATE: cap-panic handoffs mid-atomic-step, precisely when loss risk
is highest.
SOURCE: (← msg 40; 41)

## 6. Explored but unresolved
- The concrete checkpoint format and the four transfer objects as written — assistant
  proposals, never owner-ratified point by point (← msg 39, 41).
- "Usage starting to run out" — no mechanical threshold; owner signals manually
  (← msg 38, 40).
- Provider-survivability as an explicit Autonomy Kernel v1 requirement — assistant
  proposal ("ett väldigt starkt slutprov"), unconfirmed (← msg 39).
- The fair A/B experiment (same main/task/authority/budget/gates; compare
  interventions, time, usage, defects, regressions, owner-stop false positives,
  verified quality) — sketched by the assistant off the owner's comparative question;
  no experiment decided (← msg 35; 37).
- Interaction with bootstrap-closeout-rebaseline's phase-A deferral of "Claude
  migration mid-run" — reconciliation is an open question, not resolved in this
  source.

## 7. Important trade-offs / tensions
- Continuity vs safety at the boundary: finishing the atomic step maximizes
  continuity, but only "if it can be done safely — otherwise stop at the nearest safe
  boundary" (← msg 41).
- Model-equivalence claim vs observed edge: the thesis is provider-interchangeability,
  yet the source honestly notes a possible genuine Codex advantage in long-goal
  persistence — asserted equivalence would need the A/B to be proven (← msg 37).
- Rich handoff narrative vs verifiable state: the design deliberately prefers minimal
  repo-anchored state plus re-verification over a long story of "what we think
  happened" (← msg 39).

## 8. Metaphor / concept → technical principle
"Järnvägen och tåget" (Claude built the railway; Codex drives the train) → autonomy
lives in the rails (harness/authority/epistemology), not the locomotive (model) →
MUST NOT be read as a claim that models are identical in capability (← msg 37).
"Replaceable worker" → any executor may be swapped while Nortropic retains authority,
evidence, state and process → MUST NOT justify skipping per-provider verification of
the actual switch (← msg 39).

## 9. External evidence mentioned in the conversation
All MENTIONED IN SOURCE (assistant web citations in msgs 36–37); none INDEPENDENTLY
VERIFIED during this packaging run: Anthropic material on Claude Code sandboxing,
Auto mode and lengthening unattended sessions, and the "human decides what, Claude
decides how" usage analysis; OpenAI's positioning of Codex for multi-agent, long-
horizon work and its sandbox-boundary vs approval-policy model with Auto-review. The
surrounding thread's Codex reports (SHAs, PR #174/#175, H035-R15/R16/R17 chronology)
are owner-relayed machine evidence — execution log, deliberately excluded from this
idea's decisions; two large pasted night-logs live in uncaptured attachments
(Inklistrad markdown(1–2).md).

## 10. Evolution / pivots
1. "Why is Codex more autonomous?" → five-factor decomposition: it's mostly the
   harness/mandate, not the model (← msg 35 → 36–37).
2. Comparative observation → durable failover intention: Claude continues the same
   way at cap exhaustion (← msg 37 → 38).
3. Ad-hoc contingency → standing two-prompt protocol with fail-safe worktree rule and
   Claude↔Codex symmetry (← msg 38 → 39 → 40–41).

## 11. Retrieval map

| topic | message range |
|---|---|
| Owner's comparative question | 35 |
| Five-factor autonomy analysis; A/B sketch; replaceable-worker principle | 36–37 |
| Owner failover intention | 38 |
| Four transfer objects; inspect-before-mutation; standing protocol; Kernel v1 proposal | 39 |
| Owner trigger procedure | 40 |
| Codex checkpoint contract; byte-grounded Claude prompt | 41 |

## 12. What to load when
DEFAULT IMPLEMENTATION: read `idea-claude-bootstrap-takeover-protocol.md`.
IF DESIGN RATIONALE IS NEEDED: read this file.
IF EXACT SOURCE EVIDENCE IS NEEDED: read only the relevant message ranges in
`claude-bootstrap-takeover-protocol-full-chat.md` (use §11).
Do not preload the raw transcript into the main implementing context.
