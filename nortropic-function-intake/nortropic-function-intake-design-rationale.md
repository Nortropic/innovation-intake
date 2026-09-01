# Design rationale: Nortropic Function Intake

Companion to `idea-nortropic-function-intake.md`. Derived independently from the
transcript `nortropic-function-intake-full-chat.md` (CONV-029 r1, 32 messages).

## 1. Core thesis
Nortropic's market edge is not tools but **transferred responsibility**: a customer
buys "this part of the company now works" rather than agents or automations
(← msg 3–5). For that promise to be honest, Nortropic needs a rigorous way to decide
*which* functions it can responsibly absorb — that deciding machinery is Function
Intake (← msg 6–10).

## 2. Problem / current state / intended outcome
Current state: Nortropic has deep machinery for making its own work trustworthy
(Kernel, verification, authority) but no method for assessing an **external**
organizational function. Intended outcome: a discovery method that takes a real
function and returns an evidence-based verdict on autonomizability, authority
boundaries and economics — before any commitment is made (← msg 7, 10).

## 3. Reasoning chain
1. Owner reframes the winning condition away from tools to whole-function
   responsibility (← msg 2).
2. Assistant maps this to outcome contracts: SLA/cost/result measurable, which makes
   "whole function" commercially stronger than "AI copilot" (← msg 4–5).
3. Owner asks for "Nortropic Intake but for an organizational function" (← msg 6) —
   the analogy carries: like Intake, it must preserve understanding with provenance,
   not produce a score.
4. Deep dive establishes the pipeline: function mapping → autonomizability →
   authority/risk → economics → lighthouse test → compile into Nortropic (← msg 7, 10).
5. External calibration: task-level model quality is largely solved (GDPval);
   long-horizon coherence (METR) and decision authority (Anthropic) are the real
   constraints — so the method must assess the *function's* shape, not the model's
   benchmark scores (← msg 9).
6. A live first case (Viktor) exists; the method should be case-shaped, not
   speculated (← msg 11–14). The form is the minimal first instrument (← msg 15–19).

## 4. Design decisions and why
- **Whole-function responsibility over tooling** — measurable outcome contracts;
  avoids competing on per-tool price; customer stops being the integrator (← msg 2–5).
- **First understand, then question existence, then classify** — a function copied
  as-is automates waste; APQC-style process frames support reconstruction before
  classification (← msg 8).
- **Case-shaped method** — the first real case (Viktor) forms the method rather than
  validating a finished one; cheaper to be wrong early (← msg 12, 14).
- **Person-neutral, reusable form** — one instrument for every future design partner
  (← msg 25–29); no server-side answer storage (← msg 22).

## 5. Explicit rejections / anti-requirements
- **"AI readiness assessment" framing** — too shallow; it grades the status quo
  instead of reconstructing the function (← msg 8). Failure if ignored: Nortropic
  automates an inefficient function faithfully.
- **Viktor as "first customer"** — rejected in favor of discovery candidate; a
  premature customer relationship would force delivery before the method exists
  (← msg 12).
- **Selling AI/agents as the product** — rejected as positioning; the product is
  responsibility for outcomes (← msg 3–5).

## 6. Explored but unresolved
- Which vertical/function becomes the first real outcome contract (← msg 3, 5 explore
  candidates near Digitala and beyond; no owner selection).
- When/whether Function Intake becomes a formal skill — msg 14 recommends waiting for
  the first case; trigger undefined.
- How Function Intake output enters the corpus/Recompile world (no decision in
  source).

## 7. Important trade-offs / tensions
- **Rigor vs speed**: the method must be deep enough to be honest about authority and
  economics, but the first instrument (a form) is deliberately shallow — the tension
  is resolved by sequencing (form → case → method) (← msg 14–16).
- **Public form vs privacy**: publication makes the empty form public; answers stay
  local to the filler's browser (← msg 22, 24). The trade was owner-approved
  (← msg 30).

## 8. Metaphor / concept → technical principle
- "Nortropic Intake fast på en organisatorisk funktion" → the same intake discipline
  (preserve understanding + provenance, fail closed on gaps) applied to a business
  function instead of a brainstorm (← msg 6–7).
- "Lighthouse test" → a concrete go/no-go verdict grounded in a real case rather than
  a maturity model (← msg 7, 10).

## 9. External evidence mentioned in the conversation
MENTIONED IN SOURCE (assistant-gathered, not independently verified here):
- APQC process classification frameworks (← msg 8).
- OpenAI GDPval — strong single-deliverable quality (← msg 9).
- METR — long-horizon task coherence as the binding constraint (← msg 9).
- Anthropic — separating task success, complexity, and decision authority (← msg 9).
- Luleå kommun/LTU signals on automation need (← msg 4).

## 10. Evolution / pivots
The conversation starts as a market radar report (← msg 1), pivots on the owner's
winning-condition statement (← msg 2), crystallizes the mechanism (← msg 6–10), and
ends in an executed first artifact: the published, generalized Function Discovery
form (← msg 15–32).

## 11. Retrieval map
- Winning condition / positioning: msg 2–5
- Mechanism definition (pipeline, anti-"readiness"): msg 6–10
- Viktor as first candidate: msg 11–14
- Form content (16 sections): msg 16
- Interactive/publication/generalization flow: msg 17–32

## 12. What to load when
- Planning the method: this rationale + brief §3–6.
- Building the case file format: msg 10 (pipeline detail) + msg 16 (form fields).
- Auditing what the owner actually decided: msg 2, 6, 11, 25, 30 (owner turns).
