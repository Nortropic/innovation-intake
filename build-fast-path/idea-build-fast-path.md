---
title: "Build fast path: template repo + Content-phase split"
type: idea-brief
status: clarified   # idea → clarified → planned → building → verified
slug: build-fast-path
owner: Johnny (Nortropic)
created: 2026-08-16
source_conversation: build-fast-path-full-chat.md   # reference only — this brief takes precedence
intended_repo_path: ideas/build-fast-path/idea.md
---

# Idea brief: Build fast path — template repo + Content-phase split

## 1. Summary

Make Nortropic site builds fast the way Lovable is fast — without touching the quality
gates. Two changes: (a) a `nortropic-template` repo that Init **clones** instead of
scaffolding everything from zero with `create-next-app`, and (b) splitting the autobygg
pipeline at the Content phase so everything up to a built preview becomes its own
fast command, with `/nortropic-review` and `/nortropic-launch` as separate, later
decisions. The framing decision: Lovable optimizes time-to-first-look, the v17 pipeline
optimizes time-to-deliverable — Johnny gets both as **two different commands**, never as
one "faster pipeline". A third, owner-confirmed track rides along: the Thursday retro
becomes a `/schedule` cloud routine (see D8).

## 2. Context you need

The system is v17 in the `nortropic-system` repo (pipeline: research → plan → build →
audit → fix → handover). Relevant facts established in the source chat by reading the
actual code:

- `stack-builder` currently runs `create-next-app` and reasons its way through setup
  from scratch every run — the bulk of build wall-clock, and the origin of finding AG3
  (create-next-app colliding with onboarding artifacts in the clone).
- An estimated 70–80% of every build is plumbing that is identical across customers
  (Grens, Bellsblomster, Fanérverket): lead-action with honeypot/time-trap, CSP headers
  in `next.config.ts`, schema components, `sitemap.ts`/`robots.ts`, error pages,
  analytics wiring.
- Audit gates already run in parallel (`nortropic-launch.js`), partial re-audit already
  exists, and a verify-suite with frozen baselines exists. Parallelism is NOT the
  bottleneck; adversarial verify, the design canon loads, and autobygg's double review
  are the big cost posts (see `verify-kalibrering.md` and justeringskartan — separate
  protocols, not this idea).
- Finding AG5: sites converging into siblings; the differentiation check compares
  declared tokens, not perceptual gestalt — so a template that leaks expression would
  not be caught.

Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.

## 3. Destination (goal, not implementation plan)

- A `nortropic-template` repo containing the shared plumbing, so Init becomes
  `git clone` + `pnpm i` — seconds instead of many minutes — and AG3 becomes
  impossible by construction (no `create-next-app` into an existing directory).
- A fast-path command that stops where Lovable stops:
  plan → clone template → fill `content/*.ts` → design tokens → generate pages →
  `pnpm build` → **Vercel preview URL**. No review, no gates, no verification inside it.
- The Thursday retro runs as a `/schedule` cloud routine instead of a manual session
  (shape per the chat's v18 sketch: mine recent production runs for recurring
  corrections → cluster in parallel → adversarially verify each candidate rule →
  distill survivors into CLAUDE.md/skills).
- Review and launch remain untouched, downstream, and explicitly separate decisions.
- A side benefit to preserve: a template that passes Gates 0, 3, 4, 7 by construction
  means fewer findings → fewer skeptics → shorter Verify phase in later review.
- Choose architecture, decomposition, and tooling yourself within §6.

## 4. Decisions already made (do not relitigate silently)

- D1. The two speed wins are the template repo and the Content-phase split, and BOTH
  are in scope — because the identical 70–80% is re-reasoned every run, and the
  pipeline currently runs QA on drafts. (Chat's closing summary; the in-chat "nej tack"
  only declined a file-tree sketch — owner confirmed the decision 2026-08-16, see
  Clarifications.)
- D2. REJECTED: git worktrees for faster builds — because worktrees solve write
  conflicts, not wait time; the fix loop is sequential by design ("så två agenter
  aldrig skriver samtidigt"), and worktree isolation is already GATED (Y1 repo
  structure provides sandboxing; reintroducing worktrees reopens `/c/`→`C:\c\`
  mangling). Only legitimate homes: tournament pattern and provably disjoint fixers.
- D3. REJECTED: replacing the hand-built fix loop with `/goal` — because string-matching
  `BLOCKERS: 0` is deterministic and an evaluator model is a judgment call.
- D4. REJECTED: dynamic workflows in the production pipeline — because the pipeline has
  the same shape every run; a fresh unvalidated harness per customer trades the hardened
  v17 chain for risk. (Right place is the retro — out of scope here.)
- D5. The template is plumbing only, never expression — because layout, section order,
  component composition or design tokens in the template automates AG5, and the current
  differentiation check cannot catch it. Form logic is template; form appearance is not.
- D6. REJECTED: parallelizing the site build itself (one agent hero+services, another
  about+contact) — because gestalt requires one context owning the whole; splitting it
  is the exact mechanism that produced AG5.
- D7. Measure before any further rebuild — a full review read through `/workflows` +
  `/usage` decides whether verify-calibration or anything else is the next win; the
  concurrency-cap question (queued vs truly parallel) is open. (Owner chose to keep
  the measurement parked as its own track, outside this scope.)
- D8. The Thursday retro becomes a `/schedule` cloud routine — because it is recurring
  work with the same shape and varying input (canonical routine), and the cloud path
  avoids the `/c/`→`C:\c\` mangling entirely. (Parked in the first distillation;
  owner promoted it to an in-scope decision 2026-08-16, see Clarifications.)

## 5. Acceptance criteria (v1)

- AC1. WHEN the fast-path command runs for a new customer, THE system SHALL produce a
  green `pnpm build` and a Vercel preview URL without invoking any review, gate, or
  verify agent.
- AC2. WHEN Init runs in the fast path, THE system SHALL clone `nortropic-template` and
  install dependencies; `create-next-app` SHALL NOT run anywhere in the fast path.
- AC3. WHEN the template repo is inspected, THE template SHALL contain the shared
  plumbing (lead-action, security headers, schema components, sitemap/robots, error
  pages, analytics wiring) and SHALL NOT contain design tokens, typography scale,
  section composition, hero structure, image language, or copy.
- AC4. WHEN the fast path completes, THE system SHALL stop — review/launch run only as
  separate explicit commands, and WHEN they later run on a fast-path site, all existing
  gates SHALL run unchanged.
- AC5. WHEN the fast path is timed on a real or synthetic customer, THE Init phase
  SHALL complete in well under a minute, and end-to-end wall-clock SHALL be recorded
  against a baseline autobygg run.
- AC6. WHEN the scheduled retro routine fires, THE routine SHALL run unattended in the
  cloud, produce a human-readable retro report, and SHALL NOT write to CLAUDE.md,
  skills, or rules without each candidate rule having passed adversarial verification —
  final commit of surviving rules remains a human action (§A6).

## 6. Constraints & implementation notes (suggestions, not orders)

- The template/expression boundary from the chat: in template — lead-action, headers,
  schema components, sitemap, error pages, analytics; generated per customer — design
  tokens, typography scale, section composition, hero build-up, image language, copy.
- Keep the fast path additive: no existing gate, hook, or §-rule is modified or
  weakened; the split point is the Content phase of autobygg.
- Deterministic work as scripts, not reasoning (the system's own principle).
- Fail closed: if `pnpm build` fails, the fast path reports it — it does not silently
  hand over a broken preview.

## 7. Out of scope (v1)

- Unmanned/headless night runs (`claude -p`, cron, autonomy contracts) — superseded
  in-chat by built-in primitives; separate idea if revived.
- Planner rewrite as tournament; re-triaging the retro inbox against primitives.
  (Retro as `/schedule` was promoted INTO scope — see D8.)
- Verify calibration (one skeptic, CRITICAL/HIGH only) and the autobygg double-review
  decision — owned by `verify-kalibrering.md` and the freshness gate respectively.
- The AG5 gestalt-verify fix (Vercel-preview side-by-side judgment) — already in
  progress on its own track.
- Any git-worktree mechanism (D2).

## 8. Verification (how we know it works)

One end-to-end run on a synthetic customer: fast-path command from zero to Vercel
preview URL, timed, with the baseline autobygg timing beside it; then
`/nortropic-review` on the result showing all gates fired unchanged. For the retro
track: one dry-run firing of the scheduled routine producing a retro report from real
run data. Evidence: timing table, preview URL, gate report, retro report — confirmable
from the record alone.

## 9. Open questions (for the plan phase)

- Q1. Where does `nortropic-template` live (own private GitHub repo? folder in
  nortropic-system?) and how do template updates propagate to already-built sites —
  or don't they? (Owner explicitly deferred this to planning.)
- Q2. Ambiguous boundary items: sticky header with `tel:` and the floating call button
  were listed as identical-bits, but header/button are visible expression — template
  or generated?
- Q3. What is the command named (`/nortropic-draft`? `/nortropic-fast`?), and may the
  fast path reuse the existing plan phase output unchanged?
- Q4. Retro routine specifics: cadence (weekly Thursday?), exactly which run data it
  mines, and where the retro report lands so Johnny sees it.

## Clarifications (owner interview, 2026-08-16)

- D1 confirmed: BOTH the template repo and the Content-phase split command are the
  idea to build. The in-chat "nej tack" was not a rejection of the idea.
- The fast path ends at a **Vercel preview URL** (closest to the Lovable experience),
  not a localhost build.
- Template home: deliberately left to the plan phase (Q1).
- Side-track promotion: **retro as `/schedule` routine** is a decision, now D8 and in
  scope. Measurement (D7), verify calibration, and the AG5 gestalt fix stay parked as
  separate tracks.

## 10. Process for this brief

1. Clarify: first send a subagent to read the source conversation and report back the
   rationale relevant to §9 (keeps the transcript out of main context); then interview
   the owner on §9 (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code ("address all notes, don't
   implement yet").
3. Implement in a fresh session from the approved plan.
4. Adversarial review: fresh subagent checks the diff against this brief; report only
   gaps affecting correctness or stated requirements.
5. Traceability: commit messages cite this brief's slug (`build-fast-path`).

## References

- Source conversation: `build-fast-path-full-chat.md` (same folder)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
