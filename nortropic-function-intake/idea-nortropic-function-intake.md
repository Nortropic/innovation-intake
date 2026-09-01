---
title: "Nortropic Function Intake — dissect an organizational function until Nortropic can take responsibility for it"
type: idea-brief
status: idea
slug: nortropic-function-intake
owner: Johnny (Nortropic)
created: 2026-09-01
source_conversation: nortropic-function-intake-full-chat.md
design_rationale: nortropic-function-intake-design-rationale.md
intended_repo_path: nortropic-function-intake/idea-nortropic-function-intake.md
context_revision: 1
related: [nortropic-marknadsposition, nortropic-organization-os, project-corpus-intake]
---

# Idea brief: Nortropic Function Intake

## 1. Summary
The owner set the winning condition: Nortropic must win by **performing a whole
professional function better and more autonomously than the old supplier model**
(← msg 2). From that, the conversation derived a positioning thesis — *"we don't sell
AI; we sell responsibility for a professional function"* (← msg 3–5) — and the owner
commissioned its mechanism: **a sister to Nortropic Intake that dissects an
organizational function** ("djupdykning nortropic intak[e] fast på en organisatorisk
funktion", ← msg 6), ratified as the right direction (← msg 11). The mechanism walks
function mapping → autonomizability → authority/risk → economics → lighthouse test →
what can be compiled into Nortropic (← msg 7, 10). A first executed artifact exists:
the **Nortropic Function Discovery form** — 64 fields, 16 sections, interactive web
version with local autosave and `.md` export — published person-neutral and reusable
at `https://nortropic-function-discovery.johnnystrandkonsult.chatgpt.site`
(← msg 15–32, publication owner-approved ← msg 30). Viktor's company is the first
external Function Discovery candidate (← msg 11).

## 2. Context you need
Nortropic's internal build direction (Autonomy Kernel, Organization OS, Digitala as
first qualified förvaltning) answers *how* autonomous work becomes trustworthy.
Function Intake answers a different question: **which external professional function
can Nortropic take outcome responsibility for, and how do we find out rigorously?**
It is discovery machinery, not execution machinery — it produces understanding of a
function, not agents. The conversation explicitly distinguishes it from a shallow
"AI readiness assessment": first understand the work actually performed, then question
whether the work should exist in its current form at all, and only then decide what is
eliminated / agent-performed / human-performed / behind an authority boundary
(← msg 8). Key external calibration: single-task model quality (OpenAI GDPval) is not
the binding constraint — long-horizon coherence (METR) and how much decision authority
a task actually carries (Anthropic) are (← msg 9).

This brief is the primary intake artifact. Deeper design logic lives in the linked
design rationale; the full chat is raw evidence — read targeted message ranges only if
the rationale is insufficient. Current canonical repository authority beats all intake
artifacts. Invariants: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`). Pointer only.

## 3. Destination (goal, not implementation plan)
- A repeatable Function Intake method exists: given a real organization's function, it
  produces a case file covering (a) what the function actually does (first-principles
  reconstruction, not org-chart copying), (b) autonomizability per activity,
  (c) authority/risk boundaries, (d) economics of an outcome contract, (e) a
  lighthouse-test verdict: can Nortropic take responsibility for this function?
- The Function Discovery form is the standing first-contact instrument; completed
  forms flow into Function Intake cases.
- The first real case (Viktor's company) has been run and has *shaped the method* —
  the method is derived from a real case, not speculated in advance (← msg 14).
- Output is compatible with the corpus/Recompile world: a Function Intake case is
  evidence and option space, never an automatic commitment.

## 4. Decisions already made (do not relitigate silently)
- **D1.** Winning condition: whole professional function, better and more autonomous
  than the old supplier model — because partial tooling keeps the customer as
  integrator and keeps Nortropic comparable on price-per-tool (← msg 2, owner).
- **D2.** Build a Function Intake deep-dive mechanism, sister to Nortropic Intake —
  because market analysis alone cannot tell Nortropic whether it can *take
  responsibility* for a function (← msg 6, owner; elaborated msg 7–10).
- **D3.** Viktor's company is the first **external Function Discovery candidate** —
  not "first customer"; the case exists to test and shape the method (← msg 11 owner;
  reframing msg 12).
- **D4.** The Function Discovery form is person-neutral and reusable — because the
  same instrument must serve any future design partner (← msg 25, owner).
- **D5.** The form is published publicly (empty form public; answers stay in the
  filler's browser, exported manually) — owner approved publication (← msg 30).

## 5. Acceptance criteria (v1)
- **AC1.** WHEN a completed Function Discovery export is received, THE Function Intake
  method SHALL produce a case file with function map, autonomizability assessment,
  authority/risk boundary, economics sketch and lighthouse verdict, each traceable to
  specific form answers.
- **AC2.** WHEN a function is assessed, THE method SHALL explicitly separate
  eliminate / agent / human / authority-boundary classifications rather than a single
  "AI readiness" score (← msg 8).
- **AC3.** WHEN the first real case (Viktor) completes, THE method definition SHALL be
  revised against what the case actually taught before any second case runs (← msg 14).

## 6. Constraints & implementation notes (right altitude)
- Do not build a new skill prematurely; the first real case shapes the method — the
  "no new skill yet" sequencing is the assistant's recommendation the owner acted in
  line with by requesting the form first (← msg 14–15), not an owner prohibition.
- Function Intake output is discovery evidence. It carries no execution authority and
  activates nothing by itself (INTAKE ≠ BACKLOG applies here too).
- The published form must keep its no-server-storage property: answers autosave
  locally and are exported by the filler (← msg 22).

## 7. Out of scope (v1)
- Building agents/automation for any discovered function.
- Pricing/contract templates for outcome contracts.
- A second discovery case before the first has reshaped the method.

## 8. Verification (how we know it works)
A completed real case (Viktor) exists whose case file lets the owner answer, with
evidence rather than optimism: "could Nortropic take responsibility for this function —
and if not, exactly what capability, authority or economics is missing?"

## 9. Open questions (interview the owner before planning)
- **Q1.** Which function/vertical is the intended first outcome-contract target beyond
  the internal Digitala/web lane?
- **Q2.** What triggers turning Function Intake from method-in-a-case into a real
  skill/mechanism (how many cases, what evidence)?
- **Q3.** How does a Function Intake case feed RND_COMPILE/Recompile — as a swept
  source, an explicit source set, or a new source class?
- **Q4.** Has Viktor received the form, and is there a response deadline/expectation?

## 10. Process for this brief
Clarify (owner interview on §9) → Plan (Plan Mode against current repo reality) →
Implement fresh → Adversarial review. Status stays `idea` until pulled to build.

## References
- Source episode 1: `nortropic-function-intake-full-chat.md` (= Improvements sweep
  CONV-029 r1, chatgpt.com/6a970273-24f0-83eb-b033-ee199e96d345, 32 messages,
  captured 2026-09-01). Message tags `(← msg N)` resolve there.
- Published artifact: `https://nortropic-function-discovery.johnnystrandkonsult.chatgpt.site`
- Related: `nortropic-marknadsposition` (strategy option space this mechanism serves),
  `nortropic-organization-os` (internal capability architecture), `project-corpus-intake`
  (the intake discipline this mechanism mirrors).
