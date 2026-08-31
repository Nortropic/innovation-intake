---
title: "Foundation Repair Gate: vendored-skill provenance, repo-native factory root, pinned measurement"
type: idea-brief
status: idea
slug: foundation-repair-gate
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: foundation-repair-gate-full-chat.md
design_rationale: foundation-repair-gate-design-rationale.md
intended_repo_path: foundation-repair-gate/idea-foundation-repair-gate.md
related: [nortropic-frontier-delta]
---

# Idea brief: Foundation Repair Gate

## 1. Summary
A supply-chain/trust repair campaign elevated to durable architecture: containment →
provenance → pinning → verification → owner publication, triggered by a real
vendored-skills provenance finding. The key framing decision: measurement must be
separated from the measured — the factory is an identity-verified git checkout,
installed copies are derived and byte-verified, the verifier is read-only and itself
pinned, and "UNKNOWN_UPSTREAM must never silently equal TRUSTED". Executed live as
rounds R1–R6 (PR #102–#115 merged); the thread ends mid-R7.

## 2. Context you need
During the Digitalförvaltningen specialkompetens design, a provenance gap in vendored
skills surfaced; the owner ordered a final adversarial review of the whole vision and
its conversion into an executable closeout prompt, which became the Foundation Repair
Gate campaign run turn-by-turn from ChatGPT against Claude Code/Codex. This brief
covers only msgs 226–336 of the source conversation; the design sprint itself
(136–231), the unattended-execution model and the cockpit are separate briefs.
IMPORTANT caveat: most in-range contracts were authored by agents and relayed through
owner-role messages (20 of 27 owner turns in msgs 232–336 are pasted agent output);
only the genuine owner acts are recorded as decisions below.

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
- Provenance discipline for all vendored components: BYTE MATCH > VERSION CLAIM >
  REPOSITORY SIMILARITY; UNKNOWN_UPSTREAM never silently equals TRUSTED.
- The repo-native factory model: factory = identity-verified git checkout; installed
  copies derived and byte-verified; runtime state separated from professional
  knowledge.
- Measurement/measured separation: an external reviewed integrity manifest plus a
  read-only verifier with no update flags, the verifier itself pinned;
  engine-substitution defense (a customer repo's node_modules must never define
  Nortropic's measuring engine).
- The five-layer authority stack (OWNER POLICY → NORTROPIC CAPABILITY → HARNESS
  PERMISSION → OS CAPABILITY → EXTERNAL EFFECT; all must say yes; never bypass the
  harness's own boundary) and three distinct sandboxes.
- Tri-state verdict algebra PASS/FAIL/ODÖMBART ("tool failure is never site pass"), the
  INP truth boundary ("truth repair is preferable to a fake green"), the fixture ladder
  with FIXTURE_REGIME_CHANGE, and serialized publication windows for trust transitions.
Choose architecture, decomposition and tooling yourself, within §6's constraints.

## 4. Decisions already made (do not relitigate silently)
D1. Run a final adversarial review of the whole vision before implementation, and turn
    it into an executable closeout prompt — because "Analysera, granska, tänk kritiskt
    … innan vi går till implementation" (← msg 226; prompt commissioned ← msg 230).
D2. The Mac is the canonical factory host; the desktop machine is at most a forensic
    source — because "resan började på min stationära men nu gäller macen" (← msg 259).
D3. Legacy fixture evidence is rejected, not rescued: LEGACY_FIXTURE_RECOVERY=
    REJECTED_BY_OWNER; a new portable fixture regime replaces it — because "vi vill
    inte rädda den evidensen, den var dålig" (← msg 263).
D4. Full session restart is the sandbox-rebuild procedure — because a stale session
    cannot be trusted to rebuild its own confinement (← msg 279).
D5. Auto mode is allowed inside a bounded R-box, with the owner present at every
    publication/trust transition — because speed inside the box is safe when the
    box's exits stay human (← msg 286).

R1. Tuning new fixtures to reproduce old scores — because that manufactures continuity
    instead of measuring; the regime change is declared instead (FIXTURE_REGIME_CHANGE)
    (← msg 263; mechanism in agent arc msgs 242–243, 258–281).

## 5. Acceptance criteria (v1)
AC1. WHEN a vendored skill/component is installed or audited, THE system SHALL grade
     provenance by BYTE MATCH > VERSION CLAIM > REPOSITORY SIMILARITY and SHALL NOT
     let UNKNOWN_UPSTREAM equal TRUSTED (← msgs 226, 230, owner commission; contract
     in agent arc msgs 236–238, 285–293).
AC2. WHEN integrity is verified, THE verifier SHALL run read-only against the external
     reviewed manifest, expose no update flags, and itself be pinned (← msg 230, owner
     commission; arc msgs 251–258).
AC3. WHEN a measurement tool fails, THE verdict SHALL be ODÖMBART — never PASS
     (← msgs 226, 230, owner commission; verdict algebra in agent arc msgs 254–336).
AC4. WHEN legacy fixtures are replaced, THE system SHALL declare FIXTURE_REGIME_CHANGE
     and SHALL NOT tune new fixtures to reproduce legacy scores (← msg 263).
AC5. WHEN a publication/trust transition runs, THE owner SHALL be present and auto
     mode SHALL remain confined to the bounded R-box (← msg 286).

## 6. Constraints & implementation notes (suggestions, not orders)
Invariants: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`). Pointer only.
- Engine-substitution defense: never let the measured project's dependencies define
  the measuring engine.
- All five authority layers must consent; never bypass the harness's own boundary —
  including refusing persistent wildcard harness permissions (agent-ruled at msg 326,
  interactive approval per run; ratification is §9 Q3).
- "Truth repair is preferable to a fake green": never synthesize a metric (e.g.
  INP_PASS from a TBT proxy — banned in agent ruling msg 336; ratification §9 Q3).

## 7. Out of scope (v1)
- The Digitalförvaltningen design content itself (msgs 136–231), the
  unattended-execution model (msgs 27–135), the cockpit (msgs 118–122, 135) — separate
  briefs.
- Rescuing legacy fixture evidence (D3/R1).
- R7–R11 execution — the thread ends with R7 authorized but unexecuted.

## 8. Verification (how we know it works)
End-to-end: run the full chain on one vendored component and one fixture site —
containment → provenance grading → pin → read-only verification → owner-present
publication — producing a record (verdicts incl. at least one deliberate ODÖMBART
path, manifest hashes, PR trail) an independent reviewer can confirm from the record
alone.

## 9. Open questions (interview the owner before planning)
Q1. R7–R11, the Foundation §A6 cut, gate-green state and S1-min all remain open (the
    thread ends mid-R7, msg 336). What is the current repository truth?
Q2. Status of PR #105 (twelve ~1900-line paper drafts, ~40 open questions) —
    explicitly non-authoritative; keep, park or close?
Q3. Which relayed agent-authored contracts does the owner ratify as standing (e.g.
    BROWSER_VERIFICATION_EXECUTION capability, interactive-approval-per-run for
    browser verification (msg 326), the INP truth boundary (msg 336))?
Q4. PENDING OWNER REVIEW: the campaign re-baselined sequencing so
    FOUNDATION_REPAIR_GATE blocks S1–S5 and the old S14–S20 meta-loop numbering never
    reappears (agent arc msgs 238, 246, 251–252). This contradicts the earlier
    "do not interrupt S3→S13" position and is NOT presented as decided here — it needs
    explicit owner authorization to count as a settled re-baseline.

## 10. Process for this brief
1. Clarify: first send a subagent to read
   `foundation-repair-gate-design-rationale.md` and report what bears on §9; only if
   evidence is missing there, read the targeted message ranges via the rationale's
   retrieval map — never the whole transcript, and keep both out of main context; then
   interview the owner on §9 (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code.
3. On explicit owner approval, persist the approved plan as
   `foundation-repair-gate-approved-plan.md`, validate and bind it in the frontmatter,
   then set `status: planned`.
4. Implement in a fresh session started from the approved plan; after any compaction
   re-read the plan from disk.
5. Adversarial review: fresh subagent checks the diff against this brief and the plan.
6. Traceability: commit messages cite this brief's slug.

## References
- Source conversation: `foundation-repair-gate-full-chat.md` (same folder)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
