# Fullständigt transkript — Snabba upp loopar effektivt

## Metadata

- **Källa:** ChatGPT, projekt "Improvements"
- **Chattitel:** Snabba upp loopar effektivt
- **URL:** https://chatgpt.com/c/6a8042d8-9c50-83eb-a898-f5ca6f1196ca
- **Exportdatum:** 2026-08-20
- **Antal meddelanden:** 5 (1 användare / 4 assistent)
- **Fidelity:** verbatim (data-layer-capture, fail-closed-verifierad: exakt längd, JSON, balanserade kodstaket, första/sista meddelande)
- **Bilagor:** inga
- **Syfte (en rad):** Snabba upp Nortropics autopiloter/loopar dramatiskt i wall-clock-tid utan att röra frozen gates, reviewer-separation, candidate binding eller owner authority.

**Om källhänvisningsmarkörer:** Sekvenser med Unicode-tecken i privata området
(U+E200–U+E202, synliga som `cite`/`turnNNN…`) är ChatGPT:s käll-chips; de renderas
som små källänkar i UI:t och har bevarats som de är i texten.

## Innehåll i korthet

Johnny ber (med Silicon Valleys "middle-out compression" som metafor) om sätt att snabba
upp alla loopar utan att tumma på kvaliteten. ChatGPT researchar OpenAI/Codex, Anthropic,
Lovable och GitHub-loopar och landar i en "Middle-Out Loop Architecture": behåll den
seriella trust-ryggraden orörd, komprimera information in mot den (Task Capsule,
LLM-fritt kontrollplan, `nortropic inspect --json`), parallellisera säkert arbete ut från
den (read-only scout fan-out, parallell verifiering efter candidate freeze, Speculative
Build för svåra tasks), byt prosa-handoffs mot content-addressed artifacts, utnyttja Fast
mode och prompt caching, samt mät med LOOP_COMPRESSION_RATIO + EVIDENCE_EQUIVALENCE=YES.
En 9-stegs införandeordning föreslås, med varningen att harness-logik inte får bli ett
museum över tidigare modellers svagheter.

## Meddelande 1 — Johnny (användare)

Nu har vi byggt ganska stora autopiloter och loopar, och jag tänker på snabbheten. Vi tidigare pratade om Loveable, hur snabbt det går att bygga där. Och det jag tänker är, det finns en tv-serie som du kan websearcha på, som heter Silicon Valley, där de tar fram en komprimeringskod, Richard, som ger mig idéer. Och jag skulle vilja att du tänker utifrån det scenariot och komprimeringskoden där, gör att det går mycket, mycket snabbare. Så egentligen, finns det sätt, utan att tumma på kvaliteten, att snabba upp alla loopar? Vad säger best practices, codex, Antropics dokumentation? Vad finns på GitHub? Websearcha, Think hard, Iterate.

---

## Meddelande 2 — ChatGPT (assistent)

Jag tänker behandla “Silicon Valley-kompressionen” som en **arkitekturmetafor**: inte snabbare modell, utan mindre information och färre steg på den kritiska vägen. Jag jämför nu det mot OpenAI/Codex, Anthropic/Claude Code och konkreta GitHub-mönster — med målet **samma eller starkare beviskrav, lägre wall-clock-tid**.

---

## Meddelande 3 — ChatGPT (assistent)

En tydlig riktning syns redan: både OpenAI och Anthropic går mot **parallella agenter**, men Anthropic varnar samtidigt för att äldre harness-logik kan bli “dead weight” när modellerna förbättras. Det är viktigt för Nortropic: snabbaste vägen är sannolikt **inte att ta bort verifiering**, utan att flytta deterministiskt arbete ur LLM-loopen och göra bara de verkligt beroende stegen seriella.

---

## Meddelande 4 — ChatGPT (assistent)

Jag vill också skilja två sorters “snabbhet”: **modellhastighet** och **loop-hastighet**. Min preliminära slutsats är att Nortropic har mycket större hävstång i den senare — färre serialiserade agentvändor, mindre kontextkopiering och mindre väntan — än i att bara byta till en snabbare modell.

---

## Meddelande 5 — ChatGPT (assistent)

Ja. Efter att ha jämfört **Silicon Valley-idén, OpenAI/Codex, Anthropic/Claude Code, Lovable och flera aktuella GitHub-loopar** tycker jag att det finns en ganska tydlig motsvarighet till Richards “middle-out compression” för Nortropic.

Den är inte en magisk komprimeringsalgoritm. **Middle-out i *Silicon Valley* är fiktion**, även om Stanford-forskare hjälpte serien att göra den tekniskt plausibel. citeturn325154search0turn325154search9 Men som arkitekturmetafor är den mycket bra:

> **Komprimera inte bort kvalitet. Komprimera bort det arbete som ligger mellan kvalitetssäkringarna.**

Och jag tror faktiskt att det kan göra Nortropic **dramatiskt snabbare i wall-clock-tid utan att ta bort frozen gates, reviewer-separation, candidate binding eller owner authority**.

## Nortropics “middle-out”

Den nuvarande modellen har medvetet en stark trust-kedja: frozen authority → builder → immutable candidate → independent reviewer → owner final gate → push/merge. Frozen gates är authority; agentrollerna är workflow. fileciteturn0file0

**Den ryggraden skulle jag inte röra.**

Det jag skulle göra är att bygga om allt *runt omkring* ryggraden:

```text
                  READ-ONLY FAN-OUT
             ┌────────┬────────┬────────┐
             │ repo   │ tests  │ risk   │
             │ scout  │ scout  │ scout  │
             └────┬───┴───┬────┴───┬────┘
                  └───────┼────────┘
                          ▼
                 ┌─────────────────┐
FROZEN TASK ───▶ │   SINGLE WRITER │
                 │     BUILDER     │
                 └────────┬────────┘
                          ▼
              ╔═════════════════════╗
              ║ IMMUTABLE CANDIDATE ║
              ║        SHA          ║
              ╚══════════╤══════════╝
                         │
            ┌────────────┼─────────────┐
            ▼            ▼             ▼
       FROZEN GATE    INVARIANTS    REVIEWERS
       deterministic deterministic  read-only
            │            │             │
            └────────────┼─────────────┘
                         ▼
                  OWNER FINAL GATE
                         │
                         ▼
                       MERGE
```

**Det där är min version av Middle-Out Loop Architecture.**

All fri, dyr, kontexttung intelligens sker ute på kanterna. I mitten finns ett väldigt litet deterministiskt trust-objekt: **exakt task + exakt candidate SHA + exakt evidence**.

---

## Varför jag tror att detta är rätt väg

OpenAI skrev nyligen något som nästan är hela svaret på din fråga. En enda Codex-task kan innebära exempelvis **30 separata model requests**. Varje gång betalar systemet för context assembly, inference, tools och process-start. Deras slutsats är att systemprestanda därför förbättras genom att **ta bort repeated work ur loopen**, inte bara genom att göra själva modellen snabbare. citeturn342527view5

Det är precis samma tanke som din Silicon Valley-association.

Vi har hittills tänkt ungefär:

```text
hur får vi agenten att tänka bättre?
```

Nästa nivå är:

```text
hur får vi agenten att behöva tänka
så få gånger som möjligt?
```

Det är en mycket större arkitekturfråga.

### 1. Gör kontrollplanet nästan helt LLM-fritt

Det här är den största förändringen jag skulle göra.

En modell ska inte behöva resonera för att avgöra:

```text
vilken task är nästa?
vilken SHA är HEAD?
är worktree clean?
har frozen files ändrats?
vilka filer är allowed_write?
vilka gates ska köras?
vad blev exit code?
ska tasken retry?
vilken reviewer hör till candidate?
är alla prerequisites klara?
```

Det är **programlogik**.

Anthropic skiljer själva mellan deterministic workflows och agents och rekommenderar den enklaste lösningen som fungerar, eftersom agentisk komplexitet medför latency och cost. citeturn419702view4 Ett intressant community-exempel är Bernstein, som uttryckligen håller modellen helt utanför coordination loop och använder vanlig kod för scheduling, worktrees, gates och lineage. Projektet är beta och ska inte behandlas som authority, men designmönstret är relevant. citeturn990911search0

Så:

```text
NU

LLM
 ↓
shell
 ↓
LLM tolkar
 ↓
shell
 ↓
LLM tolkar
 ↓
nästa state


MIDDLE-OUT

controller.inspect(task)
 ↓
ett strukturerat resultat
 ↓
LLM endast om judgment behövs
```

Exempelvis borde en modell inte köra tio separata kommandon för candidate prestate.

Den borde få:

```json
{
  "task": "h-004",
  "base_sha": "...",
  "candidate_sha": "...",
  "worktree_clean": true,
  "allowed_write": "PASS",
  "frozen_artifacts": "UNCHANGED",
  "remote_main": "...",
  "required_gates": [...]
}
```

från **ett deterministiskt Nortropic-kommando**.

Anthropic har byggt exakt samma princip i “programmatic tool calling”: flera verktygsoperationer körs i kod, filtreras där, och bara resultatet förs tillbaka till modellen. Det reducerar både model round-trips och context. citeturn342527view4

Det här tror jag är en mycket stor Nortropic-vinst.

---

## 2. Byt enorm kontext mot en kompilerad “Task Capsule”

OpenAI säger numera uttryckligen:

> ge Codex en karta, inte en tusensidig manual.

De övergav en monolitisk `AGENTS.md` eftersom den trängde undan den faktiska uppgiften och gjorde modellen mindre fokuserad. I stället använder de en kort router till strukturerad repo-kunskap. citeturn342527view0

Anthropic säger nästan samma sak: håll den aktiva kontexten till **minsta högsignal-mängd som behövs**, behåll paths/IDs/referenser och ladda information just-in-time. citeturn342527view1turn906912view2

Jag skulle därför införa:

```text
TASK CAPSULE
```

ungefär:

```text
task_capsule.json

TASK=h-031
BASE_SHA=...
TASK_SPEC_BLOB=...
FROZEN_GATE_BLOB=...
ALLOWED_WRITE=[...]
FORBIDDEN_WRITE=[...]
RELEVANT_FILES=[...]
REQUIRED_GATES=[...]
CURRENT_FINDINGS=[...]
CANDIDATE_SHA=...
ENV_FINGERPRINT=...
```

plus referenser:

```text
CONSTITUTION → docs/07-konstitution.md#...
RULES        → docs/loop/regler.md#...
TASK         → specs/tasks.spec.json:h-031
```

Inte:

```text
här är 40 000 tokens med allt vi någonsin bestämt
```

Det är bokstavligen **context compression**.

Och den sker utan informationsförlust, eftersom originalet fortfarande finns och kan hämtas vid behov.

---

## 3. Kopiera Lovables viktigaste hastighetsarkitektur

Det här var kanske researchens mest slående fynd.

Lovable har nyligen byggt om sin agent så att flera **read-only subagenter** samtidigt kan söka kodbasen, undersöka problem och göra research. De får egna rena context windows och lämnar bara sina koncentrerade fynd tillbaka. Men **de får inte ändra koden**; huvudagenten är fortfarande writer. Lovable säger att read-only var området där de såg de största vinsterna samtidigt som de kunde behålla kontrollen. citeturn906912view5

OpenAI rekommenderar i princip samma sak för Codex: börja med parallella agenter för **exploration, tests, triage och summarization**; var mycket försiktigare med parallella writers eftersom coordination och conflicts kan äta upp vinsten. citeturn419702view0

Det passar Nortropic nästan perfekt:

```text
                 BUILDER
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
 CODE SCOUT    TEST SCOUT   RISK SCOUT
 read-only     read-only    read-only
       │           │           │
       └───────────┼───────────┘
                   ▼
              compressed
               findings
                   │
                   ▼
               BUILDER
              single writer
```

Alltså **många ögon, en penna**.

Det är både snabbare och enklare att säkra än fem agenter som samtidigt skriver i samma candidate.

---

## 4. Den stora Nortropic-vinsten: parallellisera *efter* candidate freeze

Här tror jag att vi hittills har tänkt lite för seriellt.

När candidate är fryst till:

```text
CANDIDATE_SHA=abc123...
```

har vi ett immutable objekt.

Då finns ingen anledning att göra:

```text
frozen gate
    ↓
invariants
    ↓
reviewer
    ↓
security review
    ↓
owner checks
```

om de första fyra bara **läser samma SHA**.

Vi kan göra:

```text
                abc123
                   │
       ┌───────────┼───────────┬────────────┐
       ▼           ▼           ▼            ▼
   h-031 gate   invariants   semantic     security
                            reviewer      reviewer
       │           │           │            │
       └───────────┴───────────┴────────────┘
                          │
                          ▼
                  OWNER FINAL GATE
```

Owner final gate väntar fortfarande på **alla**.

Kvalitetskravet är exakt samma.

Men wall-clock blir ungefär den långsammaste verifieringsgrenen i stället för summan av grenarna.

Codex dokumenterar uttryckligen subagent-review som ett användningsfall, exempelvis separata agenter för security, test gaps och maintainability. citeturn419702view0

Det här skulle jag göra relativt tidigt.

---

## 5. “Speculative decoding” — fast för kod

Här kommer den mest Silicon Valley-aktiga idén.

OpenAI beskriver speculative decoding som att en billigare draft-komponent arbetar fram kandidater som en starkare modell sedan verifierar, vilket reducerar mängden dyrt seriellt arbete. citeturn342527view5

Vi kan applicera samma idé **en nivå högre**.

För svåra tasks:

```text
            FROZEN TASK
                │
       ┌────────┴────────┐
       ▼                 ▼
  BUILDER A          BUILDER B
  worktree A         worktree B
       │                 │
       ▼                 ▼
 candidate A         candidate B
       │                 │
       └───── gates ─────┘
               │
               ▼
          strongest
          candidate
               │
               ▼
       independent review
```

Inte två builders som bråkar i samma repo.

Två **helt isolerade hypotheses**.

Det kostar mer compute, men för en task där builder annars riskerar:

```text
attempt
fail
repair
fail
repair
review finding
repair
...
```

kan två candidates parallellt slå seriella retries rejält.

Jag skulle kalla det:

**Speculative Build.**

Inte default. Bara när historisk data visar att en viss taskklass har hög lösningsvarians.

Quality bar ändras inte överhuvudtaget. Kandidaten måste fortfarande igenom exakt samma frozen gates och reviewer.

---

## 6. Separera “inner loop” från “trust loop”

Det här är också viktigt.

Buildern behöver snabb feedback:

```text
edit
→ targeted test
→ edit
→ targeted test
→ edit
```

Den behöver inte nödvändigtvis betala kostnaden för hela den slutliga trust-kedjan efter **varje enskild edit**.

Anthropic rekommenderar inkrementellt arbete feature-by-feature och använder en separat evaluator mot tydliga success criteria. citeturn419702view3turn906912view1

Jag skulle formalisera:

```text
FAST INNER LOOP

edit
↓
affected tests
↓
static checks
↓
targeted regression


TRUST BOUNDARY

candidate freeze
↓
FULL frozen gate
↓
FULL invariants
↓
independent review
↓
owner final gate
```

**Full gate försvinner inte.**

Vi slutar bara köra dyr global verification som om varje tangenttryckning vore en promotion candidate.

---

## 7. Context ska färdas som artifacts, inte berättelser

Ralph-communityn använder en enkel men viktig princip: varje ny agent kan börja med clean context och rekonstruerar state från Git, `progress.txt` och strukturerad task-state. citeturn990911search2

Gas Town går längre med persistent Git-backed task state och ephemeral worker sessions. citeturn990911search1

Jag skulle göra Nortropics variant betydligt striktare:

```text
builder_report.txt
```

bör egentligen inte vara primär machine-to-machine handoff.

I stället:

```text
candidate-manifest.json
evidence.jsonl
test-results.json
findings.json
candidate.sha
task-capsule.json
```

och sedan kan ett human-readable report **renderas från dessa**.

Så:

```text
machine → structured artifact → machine
```

inte:

```text
machine
  ↓
8000-token prose
  ↓
nästa machine läser prose
  ↓
försöker rekonstruera sanningen
```

Det ger både snabbhet och högre fidelity.

---

## 8. Model speed: här finns också gratis latens att hämta

Det här är den enklaste förändringen.

Codex har nu **Fast mode**, som enligt OpenAI kör stödda modeller **1,5× snabbare utan att byta till en mindre intelligent modell**. För GPT-5.6 kostar det mer credits — 2,5× Standard credit rate — men själva modellen är samma. `/fast on` aktiverar det i CLI. citeturn562426view0

För de trust-kritiska rollerna är det därför mycket mer attraktivt än att reflexmässigt nedgradera modellen.

Därefter skulle jag routa modeller, men endast efter eval:

```text
DETERMINISTIC CONTROL
    → ingen LLM

simple extraction / capsule
    → Luna

repo exploration / logs / test triage
    → Terra

difficult implementation
    → Sol

independent adversarial judgment
    → Sol high/max
```

OpenAI rekommenderar själva Luna för tydliga repetitiva uppgifter, Terra för vanligt arbete och Sol för komplexa/öppna problem; de rekommenderar också lägsta reasoning effort som faktiskt klarar uppgiften. Ultra är till för arbete som verkligen går att dela upp, och OpenAI säger uttryckligen att de flesta tasks inte behöver Max eller Ultra. citeturn419702view1

Men för Nortropic skulle modellnedväxling **alltid behöva empiriskt bevisas på våra egna replay-evals** innan den blir canonical routing.

Fast mode kräver däremot ingen sådan capability-downgrade.

---

## 9. Optimera prompt caching som om det vore CPU-cache

Det här är mer tekniskt men viktigt.

Codex konstruerar nästa model request så att den tidigare prompten är ett exakt prefix. OpenAI gör detta medvetet för prompt caching. Ändrar man tool-list, model, sandbox eller andra tidiga delar av prompten kan man förstöra cacheträffen. citeturn342527view6

OpenAI säger också att deras nuvarande harness håller model-visible history append-only och tool ordering deterministisk just för att maximera cache hits. citeturn342527view5

För Nortropic betyder det:

```text
STABLE PREFIX

role instructions
constitutional map
tool definitions
output schema

-------------------

VARIABLE SUFFIX

task capsule
candidate SHA
latest findings
```

Inte att generera en helt ny jättelik prompt i olika ordning för varje attempt.

Det är **lossless compression genom återanvändning**.

---

# GitHub-världen pekar åt samma håll

Det intressanta är inte att kopiera en specifik repo, utan att flera oberoende projekt konvergerar mot samma mönster.

Bernstein använder deterministic coordination, isolerade worktrees, gates och replayable lineage. citeturn990911search0 Ralph använder fresh contexts men persistent state utanför modellen. citeturn990911search2 Gas Town kombinerar ephemeral workers med persistent Git-backed work state och watchdogs. citeturn990911search1 Architect-loop kombinerar fresh strategist/builder agents, worktrees, deterministic checks och read-only final review. citeturn906912view4

Jag skulle **inte importera deras trust policies**. Architect-loop har exempelvis medvetet inga human approval gates och beskriver en betydligt svagare sandboxmodell än Nortropic, vilket inte matchar vår authority-design. citeturn906912view4

Men mönstret är väldigt tydligt:

> **State i kod/filesystem. Coordination deterministiskt. Agenter på de problem som kräver intelligens. Worktrees för isolation. Gates för sanning.**

---

# En viktig varning från Anthropic

Här tycker jag faktiskt Anthropic säger något Nortropic måste ta till sig.

De skriver 2026 att **agent harnesses kodar in antaganden om vad modellen inte klarar**, och att dessa antaganden kan bli föråldrade. De ger ett konkret exempel där extra context-reset-logik behövdes för en äldre Claude-modell men blev ren “dead weight” med en senare modell. citeturn906912view3

Det betyder:

**Nortropic får inte bli ett museum över tidigare modellers svagheter.**

Vi behöver behålla:

```text
security properties
authority boundaries
evidence requirements
frozen acceptance
independent falsification
```

men regelbundet fråga:

```text
behöver vi fortfarande denna LLM-fas?

eller

var det en workaround för en modell
som inte längre behöver workarounden?
```

Det är en viktig distinktion.

**Security invariant ≠ harness ritual.**

---

# Så här skulle jag faktiskt bygga nästa generation

Jag skulle göra det i den här ordningen:

1. **Mät först utan beteendeförändring.** Lägg timestamps på task-ready, agent-start, first-tool, last-edit, test-start/end, freeze, reviewer-start/end, final-gate och merge. Logga dessutom antal model turns, tool calls, process starts och ungefärlig contextstorlek. OpenAI pekar specifikt ut repeated model/tool iterations som multiplikatorn som måste reduceras. citeturn342527view5
2. **Bygg `nortropic task-capsule` och `nortropic inspect --json`.** En deterministic compiler från canonical authority till den minimala input varje agent behöver.
3. **Flytta all coordination som inte kräver judgment ur modellerna.** Scheduler, routing, retries, SHA-binding, allowed-write, frozen hashes, state transition och exit classification ska vara controllerkod.
4. **Inför read-only discovery fan-out.** Flera lätta scouts, en writer — exakt det Lovable och Codex nu rekommenderar. citeturn906912view5turn419702view0
5. **Parallellisera all verification efter immutable candidate freeze.** Frozen gate, invariants och olika read-only review-lanes får arbeta samtidigt; owner final gate konvergerar resultaten.
6. **Byt prose-handoffs mot content-addressed artifacts.** JSON/JSONL + SHA blir primärt; human reports renderas ovanpå.
7. **Aktivera Fast mode på de dyra kritiska Codex-rollerna** där creditkostnaden är acceptabel. Det är den enklaste rena latencyvinsten. citeturn562426view0
8. **Eval-gata model routing.** Lägre modell/effort för scouts och mekaniska jobb först när historiska Nortropic-tasks visar samma utfall på våra verkliga gates.
9. **Experimentera sist med Speculative Build.** Två isolerade implementationshypoteser parallellt endast för taskklasser där seriell remediation historiskt är dyr.

---

# Och jag skulle skapa vårt eget “Weissman score”

Inte som en skämt-metric som avgör kvalitet, utan som performance telemetry.

Till exempel:

```text
LOOP_COMPRESSION_RATIO
=
baseline critical-path model round-trips
/
new critical-path model round-trips
```

med ett separat absolut krav:

```text
EVIDENCE_EQUIVALENCE=YES

same frozen gates
same candidate binding
same allowed_write proof
same reviewer requirement
same owner final authority
```

Om:

```text
round trips ↓
wall clock ↓
```

men:

```text
EVIDENCE_EQUIVALENCE=YES
```

har vi lyckats.

Det gör att vi **aldrig behöver säga “det känns snabbare och verkar lika bra”**.

Vi mäter det.

---

# Min slutsats

Jag tror inte nästa stora Nortropic-genombrott är **ännu en smartare agent**.

Jag tror det är att göra Nortropic till ett slags **agent-kompilator/runtime**:

```text
                INTENT
                  │
                  ▼
        deterministic compiler
                  │
             TASK CAPSULE
                  │
        ┌─────────┼─────────┐
        │         │         │
      scouts    scouts    scouts
        └─────────┼─────────┘
                  ▼
              ONE WRITER
                  │
                  ▼
          IMMUTABLE CANDIDATE
                  │
        ┌─────────┼─────────┐
        │         │         │
      gate      gate      review
        └─────────┼─────────┘
                  ▼
            TRUST CONVERGENCE
                  │
                  ▼
                MERGE
```

**Lovable-snabbheten och Nortropic-kvaliteten behöver alltså inte vara motsatser.**

Lovable visar redan att **parallell read-only discovery + single writer** är en effektiv väg till snabbare builds. citeturn906912view5 OpenAI visar att repeated model calls, context bloat, process overhead och dålig caching är centrala latencykostnader. citeturn342527view5turn342527view6 Anthropic visar att context bör hämtas just-in-time och att deterministic program logic bör ersätta onödiga model round-trips. citeturn342527view1turn342527view4

Så min **Pied Piper-idé för Nortropic** är:

> **Behåll den lilla seriella trust-ryggraden orörd. Komprimera all information in mot den. Parallellisera allt säkert arbete ut från den. Och betala bara frontier-model reasoning där maskinell kod inte kan avgöra svaret.**

Det är den arkitekturriktning jag skulle ta innan vi gör autopiloterna ännu större.
