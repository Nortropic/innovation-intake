# Fullständigt transkript — Bevaka Frontier AI Engineering

## Metadata

- **Källa:** ChatGPT, projekt "Improvements"
- **Chattitel:** Bevaka Frontier AI Engineering
- **URL:** https://chatgpt.com/c/6a854358-92f8-83ed-bc44-a44df74f99f1
- **Exportdatum:** 2026-08-20
- **Antal meddelanden:** 19 (4 användare / 15 assistent)
- **Fidelity:** verbatim (data-layer-capture; SHA256-verifierade chunkar ur persisterad verktygsutdata; fail-closed-verifierad)
- **Bilagor:** inga
- **Syfte (en rad):** Jämföra Nortropics arbetssätt mot frontier-labbens, aktivera daglig bevakning, och eskalera bevakningsidén till ett fullt "Nortropic Frontier Observatory" (yttre nervsystem med Sensor Mesh + självexpanderande People Radar).

**Särskild form:** Chatten aktiverar ännu en DAGLIG bevakningsautomation ("Bevaka
Frontier AI Engineering", msg 6) — senare rapporter appendas i källchatten (msg 19 är
en sådan). Snapshot per exportdatumet.

**Om källhänvisningsmarkörer:** Sekvenser med Unicode-tecken i privata området
(U+E200–U+E202, synliga som `cite`/`filecite`/`turn…`) är ChatGPT:s käll-chips; de har
bevarats som de är i texten.

## Innehåll i korthet

Johnny ber om en ärlig jämförelse: hans arbetssätt kontra OpenAI/Anthropic. Analysen
(mot faktiska repot): trust/verifiering 🟢 extremt starkt, agentroller/provider-
neutralitet/repo-as-truth 🟢, dokumentation 🟡 (stark men tung), verifiering 🟡
(deterministiskt stark, eval-obalanserad), orkestrering 🟡 (issue-tracker-som-
kontrollplan är nästa möjlighet), agent observability 🔴, produktfeedback 🔴,
engineering metrics 🔴. En daglig bevakning aktiveras (msg 6). Därefter Jake Van
Clief-spåret (ICM-paper) → idén att systematiskt hitta "nästa Van Clief" → Johnny:
"Vi tar alltid fulla steg, next level" → målbilden Nortropic Frontier Observatory:
tre system (Observatory = perception/vetenskapligt lärande; Engineering OS; Trust
Kernel), eget repo frontier-observatory som producerar evidens → knowledge →
innovation-intake → nortropic-system via befintlig authority; Sensor Mesh över labs/
människor/arXiv/OpenAlex/GH Archive/communities/Nortropic självt; självexpanderande
People Radar via citations-/forkgrafer. Principlås: Observatory blir aldrig trust
authority och ska inte vara en separat "research-agent" vid sidan av systemet.
Msg 19 är en daglig delta-rapport (bl.a. ADOPT-signal om event-driven coordination).

## Meddelande 1 — Johnny (användare)

Jag arbetar med min egna AI infrastruktur (Nortropic) och vill arbeta som de gör i silicon valley, openai, anthropic, bevaka utveckling, optimala workflows, hur ser det ut det jag gör idag kontra hur de arbetar? Jag tänker om man ser till hur en AI utvecklare arbetar på dessa professionella företag, dokumentation, workflow, github med mera. Hur arbetar jag kontra de? 

Brainstorma och kom med input vilka områden som är bra, vilka jag saknar och helt enkelt hur jag kan bli bättre.

---

## Meddelande 2 — ChatGPT (assistent)

Jag tänker jämföra **Nortropic som det faktiskt ser ut i ditt nuvarande arbetssätt** mot det som går att belägga offentligt hos OpenAI, Anthropic och andra starka AI-engineeringmiljöer — inte mot en romantiserad “Silicon Valley”-bild. Jag kommer särskilt leta efter skillnaden mellan att ha bra agenter och att ha ett **professionellt AI-engineering operating system**: idé → specifikation → kod → evals → review → deploy → observability → lärande.

---

## Meddelande 3 — ChatGPT (assistent)

En första tydlig observation redan nu: du ligger **ovanligt långt fram på trust/verification-sidan**. Nortropic har frysta exit-gates, rollseparation, `allowed_write`, provider-neutral Trust Kernel, evidenskontrakt och uttrycklig fail-closed-logik — det är mer rigoröst än ett normalt litet utvecklingsteam och ligger nära samma problemklass som OpenAI/Anthropic beskriver för autonoma agenter. 

Men frontlinjelabben verkar lägga betydligt mer vikt än du gör idag på en annan axel: **repo-legibility + eval-driven product development + observability + hög genomströmning**. Där misstänker jag att Nortropic har byggt mer “kontrollplan” än “lärande- och produktplan”. Jag verifierar den hypotesen mot både ditt repo och deras senaste engineering-material.

---

## Meddelande 4 — ChatGPT (assistent)

Det andra tydliga fyndet är nästan motsatsen till det första: **du har mycket bra “safety capital”, men du spenderar för mycket mänsklig uppmärksamhet på själva transporten av arbete.** OpenAI beskriver exakt samma fasproblem: när ingenjören sitter och följer 3–5 agent-sessioner blir människan flaskhalsen; deras nästa steg blev att låta task-boardet vara kontrollplanet och låta agenter plocka upp arbetet själva. 

Nortropic är alltså inte “amatörmässigt jämfört med Silicon Valley”. Snarare har du byggt vissa frontier-principer tidigt, men **obalanserat**: mycket verifierings- och authority-engineering, mindre produkttelemetri, eval-hillclimbing, issue-driven orchestration och mätning av faktisk leveransförmåga.

---

## Meddelande 5 — ChatGPT (assistent)

Ja. Jag har nu jämfört det faktiska Nortropic-repot med det OpenAI och Anthropic offentligt beskriver under 2026. Min huvudslutsats är:

> **Nortropic är redan betydligt närmare en intern AI-engineeringplattform än ett vanligt “jag använder Claude Code”-upplägg. Men du har optimerat mycket hårdare för trust, verifiering och autonom säkerhet än för throughput, observability, produktfeedback och kontinuerligt lärande.**

Det är alltså inte främst fler agenter eller ännu en autonom loop du saknar. Nästa steg är att göra **hela engineering-systemet** lika välbyggt som din Trust Kernel.

## Hur frontier-arbetssättet faktiskt ser ut

OpenAI beskriver en ganska fundamental förändring av utvecklarrollen: människan skriver i mindre grad kod och arbetar i högre grad med **miljö, intent, specification, acceptance criteria och feedback loops**. I deras Codex-first-experiment byggdes även tester, CI, dokumentation, observability och interna verktyg av agenter. Det viktiga var inte “AI skriver kod”, utan att människorna byggde ett system där agenten själv kunde förstå, genomföra, testa och korrigera arbete. citeturn851310view0

De har också gjort repot till agentens verkliga värld. `AGENTS.md` är en kort karta snarare än en encyklopedi; djupare kunskap ligger strukturerat i repo-lokala design docs, product specs, execution plans, quality, reliability och security. Dokumentationen freshness-kontrolleras mekaniskt och en återkommande agent städar gammal dokumentation. citeturn851310view0

Anthropic kommer fram till nästan samma arkitektur från ett annat håll. De betonar strukturerade artefakter mellan kontextfönster, planner/generator/evaluator-separation och eval-driven development. Samtidigt varnar de uttryckligen för att harness-logik kodar antaganden om modellernas begränsningar som snabbt kan bli gamla när modeller förbättras. citeturn634333view9turn634333view6turn415463view3

Det är väldigt nära flera av de idéer du redan byggt.

---

## Nortropic kontra ett frontier AI-team

| Område | Nortropic idag | OpenAI/Anthropic-mönstret | Min bedömning |
|---|---|---|---|
| **Trust / authority** | Frozen gates, `allowed_write`, candidate identity, attestering, rollseparation, fail-closed, provider-neutral Trust Kernel. fileciteturn7file0L1-L2 | Bounded execution, sandbox, riskstyrda approvals, telemetry. citeturn415463view4 | 🟢 **Extremt starkt** |
| **Agentroller** | Test-author, builder, reviewer, architect, autopilot etc. fileciteturn7file0L1-L2 | Planner/generator/evaluator och specialiserade roller när de ger mätbar lift. citeturn634333view7turn634333view8 | 🟢 Stark |
| **Provider-neutralitet** | Reasoning hos Claude/Codex, trust transitions hos Nortropic. fileciteturn7file0L1-L2 | Anthropic separerar session, harness och sandbox bakom stabila gränssnitt. citeturn415463view3 | 🟢 **Frontier-aligned** |
| **Repo som source of truth** | Ja, explicit. Kunskapsrepo separat från execution authority. fileciteturn6file0L1-L2 fileciteturn10file0L1-L2 | Repo-local knowledge är centralt. citeturn851310view0 | 🟢 Stark |
| **Dokumentation** | Mycket omfattande, två lager, regler, scope, constitution, decision log. fileciteturn15file0L1-L2 | Kort karta + små specialiserade docs + automatiserad freshness. citeturn851310view0 | 🟡 Stark men börjar bli tung |
| **Verifiering** | Mycket stark deterministic verification. | Capability-evals + regression-evals + graders + produktkvalitet. citeturn634333view4turn634333view5 | 🟡 Obalanserad |
| **Orkestrering** | Egen autonom kontrollplan/autopilot. | Issue tracker blir kontrollplanet; agentworkspace per task. citeturn634333view1turn634333view3 | 🟡 Nästa stora möjlighet |
| **Agent observability** | Jag ser inte motsvarande full stack tydligt i den struktur jag inspekterade. | Agenten ser UI, DOM, screenshots, logs, metrics och traces själv. citeturn851310view0 | 🔴 Viktigt gap |
| **Produktfeedback** | Systemet verifierar framför allt att processen och artefakten är korrekt. | User feedback översätts till acceptance criteria och därefter verktyg/regler/evals. citeturn851310view0 | 🔴 Bör stärkas |
| **Engineering metrics** | Inte ett framträdande lager i det jag inspekterade. | Delivery throughput och instability mäts systematiskt. citeturn415463view0 | 🔴 Gap |
| **Research/intelligence** | Knowledge + innovation intake finns, men intake-repots README är ännu tom. fileciteturn11file0L1-L2 | Kontinuerlig teknisk omvärldsbevakning + experiments. | 🟡 Fundament finns |
| **Harness-minimering** | V4 går redan åt rätt håll. | Ta bort scaffolding när modellen inte längre behöver den. citeturn415463view3 | 🟢 riktning, 🟡 utförande |

Det intressanta är alltså att **du är före många team på de svåra säkerhets- och authority-problemen**, men efter frontier-mönstret på några mer vardagliga engineeringdiscipliner.

---

# Den största förändringen jag skulle göra

Jag skulle börja tänka på Nortropic som ett **Engineering Operating System**, inte primärt som en agentfabrik.

Din nuvarande kärna är ungefär:

```text
Task
  ↓
Specification
  ↓
Frozen verification
  ↓
Builder
  ↓
Reviewer
  ↓
Trust transition
```

Den professionella helheten bör snarare vara:

```text
WORLD / USERS / RESEARCH
          ↓
       SIGNAL
          ↓
  INNOVATION INTAKE
          ↓
   RFC / PRODUCT SPEC
          ↓
 SUCCESS CRITERIA + EVALS
          ↓
      ISSUE / DAG
          ↓
   AGENT WORKSPACE
          ↓
 IMPLEMENT → TEST → REVIEW
          ↓
    GUARDED MERGE
          ↓
       DEPLOY
          ↓
 UI + LOGS + METRICS + TRACES
          ↓
 PRODUCT / USER OUTCOME
          ↓
      LEARNING
          ↓
 docs / eval / invariant / skill
          ↓
       SYSTEM ↑
```

**Det är den sista halvan som jag tycker Nortropic behöver bygga ut nu.**

## Mina åtta högst prioriterade förbättringar

1. **Gör issue trackern till det verkliga kontrollplanet.** OpenAI Symphony är särskilt relevant för Nortropic. De gick från att människor hanterade flera Codex-sessioner till att varje aktiv issue får en egen workspace och agent; ticket-statusen fungerar som state machine. OpenAI rapporterar att vissa team fick omkring 500 % fler landade PR:er under de första veckorna. citeturn634333view1turn634333view2 För dig innebär det att **tasken ska leva längre än Claude/Codex-sessionen**. En feature är ett objekt med state, dependencies, spec, evals och resultat; agenter kommer och går runt den.

2. **Dela upp “verification” i flera helt olika eval-lager.** Ditt frozen-gate-system är utmärkt för “får detta ske?” och “är kontraktet uppfyllt?”. Men Anthropic skiljer mellan capability evals, som medvetet ska vara svåra och ge en kulle att bestiga, och regression evals som bör ligga nära 100 %. citeturn634333view4turn634333view5 Nortropic behöver därför åtminstone `Trust/Policy → Regression → Capability/Quality → Product outcome`. Exempelvis ska en ny designagent inte bara PASS:a tekniska krav; den ska kunna gå från 62 → 71 → 79 på en kalibrerad designrubrik.

3. **Bygg agent-legible observability.** Det här tror jag kan bli en enorm hävstång. OpenAI låter Codex starta en isolerad app per worktree och själv se DOM, navigera UI, ta screenshots och läsa logs, metrics och traces. citeturn851310view0 Din agent bör kunna säga: “Jag implementerade detta, startade sajten, körde de fem journeysen, såg layouten, läste console/server logs, jämförde metrics och verifierade resultatet” — utan att du tittar först. Då försvinner mycket av behovet av mänsklig mellanhand.

4. **Komprimera dokumentationen i stället för att utöka den.** Du har redan rätt princip: `AGENTS.md` är router och deeper authority ligger annorstädes. fileciteturn7file0L1-L2 Men `docs/05-beslutslogg.md` är nu över 400 kB. fileciteturn15file0L1-L2 Jag skulle gå mot individuella ADR:er med index, `active/completed` exec plans, tech-debt tracker och separata `PRODUCT`, `QUALITY`, `RELIABILITY`, `SECURITY`-kartor. Därefter en **doc-gardener** som hittar motsägelser, stale SHAs, döda länkar och dokument som inte längre beskriver implementationen. Det är mycket nära OpenAI:s modell. citeturn851310view0

5. **Inför riskbaserad snabbfil.** Din stora risk framåt är att fail-closed-principen sprider sig till saker där kostnaden av verifieringen är större än blast radius. OpenAI:s uttalade modell är bounded execution där rutinmässigt låg-riskarbete ska vara friktionsfritt medan högre risk stoppar för review. citeturn415463view4 Jag skulle behålla Nortropics extrema rigor för credentials, trust authority, production, security, irreversible state och juridik — men låta reversibla dokumentationsfixar, tester, refactors och lokala experiments flyga snabbare. **En 20-raders README-fix ska inte behöva samma ceremoni som ett authority-byte.**

6. **Mät Nortropic som ett produktionssystem.** DORA använder idag fem delivery-mått: change lead time, deployment frequency, failed-deployment recovery time, change fail rate och deployment rework rate. citeturn415463view0 Lägg ovanpå det agentmått som faktiskt är viktiga för Nortropic: mänskliga minuter per task, agentkostnad per accepterad task, antal retries, procent tasks utan mänsklig intervention, tid BLOCKED, eval-delta per förändring och hur ofta reviewer hittar något buildern missade. Då kan du veta om en ny loop **faktiskt gör Nortropic bättre**, i stället för att bara känna det.

7. **Ablation-testa själva harnesset.** Detta tycker jag är särskilt viktigt. Anthropic beskriver uttryckligen hur en kontext-reset som behövdes för Sonnet 4.5 blev rent “dead weight” när Opus 4.5 klarade beteendet själv. citeturn415463view3 Gör därför regelbundet experimentet: *“Vad händer om vi tar bort reviewer? Vad händer utan planner? Vad händer utan denna retry-loop? Vad händer om Claude får lösa hela problemet?”* Behåll endast lager som visar mätbar kvalitets-, kostnads- eller säkerhetsvinst. **Harness debt kommer bli en verklig typ av technical debt.**

8. **Formaliserad Frontier Delta istället för sporadisk AI-news.** Officiella källor är redan maskinläsbara: OpenAI har release notes med Codex/API-filter och RSS, och Claude Code har en detaljerad löpande changelog. citeturn415463view1turn415463view2 Jag skulle ha automatisk daglig ingestion men bara en kondenserad review till dig. Varje förändring klassificeras exempelvis som `IGNORE / WATCH / EXPERIMENT / ADOPT`, och den centrala frågan är: **“Vilket antagande i Nortropic blir nu falskt?”** Om Claude plötsligt kan göra något som du byggt 1 500 rader harness för, skapas ett ablation-experiment — inte ännu ett dokument.

---

## En sak jag särskilt skulle ändra i hur *du* arbetar

Frontier AI-utvecklaren håller på att flytta upp en abstraktionsnivå.

Inte:

```text
Jag → ChatGPT → prompt → Claude Code → output
       ↑                         ↓
       └──── jag koordinerar ───┘
```

utan:

```text
Jag
 ↓
mål + prioritet + quality bar
 ↓
Nortropic Engineering OS
 ↓
tasks / agents / experiments / reviewers
 ↓
evidence + outcomes + exceptions
 ↑
Jag
```

Din roll blir alltså mer **Principal Engineer + Product Owner + AI Systems Architect** än “personen som kör Claude Code”.

OpenAI beskriver exakt denna förändring: människorna prioriterar arbete, översätter användarfeedback till acceptance criteria och validerar outcomes; när agenten misslyckas behandlas det som information om vilken capability, guardrail eller feedback-loop som saknas. citeturn851310view0

Det är en ganska viktig mental modell för Nortropic.

---

## Något jag *inte* tycker att du ska kopiera

Jag skulle inte kopiera OpenAI:s “0 manuellt skriven kod” som ideologi. Det var ett medvetet experiment för att tvinga fram agentvänlig infrastruktur. citeturn851310view0

Jag skulle heller inte kopiera deras minimala merge-gates rakt av. Deras argument är att extrem throughput gör korrigering billig och väntan dyr. citeturn851310view0 Det är sant för många produktändringar, men inte automatiskt för Nortropics trust authority.

Och jag skulle absolut inte skapa fler roller bara för att Anthropic har planner/evaluator eller OpenAI har fler agenttyper. Anthropic fann själva att evaluatorn kunde bli onödig overhead när den underliggande modellen blev bättre. citeturn634333view8

**Kopiera principerna, inte organisationsdiagrammet.**

---

# Min övergripande diagnos

Om jag delar Nortropic i två halvor ser jag ungefär:

**Control & Trust Plane:** mycket avancerat.

```text
authority
identity
containment
frozen gates
role separation
attestation
promotion
recovery
provider neutrality
```

**Engineering & Learning Plane:** mycket mer att vinna.

```text
product sense
capability evals
issue orchestration
agent observability
production telemetry
delivery metrics
user feedback
experimentation
frontier research
automatic knowledge gardening
harness ablation
```

Det betyder något positivt för riktningen:

### Jag skulle inte lägga nästa stora utvecklingsperiod på att bygga ännu en autonom agent-loop.

Jag skulle lägga den på **Nortropic Engineering OS** ovanpå det du redan har.

De tre första sakerna jag skulle bygga är:

**Issue Control Plane → Eval Stack → Agent Observability.**

När de tre sitter börjar nästan allt annat förstärka varandra. Ett forskningsfynd kan bli ett experiment. Experimentet får en issue. En agent bygger. Evalsen mäter om det faktiskt blev bättre. Observability visar verkligt beteende. Ett lyckat experiment blir standard. Ett misslyckat försvinner. Och människan behöver bara hantera **prioriteringar, quality bar och undantag**.

Det är mycket närmare hur jag skulle definiera *“arbeta som ett frontier AI engineering-team”* än att bara använda de senaste modellerna.

Jag tycker dessutom att nästa naturliga steg är att vi gör en **riktig gap analysis av hela Nortropic** mot kanske 12–15 sådana engineering-discipliner — repo, docs, specs, evals, observability, CI/CD, issue management, security, research, knowledge, product feedback, developer experience, metrics, harness/context engineering — och därefter får du en konkret **Nortropic → Frontier Engineering roadmap** med `KEEP / IMPROVE / ADD / DELETE`.

Eftersom området förändras snabbt kan jag också bevaka OpenAI, Anthropic och de viktigaste engineering-källorna och bara flagga sådant som faktiskt kan förändra Nortropic.  
genui{"suggest_automation":{"label":"Bevaka Frontier AI Engineering"}} memcite

---

## Meddelande 6 — ChatGPT (assistent)

Klart. **Bevaka Frontier AI Engineering** körs dagligen och meddelar dig bara när något meningsfullt dyker upp för Nortropic.

Varje relevant fynd ska klassificeras som **IGNORE / WATCH / EXPERIMENT / ADOPT**, kopplas till vilken del eller vilket antagande i Nortropic det påverkar, och vid behov få ett förslag på minsta användbara experiment. memcite

---

## Meddelande 7 — Johnny (användare)

Jake Van Clief verkar ha lite radikala eller innovativa tankar, brainstorma kring detta

---

## Meddelande 8 — ChatGPT (assistent)

Jag börjar med att reda ut **vilken Jake Van Clief och vilka idéer du syftar på**, eftersom namnet är tillräckligt nischat för att jag inte vill gissa. Sedan bryter jag ner det i: vad som faktiskt är radikalt, vad som bara låter radikalt, och vad som skulle kunna översättas till Nortropic som experiment snarare än trosartikel.

---

## Meddelande 9 — ChatGPT (assistent)

Nu ser jag varför du reagerade på honom. Det mest intressanta är egentligen **inte** hans provokativa “agents are a waste of time”, utan en djupare tes:

> **Vi kanske har lagt arkitekturen på fel ställe. I stället för att bygga intelligenta agentobjekt ska vi bygga ett intelligibelt informationslandskap som en stark modell kan navigera.**

Det träffar Nortropic väldigt nära. Och här finns faktiskt några idéer som kan förändra hur jag skulle designa nästa generation av systemet.

---

## Meddelande 10 — ChatGPT (assistent)

Ja — och efter att ha läst hans ICM-paper, senaste inlägg och jämfört det med Anthropic/OpenAI tycker jag att **Jake Van Clief är mer intressant för Nortropic än hans “agents are a waste of time”-rubriker först antyder**.

Det finns en kärna i hans tänkande som jag tror vi bör ta på stort allvar.

## Den stora idén: kanske bygger vi AI-system på fel abstraktionsnivå

Van Cliefs ICM, *Interpretable Context Methodology*, utgår från något väldigt enkelt:

> I ett sekventiellt workflow behöver du kanske inte `Research Agent → Planning Agent → Writing Agent → Reviewer Agent` som separata programobjekt. Du kan ha **en stark modell som befinner sig i olika väldefinierade kontexter**.

I hans modell blir:

```text
agent-identitet
      ↓
vilken kontext modellen just nu befinner sig i
```

snarare än:

```text
agent-identitet
      ↓
ett separat program / process / persona / service
```

Folderstrukturen definierar ordningen, markdown definierar kontrakten, filer bär state och outputs blir nästa stegs input. Hans fem lager skiljer bland annat global identitet, routing, stage-kontrakt, stabil referenskontext och run-specifika arbetsartefakter. citeturn972695view0

Det här är **väldigt relevant för Nortropic**.

---

# 1. “Agent” kanske egentligen borde vara en **context projection**

Det här är den idé jag tycker är mest explosiv.

Vi tänker lätt:

```text
planner
builder
reviewer
architect
researcher
```

som fem agenter.

Van Clief skulle snarare kunna säga:

```text
             MODEL
               │
       ┌───────┼────────┐
       ↓       ↓        ↓
   planner   builder  reviewer
   context   context   context
```

Samma intelligens. Olika:

- authority
- inputs
- instructions
- tools
- reference material
- output contract
- quality criteria.

ICM-pappret uttrycker precis detta: samma modell beter sig olika därför att **informationen som levereras till modellen förändras**, inte därför att modellens grundkapacitet förändras. citeturn754370view2

### Nortropic-konsekvens

Det får mig att ifrågasätta hur mycket framtida Nortropic ska modellera **agenter** och hur mycket vi istället ska modellera:

> **Context Views / Workspaces / Task Environments.**

Exempel:

```text
task/
├── 00-identity/
├── 01-problem/
├── 02-research/
├── 03-specification/
├── 04-build/
├── 05-verification/
└── 06-learning/
```

Claude eller Codex är interpretern.

Det som gör den till “reviewer” är vad `05-verification/` tillåter den att se och göra.

### Min dom

**ADOPT som designprincip.**

Inte “ta bort alla agenter”, utan:

> **Sluta anta att varje kognitiv roll behöver en egen agentarkitektur.**

---

# 2. “Folder structure as agent architecture”

Det låter nästan löjligt enkelt.

Men det finns ett ganska djupt datavetenskapligt argument bakom.

ICM jämför det med Unix, Make och multi-pass compilers:

```text
input
 ↓
pass 1
 ↓
intermediate representation
 ↓
pass 2
 ↓
intermediate representation
 ↓
pass 3
 ↓
output
```

Byt ut compiler passes mot AI-arbetssteg:

```text
idea
 ↓
research.md
 ↓
spec.md
 ↓
implementation
 ↓
evaluation.md
 ↓
product
```

Filerna blir **intermediate representations**, IR. citeturn972695view0

Och här börjar det bli riktigt intressant för våra tidigare diskussioner om:

**brainstorming → dokumentation → implementation.**

Kanske problemet aldrig borde lösas genom “överför chatten till Claude Code”.

Problemet är snarare:

> Vi saknar en definierad compiler pipeline från mänskligt tänkande till executable work.

---

# 3. Nortropic som **compiler för intention**

Van Clief återkommer till metaforen att LLM:er är nästa lager ovanpå programmeringsspråk: maskinen kan fungera som en compiler från mänsklig intention till resultat. Han argumenterar därför för att det verkliga arbetet flyttar från syntax till att strukturera intention, kontext och kvalitetsbedömningar. citeturn968179search1turn968179search0

Jag tycker man kan göra en mycket starkare Nortropic-version:

```text
HUMAN INTENT
     │
     ▼
WAYFINDING
     │
     ▼
RESEARCH
     │
     ▼
SPECIFICATION
     │
     ▼
TASK GRAPH
     │
     ▼
EXECUTION
     │
     ▼
VERIFICATION
     │
     ▼
PRODUCT
```

Nortropic är då inte egentligen “ett antal agenter”.

Det är:

> **en compiler från intention → verifierat resultat.**

Claude/Codex är exekveringsmotorn.

Det här är, tycker jag, en mycket renare mental modell för vad vi håller på att bygga.

---

# 4. Den kanske viktigaste Van Clief-idén: **productionize your opinion**

Här tycker jag han träffar ett område där Nortropic fortfarande har mycket kvar.

Hans argument är att modellen redan känner till generella best practices. Problemet är att den inte känner till **din version av “bra”** eller kundens version av “bra”. Därför ska man inte bara productionisera processen utan även omdömet — taste, preferenser och fuzzy decisions. citeturn968179search1

Detta är enormt relevant.

Vi har varit väldigt fokuserade på:

```text
Är ändringen korrekt?
Är den tillåten?
Är kraven uppfyllda?
Är verifieringen oberoende?
```

Men frontier-kvalitet kräver också:

```text
Är detta Nortropic-bra?
Är detta elegant?
Känns sajten premium?
Är UX-beslutet intelligent?
Är copy:n övertygande?
Är lösningen enklare än alternativet?
Skulle Johnny valt A eller B?
Varför?
```

Det är en helt annan kunskapstyp.

### Där ser jag ett nytt Nortropic-lager

Inte bara:

```text
PROCESS
RULES
CONSTITUTION
SPECS
```

utan:

```text
TASTE
JUDGMENT
HEURISTICS
EXEMPLARS
ANTI-PATTERNS
CUSTOMER PREFERENCES
QUALITY CANONS
```

Och framför allt:

### **beslutspar**

När du säger:

> “A är mycket bättre än B eftersom ...”

är det extremt värdefull tränings-/kontextdata för Nortropic.

Det bygger **Nortropic taste**.

Detta är potentiellt viktigare än ännu 500 rader harness.

---

# 5. Här kopplas Van Clief direkt till vår Quality Gauntlet

Anthropic har nästan samma observation från ett annat håll.

I deras 2026-harness-experiment fick en generator och evaluator först enas om ett sprintkontrakt — vad som skulle byggas och hur det skulle verifieras — innan implementationen började. Evaluatorn använde sedan den körande applikationen för QA. citeturn602495view3

Det kompletterar Van Clief:

```text
Van Clief:
rätt information
vid rätt steg
i rätt struktur

Anthropic:
rätt kvalitetskriterier
+ feedback
+ evaluator

Nortropic:
extern trust authority
+ deterministic gates
+ containment
```

Kombinera dem:

```text
              NORTROPIC

         Intent / Wayfinding
                 ↓
          Context Workspace
                 ↓
             Specification
                 ↓
         Quality Definition
                 ↓
        Provider Intelligence
          Claude / Codex
                 ↓
       ┌─────────┴─────────┐
       ↓                   ↓
   Semantic QA      Deterministic Gates
       │                   │
       └─────────┬─────────┘
                 ↓
           Trusted Outcome
```

Det börjar kännas som en betydligt mer komplett arkitektur.

---

# 6. “The folder is the app”

Här blir han mer radikal.

Han beskriver interna workflow-appar där:

```text
folder structure = application
markdown          = interface
output folders    = database/state
Claude Code       = runtime
VS Code           = UI
```

och argumenterar för att man bör fråga om en workflow verkligen behöver React, databas, server och auth innan man bygger allt det. citeturn968179search7

Jag tycker **principen är lysande**, men slutsatsen måste begränsas.

För Nortropic:

### Mycket lämpar sig perfekt för detta

```text
research
innovation
RFCs
brainstorming
specification
design exploration
knowledge
handoffs
reports
postmortems
customer discovery
content
```

Där kan Markdown + Git + Claude vara enormt kraftfullt.

### Men inte allt

```text
credentials
concurrent workers
transactional state
authorization
remote state
deployments
locks
leases
recovery
security boundaries
```

Här behöver riktig mekanik finnas.

Och Jake själv medger detta: ICM är avsiktligt sekventiellt och passar sämre för realtidskoordination, automatiskt branching och concurrent execution. citeturn754370view1

Det passar därför perfekt ihop med Nortropics **provider-neutral Trust Kernel**:

```text
SEMANTIC WORK
folders / markdown / model
        │
        │ request
        ▼
──────────────────────────
      TRUST KERNEL
──────────────────────────
identity
authorization
containment
gates
promotion
credentials
transactions
```

**Folders får aldrig bli security boundary.**

Det är där jag inte skulle följa Van Clief hela vägen.

---

# 7. Han har faktiskt upptäckt en idé som jag vill stjäla direkt: **Walk Test**

Hans alldeles senaste `icm-architect` använder ett mycket elegant test:

> En agent utan tidigare minne ska öppna roten, orientera sig, förstå vad den ska göra och rapportera status utifrån filerna. Om den inte kan det är workspace-strukturen fel. citeturn968179search5

Det här är nästan skräddarsytt för Nortropic.

Jag skulle göra det mycket hårdare:

## Nortropic Cold-Start Test

Starta helt färsk Claude/Codex utan tidigare chatt.

Den får bara repot.

Den ska kunna svara korrekt på:

```text
Vad är detta system?

Vad är source of truth?

Vilka authorities gäller?

Vad är aktuellt state?

Vad är nästa arbete?

Vad får jag ändra?

Vad får jag INTE ändra?

Hur verifieras arbetet?

Vad kräver mänsklig authority?

Var finns relevant kontext?

Vilken information behöver jag INTE läsa?
```

Om den inte klarar det:

**repo legibility failure.**

Detta kan bli ett faktiskt eval.

Jag gillar den idén väldigt mycket.

---

# 8. Ännu mer intressant: **semantic source maps**

Van Clief identifierar själv en svaghet i ICM.

Filer gör state synligt, men om slutresultatet är fel vet man fortfarande inte exakt **vilken instruktion eller vilken referens som orsakade felet**.

Han föreslår därför något som liknar compiler source maps:

```text
OUTPUT
  ↑
  │ generated from
  │
stage contract
  ↑
reference
  ↑
source decision
```

med provenance mellan output och källkontext. citeturn754370view3

Det här tycker jag är **extremt intressant för Nortropic**.

Tänk:

```text
button CTA:
"Begär offert"

PROVENANCE
├── customer-research.md §4
├── conversion-canon.md §CTA-2
├── brief.md §business-goal
└── decision ADR-018
```

Eller:

```text
architectural decision
        ↓
task requirement
        ↓
implementation
        ↓
test
        ↓
observed result
```

Då får vi något mycket större än documentation.

Vi får:

# **causal traceability**

Det kan bli ett av Nortropics verkligt differentierande lager.

---

# 9. Och sedan kommer nästa fina princip: **Edit Source, Not Output**

Han säger i princip:

Om människan korrigerar samma typ av output flera gånger ska man inte fortsätta korrigera outputen.

Man ska fråga:

> Vad i systemets källa gjorde att modellen fortsatte göra detta?

ICM-pappret föreslår att återkommande mänskliga korrigeringar kan identifieras och omvandlas till uppdateringar av stage contracts, reference files eller constraints. citeturn754370view4

Detta är precis hur jag tycker Nortropic självförbättring borde fungera.

```text
Human correction
       ↓
Was this one-off?
       │
       ├── YES → fix output
       │
       └── NO
            ↓
     find root source
            ↓
 contract / skill / canon / eval
            ↓
          change
            ↓
       regression eval
```

Det är en ren **learning loop**.

Mycket bättre än:

> “agenten gjorde fel → skriv en längre prompt.”

---

# 10. “Configure the factory, not the product”

Det här är nästan komiskt kompatibelt med Nortropic.

ICM:s femte princip är att du konfigurerar fabriken en gång — preferences, rules, style, structure — och därefter genererar varje run en ny produkt. citeturn972695view0

Nortropic gör redan i princip:

```text
Nortropic Factory
       ↓
customer context
       ↓
website
```

Men det väcker en större strategisk tanke:

## Kundsajten ska kanske behandlas som **compiled artifact**

Inte som Nortropics primära intellectual property.

```text
NORTROPIC IP
├── customer understanding
├── process
├── taste
├── context architecture
├── quality functions
├── evals
├── learning
└── trust kernel

         ↓ compile

    customer website
```

Detta hakar dessutom i hans mer radikala tes om att mycket mjukvara blir billig och disponibel när modeller kan generera den efter behov. citeturn968179search0

Jag skulle inte köpa hans “software startups become extinct”-retorik bokstavligt.

Men riktningen är viktig:

> **Kod blir billigare. Kontext, distribution, judgement, data, trust och feedback loops blir relativt dyrare.**

För Nortropic är det en potentiellt mycket viktig strategisk insikt.

---

# Där jag tycker Jake går för långt

Hans LinkedIn-formulering att “agents are a waste of time” är bra marknadsföring men dålig arkitekturregel.

Hans **eget paper** använder Opus som orchestrator och Sonnet-subagents, och paperet säger uttryckligen att komplex branching, concurrency och realtidskoordination fortfarande kan behöva riktig agentinfrastruktur. citeturn754370view0turn754370view1

Anthropic ligger också mycket närmare:

> “Use the simplest harness that measurably works.”

än:

> “Do not use agents.”

De fick stor kvalitetsvinst av planner/generator/evaluator-harnesset, men började sedan metodiskt ta bort komponenter när Opus 4.6 själv blivit bättre. citeturn602495view3

Och för verkligt långlivade agenter bygger Anthropic fortfarande durable session state, sandbox isolation, credential separation och stabila harness interfaces — alltså sådant som filer ensamma inte löser. citeturn602495view4

OpenAI gör samma sak från andra hållet: Symphony är väldigt minimalistiskt och spec-drivet, men har fortfarande en verklig orchestrator som mappar issues till isolerade agentworkspaces. citeturn602809view5

Så min syntes är:

> **Van Clief har sannolikt mer rätt om context architecture än han har om agent architecture.**

---

# En viktig vetenskaplig brasklapp

Jag skulle ännu inte kalla ICM empiriskt bevisat överlägset.

Paperet är ett arXiv-preprint och författarna är själva ganska öppna med begränsningarna: 33 practitioners ligger bakom en del av observationerna, resultaten är i stor utsträckning självrapporterade, communityn är självselekterad, alla tester gjordes på Claude-familjen och det finns ännu ingen kontrollerad jämförelse mellan ICM och monolitisk prompting på samma tasks. citeturn754370view1

Det är faktiskt ett plus för trovärdigheten att de skriver ut detta.

För Nortropic betyder det:

**vi ska testa tesen, inte tro på den.**

---

# Min nya syntes för Nortropic

Vår tidigare modell har ungefär varit:

```text
NORTROPIC
├── Context Engineering
├── Memory Engineering
├── Harness Engineering
└── Trust / Verification
```

Efter Van Clief skulle jag lägga till ett lager **ovanför context engineering**:

```text
NORTROPIC AI INFRASTRUCTURE

┌──────────────────────────────┐
│  WORKSPACE ARCHITECTURE      │
│  information topology        │
│  stage boundaries            │
│  context routing             │
│  intermediate representations│
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│  CONTEXT ENGINEERING         │
│  what enters each window     │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│  MODEL / PROVIDER HARNESS    │
│  Claude / Codex              │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│  TRUST KERNEL                │
│  authority / gates / security│
└──────────────────────────────┘
```

Jag skulle kalla det exempelvis:

## **Workspace / Information Architecture**

eller ännu bättre:

## **Context Topology**

Context engineering frågar:

> *Vad ska modellen veta?*

Context topology frågar:

> **Var ska kunskapen bo, vilken typ är den, när ska den synas, vad transformerar den till och hur färdas den genom systemet?**

Det är faktiskt ett separat engineeringproblem.

---

# Om jag plockar ut Van Cliefs idéer för Nortropic

| Idé | Min dom |
|---|---|
| Context > agent personas | **ADOPT** |
| Folder structure som workflow architecture | **ADOPT, där problemet är sekventiellt** |
| En modell istället för många agents | **EXPERIMENT** |
| Markdown/files som intermediate representations | **ADOPT** |
| Configure factory, not product | **ADOPT — Nortropic gör redan mycket av detta** |
| Productionize your opinion/taste | **ADOPT — mycket hög prioritet** |
| Walk test med helt minneslös agent | **ADOPT omedelbart** |
| Semantic source maps / provenance | **RESEARCH → EXPERIMENT** |
| Edit source, not repeated outputs | **ADOPT som learning principle** |
| Software becomes disposable | **WATCH/strategisk tes** |
| Folders ersätter databases/services | **REJECT som generell princip** |
| “Agents are waste of time” | **REJECT bokstavligt, behåll provokationen** |

Och det ger mig faktiskt en lite annorlunda bild än jag hade i vårt förra resonemang.

**Jag tror inte längre att Nortropics nästa stora frontier endast är Engineering OS → issue orchestration → observability.**

Jag tror det finns ett lager vi bör undersöka **före** det:

> **Kan vi drastiskt förenkla Nortropics kognitiva arkitektur genom att göra repot/workspacet så välstrukturerat att Claude/Codex behöver betydligt mindre egen orchestrator- och agentlogik?**

Det är exakt den typ av ablation som både Van Clief och Anthropic pekar mot från olika håll. Anthropic konstaterar uttryckligen att harness-delar kodar antaganden om vad modellen inte klarar, och att de antagandena blir “dead weight” när modellen förbättras. citeturn602495view4

**Det här skulle jag vilja djupdyka i nästa gång:** ta Nortropics faktiska arkitektur och göra ett tankeexperiment där vi reducerar den enligt **Van Clief/ICM + Anthropic harness-minimalism + OpenAI Symphony**, utan att röra Trust Kernel. Då kan vi upptäcka om 20–50 % av det vi betraktar som “agent infrastructure” egentligen borde vara **context topology och filer**. Det skulle kunna vara en genuint stor förenkling. memcite

---

## Meddelande 11 — Johnny (användare)

Det låter bra, jag undrar om det går att identifiera liknande Van Clief människor som kan vara värda att följa? Det vill säga, innovativa AI ”tänkare”, filosofer, experter, sakkunniga, ja du förstår vad jag menar. Jag är även nyfiken på som man kan scrapa github på alla open source löpande som tittas på om det är nåt värt att ta efter eller tillämpa? Ständig bevakning för konstant utveckling, förbättring, analys, reflektion etc. 

Brainstorma

---

## Meddelande 12 — ChatGPT (assistent)

Ja — och här tror jag vi kan göra något större än en “lista på bra personer att följa”. Jag vill tänka i termer av ett **Nortropic Intelligence System**: människor, papers, GitHub, release notes och faktisk kodförändring som kontinuerligt fångas, dedupliceras, kritiseras och översätts till `IGNORE / WATCH / EXPERIMENT / ADOPT`.

Jag kommer också separera **signal-personer** (originella idéer), **builders** (visar vad som faktiskt fungerar), **eval/reliability-folk** och **contrarians** — annars blir bevakningen lätt en ekokammare.

---

## Meddelande 13 — ChatGPT (assistent)

Det finns dessutom en viktig skillnad mellan **“person att följa”** och **“källa som gör Nortropic bättre”**. Karpathy kan ge en idé som förändrar forskningsloopen; Hamel/Shreya kan avslöja att en eval är felkonstruerad; Steve Yegge kan visa en extrem multi-agent-arkitektur som vi sedan *inte* ska kopiera men använda som falsifiering; Geoffrey Litt kan förändra själva bilden av vad software borde vara.

Så jag skulle bygga bevakningen för **intellektuell diversitet**, inte popularitet. Målet är inte att veta vad AI-Twitter pratar om utan att upptäcka *nya antaganden som kan göra delar av Nortropic obsolete eller radikalt bättre*.

---

## Meddelande 14 — ChatGPT (assistent)

Ja. Det du beskriver är egentligen **inte en omvärldsbevakare**. Det är början på ett **ständigt lärande R&D-system för Nortropic**.

Och jag tror att Jake Van Clief-fallet visar varför det behövs: en relativt okänd person kan formulera en idé som plötsligt får oss att ifrågasätta en hel arkitektonisk premiss. Om vi bara följer OpenAI/Anthropic missar vi sådana signaler. Om vi bara följer Twitter/GitHub drunknar vi däremot i brus.

Jag skulle därför bygga tre sammankopplade radarer:

```text
              NORTROPIC FRONTIER INTELLIGENCE

        ┌──────────────┬──────────────┬──────────────┐
        │              │              │
   PEOPLE RADAR    OSS RADAR     RESEARCH RADAR
   thinkers        GitHub        papers/labs
        │              │              │
        └──────────────┴──────────────┘
                       ↓
                SIGNAL EXTRACTION
                       ↓
             CLAIM / PATTERN GRAPH
                       ↓
                RED-TEAM ANALYSIS
                       ↓
        IGNORE / WATCH / EXPERIMENT / ADOPT
                       ↓
                 NORTROPIC DELTA
                       ↓
                    EXPERIMENT
                       ↓
                MEASURED RESULT
                       ↓
              KNOWLEDGE / SYSTEM
                       ↺
```

Det viktiga är **↺**. Bevakningen ska inte producera nyhetsbrev. Den ska ibland förändra Nortropic.

---

# 1. Ja: det finns fler “Van Clief-personer”

Jag skulle inte göra en lista med “de största AI-profilerna”. Jag skulle istället välja personer som **producerar nya mentala modeller**.

Några jag skulle sätta mycket högt just nu:

| Person | Varför intressant för Nortropic | Typ av signal |
|---|---|---|
| **Ryan Lopopolo** | Harness engineering, agent-first engineering, repo-legibility, humans steer/agents execute | Systemarkitektur |
| **Armin Ronacher** | Loops ovanpå agent-loopar, men samtidigt stark kritik mot obegriplig autonom kod | Contrarian engineering |
| **Mario Zechner** | Minimalistiska coding agents, ifrågasätter MCP/komplexa harness, context-first | Minimalism |
| **Jason Liu** | Context engineering, evals, “no multi-agents”, grep/direct exploration vs komplex RAG | Praktisk falsifiering |
| **Steve Yegge** | Gas Town/Beads, extrem motsats: massiv multi-agent orchestration och persistent work state | Maximalism |
| **Nicholas Carlini** | Faktiska storskaliga agentteamsexperiment med hundratals/tusentals sessions | Empirisk autonomy |
| **Andrej Karpathy** | Autoresearch: agenten experimenterar, mäter, behåller/förkastar; människan programmerar `program.md` | Autonomous R&D |
| **Hamel Husain** | Evals, error analysis, product quality som mätbar disciplin | Quality science |
| **Shreya Shankar** | Agent-evals, data/evaluation methodology, trace-driven improvement | Evaluation research |
| **Simon Willison** | Oberoende experiment, Agentic Engineering Patterns, extremt snabb på att testa nya beteenden | Reality check |
| **Thorsten Ball** | Amp; ifrågasätter själva “coding agent”-produkten och flyttar mot parallella/remote loops | Frontier UX |
| **Geoffrey Litt** | Malleable software, human understanding, cognitive debt, människans roll när agents bygger allt | AI/software philosophy |
| **Chip Huyen** | Production AI + systemtänk + omfattande kartläggning av open source AI | Ecosystem / production |
| **swyx** | Bra metasignal för vad AI-engineering-communityn håller på att konvergera mot | Trend synthesis |

## Ryan Lopopolo är nästan obligatorisk

OpenAI:s egen artikel av Ryan Lopopolo beskriver ett team där all application logic, tests, CI, docs, observability och tooling skrevs av Codex, uppskattningsvis på omkring en tiondel av normal utvecklingstid. Den centrala lärdomen var att ingenjörsarbetet flyttar till **environment design, intent specification och feedback loops**. citeturn922487search0

Detta ligger så nära Nortropics problemområde att jag skulle bevaka honom personligen.

---

# 2. Armin Ronacher är särskilt värdefull eftersom han **motsäger hypen**

Hans *The Coming Loop* från juni är mycket intressant.

Han identifierar en loop **utanför** agentens normala tool-call-loop:

```text
TASK
 ↓
agent attempts
 ↓
harness evaluates
 ↓
done?
 ├─ yes
 └─ no → continue / new context / new agent
```

Men han varnar samtidigt för att hands-off loops kan ackumulera lokal defensiv kod, fallbacks och dåliga abstraktioner tills systemet ser robust ut men blir svårare att förstå. Han säger också att loops verkar fungera särskilt bra för exempelvis performance experiments, portning, säkerhetssökning och research där feedbacksignalen är tydlig eller artefakten inte behöver leva länge. citeturn574438view1

Detta är **perfekt motgift** till Nortropics autonomy-entusiasm.

Vi vill följa människor som kan säga:

> “Den där idén ni just blev förälskade i har detta fundamentala problem.”

---

# 3. Mario Zechner är nästan Van Cliefs intellektuella kusin

Hans publicerade ämnen säger en hel del i sig:

- *Prompts are code, .json/.md files are state*
- *What if you don't need MCP at all?*
- *What I learned building an opinionated and minimal coding agent*

Han jobbar alltså från samma typ av first-principles-fråga:

> Hur mycket infrastruktur är faktiskt nödvändigt?

Hans blogg har fortsatt aktiv publicering under 2026. citeturn574438view0

Han och Van Clief skulle därför ligga i samma **Harness Minimalism / Context First**-cluster.

---

# 4. Sedan behöver vi deras motsats: Steve Yegge

Det här är viktigt.

Om vi bara följer personer som säger:

> “Färre agents! Färre frameworks! Fler filer!”

kommer Nortropic bara att bekräfta sin senaste övertygelse.

Steve Yegges Gas Town är nästan den diametrala motsatsen.

Gas Town hanterar persistent work state, identities, handoffs, flera coding-agent providers och många samtidiga workers. Beads fungerar som persistent arbets-/issue-lager. citeturn137632search9turn137632search0

Hans VC-projekt går ännu längre och beskriver:

```text
AI Supervisor
      ↓
Issue workflow
      ↓
Worker agents
      ↓
Quality gates
      ↓
AI decides:
close / partial / blocked
```

och bygger explicit på issue-oriented orchestration och self-hosting. citeturn137632search2

Det är **en fantastisk falsifieringskälla för Van Clief**.

Kanske:

```text
Van Clief har rätt
för sekventiell knowledge work.

Yegge har rätt
för concurrent distributed work.
```

Det är exakt sådana synteser vårt intelligence-system ska upptäcka.

---

# 5. Nicholas Carlini bör också bevakas mycket noga

Anthropic lät honom köra **16 parallella Claude-agenter** för att bygga en Rust-baserad C-kompilator som kunde kompilera Linux-kärnan. Experimentet omfattade nästan 2 000 Claude Code-sessioner, runt $20 000 API-kostnad och resulterade i ungefär 100 000 rader kod. Hans fokus ligger mycket på hur tester, decomposition och harness-design kan hålla autonoma team på spåret. citeturn922487search6

Detta är värdefullt eftersom det är:

**radikal idé + faktisk implementation + faktisk kostnad + faktiskt resultat.**

Jag skulle väga sådan evidence mycket högre än en viral tråd.

---

# 6. Karpathys `autoresearch` är kanske ännu viktigare för din vision

Hans 2026-projekt låter en agent:

```text
change
 ↓
train
 ↓
measure
 ↓
better?
 ├─ YES → keep
 └─ NO  → revert
 ↓
repeat
```

Det intressanta är att människan i huvudsak arbetar med `program.md`, som definierar agentens research organization, snarare än att manuellt göra experimenten. citeturn577167search0turn577167search5

Det är nästan **Darwinistisk Nortropic-utveckling**:

```text
hypothesis
   ↓
variation
   ↓
experiment
   ↓
selection
   ↓
next generation
```

För allt som går att mäta objektivt är detta väldigt kraftfullt.

---

# 7. Hamel Husain + Shreya Shankar är en annan sorts thinkers

De är mindre “radikala filosofi-trådar” och mer:

> Hur vet vi egentligen att vi blev bättre?

Det behövs som broms på alla andra.

Deras eval-arbete rekommenderar bland annat att börja med konkret error analysis och riktiga traces snarare än att först bygga stor eval-infrastruktur. Ett minimum kan vara att en domänexpert manuellt granskar 20–50 outputs när systemet förändras väsentligt. citeturn577167search7turn577167search9

Hamel argumenterade dessutom nyligen att:

> om outputen är väldigt svår att evaluera kan det vara ett **product smell**, inte bara ett eval-problem. citeturn577167search10

Det är ett väldigt Nortropic-kompatibelt sätt att tänka.

---

# 8. Jason Liu tycker jag också hamnar väldigt högt

Han arbetar nu på Codex-teamet enligt sin egen sajt och skriver uttryckligen om:

- Context Engineering
- “Grep Beats Embeddings”
- “No Multi-Agents”
- compaction
- Codex workflows
- memory
- durable threads. citeturn497395search4turn497395search8turn497395search14

Han är värdefull just eftersom han ofta börjar med:

> Vad är den enklaste mekanismen som faktiskt fungerar?

Det gör honom till en naturlig kandidat för vår framtida **harness ablation-bevakning**.

---

# 9. Geoffrey Litt bevakar ett problem jag tycker Nortropic ännu knappt börjat lösa

Hans tes sommaren 2026 är:

> **“Understanding is the new bottleneck.”**

När agents skriver koden snabbare än människan kan förstå den uppstår cognitive debt. Han experimenterar därför med:

- code explainer docs
- literate diffs
- quizzes
- micro-worlds
- interaktiva visuella modeller

för att låta människan hinna bygga mental förståelse av det system agenten producerar. citeturn574438view2

Detta tycker jag kan bli ett helt Nortropic-område:

## **Human Comprehension Engineering**

Inte bara:

```text
Can agent understand repo?
```

utan också:

```text
Can Johnny understand
what the agents have built?
```

Det är en oväntat viktig motvikt när autonomin växer.

---

# 10. Och Thorsten Ball/Amp representerar en annan radikal frontier

Amp skrev i februari uttryckligen **“The Coding Agent Is Dead”**.

Deras tes var inte att AI coding försvinner, utan att modeller blivit så kapabla att själva agent-wrappern inte längre är huvudbegränsningen; istället blir codebase-organisation och organisationens sätt att använda agents bottleneck. De började därför flytta fokus bort från editor-sidebar-formen. citeturn574438view3

Det ligger väldigt nära Van Clief:

> kanske optimerar vi fel lager.

Bra bevakningssignal.

---

# 11. Simon Willison bör vara en slags **Nortropic reality oracle**

Han började 2026 dokumentera **Agentic Engineering Patterns** — praktiska mönster för professionella ingenjörer som arbetar med coding agents. citeturn577167search8

Han är dessutom ovanligt snabb på att faktiskt prova saker och skriva vad som fungerar och inte fungerar. Exempelvis beskriver han hur nya modeller i agent-harnesses nu kan läsa dokumentation för helt nya verktyg och arbeta effektivt med dem även när de inte finns i träningsdata. citeturn577167search1

Han är därför bra som:

> **“Har någon faktiskt provat den här idén?”**

---

# Det viktiga: bygg inte en statisk “follow list”

Jag skulle bygga en **självexpanderande People Graph**.

Exempel:

```text
Ryan Lopopolo
      │ cites
      ▼
person X
      │
      ├── repo
      ├── paper
      └── blog
             │
      independently cited by
             │
     ┌───────┴────────┐
 Simon              Anthropic
     │                  │
     └────────┬─────────┘
              ↓
     CANDIDATE SIGNAL PERSON
```

En okänd person blir intressant om till exempel:

- två betrodda personer refererar till dem
- de introducerar en ny term som börjar spridas
- deras repo får ovanlig adoption bland högkvalitativa builders
- en idé först dyker upp hos dem och senare hos ett frontier lab
- de producerar flera bra förutsägelser/experiment över tid.

### Det hade kunnat upptäcka nästa Van Clief automatiskt.

---

# 12. GitHub-idén: **ja — men inte “scrapa allt och låt en LLM läsa allt”**

Det är tekniskt fel nivå.

GitHubs egen Events API visar som mest ungefär 300 events och högst 30 dagars historik, och GitHub säger själva att event-feeden inte är avsedd som realtidsström och kan släpa från cirka 30 sekunder till flera timmar. citeturn692030search2

Dessutom har Search API egna, striktare rate limits än vanlig REST-åtkomst. citeturn692030search0turn692030search5

### Men det finns en mycket bättre väg.

**GH Archive** registrerar GitHubs offentliga event timeline i timvisa arkiv, och hela datamängden kan analyseras via BigQuery. citeturn629584search0turn629584search3

Alltså:

```text
ALL PUBLIC GITHUB ACTIVITY
          ↓
      GH ARCHIVE
          ↓
       BigQuery
          ↓
    Cheap filtering
          ↓
   interesting repos
          ↓
   GitHub API / clone
          ↓
 deep AI inspection
```

Det är mycket intelligentare än att crawla miljontals repositories.

---

# 13. Tänk “teleskop”, inte “dammsugare”

Första lagret tittar bara på metadata.

Exempel på event:

```text
CreateEvent
PushEvent
ReleaseEvent
WatchEvent
ForkEvent
PullRequestEvent
IssueEvent
```

GitHubs Events-modell har dessa typer explicit. citeturn692030search4

Därifrån kan vi hitta:

### **Acceleration**

```text
repo went:
20 stars → 800 stars in 72h
```

### **Expert adoption**

```text
5 personer på vår trusted-builder-list
börjar star/forka samma repo
```

### **Contributor acceleration**

```text
2 maintainers
      ↓
12 serious contributors
på 3 veckor
```

### **Release velocity**

```text
v0.1
 ↓
v0.2
 ↓
v0.3
på 10 dagar
```

### **Pattern diffusion**

Plötsligt börjar många starka repos lägga till exempelvis:

```text
AGENTS.md
skills/
evals/
worktrees/
traces/
progress.md
TaskContract
```

Det kan vara viktigare än en enskild repo.

---

# 14. Sedan kommer AI-filtret

När GitHub-radarn hittar:

```text
100,000 candidate events
```

ska kanske:

```text
1,000
```

passera första maskinfiltret.

Sedan:

```text
100
```

får semantic analysis.

Sedan:

```text
10
```

får riktig djupanalys.

Och kanske:

```text
1
```

är relevant nog för Nortropic.

### Det är den tratten vi vill optimera.

Inte:

> “Läs hela GitHub.”

---

# 15. Vi har redan ett bra bootstrap-underlag

Chip Huyen har i praktiken redan börjat bygga en AI-specifik GitHub-index.

Hennes **Good AI List** uppdateras dagligen och visar för närvarande omkring **16 980 repositories**; hennes egen analys beskriver listan som en fortsättning på kartläggningen av open-source AI-landskapet. citeturn823493search2turn823493search9turn497395search7

Så Nortropic behöver inte ens börja från noll.

Jag skulle använda:

```text
GH Archive
    +
Good AI List
    +
GitHub Search
    +
hand-curated seed repos
```

som discovery-källor.

---

# 16. Men **stjärnor är ett dåligt truth metric**

En repo ska inte automatiskt få hög prioritet för att den har 50 000 stars.

Vi bör leta efter ett kombinerat signalvärde.

Jag tänker ungefär:

```text
NORTROPIC SIGNAL SCORE

Novelty
   ×
Relevance
   ×
Evidence
   ×
Adoption velocity
   ×
Source credibility
   ×
Transferability
   ÷
Hype / complexity / risk
```

Inte bokstavligen exakt den matematiken från början, men de dimensionerna.

En Van Clief-post med 400 läsare kan då slå ett 80 000-star “AI agents framework”.

Det är viktigt.

---

# 17. Och sedan något ännu mer intressant: **Convergence Detection**

Säg att följande händer oberoende:

```text
Jake Van Clief
     ↓
"agents → contexts"

Mario Zechner
     ↓
"minimal harness"

Jason Liu
     ↓
"no multi-agents"

Anthropic
     ↓
"remove harness assumptions"

Amp
     ↓
"agent wrapper isn't bottleneck"
```

En vanlig news aggregator visar fem artiklar.

### Nortropic Intelligence bör säga:

> **CONVERGENCE DETECTED**
>
> Flera oberoende källor verkar konvergera mot tesen att model-facing harness complexity bör minska när modeller förbättras.
>
> Nortropic exposure:
> `agent roles`, `custom orchestration`, `context routing`.
>
> Proposed experiment:
> single-model / context-projection ablation.

Det är **analys**.

Inte aggregation.

Anthropic uttrycker själva principen att varje harness-komponent kodar ett antagande om vad modellen inte kan göra, och att dessa antaganden måste omprövas när modellerna förbättras. citeturn922487search1turn922487search2

---

# 18. Vi behöver även **Contradiction Detection**

Samma system bör upptäcka:

```text
Van Clief:
multi-agents unnecessary

      VS

Carlini:
16 agents achieved something
single agent couldn't
```

Sedan skapa:

```text
THESIS
Multi-agent architectures are beneficial
only when parallel decomposition produces
a measurable advantage.

SUPPORT
Carlini
Yegge

COUNTER
Van Clief
Zechner
Liu

STATUS
UNRESOLVED

EXPERIMENT
Nortropic benchmark A/B

A = context-stage single model
B = role-separated agents

measure:
quality
cost
time
human intervention
coordination failures
```

Detta är en **levande vetenskaplig metod för Nortropic**.

Och det är mycket bättre än att vi två argumenterar om vilken bloggare som låter mest övertygande.

---

# 19. Jag skulle kalla det **Nortropic Thesis Ledger**

Varje viktig idé blir ett claim-objekt.

Exempel:

```text
THESIS-0042

CLAIM
Persistent work state should live
outside model memory.

CONFIDENCE
0.92

SUPPORT
Anthropic Managed Agents
Gas Town / Beads
OpenAI Symphony
ICM artifacts

COUNTER-EVIDENCE
none significant

NORTROPIC STATE
already mostly aligned

ACTION
KEEP
```

Annat exempel:

```text
THESIS-0043

CLAIM
Dedicated reviewer agents improve
quality enough to justify their cost.

CONFIDENCE
0.58

SUPPORT
Anthropic generator/evaluator harness

COUNTER
stronger models may self-review
Van Clief
minimal-harness camp

ACTION
EXPERIMENT

NEXT REVIEW
when Claude/Codex generation changes
```

Detta gör vår arkitektur **epistemisk**.

Vi vet inte bara *vad* Nortropic gör.

Vi vet:

> **Varför vi tror att det är rätt och vilken evidence som skulle få oss att ändra oss.**

Det vore ett mycket moget lager.

---

# 20. Sedan skulle jag bygga fyra bevakningskadencer

Inte en enorm daglig rapport.

## Continuous — machine only

```text
GitHub events
releases
papers
RSS
blogs
changelogs
trusted people
```

Ingen människa behöver se det.

---

## Daily — exceptions only

Du får bara något om:

```text
HIGH SIGNAL
```

Exempel:

> **ADOPT CANDIDATE**
>
> Anthropic och två oberoende builders har gått mot samma pattern.
>
> Nortropic berörs i `context/reviewer orchestration`.
>
> Confidence: HIGH.
>
> Experiment rekommenderas.

---

## Weekly — Frontier Synthesis

Inte “17 saker hände”.

Utan:

```text
WHAT CHANGED IN OUR MODEL OF THE WORLD?
```

Exempel:

### Emerging thesis
Repo-legibility verkar bli viktigare än custom agent prompts.

### Evidence
5 independent sources.

### Nortropic implication
Potential deletion of X/Y/Z.

### Counterargument
Carlini shows orchestration still matters at high parallelism.

### Next experiment
Cold-start agent benchmark.

---

## Monthly — Architecture Review

Fråga systematiskt:

```text
What can we DELETE?

What assumption became false?

What new capability appeared?

What is now cheaper?

What is now safer?

What is now measurable?

What did we repeatedly correct?

What does everyone suddenly converge on?
```

Det är här research faktiskt förbättrar systemet.

---

# 21. Jag skulle dessutom ha en **Nortropic Anti-Hype Agent**

Den är viktig.

Den får varje föreslagen innovation och försöker döda den.

Exempel:

> “Gas Town har 17k stars!”

Anti-hype svarar:

```text
Stars ≠ quality.

Can we reproduce claims?
Is architecture needed at our scale?
Does it solve a Nortropic problem?
Could Claude now do this natively?
What is maintenance cost?
What assumptions does it introduce?
What is the simplest competing solution?
```

Anthropics egna harness-experiment visade varför detta är viktigt: deras första avancerade version gav bättre output men var över 20× dyrare än solo-körningen, och de behövde sedan ablationstesta vilka delar som faktiskt var load-bearing. citeturn922487search2

**Innovation utan deletion pressure producerar bara mer system.**

---

# 22. Och en **Weak Signal lane**

Här får vi med:

- små Substacks
- små GitHub-repos
- nya arXiv papers
- GitHub Discussions
- HN
- Reddit
- podcasts
- YouTube transcripts
- X/LinkedIn.

Men:

```text
WEAK SIGNAL
≠
EVIDENCE
```

De används bara för discovery.

Sedan försöker systemet hitta:

```text
paper?
code?
experiment?
primary source?
reproduction?
independent convergence?
```

Jake Van Clief börjar kanske som weak signal.

När vi hittar paper + metod + andra liknande observationer:

```text
WEAK SIGNAL
      ↓
CANDIDATE THESIS
```

Det är precis den transformation vi gjorde manuellt.

---

# 23. Den ännu större idén: **Nortropic kan själv leta efter sina framtida lärare**

Vi börjar med:

```text
SEED PEOPLE
├── Van Clief
├── Lopopolo
├── Karpathy
├── Ronacher
├── Zechner
├── Liu
├── Yegge
├── Carlini
├── Husain
├── Shankar
├── Willison
├── Litt
├── Ball
├── Huyen
└── swyx
```

Sedan analyserar vi kontinuerligt:

```text
Who do they cite?

Whose repos do they star?

Whose papers do they mention?

Who do they disagree with?

Who appears repeatedly before
an idea becomes mainstream?
```

Efter ett år kan vi ha:

```text
SOURCE REPUTATION GRAPH

person
 ↓
claims
 ↓
predictions
 ↓
evidence
 ↓
eventual outcome
```

Då kan systemet börja upptäcka:

> “Den här personen har vid fyra tidigare tillfällen identifierat agent-infrastrukturförändringar 2–4 månader innan de nådde mainstream.”

### Det börjar likna technological intelligence på riktigt.

---

# 24. Open source-radarn kan göra samma sak

Inte bara:

```text
repo → stars
```

utan:

```text
repo
├── ideas introduced
├── architectural patterns
├── influential contributors
├── forks
├── dependencies
├── downstream adoption
├── release velocity
├── reliability
├── documentation quality
└── later influence
```

Vi kan då upptäcka:

> “Det här lilla 300-star-repot introducerade ett pattern som nu finns i fem 20k-star-projekt.”

**Det är mycket mer värdefullt än trending.**

---

# 25. Jag ser alltså ett nytt Nortropic-system

Jag skulle tills vidare kalla det:

# **Nortropic Frontier Observatory**

med sex komponenter:

```text
1. PEOPLE RADAR
   thinkers / builders / contrarians

2. OSS RADAR
   GitHub / GH Archive / repositories

3. RESEARCH RADAR
   papers / labs / benchmarks

4. THESIS ENGINE
   claims / convergence / contradictions

5. FRONTIER DELTA
   what changed relative to Nortropic?

6. EXPERIMENT ENGINE
   prove before adopting
```

Och dess viktigaste output ska **inte** vara:

```text
research-report.md
```

utan:

```text
NO ACTION
```

eller:

```text
EXPERIMENT-017

Hypothesis:
single-model context topology can replace
three role-specific agent transitions.

Why now:
4 independent sources converge.

Affected Nortropic layer:
provider harness.

Trust Kernel impact:
NONE.

Smallest experiment:
...

Success metric:
...

Kill criteria:
...
```

Det är precis så jag skulle vilja att ett världsledande självförbättrande system beter sig.

---

## Min prioritering

Jag skulle **inte börja med att bygga hela GitHub-scrapern**.

Första versionen bör vara mycket enklare:

```text
V0
│
├── curated 15–25 people
├── OpenAI / Anthropic / Amp / Cursor / GitHub
├── Good AI List
├── GitHub targeted searches
├── selected arXiv/OpenReview streams
│
↓
weekly synthesis
│
↓
Thesis Ledger
│
↓
Nortropic Delta
│
↓
experiments
```

När vi ser att denna process faktiskt hittar värdefulla förändringar bygger vi:

```text
V1
GH Archive firehose
+
automatic people discovery
+
repo acceleration detection
+
convergence detection
```

Och först därefter kanske:

```text
V2
fully autonomous R&D loop
```

Då har vi egentligen byggt något som motsvarar:

> **ett autonomt CTO/R&D-labb vars uppgift är att göra Nortropic mindre fel varje vecka.**

Det tycker jag är en mycket stark riktning.

Vi har redan automationen **Bevaka Frontier AI Engineering**. Nästa logiska steg skulle vara att bredda just den till **People Radar + OSS Radar + Thesis/Contradiction detection** snarare än att skapa ännu en separat nyhetsbevakning. Om du vill kan jag ta nästa steg och göra en **full design för Nortropic Frontier Observatory** — sources, person-watchlist, GitHub-query-strategi, scoring, Thesis Ledger, agents/loops och exakt vad som ska automatiseras kontra ligga utanför systemet. memcite

---

## Meddelande 15 — Johnny (användare)

Vi tar alltid fulla steg, next level, det är så vi arbetar

---

## Meddelande 16 — ChatGPT (assistent)

Då ändrar jag angreppssättet: **ingen V0 som bara sammanfattar några källor**. Vi designar slutarkitekturen först — ett fullskaligt **Nortropic Frontier Observatory** som kan upptäcka människor, idéer, papers, repos och konvergerande mönster, falsifiera dem, koppla dem mot Nortropics faktiska arkitektur och driva mätbara experiment. Sedan kan implementationen ske i slices, men **målbilden kompromissas inte ned**.

---

## Meddelande 17 — ChatGPT (assistent)

Det finns en princip jag vill låsa redan nu: **Observatory ska inte vara en separat “research-bot” bredvid Nortropic.** Det ska vara Nortropics externa perceptions- och evolutionslager. OpenAI:s erfarenhet är att den verkliga hävstången kommer när feedback, observability och återkommande cleanup blir delar av själva engineeringmiljön, inte sidoprocesser. 

Och GitHub-delen ska byggas som ett teleskop: GH Archive/BigQuery för bred discovery, GitHub API endast för selektiv enrichment och kodinspektion. GitHubs egna eventflöden kan ha upp till timmars latency och API/search har separata rate limits, medan GH Archive redan exponerar den publika eventströmmen timvis i BigQuery.

---

## Meddelande 18 — ChatGPT (assistent)

Bra. Då släpper vi tanken på en liten “bevakningsagent”. **Målbilden ska vara ett autonomt teknologiskt intelligens- och evolutionssystem för Nortropic.**

Jag skulle kalla det:

# **Nortropic Frontier Observatory**
### External perception → epistemic reasoning → experimentation → evolution

Det ska inte svara på frågan *“vad har hänt inom AI?”*.

Det ska svara på:

> **Vad har förändrats i världen som gör att något Nortropic tror, bygger eller gör inte längre är optimalt — och hur bevisar vi vad vi bör göra istället?**

Det är en fundamental skillnad.

---

## 1. Observatory blir Nortropics “yttre nervsystem”

Jag ser egentligen Nortropic som tre stora system:

```text
                         THE WORLD

        people · GitHub · papers · labs · products
                 ↓                ↓
       ┌───────────────────────────────────┐
       │ NORTROPIC FRONTIER OBSERVATORY   │
       │ perception + scientific learning │
       └─────────────────┬─────────────────┘
                         ↓
                  new knowledge
                  new hypotheses
                  falsification
                         ↓
       ┌───────────────────────────────────┐
       │ NORTROPIC ENGINEERING OS         │
       │ specs · tasks · evals · builds   │
       └─────────────────┬─────────────────┘
                         ↓
       ┌───────────────────────────────────┐
       │ NORTROPIC TRUST KERNEL           │
       │ authority · gates · promotion    │
       └───────────────────────────────────┘
```

**Observatory får observera, resonera, experimentera och rekommendera.**

Det får **inte** själv bli trust authority.

Det passar dessutom din befintliga arkitektur: `nortropic-knowledge` är uttryckligen icke-auktoritativt och får inte bli runtime- eller verification dependency. fileciteturn10file0L1-L2

Så jag skulle **inte lägga Observatory-runtime i knowledge-repot**.

Jag skulle sannolikt ha:

```text
Nortropic/frontier-observatory
        │
        ├── discovers
        ├── analyzes
        ├── experiments
        └── produces evidence
                 ↓
Nortropic/nortropic-knowledge
        durable knowledge
                 ↓
Nortropic/innovation-intake
        actionable candidates
                 ↓
Nortropic/nortropic-system
        accepted implementation
        through existing authority
```

Det är en mycket ren separation.

---

# 2. Sensor Mesh — inte en RSS-läsare

Första lagret ska vara ett **massivt heterogent sensorsystem**.

```text
                         SENSOR MESH

 Official labs       People           Research
───────────────    ─────────────    ─────────────
OpenAI             Van Clief         arXiv
Anthropic          Karpathy          OpenAlex
GitHub             Lopopolo          OpenReview
Google DeepMind    Ronacher          papers
Cursor             Zechner           citations
Amp                Liu
...                Yegge
                   Carlini
                   ...

 GitHub universe       Communities        Nortropic itself
────────────────    ───────────────     ────────────────
GH Archive          HN                  architecture
Repos               blogs               failures
PRs                 podcasts            eval results
Issues              discussions         human corrections
Releases            weak signals        bottlenecks
```

Researchradarn kan använda OpenAlex för author-, work-, topic- och citation graphs; OpenAlex exponerar uttryckligen både citationer, related works och authorrelationer via API. citeturn803953search0turn803953search2

Det innebär att vi inte behöver känna till nästa Van Clief i förväg.

Systemet kan hitta honom.

---

# 3. People Radar måste vara **självexpanderande**

Vi seedar kanske 30–50 människor.

Men de är bara startpunkter.

Observatory bygger sedan en graf:

```text
             Jake
              │
           cites
              ↓
           Person B
           /      \
       paper      repo
         │          │
      cited by   forked by
         │          │
      Person C   Person D
          \        /
           \      /
          same idea
              ↓
       emerging cluster
```

En person börjar få hög signal om exempelvis flera oberoende starka källor börjar hänvisa till personen, deras idéer föregår senare adoption, de publicerar reproducerbara experiment eller deras repos börjar påverka andra relevanta repos.

### Viktigt:

Vi rankar **inte personer efter followers**.

Vi bygger en långsiktig:

# **Source Reputation Model**

som exempelvis innehåller:

```text
Originality
Empirical rigor
Reproducibility
Predictive track record
Technical depth
Independence
Correction behavior
Signal-to-noise
Nortropic relevance
```

Då kan en okänd researcher med 700 följare rankas över en AI-influencer med 700 000.

---

# 4. GitHub blir ett riktigt teknologiskt teleskop

Här tycker jag din ursprungliga idé är helt rätt, men vi ska göra den större.

Vi ska **inte kontinuerligt clone:a hela GitHub**.

GitHubs egna event-endpoints kan ha mellan ungefär 30 sekunders och sex timmars latency, och Search API har striktare rate limits än vanlig REST. citeturn803953search5turn803953search8

I stället:

```text
                  ALL PUBLIC GITHUB
                         ↓
                    GH ARCHIVE
                 hourly event stream
                         ↓
                       SQL
                         ↓
                 SIGNAL DETECTION
                         ↓
                  100k candidates
                         ↓
                  metadata filter
                         ↓
                    1k repos
                         ↓
                  semantic filter
                         ↓
                     50 repos
                         ↓
                deep repo inspection
                         ↓
                     1–5 ideas
```

GH Archive har den publika GitHub-eventströmmen och gör hela datasetet tillgängligt i BigQuery med timvisa uppdateringar. citeturn803953search1turn803953search26

Sedan använder Observatory GitHub API endast för **precision enrichment**.

---

# 5. OSS Radar ska inte primärt hitta populära repos

Det mest intressanta är **förändringshastighet och diffusion**.

Observatory kan upptäcka:

```text
star acceleration

fork acceleration

new high-quality contributors

release acceleration

rapid PR activity

cross-repo contributor migration

new architectural vocabulary

new recurring folder structures

new AGENTS.md patterns

new eval frameworks

new skills conventions

new observability patterns

new context/memory mechanisms

new orchestration mechanisms
```

Säg att 40 relativt bra agentprojekt inom tre månader oberoende börjar introducera:

```text
beliefs.md
progress.md
AGENTS.md
evals/
skills/
```

Det är i sig en signal.

### Observatory ska upptäcka patterns **mellan repos**, inte bara repos.

Det är en mycket större idé.

---

# 6. Vi bygger ett **Idea Lineage Graph**

Anta att detta inträffar:

```text
Feb
small repo introduces pattern X

Mar
researcher describes X

Apr
three projects adopt X

May
Anthropic describes related mechanism

Jun
OpenAI ships equivalent idea
```

Ett vanligt bevakningssystem säger:

> OpenAI lanserade X.

Observatory säger:

> **Pattern X first appeared ~4 months earlier.**
>
> Origin cluster: ...
>
> Adoption velocity increasing.
>
> Frontier-lab validation now present.
>
> Nortropic exposure: ...
>
> Recommended action: ...

Det ger Nortropic möjlighet att ligga **före mainstream**, inte reagera på den.

---

# 7. Kärnan blir inte en knowledge graph — utan en **Thesis Graph**

Det här tycker jag är viktigast.

Vi samlar inte bara:

```text
papers
people
repos
articles
```

Vi extraherar:

```text
CLAIMS
```

Exempel:

```text
CLAIM-0193

Dedicated multi-agent reviewer
architectures improve software
quality enough to justify their cost.
```

Sedan:

```text
SUPPORTS
Anthropic harness experiment

CONTRADICTS
Van Clief
Jason Liu
some ablation study

QUALIFIES
Carlini:
parallel agents useful at sufficient decomposition

NORTROPIC EXPOSURE
reviewer architecture

CONFIDENCE
0.61

STATUS
UNRESOLVED
```

Detta är **Nortropic Thesis Ledger**.

---

# 8. Observatory ska upptäcka **Convergence**

Detta är en av de mest värdefulla maskinerna.

Exempel:

```text
Van Clief
    ↓
context > agents

Zechner
    ↓
minimal harness

Jason Liu
    ↓
avoid unnecessary multi-agent systems

Anthropic
    ↓
harness assumptions become stale

Amp
    ↓
agent wrapper is becoming less important
```

Ingen källa ensam behöver ha rätt.

Men fem relativt oberoende källor ger:

```text
CONVERGENCE CLUSTER #41

THESIS:
Increasing model capability is shifting
engineering leverage from orchestration
toward context/environment design.

INDEPENDENT SOURCES: 5

EVIDENCE QUALITY: HIGH

TREND VELOCITY: RISING

NORTROPIC EXPOSURE:
custom orchestration
agent roles
context routing

RECOMMENDATION:
ABLATION EXPERIMENT
```

Anthropic ger oss dessutom en stark princip här: varje harness-komponent kodar ett antagande om vad modellen inte klarar själv; när modeller förbättras måste dessa antaganden stress-testas och komponenter metodiskt tas bort. citeturn588556search1turn588556search4

---

# 9. Lika viktigt: **Contradiction Engine**

Observatory får aldrig bara leta konsensus.

Exempel:

```text
THESIS
"Multi-agent is unnecessary"

         VS

Carlini
16 agents
~2,000 sessions
100k-line C compiler
Linux compilation
```

Anthropics experiment visar att massiv parallellisering faktiskt kan lösa en mycket stor uppgift, men också var decomposition, tests och coordination blir avgörande. citeturn588556search8

Då blir output:

```text
CONTRADICTION DETECTED

Possible synthesis:

Sequential cognitive workflow
→ context topology may dominate.

Highly parallel decomposable workflow
→ explicit multi-agent orchestration
may dominate.

UNKNOWN:
transition point.

EXPERIMENT NEEDED.
```

### Det är forskning.

Inte content aggregation.

---

# 10. Nästa lager är **Nortropic Delta Engine**

Varje stark claim jämförs maskinellt mot Nortropics faktiska state.

Inte:

> “Intressant artikel om context engineering.”

Utan:

```text
WORLD CHANGE
       ↓
assumption matching
       ↓
NORTROPIC ASSUMPTION #74
"review requires persistent role agent"
       ↓
potential contradiction
       ↓
affected:
agents/reviewer
orchestrator
task lifecycle
       ↓
trust boundary affected?
NO
       ↓
candidate ablation
```

Jag skulle ha särskilda klasser:

```text
NEW_CAPABILITY
ASSUMPTION_INVALIDATED
COMPONENT_POTENTIALLY_OBSOLETE
NEW_BEST_PRACTICE
NEW_RISK
NEW_MEASUREMENT
NEW_ABSTRACTION
NEW_PRODUCT_POSSIBILITY
DELETE_OPPORTUNITY
```

**DELETE_OPPORTUNITY** ska vara förstaklassmedborgare.

Det är kritiskt.

---

# 11. Observatory behöver en **Anti-Hype Engine**

Varje innovation får en adversariell analys.

Inte bara:

> “Coolt, implementera!”

utan:

```text
Is the evidence causal?

Is this just model improvement?

Is the author selling something?

Has anyone independently reproduced it?

Does this matter at Nortropic's scale?

Could native Claude/Codex already solve it?

What new maintenance does it create?

What can we DELETE instead?

Could the same outcome be reached
with a 20-line mechanism?

What evidence would falsify this?
```

Anthropic gjorde i praktiken exakt den typen av ablation på sitt långkörande harness: den första fulla konstruktionen gav mycket bättre output men kostade över 20× solo-runnen, så de började metodiskt ta bort komponenter och mäta vad som faktiskt var load-bearing. citeturn588556search1

Det är en mycket bra Nortropic-princip:

> **Innovation must survive deletion pressure.**

---

# 12. Sedan kommer **Experiment Engine**

Ingen arkitekturförändring får gå direkt:

```text
article
 ↓
ADOPT
```

utan:

```text
signal
 ↓
thesis
 ↓
evidence
 ↓
counter-evidence
 ↓
Nortropic impact
 ↓
experiment
 ↓
measurement
 ↓
decision
```

Karpathys `autoresearch` är en väldigt ren illustration av den grundprincipen: agenten modifierar något, kör ett tidsbegränsat experiment, mäter resultatet och behåller eller förkastar ändringen. citeturn447763search3turn447763search5

Nortropic-versionen blir mycket bredare.

Exempel:

```text
EXP-0081

THESIS
Context-projected reviewer
can replace dedicated reviewer role.

BASELINE
current reviewer architecture

VARIANT
same model + verification workspace

MEASURE
quality
defects detected
false positives
tokens
wall time
human intervention
context usage

TRUST KERNEL
unchanged

SUCCESS
>= current quality
-30% complexity
-20% cost

FAILURE
missed frozen negative controls
```

Sedan får verkligheten avgöra.

---

# 13. Vi ska dessutom låta **experimenten förbättra researchern**

Det är nästa nivå över Karpathy.

Observatory ska registrera:

```text
prediction before experiment

confidence before experiment

result

prediction error

why prediction was wrong

which source was overweighted

which source was underweighted
```

Efter 500 experiment får vi alltså inte bara ett bättre Nortropic.

Vi får en bättre **Nortropic epistemology**.

Systemet lär sig exempelvis:

> GitHub-star acceleration har nästan inget prediktivt värde för oss.

eller:

> Anthropic engineering + två independent builder reproductions har historiskt 78 % adoption yield.

Det är fantastiskt värdefullt.

---

# 14. Då kan vi skapa **Source Alpha**

Som inom investering.

Inte ekonomisk alpha, utan:

> Hur ofta ger denna källa information tidigare och bättre än mainstream?

Exempel:

```text
SOURCE: Person X

novel claims:       31
later validated:    19
Nortropic relevant: 11
successful exp:      7
false signals:       4

FRONTIER ALPHA:
HIGH
```

Observatory kan därefter lägga mer discovery-budget runt deras nätverk.

### Det är så nästa Van Clief hittas automatiskt.

---

# 15. Och en egen **Nortropic Assumption Registry**

Det här saknas i nästan alla system.

Alla viktiga arkitekturval bör i slutänden kunna uttryckas som:

```text
ASSUMPTION-034

We believe:
Independent role-separated review
outperforms same-session self-review.

Why:
evidence ...

Introduced:
2026-...

Confidence:
HIGH

Depends on:
current provider capability

Falsified if:
...

Next mandatory re-evaluation:
major Claude/Codex generation
```

När exempelvis Opus/Codex förbättras:

```text
MODEL CAPABILITY CHANGE
         ↓
search affected assumptions
         ↓
ASSUMPTION-034
ASSUMPTION-061
ASSUMPTION-083
         ↓
automatic re-evaluation candidates
```

Detta skulle vara **enormt kraftfullt**.

---

# 16. Observatory blir dessutom sin egen garbage collector

OpenAI beskriver att deras agent-first-team gick från att manuellt lägga en stor del av fredagarna på “AI slop” till återkommande Codex-jobs som letar avvikelser mot “golden principles”, uppdaterar quality grades och öppnar små refactoring-PR:er. citeturn588556search0

Vi kan tillämpa samma princip på själva Nortropic-intelligensen:

```text
stale thesis
duplicate claim
dead source
contradicted recommendation
obsolete experiment
stale architectural assumption
knowledge without provenance
unfollowed promising signal
```

Observatory städar sitt eget epistemiska lager.

---

# 17. Context Topology gäller även här

Vi ska **inte bygga 17 persona-agenter** för detta.

Van Clief-pappret argumenterar specifikt för att sekventiella workflows ofta kan representeras som filesystem/workspace-steg där samma modell får rätt kontext vid rätt moment, medan explicit multi-agent-infrastruktur reserveras för komplex concurrency. citeturn447763academia36

Så jag skulle tänka:

```text
same frontier model

      ↓ context projection

DISCOVER
      ↓
EXTRACT CLAIMS
      ↓
FALSIFY
      ↓
MAP TO NORTROPIC
      ↓
DESIGN EXPERIMENT
      ↓
EVALUATE RESULT
```

Om vi senare empiriskt bevisar att parallel specialist-agents ger lift:

då använder vi dem.

Inte för att arkitekturen “ser agentisk ut”.

---

# 18. Observatory ska ha en **kontrollplan**

OpenAI Symphony är relevant här eftersom de gjort projekt-/issue-boardet till kontrollplanet för coding agents snarare än att människan koordinerar enskilda sessioner. citeturn588556search2

Samma princip:

```text
Signal
 ↓
Candidate
 ↓
Investigating
 ↓
Thesis
 ↓
Experiment proposed
 ↓
Experimenting
 ↓
Adopt / Watch / Reject
 ↓
Re-evaluate
```

Claude/Codex-sessionen är tillfällig.

**Intelligence-objectet är permanent.**

---

# 19. Full autonom kadens

När målbilden är klar ser jag följande rytm:

| Kadens | Vad händer |
|---|---|
| **Kontinuerligt** | GitHub/publications/releases/people ingest |
| **Timvis** | dedupe, novelty, velocity, graph updates |
| **Dagligen** | exception detection + high-signal deep dives |
| **Veckovis** | convergence, contradiction och Frontier Delta synthesis |
| **Månadsvis** | architecture/assumption audit |
| **Vid modellrelease** | automatic harness-ablation review |
| **Kvartalsvis** | source reputation + Observatory calibration |
| **Kontinuerligt** | godkända experiment matas tillbaka till Thesis Ledger |

Det är här vår nuvarande **Bevaka Frontier AI Engineering** till slut bör bli bara notifieringsytan ovanpå ett mycket större system — inte själva intelligence-systemet.

---

# 20. Och Observatory själv måste evalueras

Annars bygger vi ännu en AI-maskin som producerar övertygande text.

Dess KPI:er bör snarare vara:

```text
Precision of alerts
Useful discoveries / total alerts

Time-to-signal
How early did we detect it?

Experiment yield
How many hypotheses produced measurable lift?

Adoption yield
How many ADOPT recommendations survived?

Deletion yield
How much obsolete Nortropic complexity was removed?

False-hype rate
How often did we chase nonsense?

Source diversity
Are we inside an echo chamber?

Prediction calibration
Does 80% confidence mean ~80% success?

Frontier lead
How early did Nortropic act
relative to mainstream adoption?
```

Den sista är spännande.

Vi kan faktiskt mäta:

# **Nortropic Frontier Lead**

---

# Slutmål

Det här är inte längre:

> “En agent som läser AI-nyheter varje dag.”

Det är:

```text
               NORTROPIC FRONTIER OBSERVATORY

                       OBSERVE
                          ↓
                       DISCOVER
                          ↓
                        MODEL
                          ↓
                       QUESTION
                          ↓
                       FALSIFY
                          ↓
                       SYNTHESIZE
                          ↓
                    FORM HYPOTHESIS
                          ↓
                       EXPERIMENT
                          ↓
                       MEASURE
                          ↓
                        LEARN
                          ↓
                       SIMPLIFY
                          ↓
                        EVOLVE
                          │
                          └──────────────↺
```

Och jag tror faktiskt att detta börjar ge oss en mycket starkare definition av **“självförbättrande Nortropic”**.

Inte ett system som själv skriver mer kod.

Utan:

> **ett system som kontinuerligt förbättrar sin egen modell av hur bra AI engineering bör bedrivas, testar den modellen mot verkligheten och förändrar sig när evidensen säger att den har fel.**

Det är nivån jag tycker vi ska sikta på. Implementation bör sedan ske i fullständiga vertikala slices, men **utan att reducera målarkitekturen till en leksaksversion först**. memcite

---

## Meddelande 19 — ChatGPT (assistent)

Det finns **tre nya signaler som klarar tröskeln** den här gången.

### **ADOPT — Event-driven autonomy börjar ersätta polling**
Den 19 augusti släppte Cursor en tydlig harness-förändring: cloud agents kan nu **prenumerera på PR-/Slack-events, hålla ett långlivat mål tills det är uppfyllt, och köra subagents i separata virtuella maskiner med ren kontext**. Agenten följer automatiskt sin egen PR, vaknar på CI-/review-events, rättar fel och fortsätter tills målet är klart. citeturn893059view1

Detta påverkar direkt Nortropics supervisor/autopilot-antagande: **en central loop behöver inte aktivt polla allt**. Mycket koordinering kan flyttas till event → wake → continue, medan TaskContract och Trust Kernel fortsatt äger authority.

Minsta nyttiga experiment: välj **en enda PR-livscykel** och ersätt pollingen med eventdriven återupptagning:

`candidate PR → CI/review event → runner wakes → remediation → frozen gate → next state`.

Mät wall time, antal onödiga agentstarter, tokens och koordinationsfel mot nuvarande loop. **Trust transitions ändras inte.**

### **EXPERIMENT — Claude Code har nu provider-native cross-session coordination**
Claude Code v2.1.236 släpptes den **19 augusti** och v2.1.237 den **20 augusti**. Den viktigaste Nortropic-signalen är inte output-style-förändringen utan `notify_when_idle`: en session kan be en annan session på samma maskin att skicka **en engångsnotis när den blir idle, utan polling**. Samtidigt har `/goal` fått automatiska check-ins när bakgrundsarbete blockerar målet. citeturn264228view1

Detta är nästan en direkt validering av Nortropics provider-neutral-harness-riktning: **ännu mer orchestration flyttar in i providerns runtime**. Varje sådan native primitive bör utlösa frågan “vilken egen Nortropic-mekanik kan nu tas bort?”.

Minsta experiment: två disposable Claude Code-sessioner, där `builder → notify_when_idle(reviewer)` ersätter exakt **en** supervisor-pollingkant. Jämför samma task med nuvarande mekanism. Om native primitive ger samma determinism utan att påverka authority kan den custom-koden bli en deletion candidate.

### **ADOPT — två nya security-regressioner bör in i Nortropics negativa kontroller**
Samma Claude Code-release hårdnade macOS-sandboxen så att wildcard read-denies som `**/.env` vinner även inne i annars tillåtna läsregioner och inte kan kringgås genom att döpa om filen. Auto mode ändrades också så att `git status` inte kan luras av repo-inställningen `status.showUntrackedFiles=no` att rapportera ett smutsigt repo som rent. citeturn264228view1

Detta träffar Nortropic mycket exakt: **protected-path semantics och clean-tree identity är trust inputs**. Jag skulle inte vänta med dessa principer till någon större redesign.

Nortropic bör ha negativa tester motsvarande:

```text
DENIED_SECRET_RENAMED_INSIDE_ALLOWED_ROOT → STILL_DENIED

git config status.showUntrackedFiles no
+ untracked protected/relevant file
→ WORKTREE_CLEAN must NOT become true
```

GitHub Agentic Workflows ger dessutom oberoende konvergens kring samma filosofi. Version 0.87.0, släppt 16 augusti, utökade confused-deputy-skydd, stärkte runtime-isoleringen med cloud-hypervisor och fortsätter modellen där agenten arbetar read-only och privilegierade GitHub-skrivningar sker genom separat validerade **safe outputs**. citeturn709589search1turn709589search6

Det stärker snarare än utmanar Nortropics grundtes:

> **model intelligence får föreslå en transition; separat mekanik måste auktorisera och utföra den.**

### **ADOPT — “Notary”-mönstret är exakt den doc-gardener Nortropic behöver**
GitHub visade den 18 augusti ett återkommande workflow som dagligen korsvaliderar **schema ↔ typed implementation ↔ parser ↔ docs ↔ verkliga workflows**. På nio körningar hade det hittat nio olika verkliga konsistensfel, med exakta filer och rader. citeturn709589search2

Detta är mer relevant för Nortropic än ännu en dokumentationsagent. Med din växande authority-/besluts-/spec-yta bör en Nortropic Notary kontrollera exempelvis:

```text
TaskSpec ↔ exit gate
AGENTS.md ↔ faktisk runtime
docs ↔ implementation
model-routing contract ↔ launcher
allowed_write ↔ faktisk write surface
reference SHA ↔ faktisk authority
```

Den ska inte “förbättra text”. Den ska **bevisa eller falsifiera att dokumentationen fortfarande säger sanningen**.

### Frontier Delta

Det finns en tydlig konvergens i veckans signaler:

**Cursor:** event subscriptions + persistent goals + isolated subagents. citeturn893059view1  
**Claude Code:** cross-session messaging, idle notification och provider-native goal continuation. citeturn264228view1  
**GitHub:** eventdrivna agentic workflows + isolated runtime + safe-output separation. citeturn709589search1turn709589search6

Min syntes är att en Nortropic-premiss börjar bli allt starkare:

> **Orchestration intelligence bör flyttas ned till provider/GitHub-native primitives när de finns; Nortropic ska koncentrera sin egen kod på durable task state, provenance, containment, deterministic gates och trusted promotion.**

Det innebär att nästa generation av Nortropic sannolikt bör innehålla **mindre polling och mindre egen agent-lifecycle-kod**, inte mer. memcite
