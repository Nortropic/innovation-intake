---
title: "Digitalförvaltningen: domain competency layer above the Trust Kernel"
type: idea-brief
status: idea
slug: digitalforvaltningen-webb-v2
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: digitalforvaltningen-webb-v2-full-chat.md
design_rationale: digitalforvaltningen-webb-v2-design-rationale.md
intended_repo_path: digitalforvaltningen-webb-v2/idea-digitalforvaltningen-webb-v2.md
related: [nortropic-frontier-delta, bevaka-frontier-ai-engineering]
---

# Idea brief: Digitalförvaltningen — domain competency layer above the Trust Kernel

## 1. Summary
Nortropic's first domain förvaltning, designed end-to-end in one owner-driven sprint: a
generic Trust Kernel / domain-pack split where the kernel answers "who may act, which
gate" and the domain layer answers "what does excellent mean here" — starting with
websites. The single most important framing decision: universal capability instead of
profession niches — the system must build an excellent site for *any* customer, driven
by a capability graph, a Website Standard with three separate verdicts, knowledge layers
kept current, a Web Gym for self-training, a specialkompetens pipeline, and (vision-level)
autonomous digital presence toward the customer.

## 2. Context you need
Nortropic today builds websites with a niche-profiled system (tradesmen, hairdressers)
and has a trust factory (gates, frozen contracts) but no explicit domain-competency
layer defining what a *good* website is or how that competence improves. This brief
covers only msgs 136–231 (the Webbförvaltningen → Digitalförvaltningen design sprint,
roots at msgs 83–84 and 138); the thread's unattended-execution, foundation-repair and
cockpit ideas are separate briefs.

This brief is the primary intake artifact for execution. Deeper design logic lives in
the linked design rationale; the full chat is raw evidence — read targeted message
ranges only if the rationale is insufficient. Current canonical repository authority
beats all intake artifacts; within the intake package this brief wins over rationale and
transcript. Once an owner-approved plan is bound (see the frontmatter), it carries
execution order above this brief and below current repository authority.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen
gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)
- A web domain layer above the Trust Kernel: Nortropic Website Standard (Integrity hard
  gates / Experience rubric / post-launch Outcome as three separate verdicts), a Site
  Quality Contract per customer site.
- A capability graph replacing profession archetypes; connected to new-customer
  onboarding.
- Five knowledge layers with a knowledge-claim lifecycle, Knowledge Radar and garbage
  collection so knowledge stays current; an Experience Layer ("yrkeserfarenhet").
- Web Gym: synthetic practice bank of fictional companies, benchmark/hidden-holdout
  separation, trainable on a bounded owner command; cross-model workforce evolution with
  blind reciprocal judging.
- A specialkompetens (skills) recruitment/certification pipeline with
  marginal-contribution testing; Instrumentarium treating tools as first-class.
- A Reality Layer (real evidence over simulation) and — vision-level, gated — Autonomous
  Digital Presence toward customer channels, acquisition/lead evolution, and a Digital
  Department/Digital Director model.
Choose architecture, decomposition and tooling yourself, within §6's constraints.

## 4. Decisions already made (do not relitigate silently)
D1. First förvaltning is web; its foundation is defining "bra hemsida" — because the
    domain layer starts from a quality definition, not from features (← msg 136).
D2. Map Nortropic's current website-building process onto the factory model — because
    the design must upgrade the real existing flow, not a hypothetical one (← msg 139).
D3. Universal capability, not profession niche — because "jag vill kunna gör en bra
    hemsida oavsett vem som kommer till mig" (← msg 149).
D4. The capability layer connects to the new-customer onboarding flow — because quality
    starts at intake, not at delivery (← msg 152).
D5. Implementation lands via Claude Code Plan Mode prompts, iteratively — because the
    owner drives design in chat and freezes it into executable prompts (← msg 154;
    reaffirmed ← msgs 167, 178, 194, 200, 217, 224, 230).
D6. Keep both a "skolboks korrekt" best-practice base AND a distinct radical/innovative
    layer — because correctness without differentiation is not the ambition (← msg 159).
D7. Omvärldsbevakning/literature review before locking implementation, and a mechanism
    to keep that knowledge current — because the standard must rest on the field's state
    of the art, not on one brainstorm (← msgs 161, 163).
D8. Practice happens on generated fictional companies in a practice bank strictly
    separated from customer sites — because training must never touch production
    customers (← msg 169).
D9. The system trains itself when the owner gives a bounded command ("nu är det dags för
    gym") — because self-training is wanted, but on owner trigger (← msg 172).
D10. Cross-provider model composition and judging (e.g. a ChatGPT model reviewing a
    Claude model), conditioned on research support — because diversity is only wanted if
    evidence backs it (← msg 175).
D11. Skills are named "specialkompetens"; build the recruitment/certification pipeline;
    Emil Kowalski's work is the first exemplar — because external excellence should be
    recruited, tested and certified like an employee (← msgs 181, 183).
D12. Before adding more, run critical gap analysis against the goal — because the owner
    repeatedly demanded "tänk kritiskt" reviews rather than accumulation (← msgs 196,
    219, 226).
D13. Maximal autonomy is the vision, including customer-facing channels — "jag vill att
    allt ska vara så autonomt det kan bara bli, tillochmed mot kund"; explicitly adopted
    as vision: "ja, detta är min vision" (← msgs 204, 212). Gating is a §9 question.

R1. Profession-niche architecture (verticals for snickare/frisörer etc.) — because it
    caps the addressable market and duplicates competence per vertical; replaced by the
    capability graph (← msg 149).
R2. A single collapsed quality/site score — because one number hides which verdict
    failed and invites gaming; Integrity, Experience and Outcome stay separate verdicts
    — assistant-authored ban, owner-adopted when commissioning the design into Claude
    Code (← msg 217, adopting assistant msg 216; re-adopted ← msgs 226, 230 over
    assistant msg 225).
R3. Building a skills/MCP marketplace — because Nortropic recruits competence for its
    own workforce, it does not become a distribution platform — assistant-proposed
    boundary inside the specialkompetens prompt the owner commissioned (← msg 194,
    owner commission; boundary authored in assistant msg 195).

## 5. Acceptance criteria (v1)
AC1. WHEN a new customer from any industry enters onboarding, THE system SHALL derive
     the site plan from the capability graph without requiring a profession vertical
     (← msgs 149, 152).
AC2. WHEN a site candidate is evaluated, THE system SHALL report Integrity, Experience
     and Outcome as separate verdicts and SHALL NOT emit a composite score (← msg 217
     owner adoption; detail in assistant msg 216).
AC3. WHEN the owner issues the bounded gym command, THE system SHALL run Web Gym
     training only against the synthetic practice bank, never against customer sites
     (← msgs 169, 172).
AC4. WHEN a specialkompetens candidate is recruited, THE system SHALL certify it via
     marginal-contribution testing before it may serve customer work (← msgs 181, 183).
AC5. WHEN a knowledge claim informs a build decision, THE system SHALL take it from the
     maintained knowledge layers, with its currency/lifecycle state visible (← msgs 161,
     163).
AC6. WHEN any customer-facing autonomous action executes, THE system SHALL record it in
     an external action ledger with read-after-write verification and respect the
     progressive autonomy ladder (← msgs 226, 230, owner commission; design in
     assistant msg 229).

## 6. Constraints & implementation notes (suggestions, not orders)
Invariants: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`). Pointer only.
- The domain layer sits *above* the Trust Kernel; it never redefines who may act or
  which gate applies.
- Prefer evidence over simulation (Reality Layer); no fabricated metrics anywhere.
- Autonomy toward customer channels stays behind explicit gates (spend authority,
  autonomy ladder) until the owner answers §9.
- The ~2200-line architecture-freeze prompt (msg 231) is source material, not an
  approved plan; all embedded prompts in the transcript end "Do not implement yet".

## 7. Out of scope (v1)
- Other ideas from the same thread: unattended overnight execution, Foundation Repair
  Gate campaign, Verkstadsgolvet v2 cockpit, Frontier Delta reports — each its own
  brief/package.
- Profession-vertical architecture (R1), composite scores (R2), skills/MCP marketplace
  (R3).
- Organizational split of Webbförvaltningen/Digitalförvaltningen (deferred; §9 Q1).

## 8. Verification (how we know it works)
End-to-end: run one fictional company from the practice bank through onboarding →
capability graph → build → Website Standard evaluation, producing the three separate
verdicts plus the knowledge-claim citations used — evidence an independent reviewer can
confirm from the record alone, with zero writes to any customer site.

## 9. Open questions (interview the owner before planning)
Q1. Webbförvaltningen vs Digitalförvaltningen ("Nortropic Digital"): final name and
    whether/when to split organizationally (raised in msg 211, informally adopted by
    msgs 223–225, split explicitly deferred).
Q2. How does Web Gym relate to the existing gauntlet-wayfinder quality layer — same
    lab, adjacent lanes, or merged?
Q3. GYM_AUTONOMY promotion authority vs the no-self-authority principle: where exactly
    does the owner gate sit? Note: the maximal-autonomy positions behind D13 (msgs 172,
    204, 212) are flagged as possible relaxations of standing no-write/monitoring
    principles and await owner review — treat them as vision, not as settled authority.
Q4. Is the frozen architecture prompt (msg 231, 56 sections) owner-authorized as a
    whole, or must it be ratified per-section?

## 10. Process for this brief
1. Clarify: first send a subagent to read
   `digitalforvaltningen-webb-v2-design-rationale.md` and report what bears on §9; only
   if evidence is missing there, read the targeted message ranges via the rationale's
   retrieval map — never the whole transcript, and keep both out of main context; then
   interview the owner on §9 (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code.
3. On explicit owner approval, persist the approved plan as
   `digitalforvaltningen-webb-v2-approved-plan.md`, validate and bind it in the
   frontmatter, then set `status: planned`.
4. Implement in a fresh session started from the approved plan; after any compaction
   re-read the plan from disk.
5. Adversarial review: fresh subagent checks the diff against this brief and the plan.
6. Traceability: commit messages cite this brief's slug.

## References
- Source conversation: `digitalforvaltningen-webb-v2-full-chat.md` (same folder)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
