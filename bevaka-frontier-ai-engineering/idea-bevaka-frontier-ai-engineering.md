---
title: "Nortropic Frontier Observatory: an autonomous technological intelligence and evolution system"
type: idea-brief
status: idea   # lifecycle: idea → clarified → planned → building → verified; terminal: superseded
slug: bevaka-frontier-ai-engineering
owner: Johnny (Nortropic)
created: 2026-08-20
source_conversation: bevaka-frontier-ai-engineering-full-chat.md   # reference only — this brief takes precedence
intended_repo_path: bevaka-frontier-ai-engineering/idea-bevaka-frontier-ai-engineering.md
supersedes: [nortropic-frontier-delta]   # ägarbeslut 2026-08-20: Observatory ersätter Evolution Loop-briefen
related: [agent-harness-priorities, snabba-upp-loopar, workflow-orkestrering, brainstorma-nortropic-engineering]
---

# Idea brief: Nortropic Frontier Observatory — an autonomous technological intelligence and evolution system

## 1. Summary

Not a "bevakningsagent" — a full **autonomous technological intelligence and
evolution system**: Nortropic's outer nervous system. The Observatory answers "what
has changed in the world that makes something Nortropic believes, builds or does no
longer optimal — and how do we PROVE what to do instead?" Its architecture: three
systems (Frontier **Observatory** = perception + scientific learning; **Engineering
OS** = specs/tasks/evals/builds; **Trust Kernel** = authority/gates/promotion), with
the Observatory in its own repo producing evidence that flows
observatory → knowledge → innovation-intake → nortropic-system, always through
existing authority. The chat also contains a frank gap analysis of Johnny's practice
vs frontier labs, and activated a daily monitoring automation.

## 2. Context you need

Gap analysis against the actual repo (Aug 19): trust/verification 🟢 extreme; agent
roles, provider-neutrality, repo-as-source-of-truth 🟢; documentation 🟡 (strong but
heavy); verification 🟡 (deterministic-strong, eval-unbalanced); orchestration 🟡
(issue-tracker-as-control-plane is the next big opportunity); **agent observability
🔴, product feedback 🔴, engineering metrics 🔴** — the system is optimized for trust
far harder than for throughput/observability/learning. A daily automation ("Bevaka
Frontier AI Engineering") is ACTIVE since msg 6 and appends delta reports (msg 19
contains one, with an ADOPT-graded signal on event-driven coordination). The
Van Clief thread produced the People Radar idea: seed ~30–50 people, then
self-expand via OpenAlex citation/author graphs and GitHub fork/PR graphs — the
system finds the next Van Clief itself.
Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen
gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- A dedicated repo (e.g. `Nortropic/frontier-observatory`) that discovers, analyzes,
  experiments and produces evidence — never authority. Durable findings land in
  `nortropic-knowledge`; actionable candidates in the idea corpus; accepted work
  enters `nortropic-system` only through the existing authority chain.
- A **Sensor Mesh** over heterogeneous sources: official labs, people, arXiv/
  OpenAlex/OpenReview, the GitHub universe (GH Archive, repos, PRs, releases),
  communities (HN, blogs, podcasts) — and Nortropic itself (failures, eval results,
  corrections, bottlenecks).
- A **self-expanding People Radar**: seeded, then grown via citation/fork/author
  graphs; sources graded by evidence value, not fame.
- Epistemic processing: claims → hypotheses → falsification attempts → local
  experiments → evidence-graded recommendations (never "news summaries").
- The Observatory is integrated with (not separate from) the improvement machinery:
  its output feeds the same ladder/backlog as other evolution work.

Choose architecture/decomposition/tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

- D1. The daily "Bevaka Frontier AI Engineering" automation is ACTIVE (reports only
  threshold-passing signals) (← msg 6).
- D2. Owner directive on ambition: "Vi tar alltid fulla steg, next level" — no
  V0-that-just-summarizes; design for the full Observatory target (← msg 15–16).
- P1 (locked principle in-chat). The Observatory must never be trust authority, and
  must not live inside the knowledge repo's runtime (knowledge stays non-authoritative)
  (← msg 17–18).
- P2 (proposal). Own repo, clean flow: observatory → knowledge → intake → system
  (← msg 18).
- P3 (proposal). People Radar self-expansion via OpenAlex/GitHub graphs (← msg 12–18).
- R1 (REJECTED). A small standalone "bevakningsagent"/research agent as the end state
  (← msg 16–18).
- Also standing: the gap-analysis verdicts (observability/product-feedback/metrics as
  🔴 gaps) as assistant assessments awaiting owner triage (← msg 5).

## 5. Acceptance criteria (v1)

- AC1. WHEN the Observatory reports, THE output SHALL be evidence-graded claims with
  provenance and a recommended next action — never an unranked news digest.
- AC2. WHEN a recommendation is adopted, THE record SHALL show it passed local
  reproduction/experiment before touching Nortropic — external claims alone never
  justify change.
- AC3. WHEN the People Radar adds a source, THE addition SHALL carry the graph path
  that surfaced it and an evidence grade.
- AC4. WHEN any Observatory run completes, THE record SHALL show zero writes to
  `nortropic-system` and no authority transitions.

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants: Nortropic's trust layer — constitution & rulebook (pointer, never a copy).
Suggestions: reconcile with `nortropic-frontier-delta` FIRST (the Evolution Loop's
ladder OBSERVED→…→ADOPTED, held-out evals and Strategy Reconsideration Gate are the
natural processing spine for Observatory output — one system, not two); OpenAlex API
for citation/author graphs; GH Archive for repo events; the three-system diagram
(Observatory / Engineering OS / Trust Kernel) is a strong documentation frame.

## 7. Out of scope (v1)

- Any authority/trust capability for the Observatory (P1).
- Living inside nortropic-knowledge's runtime (P1).
- Fixing the gap-analysis 🔴s (observability, product feedback, metrics) — separate
  work; the analysis is recorded here as input for the rebaseline.

## 8. Verification (how we know it works)

End-to-end: one signal travels sensor → claim → hypothesis → local experiment →
graded recommendation → (if adopted) the normal authority chain — every step
evidenced in the record, with AC4's zero-write proof for the Observatory runs.

## 9. Open questions (interview the owner before planning)

- Q1. (Avgjord av ägaren 2026-08-20: SUPERSEDES `nortropic-frontier-delta` — se
  frontmatter. Den ersatta briefen och dess transkript kvarstår som evidens.)
- Q2. Two daily monitoring automations now run (Frontier Delta + Bevaka Frontier AI
  Engineering) plus a weekly /design watch — consolidate into one feed?
- Q3. Does Observatory wait for the bootstrap + S14-S20 sequencing (frontier-delta
  P1), or begin as a standalone repo earlier since it can't touch nortropic-system?
- Q4. The gap-analysis 🔴s: which becomes the first owner-prioritized task —
  observability, product feedback loops, or engineering metrics?
- Q5. People Radar privacy/ethics bounds: public sources only, and what grading
  criteria?

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

- Source conversation: `bevaka-frontier-ai-engineering-full-chat.md` (same folder)
- Superseded brief: `nortropic-frontier-delta/` (Evolution Loop + Frontier Delta feed — status: superseded)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
