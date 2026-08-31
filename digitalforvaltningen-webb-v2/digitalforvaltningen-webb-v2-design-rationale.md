---
title: "Digitalförvaltningen: domain competency layer above the Trust Kernel — design rationale"
type: design-rationale
status: source-derived
slug: digitalforvaltningen-webb-v2
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: digitalforvaltningen-webb-v2-full-chat.md
execution_brief: idea-digitalforvaltningen-webb-v2.md
authority: non-authoritative-rationale
fidelity: full
context_revision: 1
---

# Design rationale: Digitalförvaltningen

## 1. Core thesis
The trust factory answers "who may act and through which gate", but nothing in
Nortropic answers "what does excellent mean in this domain". The sprint's central
conceptual model is a two-layer split: a generic Trust Kernel plus per-domain
competency packs, with web as the first förvaltning — and the domain pack is founded on
a quality *definition* ("vad är en bra hemsida, vad betyder bra", ← msg 136), not on a
feature list. Everything else (Standard, Gym, knowledge layers, specialkompetens) exists
to make that definition operational, current, and self-improving (← msgs 136–231).

## 2. Problem / current state / intended outcome
Current state: Nortropic's website system is niched toward tradesman-type professions
(← msg 149) and its build process predates the factory model (← msg 139). The owner's
intended outcome, stated and re-stated: serve any customer excellently (← msg 149), tie
capability assessment into new-customer onboarding (← msg 152), rest on both schoolbook
best practice and a radical/innovative layer (← msg 159), stay current through
omvärldsbevakning (← msgs 161, 163), and run as autonomously as possible — ultimately
even toward the customer (← msgs 204, 212). OWNER DECISION: "ja, detta är min vision"
(← msg 212).

## 3. Reasoning chain
- Defining "bra hemsida" (← msg 136) led to the Nortropic Website Standard with three
  separate verdicts, because a quality definition that collapses integrity, experience
  and business outcome into one number cannot drive gates (assistant design ← msgs 138,
  140–148; adopted into prompts the owner commissioned ← msgs 154, 167).
- Mapping the current build flow onto the factory (← msg 139) exposed the niche
  limitation; the owner's universality requirement (← msg 149) killed profession
  archetypes and made a capability graph necessary — capabilities compose per customer
  instead of being duplicated per vertical (← msgs 149–153).
- Universality raised "where does the knowledge come from?": the owner ordered a
  literature/omvärldsbevakning pass before locking anything (← msg 161) and a currency
  mechanism (← msg 163), which produced the five knowledge layers, knowledge-claim
  lifecycle, Knowledge Radar and garbage collection (assistant design ← msgs 162–168).
- Knowledge without practice is inert, so the owner introduced a synthetic practice
  bank of fictional companies, separated from customer sites (← msg 169); this became
  Web Gym with practice/benchmark/hidden-holdout separation, and the owner's bounded
  self-training command ("nu är det dags för gym", ← msg 172) became GYM_AUTONOMY
  (assistant design ← msgs 170–174, 179).
- Gym results need judges; the owner proposed cross-provider composition/judging
  conditioned on research support (← msg 175), yielding cross-model workforce evolution
  with blind reciprocal judging (← msgs 176–179).
- External excellence became "specialkompetens": recruit, test marginal contribution,
  certify (owner naming ← msg 181; Emil Kowalski exemplar ← msg 183; pipeline design
  incl. a real vendored-skills provenance finding ← msgs 184–195).
- The owner's repeated "tänk kritiskt" gap analyses (← msgs 196, 219, 226) drove three
  expansions: Instrumentarium + Reality Layer (← msgs 197–201), Autonomous Digital
  Presence with Customer Truth Graph / Customer Authority Matrix / bounded spend
  authority (← msgs 202–218), and the Digital Department/Digital Director with four
  truths and measurement science (← msgs 219–225).
- A final adversarial review found nine OS-layer gaps (External Action Ledger with
  read-after-write verification, progressive autonomy ladder OBSERVE→SHADOW→
  BOUNDED_AUTO, AI identity states, tenant isolation) (assistant ← msg 229, commissioned
  ← msg 226), closed by the ~2200-line architecture-freeze prompt (← msgs 230–231).

## 4. Design decisions and why
D3 (universal capability). Why: the niche caps who Nortropic can serve; the owner wants
    any customer. Evidence: "nu är systemet nischad mot snickare … men jag vill kunna
    gör en bra hemsida oavsett vem som kommer till mig". Source: (← msg 149).
D6 (schoolbook base + radical layer). Why: correctness alone is commodity; the radical
    layer is the differentiation, but it must sit on a provably correct base. Evidence:
    owner's explicit two-part requirement. Source: (← msg 159).
D8/D9 (practice bank + bounded self-training). Why: improvement requires reps, but reps
    on customer property is unacceptable risk; the owner wants training to be a
    one-command act. Evidence: (← msgs 169, 172).
D13 (maximal autonomy vision). Why: the owner's endgame is a digital department that
    operates channels itself (Search Console API exists already; Meta/Google Ads opt-in
    at onboarding). Evidence: (← msgs 204, 212). ASSISTANT INFERENCE kept visible: all
    concrete autonomy designs keep spend/authority gates; the owner never rescinded the
    gate principle inside this range.

## 5. Explicit rejections / anti-requirements
REJECTED: Profession-niche verticals as architecture.
WHY: caps the market; duplicates competence per vertical.
FAILURE IT WOULD CREATE: every new customer type becomes a build project; competence
fragments and staleness multiplies per vertical.
SOURCE: (← msg 149).

REJECTED: One collapsed quality/site/digital score.
WHY: hides which verdict failed; invites optimizing the number instead of the site.
FAILURE IT WOULD CREATE: a "92/100" site that fails an integrity hard gate ships anyway;
gates lose meaning. ASSISTANT PROPOSAL adopted through owner-commissioned prompts.
SOURCE: (← msgs 216–217, 225–226, 230).

REJECTED: Skills/MCP marketplace.
WHY: Nortropic recruits competence for its own factory; distribution is a different
business with different trust obligations.
FAILURE IT WOULD CREATE: platform/marketplace obligations (curation, third-party trust)
without owner intent. ASSISTANT PROPOSAL (boundary), owner-commissioned. SOURCE:
(← msgs 194–195).

## 6. Explored but unresolved
- Naming/split: Webbförvaltningen vs "Nortropic Digital"/Digitalförvaltningen — raised
  (← msg 211), informally adopted in later prompts (← msgs 223–225), organizational
  split explicitly deferred. Resolution: owner naming decision.
- Web Gym vs gauntlet-wayfinder: same lab, adjacent lanes, or merged — unresolved
  (← msgs 170–179 vs existing package; mirrors frontier-delta Q5).
- GYM_AUTONOMY promotion authority vs no-self-authority: where the owner gate sits
  (← msgs 172, 174, 179). PENDING OWNER REVIEW: msgs 172/204/212 are flagged as possible
  relaxations of standing no-write principles; not settled here.
- Whether msg 231's 56-section freeze prompt is authorized as a whole or per-section.

## 7. Important trade-offs / tensions
- Autonomy vs authority: "så autonomt det kan bara bli, tillochmed mot kund" (← msg 204)
  vs every adopted design keeping spend/authority gates (← msgs 216, 229, 231).
- Correct vs radical: schoolbook base vs innovative layer (← msg 159).
- Simulation vs reality: practice bank realism vs the Reality Layer's "real evidence
  over simulation", including "should we build a website at all" (← msgs 169, 199–201).
- Accumulation vs criticality: expansion appetite vs the owner's repeated demand to
  find gaps before adding (← msgs 196, 219, 226).

## 8. Metaphor / concept → technical principle
- Förvaltning (municipal department) → domain competency pack above a shared kernel →
  do NOT copy: municipal bureaucracy/hierarchy as process (← msgs 136, 139).
- Gym → separated practice/benchmark/holdout environments with promotion rules → do NOT
  copy: training on production ("customer sites") (← msgs 169–174).
- Specialkompetens/recruitment → certification pipeline with marginal-contribution
  testing → do NOT copy: treating vendored code as an employee with standing authority
  (← msgs 181–195).
- Digital Department/Director → measurement-science role with four truths → do NOT
  copy: a human org chart (← msgs 219–225).

## 9. External evidence mentioned in the conversation
All MENTIONED IN SOURCE, none independently verified: Emil Kowalski's work as
specialkompetens exemplar (← msg 183); OpenAI/Anthropic best practices and
kurslitteratur as review inputs (← msgs 161, 226); Google Search Console API (owner
already holds one), Meta/Google Ads channels (← msg 204); vendored-skills provenance
finding surfaced during the specialkompetens design (← msgs 184–195).

## 10. Evolution / pivots
- Niche system → universal capability graph (← msgs 139 → 149–153).
- "Bra hemsida" definition → three-verdict Website Standard (← msgs 136 → 138–148).
- One-off literature pass → living knowledge layers with lifecycle/radar (← msgs
  161 → 163–168).
- Webbförvaltningen → Digitalförvaltningen framing as scope grew from sites to digital
  presence (← msgs 202–225); split deferred.
- Design sprint → adversarial nine-gap critique → architecture-freeze prompt (← msgs
  226 → 229 → 231).

## 11. Retrieval map
| topic | message range |
|---|---|
| "bra hemsida" commission; Website Standard, three verdicts | 136–148 |
| de-niching; capability graph; onboarding link | 149–153 |
| Plan Mode prompt cadence | 154–158, 167, 178, 194, 200, 217, 224, 230 |
| schoolbook + radical layer | 159–160, 168 |
| knowledge layers, lifecycle, radar, currency | 161–168 |
| practice bank; Web Gym; GYM_AUTONOMY | 169–174, 179 |
| cross-model evolution, blind judging | 175–179 |
| specialkompetens pipeline; Emil Kowalski; provenance finding | 181–195 |
| gap analysis #1; Instrumentarium; Reality Layer | 196–201 |
| autonomous digital presence; Customer Truth Graph; leads | 202–218 |
| Digital Department / Director; four truths | 219–225 |
| adversarial nine-gap review; freeze prompt | 226–231 |
| roots: workforce competency; Website Standard seed | 83–84, 138 |

## 12. What to load when
DEFAULT IMPLEMENTATION: read `idea-digitalforvaltningen-webb-v2.md`.
IF DESIGN RATIONALE IS NEEDED: read this file.
IF EXACT SOURCE EVIDENCE IS NEEDED: read only the relevant message ranges in
`digitalforvaltningen-webb-v2-full-chat.md` (use §11).
Do not preload the raw transcript into the main implementing context.
