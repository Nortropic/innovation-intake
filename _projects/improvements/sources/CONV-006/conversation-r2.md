# Agent Control-Room Watch — fullständigt transkript

**Källprojekt:** Improvements (ChatGPT-projekt)
**Chatt:** Agent Control-Room Watch
**URL:** https://chatgpt.com/c/6a8ac6dc-4314-83eb-9c3b-fbd4e6405bbd
**Exportdatum:** 2026-09-01
**Antal meddelanden:** 16 (3 användare, 13 assistent)
**Syfte:** Brainstorm om en AI-native scrum- och kontrollrumsyta för Nortropic samt bevakning av nya agentmönster.

**Innehåll i korthet:** Samtalet öppnar med: ”Nåt jag har reflekterat över är scrum så jag hade vela ha för att lättare hålla isär alltihop, vi har tidigare arbetat med dokumentationen m” och avslutas med: ”Ja — **en ny förändring runt OpenAI Codex 0.152.0, publicerad 1 september 2026, är tillräckligt viktig för att påverka Factory Room-designen”

> Notis: rader som ser ut som käll-/citat-chips från ChatGPT är en del av
> originaltexten och har bevarats ordagrant. 2 bilagor inventerade (73e0fc06-3694-4442-819e-7c3f1f9ecc39.png samt sediment-bild-/filreferenser); innehållet ej infångat i svepet.

---

## Meddelande 1 — Johnny (användare)

Nåt jag har reflekterat över är scrum så jag hade vela ha för att lättare hålla isär alltihop, vi har tidigare arbetat med dokumentationen men arbeta innovativt med en scrum skulle också vara hjälpsamt tycker jag för Nortropic. Brainstorma kring detta.

---

## Meddelande 2 — ChatGPT (assistent)

Ja — och jag tror faktiskt att du sätter fingret på ett lager som Nortropic saknar. Dokumentationen vi byggt ger oss **minne, kontrakt och source of truth**, och de autonoma looparna ger oss **execution**. Men mellan dem saknas fortfarande en riktigt bra **visuell kontrollpanel för vad som pågår just nu**.

Jag skulle därför inte införa klassisk Scrum rakt av. Jag skulle bygga en **AI-native variant för Nortropic**, där vi tar det bästa från Scrum, Kanban, Shape Up och Linear och kopplar det direkt till GitHub och våra autonoma agenter.

## Tänk “Nortropic Mission Control”, inte Jira

Bilden från *Silicon Valley* är faktiskt en ganska bra mental modell. Man tittar på väggen och förstår nästan omedelbart: *vad finns, vad gör vi, vad sitter fast och vad är akut?*

Scrum har några väldigt värdefulla grundidéer: ett övergripande Product Goal, ett Sprint Goal och kontinuerlig transparens → inspektion → anpassning. En sprint är dessutom uttryckligen tänkt som en kort period där idéer omvandlas till värde. citeturn769637search1turn769637search34 Men Nortropic skiljer sig från ett vanligt Scrum-team: vi har autonoma builders, verifierare, research, dokumentation, checkpoints, immutable commits och ibland arbete som löper i minuter medan andra frågor tar veckor.

Därför skulle jag bygga något mer i den här riktningen:

```text
                         NORTROPIC MISSION CONTROL

              NORTH STAR / CURRENT INITIATIVES / HEALTH

                 CURRENT CYCLE GOAL
    "Close Bootstrap → First Real Autonomous Launch"

┌──────────────────┬─────────┬─────────┬───────────┬───────────┬──────────┐
│ AREA             │ SHAPING │ READY   │ EXECUTING │ VERIFYING │ FROZEN   │
├──────────────────┼─────────┼─────────┼───────────┼───────────┼──────────┤
│ Autonomy         │         │         │     ●     │     ●     │    ●     │
│ Kernel/Governance│         │    ●    │           │     ●     │    ●     │
│ Providers        │    ●    │    ●    │           │           │          │
│ R&D / Frontier   │    ●    │         │           │           │          │
│ Knowledge        │         │    ●    │           │           │    ●     │
│ Verkstadsgolvet  │         │         │           │           │          │
└──────────────────┴─────────┴─────────┴───────────┴───────────┴──────────┘

              ⚠ BLOCKED / EMERGENCY
              ◉ HUMAN DECISION QUEUE
              ◉ AGENT-SAFE QUEUE
```

Det viktiga är att detta **inte blir ytterligare ett system som måste hållas synkroniserat manuellt**.

Det är snarare en vy ovanpå verkligheten.

## Den stora idén: en datamodell, många vyer

Jag skulle absolut inte skapa fem separata Scrumboards för fem delar av Nortropic. Då har vi om några månader exakt det problem du försöker lösa.

GitHub Projects passar väldigt bra som själva kontrollplanet eftersom ett organisation-level Project kan innehålla issues och PR:er från olika repos, ha egna metadatafält, iterationer, board/table/roadmap-vyer och automatisering. Samma underliggande work item kan alltså visas på helt olika sätt utan att dupliceras. citeturn769637search0turn769637search3turn769637search14

Jag skulle exempelvis ha vyerna **Control Room**, **Current Cycle**, **By Förvaltning**, **Roadmap**, **R&D / Innovation**, **Autonomy Queue** och **Frozen Checkpoints** — men de är alla olika fönster in i samma data.

Det passar också väldigt bra ihop med vår tidigare kommunmodell. Nortropic är kommunen; Autonomy, R&D, Verkstadsgolvet osv är förvaltningarna; Mission Control är kommunledningskontoret som visar hela läget.

## Och här kommer den mer radikala AI-delen

Ett vanligt Scrumkort säger ungefär:

> Implementera authentication.

Ett Nortropic-kort borde snarare vara ett **exekverbart arbetskontrakt**.

Kortet känner till varför arbetet görs, vilket mission det tillhör, vilket repo det gäller, nästa gate, vem eller vilken agent som äger det, om det är agent-safe, vilka writes som är tillåtna, vad som blockerar det och framför allt **vilket bevis som krävs för att arbetet ska räknas som klart**.

Det betyder att kolumnen `DONE` nästan försvinner.

Vi har istället:

**EXECUTING → VERIFYING → FROZEN**

Och `FROZEN` får helst inte sättas genom att Johnny drar ett kort med musen. Det sätts när systemet kan visa exempelvis verifier PASS + rätt commit + publicerad checkpoint + inga kontraktsbrott.

Det är väldigt Nortropic.

Scrum Guide kopplar Definition of Done till det färdiga incrementet. citeturn769637search10 Vi kan ta den principen mycket längre: **Done becomes cryptographically/evidentially grounded rather than declarative.**

## Jag skulle dessutom separera tre olika klockor

Det här tror jag är en av de viktigaste avvikelserna från traditionell Scrum.

**Strategiska klockan** kan vara ungefär 6–12 veckor: vart Nortropic är på väg. Exempelvis Bootstrap → Autonomous Production → Verkstadsgolvet Production → nästa större capability.

**Människoklockan** kan vara en 1-veckas Nortropic Cycle. Där bestämmer du vad som förtjänar din uppmärksamhet just nu.

**Agentklockan** är event-driven och kan gå kontinuerligt. Claude/Codex/controller behöver inte vänta på nästa Daily Scrum för att ta nästa steg.

Linear gör något liknande konceptuellt genom att använda Cycles för momentum snarare än att koppla dem till releaser, och rekommenderar vanligtvis tvåveckorscykler samtidigt som de betonar att det är rytmen, inte “sprintandet”, som är poängen. citeturn430187search0turn430187search7 För Nortropic tror jag en vecka kan fungera bättre eftersom agenternas feedbackloop är så mycket snabbare.

Resultatet blir att du inte försöker köra Scrum i samma hastighet som AI-systemet.

## Det mest intressanta WIP-limitet är inte agenternas

Här skulle jag göra något ganska ovanligt.

Traditionell Kanban begränsar Work In Progress och mäter bland annat Work Item Age, throughput och cycle time. citeturn430187search6turn430187search8 Det är bra och vi bör göra det.

Men Nortropics knappaste resurs är i längden sannolikt inte Claude-tokens eller CPU.

Det är **din uppmärksamhet och beslutskapacitet**.

Därför skulle Mission Control ha ett förstaklassmått:

**HUMAN DECISION WIP**

Om fem agenter arbetar autonomt kan det vara helt okej. Om femton frågor samtidigt kräver att du läser 800 rader rapporter och fattar arkitekturbeslut har systemet misslyckats.

Jag skulle kanske sätta ett initialt tak på ungefär **tre samtidiga ägarbeslut**. Resten köas.

Det innebär också att en controller kan arbeta som något av en automatisk Scrum Master:

```text
WIP too high?
→ stop new admission

Task aging?
→ investigate

Verification repeatedly RED?
→ escalate pattern

Agent needs architecture decision?
→ HUMAN DECISION

Task lacks evidence contract?
→ cannot enter READY

No relation to current initiative?
→ return to SHAPING / ICEBOX
```

Det börjar plötsligt bli mer än en Scrumboard. Det blir **governance för en organisation av människor och AI-agenter**.

## Shape Up passar också oväntat bra här

Basecamps Shape Up skiljer uttryckligen på **shaping** och **building**, där shaping kan pågå utanför själva byggcykeln. citeturn769637search33

Det passar väldigt väl med hur Nortropic redan håller på att utvecklas.

En Frontier-agent kan hitta någonting intressant på GitHub eller i ny AI-forskning. Det går inte direkt till Claude Code.

Det går:

```text
DISCOVER
   ↓
SHAPE
   ↓
EVALUATE
   ↓
READY
   ↓
EXECUTE
   ↓
VERIFY
   ↓
FREEZE
   ↓
OBSERVE
```

Och det är viktigt, eftersom vår Innovation Intake då fortsätter vara **idé- och researchplanet**, medan Scrum/Mission Control blir **executionplanet**.

Dokumentationen blir **knowledgeplanet**.

Git blir **evidenceplanet**.

Autopiloten blir **execution engine**.

Mission Control blir **control plane**.

Det är en ganska ren arkitektur.

## Jag skulle också göra “Icebox” brutal

Här tycker jag Linear har en sund idé: deras metod rekommenderar en hanterbar backlog i stället för att samla varje idé för evigt. citeturn430187search0

Nortropic kommer sannolikt få motsatt problem mot vanliga utvecklingsteam. Med research-agenter och brainstorming kan vi producera **fler bra idéer än vi någonsin kan implementera**.

Så `ICEBOX` ska inte betyda “to-do later”.

Det betyder snarare:

**Inte värd vår uppmärksamhet nu.**

Sedan kan saker återuppstå om Frontier Delta hittar ny evidens som gör dem relevanta igen.

## Jag skulle inte använda story points

Det tror jag blir direkt missvisande i en AI-native utvecklingsorganisation.

En uppgift som kostar Claude 25 minuter idag kan ta Codex fyra timmar imorgon därför att ett säkerhetskontrakt spricker. Modellernas kapacitet förändras dessutom över tid.

Jag skulle hellre mäta verkligt flow: **Work Item Age, Blocked Age, Cycle Time, Throughput, Verification Fail Rate, Rework Rate, Human Intervention Rate och Autonomous Completion Rate**. Kanban rekommenderar just faktisk flow-data som WIP, work-item age och throughput som centrala signaler. citeturn430187search6

Och jag skulle uttryckligen använda metrics som **diagnostik**, inte som något agenten försöker maximera.

Annars kommer vi förr eller senare skapa Goodhart-problem.

## Om jag placerar bootstrapen på den här kartan

Med den senaste bootstrap-checkpoint vi arbetat med skulle hela den enorma processen du ibland upplever som svår att överblicka plötsligt reduceras till ungefär:

```text
INITIATIVE
Autonomous Bootstrap

CURRENT CYCLE GOAL
Close provider boundary → green gates → resume supervisor
→ first real autonomous launch

EXECUTING
R116 provider confinement / staging capability

VERIFYING
H032 / H031 security + effect contracts

NEXT / READY
Provider-neutral result core
Supervisor resume
First real autonomous launch

FROZEN
R113 and previous verified checkpoints

HUMAN DECISION
Only genuine owner-policy decisions appear here
```

Det är precis därför jag tror din Scrum-idé är värdefull.

Det vi bygger är tekniskt väldigt komplext, men **du ska inte behöva bära komplexiteten i huvudet för att förstå läget**.

Mission Control ska komprimera hundratusentals rader kod, dokumentation, verifieringar, agentjournaler och commits till:

> **Vad försöker vi uppnå? Vad händer? Vad sitter fast? Vad behöver mig? Vad är bevisat klart?**

Det är nästan den viktigaste designprincipen.

## Min syntes

Jag skulle alltså **inte implementera Scrum**.

Jag skulle skapa **Nortropic Mission Control — ett evidence-driven, agent-native Scrum/Kanban control plane**.

Scrum bidrar med mål och inspektionsrytmen. Kanban bidrar med flow och WIP-kontroll. Shape Up bidrar med separationen mellan shaping och building. Linear bidrar med enkelhet, cycles, små work items och momentum. GitHub Projects ger oss den tekniska infrastrukturen med multi-repo-data, custom fields, iterations, roadmap, views och automation utan att vi behöver bygga ett nytt system. citeturn430187search0turn769637search3turn769637search4

Och sedan lägger vi Nortropics egen innovation ovanpå: **agent-safe queues, human-decision WIP, independent verification, machine-evidenced Done, immutable checkpoints och automatisk state synchronization.**

Det här känns dessutom som något som passar väldigt naturligt **direkt efter bootstrap**. När bootstrapen gör själva maskinen autonom behöver Mission Control bli instrumentpanelen där du styr maskinen. Nästa steg jag skulle vilja ta är därför att rita upp den **exakta Nortropic-boarden**, med alla kolumner, förvaltningar, fields, views, WIP-regler, agent-state transitions och hur GitHub Projects skulle kopplas till controller/Claude/Codex — som en riktig V1-spec innan vi bygger någonting. memcite

---

## Meddelande 3 — Johnny (användare)

Jag antar du kollade igenom repos på Github för inspiration?

---

## Meddelande 4 — ChatGPT (assistent)

Nej — **inte i det förra svaret**. Där utgick jag från vår tidigare Nortropic-kontext och jämförde den mot Scrum, Kanban, Shape Up, Linear och GitHub Projects. Jag tittade på publika principer/dokumentation, men jag gjorde **ingen faktisk repo-inspektion på GitHub**.

Och för just den här brainstormingen tycker jag egentligen att vi ska göra det. Annars riskerar vi att designa ett snyggt Scrum-lager ovanpå en föreställning om Nortropic, i stället för ovanpå **hur systemet faktiskt ser ut idag**.

En riktig nästa pass bör läsa igenom repona och kartlägga bland annat: befintliga task-specs och states, gates/checkpoints, agentroller, controller/supervisor-flöden, dokumentationsstrukturen, GitHub Issues/Projects/workflows, hur commits och verifieringar representerar status samt var information idag dupliceras eller saknar en tydlig “current state”.

Sedan skulle jag även vilja göra **två externa GitHub-svep**: dels etablerade engineering/project-management-system som Linear-liknande verktyg, Plane, Taiga, OpenProject, GitHub Projects-automation etc.; dels mer experimentella **AI-agent orchestration/repos** för att hitta idéer kring agent queues, machine-owned status, approval gates, observability och human-in-the-loop.

Då kan vi göra något mycket bättre än “Scrum för Nortropic”:

**Nortropic idag → identifierade koordinationsproblem → vad andra system löser bra → vad som inte passar AI-native utveckling → Nortropic-native Mission Control-arkitektur.**

Det är den analysnivå jag tycker vi ska använda innan vi bestämmer board, states eller implementation. memcite

---

## Meddelande 5 — Johnny (användare)

gör det

---

## Meddelande 6 — ChatGPT (assistent)

Ja. Nu har jag gjort den faktiska genomgången jag borde ha gjort från början: **Nortropics egna repos först**, och därefter relevanta open-source-repon och GitHub Projects. Och den ändrar min rekommendation ganska rejält.

Det viktigaste fyndet är:

> **Vi ska inte bygga ett nytt “Mission Control”. Du har redan börjat bygga det. Scrum-idén bör bli planeringslagret ovanpå det befintliga Fabriksrummet.**

### Det stora fyndet i dina egna repos

`Verkstadsgolvet` är redan beskrivet som en intern övervakningsdashboard för Nortropics agentsystem. fileciteturn49file0 Men längre fram har konceptet utvecklats mycket längre än den gamla dashboard-idén.

I `nortropic-control-room-plan-v1.md` finns redan en arkitektur för **Maskinen** med backlog, aktuell task, events, verifiering, snapshots, commands och historik. Den gör dessutom en viktig distinktion: eventströmmen är för aktivitet och observerbarhet, medan controller-genererade snapshots är den visade sanningen — `SNAPSHOT_WINS`. fileciteturn55file0 fileciteturn56file0

Sedan har det konceptet utvecklats till **Factory Room**. Roadmapen säger uttryckligen att det ska vara ett persistent rum, *inte en dashboard eller rapportsida*, där du matar in arbete, ser fabriken arbeta, inspekterar evidens och ger mycket smala intentioner, medan controllern fortfarande ensam bestämmer vad som är sant. fileciteturn60file0

Och det är inte bara en plan längre. Nuvarande `MaskinShell` är redan strukturerat som:

```text
IN → ARBETET → UT

Mata maskinen / backlog
        ↓
Aktuell uppgift
        ↓
Kandidat / verifiering / commands
        ↓
Output
        ↓
Timeline
        ↓
Live events
```

Koden kommenterar till och med att de tre banorna är en berättelse snarare än “tre likvärdiga instrumentpaneler”. fileciteturn58file0

Så när du visar bilden från *Silicon Valley* och säger *“jag vill lättare hålla isär allt”* är min nya slutsats:

**det du saknar är inte kontrollrummet. Du saknar väggen framför kontrollrummet.**

---

## Nortropic har Execution Management — det som saknas är Work Management

Factory Room svarar väldigt bra på:

**Vad gör maskinen just nu?**

Men Scrum-frågan är bredare:

**Vad håller Nortropic på med som helhet? Varför? Vad har vi valt att fokusera på? Vad väntar? Vilka större initiativ hör ihop? Vad är nästa?**

Det är två olika problem.

Och dina repos visar varför vi absolut inte ska försöka lösa båda med samma state machine.

`tasks.spec.json` säger uttryckligen att programregistret är backloggen och att specen **“inte är och aldrig blir en andra uppgiftslista”**. fileciteturn8file0

Ännu viktigare är `taskval`: **doneness läses ur ATTEST, aldrig ur state**. State är rapportering. Ett vanligt `"done"` hade kunnat bli kvar trots att verkligheten blivit stale. fileciteturn16file0

Och state-komponenten säger:

> `Loggen är sanningen; SQLite är projektionen.` fileciteturn14file0

Det här betyder att ett traditionellt Jira/Scrum-system där du drar:

`IN PROGRESS → DONE`

är nästan filosofiskt motsatsen till Nortropic.

**I Nortropic får en människa uttrycka intention. Maskinen måste bevisa verkligheten.**

Det är en mycket starkare modell.

---

# Jag skulle därför bygga: **Nortropic Planning Wall**

Inte ett nytt system. En ny vy **inne i Verkstadsgolvet / Factory Room**.

Den skulle ligga ett abstraheringslager ovanför Maskinen:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       NORTROPIC PLANNING WALL                               │
│                                                                             │
│  CYCLE 18                                                                  │
│  GOAL: Bootstrap closed → autonomous production baseline                    │
│                                                                             │
│  OWNER ATTENTION  2/3       BLOCKED  1       ACTIVE  3       PROVEN  7     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ SYSTEMFÖRBÄTTRINGAR                                                         │
│                                                                             │
│  SHAPE          READY          BUILD           PROVE          DONE          │
│                                                                             │
│  Frontier       S13            H-031           H-032          ...           │
│  observatory    read-plane     provider        review                       │
│                                boundary                                     │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ KUNDPRODUKTION                                                              │
│                                                                             │
│  SHAPE          READY          BUILD           PROVE          DONE          │
│                                                                             │
│  New brief      Website task   Hero build      Visual QA      Production    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

Det fina här är att **de två swimlanes redan finns i din arkitektur**.

Du har redan låst:

`SYSTEM_IMPROVEMENT`

och

`CUSTOMER_PRODUCTION`

som två work domains i **ett och samma Factory Room**, uttryckligen utan att skapa ett andra dashboard-, scheduler-, backlog- eller trust-system. fileciteturn62file0

Så Scrum-väggen passar nästan kusligt bra ovanpå det vi redan byggt.

---

## Men de fem kolumnerna är endast visuell kompression

Jag skulle **inte** skapa fem nya controller-states.

Factory Room har redan den finare vokabulären:

`RAW → PLANNING → NEEDS_SPEC → READY → QUEUED → WORKING → VERIFYING → REVIEWING → MERGING → DONE`

plus `STOPPED`. fileciteturn60file0

Planning Wall komprimerar dem bara:

```text
SHAPE
RAW · PLANNING · NEEDS_SPEC

READY
READY · QUEUED

BUILD
WORKING

PROVE
VERIFYING · REVIEWING · MERGING

DONE
DONE

INTERRUPT
STOPPED
```

Det är en **view**, inte en ny sanning.

Klickar du på kortet går du från väggen ner till Factory Room och sedan ner till task inspectorn med SHA, attempt, gate, review och evidence.

Det ger oss tre zoomnivåer:

```text
LEVEL 1 — PLANNING WALL
"Vad håller Nortropic på med?"

            ↓

LEVEL 2 — FACTORY ROOM
"Vad händer med arbetet just nu?"

            ↓

LEVEL 3 — TASK INSPECTOR
"Visa mig exakt varför detta är sant."
```

Det tycker jag är en exceptionellt bra informationsarkitektur för Nortropic.

---

# En idé från Scrum som jag skulle förbättra radikalt

Varje kort bör egentligen bestå av **två plan**:

```text
┌──────────────────────────────────┐
│ INTENT                           │
│                                  │
│ Initiative: Autonomous Core      │
│ Cycle: 18                        │
│ Priority: Critical               │
│ Goal: Close provider boundary    │
├──────────────────────────────────┤
│ REALITY                          │
│                                  │
│ State: REVIEWING                 │
│ Candidate: d27f78c...            │
│ Gate: PASS                       │
│ Attestation: valid               │
│ Blocker: —                       │
│ Age: 4h 12m                      │
└──────────────────────────────────┘
```

**Övre halvan äger människan. Nedre halvan äger maskinen.**

Du får ändra:

Cycle, priority, desired outcome, initiative, kanske deadline.

Du får **inte** manuellt ändra:

PASS, attested, published, candidate, verifierad, completed.

Det är en ganska fundamental förbättring av Scrum för agentiska system.

### Intent ≠ Reality

Traditionell projektledning blandar ofta ihop de två.

Nortropic behöver inte göra det.

---

# Och här hittade jag ytterligare en träff i din arkitektur

`innovation-intake` har redan en helt annan livscykel:

`idea → clarified → planned → building → verified`, med `superseded` terminalt. fileciteturn25file0

Briefen är byggkällan och chattranskriptet är rationale/evidens; idébanken är uttryckligen en separat funnel innan implementation. fileciteturn26file0

Samtidigt är `nortropic-knowledge` uttryckligen **inte execution authority**, och förbjuder en andra normativ source of truth. fileciteturn27file0

Det börjar därför framträda en väldigt ren helhet:

| Plane | Fråga | Sanning |
|---|---|---|
| **Discovery** | Vad skulle vi kunna göra? | `innovation-intake` |
| **Planning** | Vad väljer vi att fokusera på? | owner intent / cycle |
| **Execution** | Vad arbetar maskinen på? | controller |
| **Verification** | Håller resultatet? | gates + review |
| **Evidence** | Vad är faktiskt klart? | attestation + Git identity |
| **Knowledge** | Vad har vi lärt oss? | `nortropic-knowledge` |
| **Interface** | Hur ser jag allt detta? | `Verkstadsgolvet` |

Detta är enligt mig mycket bättre än “installera Scrum”.

Det är **en organisation operating system med Scrum som human coordination view**.

---

# Externa GitHub-repon gav också några tydliga signaler

Jag tittade bland annat på **Plane**, **OpenProject**, **Leantime**, **HumanLayer/12-factor-agents** och **OpenHands Agent Canvas**.

Plane delar upp arbetsmodellen i **Work Items, Cycles, Modules, Views och Analytics**. Det är relevant eftersom samma arbete kan visas olika utan att duplicera modellen. fileciteturn31file0

Leantime försöker explicit koppla ihop **strategy → planning → execution** och har både idea boards, goals och sprint management. Det är den delen jag skulle låna — inte hela PM-systemet. fileciteturn35file0

OpenProject visar hur långt åt andra hållet man kan gå: portfolio management, Scrum, SAFe, Gantt, releases, time tracking osv. fileciteturn33file0 Det är användbart som negativ referens för Nortropic: **vi ska inte bygga Jira**.

Den mest intressanta jämförelsen var faktiskt OpenHands. Deras nuvarande Agent Canvas beskriver sig som ett **developer control center for coding agents and automations**, där UI:t kan kontrollera/observera Claude Code, Codex och andra agentsystem över flera backends. fileciteturn44file0 Arkitekturen gör sedan en tydlig gräns: Canvas presenterar och skickar UI-actions, medan själva agent execution, sandbox och credentials ägs av backend. fileciteturn45file0

Det är nästan exakt den arkitektoniska riktning som ditt Factory Room redan tagit.

HumanLayers 12-Factor Agents driver dessutom idén att execution/business state bör kunna härledas från en sammanhängande state/event-history när det är möjligt, eftersom det förbättrar debugging, recovery och observability. fileciteturn41file0 De lyfter också launch/pause/resume som förstaklassoperationer snarare än något som göms i agentloopen. fileciteturn42file0

Det validerar flera av de beslut som redan finns i Nortropic snarare än att ge skäl att ersätta dem.

---

# Var passar GitHub Projects då?

Jag kollade även vad GitHub Projects faktiskt erbjuder idag.

Det har table-, board- och roadmap-vyer, custom fields, iterations, charts och automatisering. Samma dataset kan alltså ge olika backlog-, cycle- och roadmap-vyer. citeturn656674search0turn656674search1 Iteration-fält kan användas för exempelvis veckocykler, och GitHub rekommenderar även column limits för fokus/WIP. citeturn656674search5turn656674search6

Men GitHub Boards har en egenskap som gör mig mer skeptisk till att använda det som **Nortropics huvud-UI**: när man drar ett kort mellan kolumner ändras fältvärdet på itemet. citeturn656674search9

Det är precis vad vi **inte** vill göra med runtime truth.

Jag skulle därför använda GitHub Projects endast om vi vill ha en sekundär **planning/portfolio mirror**.

Exempel:

```text
GitHub Projects MAY OWN

Cycle
Priority
Initiative
Target date
Owner intent
Planning status


GitHub Projects MUST NOT OWN

Runtime state
Gate verdict
Attestation
Candidate identity
Promotion state
Current main
"Done"
```

Och GitHub har nu riktiga issue dependencies (`blocked by` / `blocking`), vilket skulle kunna vara användbart för planeringssidan om vi använder issues för större initiatives. citeturn656674search4

Men efter repoinspektionen skulle jag börja **i Verkstadsgolvet**, inte i GitHub Projects.

---

# Jag tycker också att vi ska stjäla “sprinten” men kasta kalenderstyrningen

För en AI-fabrik är det meningslöst att Claude väntar tills nästa tvåveckorssprint för att få nästa task.

Så:

**Agent execution:** kontinuerlig och event-driven.

**Nortropic Cycle:** mänsklig fokusperiod.

Jag skulle börja med **en vecka**.

Cycle Goal kan exempelvis vara:

> “Close bootstrap and establish post-bootstrap autonomous baseline.”

Under veckan kan maskinen genomföra 2 tasks eller 40 tasks. Det spelar mindre roll.

Cycle mäter **vad vi fokuserar på**, inte hur ofta agenten får arbeta.

Då blir Scrum-ritualerna också annorlunda:

`Sprint Planning` blir ett kort veckoval av mål. `Daily Scrum` blir en automatiskt genererad owner briefing, inte ett möte. `Sprint Review` blir vad som faktiskt blev verifierat/publicerat. `Retro` blir analys av blockers, omtag, owner interventions, verifieringsfel och flow.

Det känns mycket mer anpassat för Nortropic.

---

# Den viktigaste WIP-gränsen

Efter att ha läst controllern förstärks min tidigare tanke om **Human Attention WIP**.

Du har redan `OWNER_ACTION_REQUIRED` i taskval. Owner-authority work går uttryckligen inte ut till vanliga builder-lanen; persisted state blir handoffen till ägaren. fileciteturn16file0

Det är alltså inte ens någonting vi behöver hitta på.

Planning Wall borde ha detta högt uppe:

```text
OWNER ATTENTION

┌───────────────────────┐
│ 2 / 3                 │
│                       │
│ Architecture choice   │
│ Publication approval  │
└───────────────────────┘
```

När det är fullt bör systemet hellre fortsätta med agent-safe arbete än generera ytterligare fem beslut åt dig.

Det är sannolikt ett viktigare kapacitetsmått än agent throughput.

---

# En annan viktig sak jag upptäckte

Din nuvarande bootstrap-process med väldigt många review/remediation-rundor visar varför varje R116, R117, R118, R119, R120 **inte ska vara ett eget stort Scrumkort**.

Det skulle bli en vägg av intern mekanik igen.

Istället:

```text
CARD
H-031 · Provider boundary

State        REVIEWING
Round        R120
Attempts     6
Candidate    …
Gate         …
Reviewer     …
Blocker      …
```

R-rundorna hör hemma **inne i kortets timeline/inspector**.

Väggen visar den semantiska arbetsenheten.

Det här är också varför Factory Rooms progressive-disclosure-design är rätt riktning.

---

# Min nya arkitektur

Jag skulle nu beskriva Nortropic så här:

```text
                      NORTH STAR
                          │
                    PROGRAM / ROADMAP
                          │
                ┌─────────▼──────────┐
                │  PLANNING WALL     │
                │ cycle · priorities │
                │ initiatives · WIP  │
                └─────────┬──────────┘
                          │
              selected owner intention
                          │
                ┌─────────▼──────────┐
                │   FACTORY ROOM     │
                │                    │
                │ IN → WORK → OUT    │
                └─────────┬──────────┘
                          │
                    exact task
                          │
                ┌─────────▼──────────┐
                │ TASK INSPECTOR     │
                │ attempts · gates   │
                │ review · evidence  │
                └─────────┬──────────┘
                          │
                 controller / attest
                          │
                ┌─────────▼──────────┐
                │ PROVEN REALITY     │
                └────────────────────┘

DISCOVERY ── innovation-intake ─────────► PLANNING
KNOWLEDGE ◄─ learnings/research ◄──────── RESULTS
```

Och då kan vi äntligen använda en Scrum-vägg ungefär som den på bilden **utan att förenkla bort Nortropics starkaste egenskaper**.

### Slutsatsen

Repoanalysen gör mig betydligt mer positiv till din ursprungliga intuition.

Inte:

> “Nortropic behöver Scrum.”

Utan:

> **“Nortropic behöver en visuell planeringsvägg ovanpå Factory Room, där mänsklig intention och maskinbevisad verklighet hålls strikt separerade.”**

Det är mer innovativt än vanlig Scrum och framför allt ligger det **direkt i linje med arkitekturen du redan har byggt**.

Och jag skulle inte bygga detta som ett sidoprojekt. Jag skulle göra **Planning Wall till nästa naturliga produktlager i Verkstadsgolvet**, med de befintliga work domains, de 11 canonical task states, `SNAPSHOT_WINS`, innovation-intake och Factory Room som fundament. Vi behöver alltså inte börja om — stora delar av underbyggnaden finns redan. memcite

Det här utvecklas snabbt i repona. Jag kan också bevaka open-source-världen efter nya idéer för Planning Wall/agent control rooms och flagga sådant som faktiskt är bättre än vår modell.

genui{"suggest_automation":{"label":"Bevaka agentiska control-room idéer"}}

---

## Meddelande 7 — ChatGPT (assistent)

Klart. Jag bevakar **agentiska control-room-idéer dagligen** och hör bara av mig när det dyker upp något som faktiskt är relevant för Nortropics Factory Room/Planning Wall — med konkret förklaring av varför det är intressant och hur det kan tillämpas. memcite

---

## Meddelande 8 — ChatGPT (assistent)

Jag hittade faktiskt något värt att flagga. Det starkaste fyndet är att flera oberoende system nu konvergerar mot nästan exakt den riktning vi skissat för **Planning Wall → Factory Room**, men två av dem har detaljer som jag tycker Nortropic bör ta in.

1. **OpenAI Symphony gör projektboarden till själva arbets-control-plane:n, inte bara en dashboard.** OpenAI beskriver Symphony som ett skifte från att övervaka coding sessions till att hantera *deliverables*: ett öppet work item på boarden blir agentarbete i ett isolerat workspace, medan repo-versionerad workflow-policy styr hur arbetet ska utföras och resultatet ska komma tillbaka med proof-of-work. citeturn921529search1turn921529search0 För Nortropic innebär det att Planning Wall bör vara mer än en läsvy: den kan äga **mänsklig intention, cycle, prioritet, eligibility och vilket godkänt work-contract/brief som ska exekveras**. Men vi ska uttryckligen *inte* kopiera Symphonys svagare tracker-authority-modell. Nortropics nuvarande backlog säger redan att den inte är runtime-state eller backend-authority, och `SNAPSHOT_WINS` gör controller-snapshoten till displayed truth medan eventströmmen bara får bidra med transient aktivitet. fileciteturn64file0L1-L7 fileciteturn65file0L1-L7 Det ger en bättre version av Symphony-idén: **Planning Wall commands intent; Factory Room reports reality.** urlOpenAI Symphonyhttps://openai.com/index/open-source-codex-orchestration-symphony/

2. **GitHub har precis lagt till ett väldigt bra human-in-the-loop-mönster: diskutera utan att besluta.** I releasen den 13 augusti 2026 kan användaren öppna en side chat kring en agents fråga medan den ursprungliga frågan fortsätter att vänta på sitt svar. De har också gjort subagents och deras tasks synliga via `/tasks`. citeturn290038search11 Det här skulle jag direkt översätta till Nortropic som en **Deliberation lane** för `OWNER_ACTION_REQUIRED`: när ett owner-beslut blockerar arbetet ska du kunna trycka *Diskutera*, låta en modell läsa evidensen, förklara alternativen och testa invändningar — utan att något runtime-state ändras. Endast ett separat typat `Approve / Reject / Resume`-kommando får verkställa beslutet. Det är en liten UX-idé men arkitektoniskt stark: **reasoning channel ≠ authority channel**.

3. **Open Multi-Agent har en recovery-modell som passar Nortropics immutability ovanligt bra.** Deras nuvarande adaptive-recovery-kontrakt behåller task-grafen fast som standard. Om verkligheten tvingar fram en förändring sker den som en validerad `PlanPatch` vid en **outcome barrier**; patchen godkänns, appliceras atomiskt och checkpointas innan nytt downstream-arbete får släppas. Misslyckade eller ersatta historiska tasks skrivs inte om till framgång — de förblir sanningsenligt `failed`/`skipped` och pekar på revisionen som ersatte dem. citeturn130720search9 Det här bör vi överväga för Planning Wall: **ett godkänt planobjekt skrivs aldrig retroaktivt om efter att execution börjat; ändringar blir append-only Plan Revisions kopplade till det utfall som tvingade fram dem.** Då kan Wall exempelvis visa `Plan r3`, medan inspektorn visar att r2:s gren ersattes av r3 och varför. OMA:s färska RunStore-förslag från 8 augusti lägger dessutom till leases och fencing för stale workers, men där är Nortropic redan långt framme; det är främst extern validering snarare än något vi behöver importera. fileciteturn63file0L3-L6 urlOMA adaptive recoveryhttps://github.com/open-multi-agent/open-multi-agent/blob/main/docs/adaptive-recovery.md

4. **Kandev ger stöd för att göra planen till ett förstaklassobjekt mellan idé och execution.** Deras `Plan & Build` sparar agentens plan som ett strukturerat dokument, stoppar före implementation, låter människan redigera de exakta stegen och låter sedan implementationen hämta den ändrade planen. Deras längre Feature Dev-flöde använder dessutom en färsk agent-turn för separata spec-, build-, review- och QA-faser. citeturn130720search8turn130720search1 För Nortropic tycker jag inte att detta motiverar ännu en requirements-källa; snarare bör Planning Wall kunna peka på **den redan auktoritativa brief/specen med immutable identity**, visa den som “approved execution plan”, och efter admission endast tillåta ändring via revisionmekanismen ovan. urlKandev workflow patternshttps://github.com/kdlbs/kandev/blob/main/docs/workflow-tips.md

Min syntes är därför en konkret uppgradering av vår tidigare Planning Wall-idé:

**Planning Wall = intent + approved plan + prioritization.  
Factory Room = execution + transient activity.  
Controller snapshot = reality.  
Deliberation = fri diskussion utan authority.  
Plan Revision = append-only ändring vid säker outcome-barrier.**

Det mest värdefulla nya här är kombinationen **“Discuss without acting” + “Revise without rewriting history”**. Den skulle göra Nortropic bättre på precis den svåra delen av AI-native Scrum: du kan styra och tänka om snabbt utan att mänsklig UI-interaktion någonsin kan fabricera vad maskinen faktiskt har gjort. memcite

---

## Meddelande 9 — ChatGPT (assistent)

Två saker från de senaste 48 timmarna är faktiskt värda att flagga för Nortropic.

1. **GitHub Agentic Workflows har infört “steering” av en agent medan den redan arbetar.** PR #55171, mergead **24 augusti 2026**, låter en workflow-agent som arbetar mot en förskapad PR läsa nya användarkommentarer och review-kommentarer markerade för steering och använda dem som feedback under den pågående körningen. Viktigast: funktionen kräver uttrycklig `pull-requests: read` och GitHub vägrar att automatiskt bredda behörigheterna bara för att steering aktiveras. fileciteturn83file0L3-L15 fileciteturn83file0L725-L732

   Det här fyller en lucka mellan våra tidigare två idéer **“discuss without acting”** och **pause/resume**. För Nortropic skulle jag inte göra steering till fri chat som kan ändra tasken. Jag skulle modellera den som ett immutable **operator-feedback object** bundet till `run_id + task_id + attempt_id + expected_watermark + author + content digest`. Controllern får sedan konsumera feedbacken vid en definierad säker punkt och lägga den i nästa agent-context, men feedbacken får aldrig själv ändra state, gate verdict, attestation, candidate eller promotion. Det är extra viktigt eftersom Factory Rooms nuvarande command contract medvetet har **exakt fem verb** och säger att varje command bara är en intention som controllern alltid får avvisa. fileciteturn85file0L2-L6

   Min rekommendation är därför **inte** “lägg till ett sjätte verb nu”. Idén som är värd att ta med till arkitekturstadiet är snarare ett fjärde plan bredvid Intent/Reality/Deliberation: **Steering Input**. Det gör att du kan korrigera en agent mitt i ett längre arbete utan att förstöra Nortropics authority-separation.

2. **OpenAI Codex har gjort execution origin till explicit, persistent provenance.** PR #40161, mergead **23 augusti 2026**, lägger till `codex exec --thread-source <SOURCE>`. Källklassningen sätts när en ny eller forkad thread skapas, persisteras i metadata, exponeras även i TypeScript-SDK:n och skrivs inte över när man bara återupptar en existerande thread. Default är `user`; testerna visar exempel som `automated_review`. fileciteturn84file0L3-L15 fileciteturn84file0L27-L35 Codex **0.149.1** publicerades därefter den **24 augusti 2026**, och 0.149.0→0.149.1-deltat innehåller just ändringarna i exec/SDK-ytorna för thread-source. fileciteturn82file1L5-L10

   Det här tycker jag är direkt applicerbart på Factory Room. Nortropic bör på sikt bära ett immutable fält i stil med `execution_origin` eller `thread_source` från **skapelseögonblicket**, inte försöka härleda det i UI:t senare. Exempelvis skulle en run kunna vara startad av `operator`, `standing_work`, `frontier_watch`, `reviewer`, `memory`, `planner` eller annan versionerad kategori. Det är inte en roll, inte ett task-state och absolut inte authority — bara proveniens. Då kan Planning Wall svara på *“varför existerar det här arbetet?”* samtidigt som Factory Room svarar på *“vad gör det nu?”*.

Det gör att jag skulle justera vår nuvarande modell från tre till fem separerade begrepp:

**Planning Wall äger Intent → Steering tillför bounded feedback → Deliberation får resonera fritt → Controller äger Reality → Provenance berättar vem/vad som orsakade execution.**

Det är en liten arkitekturförändring på pappret men en ganska stor kvalitativ förbättring. Framför allt löser den ett framtida problem innan det uppstår: när Nortropic har många samtidiga autonoma workers kommer **“vem startade detta, varför, och vad har människan faktiskt sagt under resans gång?”** annars lätt blandas ihop med maskinens faktiska state. Här ser jag ett konkret mönster värt att ta med i Planning Wall/Factory Room-specifikationen.

---

## Meddelande 10 — ChatGPT (assistent)

Ja — **ett nytt mönster från GitHub den 25 augusti är tillräckligt bra för att jag tycker vi ska ta in det i Nortropic-designen**.

GitHubs Agentic Workflows visade upp sin **Issue Monster** som kör var 30:e minut och letar efter arbete som kan lämnas till Copilot coding agent. Det intressanta är inte själva agenten utan att de har byggt en separat **admission controller** framför execution. Den kontrollerar först bland annat att det inte redan finns fem öppna Copilot-draft-PR:er, att centrala CI-checkar är friska och att det inte finns färska rate-limit-signaler. Arbete måste dessutom redan ha passerat en särskild queue-gate (`cookie`-label). Först därefter får upp till tre ärenden skickas vidare. Själva urvalsagenten har huvudsakligen read-behörighet; den muterande övergången sker genom en smal `assign_to_agent` safe output. citeturn769660search1turn276618search0turn276618search1

Det som gör detta mer än bara en snygg idé är att GitHub redovisar verkliga körningar från den 25 augusti: fem körningar granskade backloggen, två av dem valde arbete medan **tre korrekt gjorde ingenting**. Totalt omkring 350k tokens och 125 GitHub-API-anrop, men noll errors/warnings. GitHub lyfter själva fram återhållsamheten som designpoängen: agenten ska curera och bedöma kapacitet, inte känna sig tvungen att alltid producera arbete. citeturn769660search1

För **Nortropic Planning Wall → Factory Room** tycker jag detta avslöjar ett lager vi bör göra explicit:

```text
PLANNING WALL
   │
   │ owner intent / approved work
   ▼
ADMISSION CONTROLLER
   │
   │ only if safe + useful + capacity exists
   ▼
FACTORY ROOM / CONTROLLER
   │
   ▼
EXECUTION
```

Planning Wall ska alltså inte bara ha `READY` och sedan låta nästa agent plocka något. **Ready betyder “arbetet är planeringsmässigt möjligt”; Admission betyder “det är klokt att släppa in det i fabriken just nu”.**

För Nortropic skulle admission exempelvis kunna väga samman dependency-readiness, tillgänglig worker-kapacitet, aktuellt WIP per factory lane, provider/quota health, breaker-status, kontrollplanets hälsa, överlappande write scopes och mängden arbete som redan väntar på mänsklig uppmärksamhet. Om något av detta säger nej ska resultatet vara ett legitimt **NO-OP**, inte ett misslyckande och inte ett försök att “hitta något annat att göra”.

Det sista är den viktiga skillnaden mot vanlig Scrum. En Scrum-board brukar främst visualisera WIP. **Nortropic kan mekaniskt reglera inflödet till WIP.**

Jag skulle dessutom hålla admission helt separat från runtime truth. Admission får säga ungefär *“task X är lämplig att starta nu, baserat på snapshot Y och dessa signaler”*. Den får aldrig själv göra tasken `WORKING`, skriva attestation, flytta main eller fabricera en Factory Room-status. Det fortsätter controllern att äga.

Så vår modell blir nu ännu tydligare:

**Planning Wall = vad vi vill göra.  
Admission Controller = vad fabriken bör ta in nu.  
Factory Room = vad fabriken faktiskt gör.  
Controller/evidence = vad som faktiskt är sant.**

Det här tycker jag är en riktig förbättring jämfört med den Planning Wall-modell vi hade innan. Framför allt ger det oss ett naturligt ställe för den **Human Attention WIP** vi redan resonerat kring: om ägarens decision queue är full kan Nortropic hålla tillbaka nytt arbete som sannolikt genererar ytterligare owner-stopp och istället välja autonomt säkra tasks — eller göra ingenting alls. memcite

---

## Meddelande 11 — ChatGPT (assistent)

Ja — **ett nytt mönster är värt att flagga**, och det passar Nortropic ovanligt väl.

Det nya projektet **AgentTrail** skapades den 21 augusti och har utvecklats aktivt under veckan. Kärnidén är inte ännu en agent-board, utan en uttrycklig separation mellan **Declared** och **Observed**: agentens plan säger *vad den påstår sig arbeta på*, medan filsystemet visar *vad den faktiskt rör*. Om de två divergerar visas båda. En task som redan markerats klar “tänds” dessutom igen om dess filer börjar ändras senare. AgentTrail betonar uttryckligen **observability, not orchestration** — den observerar utan att styra agenten. fileciteturn75file0L1-L2 Repo-metadata visar att projektet är färskt och publikt, skapat 21 augusti och uppdaterat 27 augusti. fileciteturn76file0L1-L2 urlAgentTrail på GitHubhttps://github.com/sodiumsun/agenttrail

Det här ger oss ett nytt signalplan som jag tycker **Factory Room bör adoptera som princip**, men inte som en ny state machine:

```text
INTENT / DECLARED
Vad tasken och planen säger ska göras
        │
        │ compare
        ▼
OBSERVED ACTIVITY
Vad workspace, filer, tester och tools faktiskt visar
        │
        ▼
ACTIVITY DIVERGENCE
observerbarhetslarm — aldrig verdict
```

Det passar särskilt bra eftersom Nortropic redan har den hårdare arkitekturen som AgentTrail saknar: `SNAPSHOT_WINS`. Nuvarande `snapshot.ts` säger uttryckligen att controller-snapshoten är displayed truth, att event/tail endast får bidra med liveaktivitet och transient fas, och att divergens får **observeras och loggas men aldrig bli en dom eller ändra state**. fileciteturn77file0L1-L2

Den konkreta Nortropic-förbättringen skulle därför vara ett **Activity Evidence Overlay** i Factory Room. Ett aktivt task-kort skulle kunna visa `Declared: controller/result/**` och under det `Observed: controller/result/consumer.py · tests/...`; om agenten börjar arbeta i en annan komponent än den deklarerade visas exempelvis **ACTIVITY DIVERGENCE**, men tasken fortsätter vara `WORKING` tills controllern säger något annat.

Det öppnar fyra ganska kraftfulla signaler utan att röra trustmodellen:

- **Scope drift early warning:** tasken säger område A men observerad aktivitet sker i B. Nortropics policy fångar felaktig diff senare; detta skulle göra avvikelsen synlig medan arbetet fortfarande pågår.
- **Post-proof mutation:** något som redan är verifierat/proven börjar ändras igen. UI:t kan direkt visa *“tidigare bevisat område förändras”*. Bara den ordinarie stale-/reverification-mekanismen får däremot ogiltigförklara sanningen.
- **Possible stall:** snapshot säger `WORKING` och heartbeat lever, men inga filer, tester eller relevanta tool-events har observerats på länge. Det blir en diagnostisk signal, inte `STOPPED`.
- **Plan/execution mismatch:** den deklarerade deluppgiften står still medan agenten upprepade gånger arbetar någon annanstans. Det är betydligt mer användbart än att bara visa “agenten är aktiv”.

Det sista är särskilt viktigt för Planning Wall. Vi har hittills separerat **Intent → Admission → Execution → Reality**. Jag skulle nu lägga till **Observed Activity** som en oberoende sensor bredvid execution:

```text
Planning Wall
     ↓
Admission
     ↓
Factory Room ──────► Declared work
     │                    │
     │                    ▼
     │              compare continuously
     │                    ▲
     │                    │
     └──────────────► Observed activity
                           │
                           ▼
                     divergence signals

Controller Snapshot ─────────────► authoritative reality
```

Det är alltså **inte ännu ett statuslager**. Det är ungefär som instrumenteringen i en fysisk fabrik: produktionsordern säger vad maskinen borde bearbeta, sensorerna visar vad maskinen faktiskt gör, men sensorn får inte själv skriva om produktionsordern eller kvalitetscertifikatet.

Jag tycker detta är tillräckligt starkt för att lägga till som en faktisk designprincip för Planning Wall/Factory Room. Framför allt kan det ge Nortropic en ovanligt bra egenskap när många Claude/Codex-workers kör parallellt: **vi kan upptäcka att en agent är upptagen utan att automatiskt anta att den gör rätt sak.** memcite

---

## Meddelande 12 — ChatGPT (assistent)

Ja — **två nya saker är tillräckligt bra för att flagga i dag**, och båda går att lägga ovanpå vår riktning utan att försvaga Nortropics authority-modell.

**1) Ett nypublicerat multi-agent Control Center har löst “Human Attention WIP” på ett konkret sätt som jag tycker vi bör stjäla.** `SamuelAlev/control-center` fick sitt första publika commit den **27 augusti 2026** och positionerar sig uttryckligen kring problemet att många agenter är enkla att starta men svåra att hålla överblick över. fileciteturn64file0L2-L2 Det intressanta är deras implementation av en särskild **attention projection**: varje feature får bidra med objekt endast när den faktiskt *blockerar operatören eller begär något av operatören*. Kommentaren i koden säger uttryckligen att den strikta regeln finns för att attention-ytan inte ska bli “en andra notification firehose”. Blockerade agent approvals kommer in där, medan exempelvis en flappande integration kollapsas till **senaste felet per vendor** i stället för att fylla kön med samma problem. fileciteturn79file0L2-L2

Det är en bättre konkretisering av vår tidigare idé än bara en räknare `OWNER ATTENTION 2/3`. Jag skulle göra **Owner Attention till en härledd projection, aldrig en manuellt skött backlog**:

```text
authoritative controller state
        │
        ├── owner decision actually required
        ├── approval blocks progression
        ├── external dependency needs operator action
        └── persistent fault only owner can resolve
                       │
                       ▼
              OWNER ATTENTION
              dedup · collapse · age
```

Vanliga warnings, agentaktivitet, retries, observations och “bra att veta” får **inte** hamna där. På så sätt blir `3 owner-actions` faktiskt ett mått på mänsklig flaskhals, inte antalet notifieringar Nortropic råkat producera.

Samma repo har dessutom ett ovanligt bra **Plan Studio-kontrakt**. Redan exekverade plansteg är immutable eftersom redigering annars skulle forka historien; varje edit eller agent-replan skapar en ny revision; en användare som redigerar en gammal revision får sin write **avvisad** om planen har hunnit ändras under tiden i stället för att systemen försöker mergea ändringarna; rewind skapar också en ny revision i stället för att skriva om historien. När execution har replannat efter ett godkännande visas dessutom diffen mellan **approved revision** och den nya live-revisionen. Agenten får föreslå och revidera, men **kan inte godkänna planen själv**. fileciteturn81file0L2-L2

Det skulle jag föra in direkt i Planning Wall-principerna:

> **Approved Plan Revision becomes an anchor.**

`plan_r7 APPROVED` förblir exakt det du godkände. Om arkitekten senare upptäcker något nytt skapas `plan_r8`; om ett redan exekverat steg måste ändras blir det en ny/superseding arbetsgren, inte en redigering av den historiska noden. Det passar extremt väl ihop med Nortropics immutable evidence-tänkande.

En mindre men bra detalj från samma system är också att dess estimat är **“honest or absent”**: cost/time visas som intervall med sample size från verklig historik; finns ingen historik visas `unknown`, inte ett uppskattat snyggt tal. Critical-path-tid beräknas för parallella grenar i stället för att summas. fileciteturn81file0L2-L2 Det bör vara vår regel om Planning Wall senare får forecasts.

urlControl Center på GitHubhttps://github.com/SamuelAlev/control-center

**2) GitHub Agentic Workflows har precis börjat behandla flera agentruns som ett dataset — inte bara som separata loggar.** Den färska `v0.87.8` publicerades **28 augusti 2026**, och de senaste ändringarna introducerar cross-run audit clustering och strukturerade graders. fileciteturn72file0L2-L2 I stället för att bara fråga “hur gick run 412?” grupperar systemet runs efter exempelvis task-domain, execution style, resource profile och outcome och kan upptäcka återkommande mönster som att en viss klass av misslyckanden konsumerar oproportionerligt många tokens eller att ett visst attribut korrelerar med failure. Grader-/eval-resultat har dessutom gjorts till en förstaklassdimension i samma cross-run-analys. citeturn367682view0turn711927view0turn877460view0

Det här skulle jag **inte** lägga i Factory Rooms runtime-state. Jag skulle lägga det bredvid som ett:

**Factory Pattern Observatory**

```text
immutable run evidence
run 1 ─┐
run 2 ─┼──► deterministic cross-run analysis
run 3 ─┤
run N ─┘
             │
             ├─ repeated blocker family
             ├─ unusual retry pattern
             ├─ verification-failure cluster
             ├─ context-growth anomaly
             ├─ provider/role correlation
             └─ owner-intervention hotspot
                       │
                       ▼
             PLANNING CANDIDATE / RETRO
```

Det avgörande är att dess fynd får vara **diagnostiska hypoteser**, aldrig controller truth. Ett mönster som “TEST_AUTHOR → owner intervention i 41 % av fallen” kan skapa ett shaping-item på Planning Wall eller ett research-item i Innovation Intake. Det får inte själv ändra task-state, gate, routing, attestation eller authority.

Det här skulle ge Nortropic något jag tror blir mycket viktigare när systemet växer: inte bara **observability of one agent**, utan **organizational learning across hundreds of agent runs**.

Så dagens egentliga arkitekturdiff blir:

```text
Planning Wall
  ├─ Intent
  ├─ Approved Plan Revision       ← förstärkt idag
  ├─ Admission
  └─ Owner Attention Projection   ← NY konkret mekanism
             │
             ▼
Factory Room / Controller
             │
             ▼
Immutable Run Evidence
             │
             ▼
Factory Pattern Observatory       ← NY
             │
             └──► shaping / retro / innovation
```

Av allt jag gick igenom idag är **attention projection med strict inclusion + cross-run pattern learning** det jag tycker är värt att faktiskt bära vidare till Nortropic. Resten av de färska projekten jag såg var mest variationer på sådant Nortropic redan gör bättre: worktree-isolation, verifiering utanför agenten, budgets, retries och tiered model routing. memcite

---

## Meddelande 13 — ChatGPT (assistent)

Tre färska förändringar från de senaste dygnen är tillräckligt bra för att jag tycker de ska påverka Nortropics Factory Room/Planning Wall-design.

1. **Anthropic har introducerat “focus-scaled observability” i Claude Code v2.1.251, släppt 28 augusti.** Remote Control kan nu streama ett **foreground-subagents faktiska tool calls och resultat live**, medan background-subagents fortfarande bara visar status. Samma release exponerar dessutom sessionens prompt-cache som warm/cold, hit ratio, misses och re-cache-tokens, plus spend limit och uppskattad re-cache-kostnad när en gammal session återupptas. fileciteturn79file1L9-L10

Det här är bättre än att Factory Room försöker visa maximal detalj för alla workers samtidigt. Jag skulle införa en explicit observationshierarki:

```text
BACKGROUND WORKER
task · phase · heartbeat · blocker
          │
          │ operator focuses
          ▼
FOREGROUND WORKER
tool calls · files · commands · results · causal trace
```

Det löser ett framtida skalproblem: 20 samtidiga Claude/Codex-workers ska inte innebära 20 terminalströmmar i ansiktet på operatören. Planning Wall visar portföljen, Factory Room visar sammanfattad fabriksaktivitet, och **den agent/task du fokuserar får högupplöst observability**. Cache-warmth, staleness och spend-budget kan samtidigt bli signaler till Admission Controller: `READY` betyder fortfarande möjligt arbete, men admission kan välja en varm/resumable worker framför en dyr cold restart. De signalerna får däremot aldrig påverka verifierad reality eller authority. urlClaude Code v2.1.251https://github.com/anthropics/claude-code/releases/tag/v2.1.251

2. **OpenAI har gjort en viktig skärpning av Human-in-the-Loop: “attention” används nu bara för frågor som kräver ett svar.** Den 28 augusti ändrades Codex `send_user_message_async` så att den inte längre ska användas för statusuppdateringar, findings eller vanliga progressmeddelanden. Den är reserverad för missing information, preferences, constraints, clarification eller approval. fileciteturn80file0L2-L2

Ännu viktigare: en separat Codex-ändring från 26 augusti fixerar approval-policy och reviewer från **det steg som faktiskt skapade approval-requesten**. En långlivad eller fördröjd approval får alltså inte plötsligt bedömas med nyare turn-settings bara för att systemet hunnit ändras under tiden. fileciteturn86file0L2-L2

De två tillsammans ger en väldigt stark Nortropic-regel:

> **Owner Attention är inte en notification inbox. Det är en kö av obesvarade frågor, bundna till den exakta kontext där frågan uppstod.**

Det skärper vår tidigare Owner Attention-projection. Jag skulle låta varje attention item semantiskt bära ungefär:

```text
OWNER_QUESTION
reason:
  missing_information
  preference
  constraint
  clarification
  approval

bindings:
  task
  attempt
  candidate
  issuing_policy
  authority_snapshot
  asked_by
```

Progress, warnings, interesting findings och observationer går till Factory Room/timeline/notifications. Endast någonting där **ett mänskligt svar faktiskt krävs** får konsumera Human Attention WIP.

Det passar dessutom direkt ovanpå Nortropics existerande owner-authority-modell. Där är `OWNER_ACTION_REQUIRED`, `OWNER_CANDIDATE_REVIEW_REQUIRED` och `OWNER_FINAL_FREEZE_REQUIRED` redan auktoritativa persisted states med hårda identity-bindningar. fileciteturn85file0L2-L2 Jag skulle alltså inte ändra den state machine:n; Planning Wall får istället projicera den till en mycket renare mänsklig frågekö.

urlCodex: async attention only for questionshttps://github.com/openai/codex/commit/7e41be641ed1133711e4f75b2e142de7affaff7a  
urlCodex: approvals use issuing-step policyhttps://github.com/openai/codex/commit/a26f1806a4f4b8cfec2ea1be129963815a61e58c

3. **OpenAI har börjat bära W3C `traceparent` genom agent→runtime→tool-callback→spawned-task-kedjan.** Codex-ändringen från 27 augusti injicerar W3C trace context i code-mode session/execution requests och fortsätter bära samma causal context genom streamade callbacks och när arbetet flyttar vidare till spawnade tasks. fileciteturn81file0L2-L2

Det här tycker jag är den konkreta tekniken vi saknat bakom vår tidigare **Activity Evidence Overlay**.

I stället för att försöka gissa:

```text
"var det här tool-callet orsakat av agent A,
som startades av task B,
som i sin tur kom från run C?"
```

kan Nortropic på sikt bära en observerbar causal lineage:

```text
Planning item
   │
   ▼
Controller run
   │ trace
   ▼
Provider invocation
   │ trace
   ├── Subagent A
   │     └── Tool call
   │           └── callback
   │
   └── Subagent B
         └── remote operation
```

Jag skulle kalla lagret **Causal Trace Plane**.

Det ska vara strikt observerande. `trace_id` kan hjälpa Factory Room att bygga korrekt timeline, gruppera tool activity, förstå subagent-träd och senare ge Factory Pattern Observatory bättre data. Men `trace_id` får aldrig bevisa `DONE`, attestation, candidate identity eller promotion. Det är korrelation, inte authority.

urlCodex W3C trace propagationhttps://github.com/openai/codex/commit/eed1dee69e8ddab6fd3344f1b7572aafb2e75cb5

Den samlade förändringen jag skulle bära vidare till Nortropic är därför:

```text
PLANNING WALL
      │
      ▼
ADMISSION CONTROLLER
  capacity
  spend
  cache warmth
  session staleness
      │
      ▼
FACTORY ROOM
  background = compressed status
  foreground = high-resolution activity
      │
      ├──────── Causal Trace Plane
      │
      ▼
CONTROLLER REALITY

OWNER ATTENTION
  questions requiring answers only
  bound to issuing context
```

Det här är inte mer “dashboard”. Det är snarare **attention management + progressive observability + causal instrumentation** för en fabrik med många samtidiga agenter. Av dagens material är framför allt **foreground/background observation tiers** och **question-only Owner Attention med issuing-context binding** sådant jag skulle ta med som faktiska krav när Planning Wall specificeras. memcite

---

## Meddelande 14 — ChatGPT (assistent)

Ja — **en förändring som skeppades i OpenAI Codex 0.151.0 den 29 augusti är tillräckligt viktig för att påverka Nortropic-designen**, och en närliggande ny extension-seam är också värd att bära med sig.

### Hierarchical Resource Envelope

Codex räknar nu **all tokenförbrukning från spawned descendants, inklusive nästlade subagents, mot root-goalens budget**. Det sker både under aktivt arbete och idle/progress-accounting; bokföringsbasen återställs när det aktiva målet byts, och implementationen har tester för child → grandchild, budget exhaustion, parent-runtimes som inte längre är laddade och samtidiga checkpoints. Funktionen ingår i 0.151.0, publicerad 29 augusti. citeturn127178view0 fileciteturn67file0L1-L2

Det här löser ett viktigt multi-agent-problem: **budget får inte kunna “försvinna nedåt” i agentträdet**. Om en agent har 100k tokens kvar och spawnar fem workers som i sin tur spawnar fler workers ska inte alla bete sig som om de var separata ekonomier.

För Nortropic skulle jag göra detta till ett förstaklasskontrakt mellan Planning Wall, Admission Controller och Factory Room:

```text
PLANNING GOAL
resource_envelope = R17
tokens / spend / wall-time
        │
        ├── worker A
        │      ├── reviewer A1
        │      └── researcher A2
        │
        └── worker B
                 └── subagent B1

ALL ACTUAL USAGE
        │
        ▼
ROOT RESOURCE ENVELOPE R17
```

Det viktiga är att **budgeten hör till arbetets mål, inte till processen som råkar utföra det**. En child får en allocation ur förälderns återstående kapacitet; grandchildren fortsätter inom samma ekonomiska träd. Planning Wall kan då visa exempelvis `resource envelope: healthy / constrained / exhausted`, medan Factory Room kan drill-downa till vilken gren som faktiskt konsumerar resurser.

Admission Controller får en mycket bättre signal än “har vi quota kvar?”: *finns tillräcklig kvarvarande budget för att rimligen påbörja nästa work item?* Och om en task börjar explodera i recursive delegation kan admission stoppa ytterligare fan-out innan hela quota-potten försvinner.

Jag skulle hålla detta strikt separat från truth-modellen:

**resource exhausted ≠ task failed verification.**

Det betyder bara att execution måste stanna, replaneras eller få mer budget. Gate, attestation, candidate och `DONE` fortsätter ha exakt sina egna authorities.

urlCodex 0.151.0 releasehttps://github.com/openai/codex/releases/tag/rust-v0.151.0

### Raw Result → Model View är värd ett eget observerbarhetskontrakt

Samma release introducerar också något mer subtilt. Codex extensions får nu intercepta ett MCP-tool-resultat **efter att verktyget körts men innan resultatet publiceras och innan modellen ser det**. Extensionen får tillgång till tool-context, rewritten arguments, extension-state och det muterbara serverresultatet och kan lämna resultatet orört eller ersätta det — även för error-resultat. citeturn127178view0 fileciteturn75file0L1-L2

Jag tycker **inte** Nortropic ska kopiera detta ordagrant. För ett evidence-drivet system är det farligt om det transformerade resultatet ersätter vetskapen om vad verktyget faktiskt returnerade.

Vi borde istället använda en dual-channel-modell:

```text
TOOL EXECUTION
      │
      ▼
RAW RESULT
immutable bytes / digest / provenance
      │
      ├──────────────► EVIDENCE / AUDIT
      │
      ▼
RESULT PROCESSOR
redaction
normalization
compression
untrusted-data wrapping
schema conversion
      │
      ▼
MODEL-VISIBLE RESULT
digest + processor identity
      │
      ▼
AGENT
```

Factory Room kan då vid behov visa:

`RAW → PROCESSOR v3 → PRESENTED`

och Task Inspector kan bevisa exakt relation mellan dem.

Det ger oss en väldigt bra plats för bland annat secret-redaction, output-komprimering, schema-normalisering och markering av extern data som **data snarare än instruktioner**, utan att originalresultatet förstörs.

Det passar dessutom fint med Causal Trace Plane-idén från tidigare: ett tool-span kan bära både `raw_result_sha256` och `presented_result_sha256` samt identiteten på transformationen. Det blir möjligt att felsöka frågan *“var verktyget fel, eller förändrade vårt presentationslager betydelsen?”* i stället för att bara se vad modellen råkade få.

### Arkitekturdiff för Nortropic

Efter dagens fynd skulle jag lägga till två saker i vår samlade modell:

```text
PLANNING WALL
   │
   ├── Intent
   ├── Approved Plan
   └── Root Resource Envelope       ← NY
            │
            ▼
ADMISSION CONTROLLER
   capacity + descendant-aware budget
            │
            ▼
FACTORY ROOM
            │
      agent tree usage
            │
            ├──────► Causal Trace Plane
            │
            └──────► Tool Result Plane     ← NY
                       RAW
                        ↓
                    PROCESS
                        ↓
                    PRESENTED
            │
            ▼
CONTROLLER / EVIDENCE TRUTH
```

Av det jag gick igenom är **hierarkisk budgetbokföring** den viktigaste nya idén. Tool-result-seamen är tvåa. Övriga färska control-room/orchestration-projekt jag hittade idag var huvudsakligen variationer på sådant Nortropic redan har eller redan har diskuterat — agent dashboards, phase views, HITL approvals, worktree isolation och vanlig run-cost visualization — och är därför inte värda att dra in som nya designspår. memcite

---

## Meddelande 15 — ChatGPT (assistent)

Ja — **två nya mönster från 30–31 augusti är värda att bära in i Nortropic**, och det första är betydligt starkare än ännu en dashboard- eller board-idé.

1. **GitHub Agentic Workflows har börjat utvärdera agentens *trajectory*, inte bara slutresultatet.** I `v0.87.10`, publicerad **31 augusti 2026**, har GitHub byggt ut sina trajectory-graders med bland annat `policy-near-miss`, `exploration-error`, `exploitation-error`, `skill-constraint-coverage` och `tool-output-consumption-rate`, och skickar grader/eval-resultat vidare som OpenTelemetry-spans. GitHubs egen veckorapport från i dag lyfter detta som ett växande lager för att förstå *hur* agenter beter sig över runs, inte bara om de avslutade uppgiften. fileciteturn67file0L2-L2 citeturn579847search0

   Det mest intressanta är vad graderna faktiskt skiljer på. `policy-near-miss` fångar en run som nådde ett “successful” outcome men **inte utförde alla deklarerade guard/policy-kontroller** — alltså ungefär “resultatet ser rätt ut, men processen hoppade över en obligatorisk kontroll”. fileciteturn68file0L2-L2 `exploration-error` klassar misslyckanden där agenten inte samlade tillräckligt med observationer/evidens, medan `exploitation-error` fångar motsatsen: agenten hade tillräckligt med evidens men **använde den inte korrekt**. De två graderna är medvetet gjorda för att inte ge samma förklaring på samma trace. fileciteturn69file0L2-L2 fileciteturn70file0L2-L2 Och `tool-output-consumption-rate` mäter specifikt hur stor andel av tool-output som faktiskt blev konsumerad av senare actions, i stället för det mycket svagare måttet “verktyget returnerade success”. fileciteturn71file0L2-L2

   **Nortropic-implikationen är ett nytt lager jag skulle kalla `Trajectory Quality Plane`.** Inte en ny truth source och absolut inte en ersättning för gates. Factory Room-roadmapen är redan tydlig med att controllern ensam äger sanningen och att rummet observerar men aldrig får mynta state. fileciteturn75file0L2-L2 Därför bör trajectory-evaluering ske **efter** runnen över immutable run evidence och svara på frågor som: *Gjorde agenten alla kontroller den borde? Letade den för lite? Hade den evidensen men ignorerade den? Hämtade den massor av tool-output som aldrig påverkade någon handling?*

   Det ger en betydligt bättre Factory Pattern Observatory än bara `PASS-rate`, tokenkostnad och retries. Exempelvis kan hundra gröna runs avslöja att reviewers systematiskt hoppar över en kontroll men räddas av den mekaniska slutgrinden. Det är **inte skäl att retroaktivt göra dessa runs röda**; det är ett diagnostiskt fynd som kan skapa ett shaping-item på Planning Wall: *“reviewer-processen har 18 % policy-near-miss på kontroll X”*. Om vi senare vill göra egenskapen trustkritisk måste den först bli ett explicit, fruset mekaniskt kontrakt på vanligt Nortropic-sätt.

   Arkitektoniskt blir alltså `Causal/Run Evidence → Trajectory Evaluation → Cross-run Pattern Observatory → Planning Wall`, medan `Controller → Gates → Attestation → Reality` förblir orört. Det här tycker jag är en **materiell uppgradering** av vår tidigare observability-modell. urlGitHub Agentic Workflows v0.87.10https://github.com/github/gh-aw/releases/tag/v0.87.10

2. **OpenAI Codex har separerat “vad användaren har auktoriserat” från “hur den aktuella konversationshistoriken råkar se ut”.** I committen **30 augusti 2026** ändrade Codex Guardian sin modell därför att compaction och host-injicerad context kan skriva om modellens synliga historik utan att användaren faktiskt har ändrat sitt godkännande. Codex håller därför nu en separat, host-owned **user-message revision**: genuina användarmeddelanden och history resets flyttar den, medan compaction och intern context-injektion inte gör det. fileciteturn63file1L1-L1

   Detta är en liten implementation men en mycket viktig princip för ett persistent Factory Room: **Context Revision ≠ Authorization Revision.** När Nortropic senare komprimerar en lång room-session, återställer den från snapshots, för in maskin-genererade sammanfattningar eller fortsätter samma arbete från Slack/telefon ska ett tidigare owner approval inte plötsligt bli ogiltigt bara för att modellcontexten blivit omskriven. Samtidigt får ett nytt verkligt owner-beslut aldrig döljas av att “conversation id är samma”.

   Jag skulle därför låta framtida owner approvals/constraints bära en mekaniskt ägd `authorization_revision` eller motsvarande, separat från conversation/session/context-generation. Riktigt owner-input, revoke eller explicit reset ökar revisionen; compaction, summaries, retrieved history och annan host-context gör det inte. Approval-objektet binds sedan till den revision som gällde när det utfärdades. Detta kompletterar vår tidigare princip om **issuing-context binding** på ett mycket renare sätt.

   En färsk Codex-ändring från **31 augusti** förstärker samma separation från ett annat håll: `update_plan` är nu **opt-in** och all medföljande planning-guidance tas bort från model-, collaboration-, multi-agent-, compaction- och continuation-prompter när capabilityn är avstängd. fileciteturn63file0L2-L2 Jag skulle ta detta som ytterligare stöd för Nortropics riktning att planändring ska vara en uttrycklig capability i rätt lane/roll — inte något varje builder/reviewer implicit kan göra bara för att modellen kan resonera om planer. urlCodex Guardian authorization/compaction changehttps://github.com/openai/codex/commit/0a12b855a0b21068108a8a3b311d492712737e0f

Den viktigaste förändringen från dagens bevakning är alltså att **“agent observability” håller på att gå från activity logs till process semantics**. För Nortropic innebär det att vi kan behålla vår starka mekaniska truth-kärna men bygga ett separat lärandelager som analyserar *kvaliteten på vägen fram till resultatet*. Det är ett av de tydligare fynden hittills som faktiskt kan göra fabriken bättre över tid, snarare än bara snyggare att titta på.

---

## Meddelande 16 — ChatGPT (assistent)

Ja — **en ny förändring runt OpenAI Codex 0.152.0, publicerad 1 september 2026, är tillräckligt viktig för att påverka Factory Room-designen**. Det är inte ännu en board-idé, utan något mer fundamentalt: **vad ett agentiskt kontrollrum gör när förbindelsen bryts mitt i arbete**. fileciteturn80file0L1-L2

Codex byggde den 31 augusti in automatisk återanslutning för out-of-process app-server-sessioner. Vid transportbortfall startas en ny klient och den befintliga threaden återupptas, samtidigt som transcript, drafts, runtime settings, tool capabilities och notifieringsrouting bevaras. Det viktiga är säkerhetssemantiken: **ingen användaroperation retryas automatiskt**. Input som kan ha skickats innan bortfallet sätts i karantän för manuell/reconciled behandling, gamla async-completions från den döda anslutningen får inte utlösa nya handlingar, och sessioner som inte går att återansluta kan fortfarande visas som read-only cached views. fileciteturn68file0L1-L2

Det här fyller enligt mig en riktig lucka mellan Nortropics nuvarande read-plane och framtida command-plane. Factory Room-roadmapen kräver redan ett persistent rum som ska fungera på distans, låta operatören lämna och komma tillbaka, och endast exponera smala typade intentioner medan controllern ensam äger sanningen. Den har dessutom redan realtime/TailStore med reconnect/backfill-mekanik, medan den live command-transporten ännu är separerad/blockerad. fileciteturn75file0L1-L2

Jag skulle därför frysa en ny princip för Factory Room:

```text
LIVE
  │
  │ connection lost
  ▼
DEGRADED / READ-ONLY
  ├─ keep last authoritative snapshot
  ├─ keep timeline / drafts / local context
  ├─ quarantine unconfirmed commands
  ├─ ignore completions from old connection generation
  └─ NEVER auto-replay mutations
  │
  ▼
RECONCILE
  ├─ resume authoritative run/thread
  ├─ fetch fresh snapshot + command outcomes
  ├─ resolve every uncertain command_id
  └─ verify new connection generation
  │
  ▼
WRITE PLANE RESTORED
```

Det centrala är **observability recovery ≠ mutation recovery**. Factory Room får gärna komma tillbaka direkt som ett läsbart rum efter ett nätverksfel, men knappar som `run.start`, `resume`, intake eller framtida steering ska inte återfå mutation authority förrän controllern har reconciliat vad som faktiskt hände. Om användaren tryckte `run.start` precis innan nätet dog och UI:t aldrig fick svaret får resultatet vara `UNCERTAIN` i presentationslagret — aldrig “failed”, aldrig “not sent”, och framför allt aldrig skickas om automatiskt. Detta bör bindas till exempelvis `command_id + issued_against_watermark + connection_generation`, där gamla generationssvar inte får påverka den nya sessionen.

Det här gör Planning Wall/Factory Room betydligt robustare för just den framtid vi bygger mot: telefon, Slack, remote clients och flera samtidiga agenter. En grön anslutningsikon betyder då inte “det är säkert att mutera”; **read freshness, command certainty och controller authority blir tre separata saker**.

Det andra fyndet är mindre visuellt men också värt att ta med. Codex började den 31 augusti persistenta **`TokenUsageRecord`** med attribution till response, turn, thread, session och root-turn. Ackumulerad usage återställs efter resume och checkpointas vid compaction, samtidigt som root-turn-lineage bevaras. fileciteturn72file0L1-L2 Tidigt den 1 september tog de nästa steg och började dessutom bevara **hela upstream `response.usage`-objektet som rå metadata**, parallellt med den normaliserade amount-vyn. fileciteturn73file0L1-L2

Det gör gårdagens idé om **Hierarchical Resource Envelope** mer konkret. Nortropic bör inte bara lagra ett UI-tal som `42k tokens`. Jag skulle hellre ha ett controller-/evidence-nära **Resource Ledger**:

```text
provider raw usage
      │
      ├── immutable/raw metadata
      │
      ▼
normalized usage record
response → attempt → task → run → root goal
      │
      ▼
Planning Wall / Admission projection
```

Då kan vi senare räkna cost, token burn, cache-effektivitet och descendant usage korrekt över resume/compaction utan att rekonstruera det ur loggar eller UI. Precis som med resten av Nortropic är raw evidence något annat än den mänskligt användbara projektionen.

Det finns dessutom en närliggande Codex-ändring från 31 augusti som stärker samma mönster: realtime conversation history flyttades ned till **Core som ensam persistence owner**, medan app-servern bara översätter Core-events till presentation/notifikationer och uttryckligen inte persisterar samma information en andra gång. fileciteturn74file0L1-L2 Det är nästan en direkt extern validering av Nortropics `SNAPSHOT_WINS`-filosofi.

Så dagens materiella delta är:

**Factory Room bör få explicit reconnect safety med mutation quarantine, och Resource Envelope bör utvecklas till ett riktigt evidence-backed Resource Ledger.**

Den första är viktigast. Den hindrar ett av de farligaste felen i ett remote agent-control-room: **att ett UI efter nätverksproblem tror att “försök igen” är samma sak som “gör det en gång”.** urlOpenAI Codex 0.152.0https://github.com/openai/codex/releases/tag/rust-v0.152.0 memcite
