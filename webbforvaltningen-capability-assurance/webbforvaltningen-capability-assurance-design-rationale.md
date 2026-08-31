---
title: "Webbförvaltningen Capability Assurance — design rationale"
type: design-rationale
status: source-derived
slug: webbforvaltningen-capability-assurance
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: webbforvaltningen-capability-assurance-full-chat.md
execution_brief: idea-webbforvaltningen-capability-assurance.md
authority: non-authoritative-rationale
fidelity: full
context_revision: 1
---

# Design rationale: Webbförvaltningen Capability Assurance

## 1. Core thesis

What began as "is the 100-day backlog still current?" (← msg 1) became a general method: the real question is not "what from the old plan is missing?" but **"how does Nortropic prove a förvaltning is complete for its declared mission, without reintroducing old architecture, missing new gaps, or confusing 'built' with 'proven'?"** (← msg 10). The answer is Assurance Compilation: historical plans, the frozen masterplan, current implementation, real-world evidence and today's frontier compile into atomic proof obligations — claim → evidence → defeaters → disposition — never into a new to-do list (← msg 10 §1).

## 2. Problem / current state / intended outcome

The day-by-day walk of D001–D100 against current `main` produced a three-part picture: Dag 1–20 largely absorbed by Trust Kernel/Bootstrap (do not rebuild); a mixed middle where CI/CodeQL/branch-protection (D21–24, D30), design intelligence (D35–40) and framework policy (D47) are genuine remaining holes while archetypes/module registries are superseded; and a surprisingly current last third — migration, final fact approval, human user testing, Care/Growth, cross-client isolation, disaster recovery, full E2E, readiness board (← msgs 2, 4). The repo's own `kompetensregister` refuses `PROVEN` at ~n≈1 real datapoints — the system already agrees the lifecycle is unproven (← msg 4). Intended outcome: after BUILD_COMPLETE, a small decidable picture — what is proven, what is only built, what is missing, what is superseded, what must be removed, what only needs reality — feeding owner-triaged implementation intake (← msgs 14, 18).

## 3. Reasoning chain

Owner asks if the backlog is still current (← msg 1) → distinction: manual = requirements/coverage source, masterplan + repo = execution authority (← msg 2) → owner requests the 1-by-1 comparison (← msg 3) → the full D001–D100 verdict table, revealing the three-part structure and "don't release v1 without modernized D61–70/D91–100" (← msg 4) → owner sets sequencing: finish the build, then Intake with a comparative prompt (← msg 5) → dispositions + atomicity + "problem solved?, not file exists?" (← msg 6) → owner invites deeper brainstorm (← msg 7) → fourfold final audit (historical, masterplan, fresh frontier, real lifecycle), atomization, two axes, zombie prevention, orphaned requirements, delta-threat-model, dual challengers (← msg 8) → owner: continue (← msg 9) → generalization to Nortropic Capability Assurance: assurance graph, defeaters, proof classes, persistence classes, boundary audit, reality/evidence gaps, negative gaps, evidence half-life, incremental re-audit, audit-of-audit with falsification cases, consequence-first prioritization, mission coverage (← msg 10) → owner: you checked nothing against POIs/agencies/literature/OpenAI/Anthropic (← msg 11) → External Comparator Audit: OpenAI evals lens, Anthropic harness-assumption audit + blast radius, Karpathy experiments, evolutionary architecture, DORA delivery-performance plane, SRE user-visible SLOs, Good Services/GOV.UK, Team Topologies, agencies, role-based POI radar, Council of Lenses, novel requirements, "what would kill the agency?" (← msg 12) → owner asks about next step (← msg 13) → two-round Intake model: capture now as `webbforvaltningen-capability-assurance`, evaluate at BUILD_COMPLETE as a new source episode; no-build contract; completion-state ladder; counterfactual, economics and tacit-dependency lenses (← msg 14) → owner demands control over all variables incl. literature + extracted design skills, anti-slop (← msg 15) → Web Excellence & Design Intelligence: source-authority classes, Web Standard × Visual Intent, skill distillation table, anti-slop-is-a-constraint, four verdicts, blind agency-grade benchmark, conflict register, SOURCE_DIVERSITY (← msg 16) → owner: ready to plan (← msg 17) → Stage A/Stage B split and the full intake prompt (← msg 18).

## 4. Design decisions and why

D1. Capture now, evaluate at BUILD_COMPLETE.
    Why: the audit target moved (49d0662… → 9ace2fb… → 9e85d7b…) during the conversation itself; judging a moving main produces stale verdicts. Evidence: SHA drift observed in-chat. Source: (← msgs 5, 14, 18).
D2. Atomic, problem/outcome-level reconciliation with two axes (disposition ≠ maturity).
    Why: one "day" holds several ideas (D038 example); `SATISFIED` must not mean both "code exists" and "works in reality". Source: (← msgs 5–6, 8).
D3. Outside-in comparator council, held as separate schools.
    Why: Nortropic-vs-Nortropic inherits shared blind spots; each school optimizes for different things (evals, harness freshness, reliability, delivery, service, craft). Source: (← msgs 11–12).
D4. Web Excellence & Design Intelligence as its own sub-audit.
    Why: two goals — objectively good per standards/research/literature AND distinct non-slop craft — where either alone fails the bar; eight design skills loading simultaneously today is ingredients, not a kitchen. Source: (← msgs 15–16).
D5. Read-only first campaign + owner triage before any implementation intake.
    Why: assurance that implements its own findings becomes governance bloat and scope creep; dedupe 100 points into few modern gaps first. Source: (← msgs 14, 17–18).
D6. Assurance claims carry defeaters and invalidation surfaces.
    Why: "reasons to doubt" plus staleness-on-change turn a snapshot audit into an incrementally re-auditable institution. Source: (← msg 10 §5, §18–19).

## 5. Explicit rejections / anti-requirements

REJECTED: Audit now against the moving build. FAILURE: stale conclusions, duplicated work, Claude re-solving solved problems in older forms. SOURCE: (← msgs 5, 14).
REJECTED: Composite completeness score. FAILURE: Goodhart — one silent fact-drift risk outweighs 50 green items; the score hides it. SOURCE: (← msg 17; msg 10 §25).
REJECTED: 100-day manual as active execution plan / "continue from Day 21". FAILURE: reverts superseded architecture (eight archetypes, module registry, own policy engine) and duplicates Trust Kernel. SOURCE: (← msg 5; msgs 2, 4).
REJECTED: Filename/component-presence matching. FAILURE: builds `FACT-LEDGER.json` because the old plan used that name, even when a better first-class carrier exists — and conversely marks live behavior "missing". SOURCE: (← msg 17; msgs 6, 10 §2).
REJECTED: Campaign implements its own findings. FAILURE: 73 issues that are really six gaps; assurance becomes a build program without owner choice. SOURCE: (← msg 17; msg 14).
REJECTED (assistant-argued within the adopted framework): letting fresh frontier findings bypass Knowledge Lane into `STILL_REQUIRED`. FAILURE: web search becomes authority. SOURCE: (← msg 17; msg 10 §14, msg 18).

## 6. Explored but unresolved

- The completion-state ladder `BUILD_COMPLETE → CAPABILITY_ASSURANCE → V1_READY/GAPS_KNOWN → real-customer evidence → PROVEN` is an assistant proposal awaiting owner ratification (← msg 14 §1).
- Which comparator lenses become canon — the ~12-lens shortlist is a proposal (← msg 14 §3).
- Proof classes P0–P5 vs the existing `DECLARED/BUILT/VALIDATING/PROVEN` vocabulary — "principen är viktigare än namnen" (← msg 10 §6).
- Where design-canon distillation runs (inside the campaign or separately), and how human taste calibration is institutionalized (← msg 16).
- Economics and operator-independence depth (← msg 14).

## 7. Important trade-offs / tensions

- Coverage vs bloat: the Coverage Challenger protects against forgetting; the Simplification Challenger against backlog inflation — deliberately opposed (← msg 8).
- Governance vs smallness: success is *fewer* orphaned requirements, duplicated authorities, unnecessary components — "audit bör generera mindre system, inte större" (← msg 10 §30).
- Standardization vs distinction: a strong design canon risks sibling convergence; anti-slop enforced as style becomes the next slop (← msg 16).
- Elegance vs reality: architecture quality does not equal customer outcome — Outcome is an independent verdict (← msgs 10 §29, 12, 16).
- Completeness vs shipping: the stop rule exists so v1 is not held hostage by infinite self-review (← msg 8).

## 8. Metaphor / concept → technical principle

- "Semantic zombies" → supersession must record the forbidden semantic role, not the filename; a re-named `module-manifest` is the same zombie. Do not copy literally: not every superseded concept needs a tripwire — only dangerous ones (← msgs 8, 10 §10–11).
- "Architecture anti-bodies" → selective mechanical tripwires (e.g. `NO_SECOND_SITE_QUALITY_CONTRACT`) against costly past mistakes (← msg 10 §10).
- "Kitchen, not eight cooks at one pot" → distill external skills into owned, conflict-resolved knowledge rather than stacking sources (← msg 16).

## 9. External evidence mentioned in the conversation

All MENTIONED IN SOURCE (not independently verified in this run): SEI assurance cases and eliminative confidence/defeaters; NASA systems-engineering bidirectional traceability & verification matrices; Thoughtworks/Building Evolutionary Architectures fitness functions; NIST SSDF traceability/provenance; OpenAI Specify→Measure→Improve evals stack (datasets, trace grading); Anthropic harness-assumption staleness, planner/generator/evaluator long-running app development, containment/blast-radius; Boris Cherny/Claude Code POI framing; Karpathy experiment discipline; Google SRE SLOs/error budgets; DORA/Accelerate; Charity Majors observability; Lou Downe Good Services; GOV.UK Service Standard (incl. 2026 AI-competence update); Team Topologies/Thinnest Viable Platform; Brad Frost design-system governance; Addy Osmani performance budgets; Baymard; Refactoring UI; Practical UI; Norman; Krug; agencies Build in Amsterdam, ustwo, Instrument, DEPT; Emil Kowalski skills repo ("sea of slop", taste-is-trained), Taste (Taste DNA), Impeccable (anti-pattern checks) (← msgs 10, 12, 16). In-repo evidence via filecite: current `design-reviewer` loads all eight design sources; gestalt sibling-similarity check exists; `kompetensregister` = VALIDATING (← msgs 4, 16).

## 10. Evolution / pivots

- "Is the backlog current?" → backlog as coverage/backstop (← msgs 1–2) → three-part verdict after the full walk (← msg 4) → fourfold audit (← msg 8) → generalized Capability Assurance (← msg 10) → + External Comparator council (← msgs 11–12) → + two-round Intake, no-build contract (← msg 14) → + Web Excellence & Design Intelligence (← msgs 15–16) → frozen direction, Stage A/B (← msgs 17–18). Early "just compare two plans" framings are superseded and must not be revived.

## 11. Retrieval map

| topic | message range |
|---|---|
| Backlog status; manual vs masterplan authority | 1–2 |
| Full D001–D100 verdict table (all ten phases) | 3–4 |
| Owner sequencing; dispositions; hard comparative prompt | 5–6 |
| Fourfold audit, atomization, zombie prevention, challengers | 7–8 |
| Generalized Capability Assurance (graph, defeaters, gaps, mission coverage, falsification of the audit itself) | 9–10 |
| External comparator council, lenses, agency failure modes | 11–12 |
| Two-round Intake, no-build contract, completion ladder, counterfactual/economics/tacit lenses | 13–14 |
| Web Excellence & Design Intelligence, anti-slop, four verdicts | 15–16 |
| Freeze decision, Stage A/B, full intake prompt | 17–18 |

## 12. What to load when

DEFAULT IMPLEMENTATION: read `idea-webbforvaltningen-capability-assurance.md`.
IF DESIGN RATIONALE IS NEEDED: read this file.
IF EXACT SOURCE EVIDENCE IS NEEDED: read only the relevant message ranges in `webbforvaltningen-capability-assurance-full-chat.md` (use §11).
Do not preload the raw transcript into the main implementing context.
