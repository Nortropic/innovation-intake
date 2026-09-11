# Agent Control-Room Watch — fullständigt transkript

**Källprojekt:** Improvements (ChatGPT-projekt)
**Chatt:** Agent Control-Room Watch
**URL:** https://chatgpt.com/c/6a8ac6dc-4314-83eb-9c3b-fbd4e6405bbd
**Exportdatum:** 2026-09-11
**Antal meddelanden:** 26 (3 användare, 23 assistent)
**Syfte:** Fångad i PROJECT_SWEEP Improvements R39 (data-layer, WYSIWYG-filtrerad); syftet med samtalet avgörs av dess innehåll, inte av denna rubrik.

**Innehåll i korthet:** Samtalet öppnar med: ”Nåt jag har reflekterat över är scrum så jag hade vela ha för att lättare hålla isär alltihop, vi har tidigare arbetat med dokumentationen men arbeta innovativt med en scrum skulle också vara hjälpsam” och avslutas med: ”Ja — **dagens sweep gav två materiella mönster som jag tycker ska in i Nortropics framtida control-plane-design, och ett av dem nyanserar en princip vi redan har fryst.** Båda kommer från färska Codex”

> Notis: rader som ser ut som käll-/citat-chips från ChatGPT är en del av
> originaltexten och har bevarats ordagrant. 1 bilagor inventerade (data-layer: distinkta plattforms-fil-id ur metadata.attachments + icke-textdelar; en bild som adaptern listar två gånger räknas en gång); bytes registreras separat via register-attachment där plattformen exponerar dem.

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

---

## Meddelande 17 — ChatGPT (assistent)

Ja — **dagens bevakning gav ett fynd som jag tycker bör bli en faktisk Nortropic-invariant, inte bara en UI-idé: en `Run Closure Barrier`.** Det finns dessutom en mindre men mycket bra utveckling för Owner Attention.

Den 1 september öppnades en färsk Codex-incidentrapport där en coordinator hann lämna sitt slutresultat medan dess descendant-agenter fortfarande levde. Enligt rapporten växte trädet från 61 avsiktligt startade subagents till **469 totalt**, nådde 101 samtidiga agents, fortsatte konsumera quota efter att huvudtasken såg färdig ut och kunde inte stoppas genom att bara avbryta föräldrarna. Rapporten efterfrågar uttryckligen recursive cancellation, delegation-budget, ett `Stop all agents in this task`-kommando och att en task inte får bli completed medan descendants fortfarande arbetar. Det här är en användarrapporterad incident, inte ännu en officiell OpenAI-root-cause, men failure mode:n är arkitektoniskt viktig. fileciteturn4file0L2-L2

Samma dag skeppade Anthropic Claude Code **v2.1.257** flera närliggande lifecycle-fixar: stopp av en background-subagent stoppar nu även dess monitors; detached background commands får inte längre överleva task-stop eller Claude Code-exit; subagents som avbryts av sleep/connection failure fortsätter kontrollerat i stället för att lämnas halvdöda; och `claude -p` väntar numera på en Monitor som agenten själv har armerat i stället för att avsluta processen direkt efter det synliga slutresultatet. fileciteturn3file0 urlClaude Code v2.1.257https://github.com/anthropics/claude-code/releases/tag/v2.1.257

Tillsammans pekar detta på en starkare princip än vår tidigare **Hierarchical Resource Envelope**:

**En run får inte vara terminal förrän dess ownership tree är terminal.**

För Nortropic skulle jag modellera det ungefär så här:

```text
RUN R17
   │
   ├── worker A
   │     ├── reviewer A1
   │     └── monitor A2
   │
   └── worker B
          └── process B1

owner requests STOP / run reaches completion
                 │
                 ▼
              CLOSING
       spawn gate = CLOSED
                 │
       cancel / join descendants
                 │
       wait for owned leases
                 │
       verify resource quiescence
                 ▼
               DONE
```

`CLOSING` här bör vara controller-owned reality, inte något Factory Room hittar på. När root-runnen går in i closure stängs först möjligheten att skapa fler descendants. Därefter måste alla ägda subagents, monitors, background processes, retries och andra execution leases antingen nå terminalt state eller **explicit transfereras** till en annan run. Först därefter får controllern mynta `DONE` eller `STOPPED`.

Det betyder också att den resource-modell vi hittade häromdagen behöver en sista pusselbit:

**Resource Envelope + Ownership Tree + Closure Barrier.**

Att bara summera child-tokens till root är inte tillräckligt. Efter terminalisering ska exempelvis följande kunna bevisas mekaniskt:

```text
spawn_gate                 CLOSED
live_descendants           0
live_monitors              0
live_background_processes  0
unresolved_execution_lease 0
unrecorded_transfer        0
post_fence_resource_delta  0
```

Factory Room kan då ha ett väldigt användbart mellanläge:

**`CLOSING · draining 3 descendants`**

och ett nödstopp i operatörsytan kan vara **`STOP RUN TREE`**, inte “stoppa den agent jag råkar titta på”. Kommandot är fortfarande bara en intention till controllern; själva UI:t får inte döda saker direkt.

Det här blir ännu viktigare när Nortropic arbetar unattended över natten. En coordinator som ser färdig ut klockan 02:14 men lämnar ett agentträd levande till 07:00 är precis den sorts fel som ett autonomt organisationssystem inte får normalisera. Ett slutresultat är därför inte samma sak som **execution closure**.

Det andra nya fyndet från **2 september** passar nästan kusligt bra med vårt arbete kring Owner Attention. Codex ersatte `send_user_message_async` med strukturerade `request_user_input_async`: en agent kan nu skicka **en eller flera explicita frågor, med valfria föreslagna svar, utan att den pågående turnen behöver stanna**. Frågornas struktur följer dessutom med genom app-server-events, thread history och schemas. fileciteturn5file0L1-L2 urlCodex structured async user inputhttps://github.com/openai/codex/commit/2c79ee6dacb6deccb7e19ac5acffb3e379bbe895

Det ger oss en viktig förfining:

**Owner question ≠ Owner stop.**

Planning Wall/Factory Room bör på sikt kunna skilja mellan exempelvis:

```text
ASYNC_OWNER_INPUT
"Vilken av dessa två riktningar föredrar du?"
→ resten av säkert arbete fortsätter

BLOCKING_OWNER_DECISION
"Vilken candidate får promotion authority?"
→ relevant execution frontier väntar
```

En fråga kan alltså få `question_id`, issuing-context, task/attempt-binding, suggested answers och vilket **scope** den blockerar. Endast det scope som faktiskt kräver svaret behöver frysa; andra oberoende branches kan fortsätta. Det ligger exakt i linje med vår riktning bort från onödiga ägarstopp.

Min samlade arkitekturdiff från dagens bevakning blir därför:

```text
Planning Wall
      │
      ├──── Async Owner Questions ───► Owner Attention
      │             │
      │        scoped blocking
      ▼
Admission
      ▼
Factory Room / Controller
      │
      ├── execution ownership tree
      ├── hierarchical resource envelope
      │
      ▼
Run Closure Barrier
      │
      └── no descendants / leases / resource burn
              after terminal state
```

**Run Closure Barrier är dagens riktiga guldkorn.** Det borde enligt min bedömning bli en del av Nortropics framtida execution-contract, inte bara något vi visar i Factory Room. Det knyter ihop cancellation, agent trees, resource accounting, unattended autonomy och sann terminalitet på ett sätt som vår tidigare modell ännu inte uttryckte lika explicit. memcite

---

## Meddelande 18 — ChatGPT (assistent)

Ja — **en ny Anthropic-förändring från Claude Code v2.1.259 är värd att föra in som en riktig Nortropic-princip**: ett unattended system bör inte automatiskt göra varje permission-fråga till ett mänskligt stopp.

Claude Code v2.1.259, publicerad **2 september 2026 kl. 22:33 UTC**, introducerar `--permission-prompts none` specifikt för unattended/headless execution. Den viktiga semantiken är att den befintliga permission-policyn fortfarande fattar sina normala beslut — inklusive `auto` — men om utfallet annars hade blivit *“fråga användaren”* blir det i unattended-läge istället **deny**. Agenten kan därefter försöka en annan väg i stället för att processen står parkerad och väntar på en människa. citeturn761693view0

Det här bör skärpa Nortropics modell till:

```text
POLICY DECISION
      │
      ├─ ALLOW ─────────────► execute
      │
      ├─ DENY ──────────────► replan / alternative
      │
      └─ ASK
           │
           ├─ true owner/authority decision
           │      └─────────► OWNER ATTENTION
           │
           └─ ordinary permission uncertainty
                  │
             unattended?
               ├─ no ───────► ASK OPERATOR
               └─ yes ──────► DENY + REPLAN
```

Det är en viktig skillnad mot både *“auto-approve allt”* och *“stoppa och fråga ägaren om allt”*. **Owner Attention bör reserveras för beslut där Nortropic faktiskt behöver din authority, information eller preferens — inte för att ett verktyg råkar sakna tillräcklig permission för sin första valda väg.** På natten ska en sådan permission-friktion i normalfallet ge agenten ett maskinläsbart avslag och möjlighet att hitta en säkrare alternativ väg. Bara när arbetets semantik verkligen kräver ägaren ska relevant frontier gå till `OWNER_ACTION_REQUIRED`.

Jag skulle kalla kontraktet **Unattended Interaction Policy**. Admission binder runnen till exempelvis `interactive | unattended`; permission-evalueringen producerar fortfarande `ALLOW | DENY | ASK`, men controllern bestämmer vad `ASK` betyder beroende på frågetyp och interaction mode. Viktigt är att agenten själv **inte** får klassificera en permission-fråga som owner-critical för att komma runt ett denial — eskaleringen måste följa ett typat kontrakt.

Samma färska release ger dessutom ett konkret skäl att göra runtime-konfiguration mer formell i Factory Room. Anthropic fixade ett fel där flera samtidiga Claude-sessioner kunde **skriva över varandras `~/.claude.json`-ändringar**, vilket kunde återställa workspace trust och tappa MCP-/projektstate. De ändrade också managed settings så att trasig policykonfiguration nu gör att Claude Code **vägrar starta och anger vilken källa som är fel**, i stället för att tyst köra utan policyn. citeturn761693view0

Det talar för en Nortropic-invariant som jag tycker hör ihop med ovanstående:

```text
RUN R17 ──binds──► runtime_config_revision C42

workers:
  read C42
  never mutate shared control config

config change:
  controller / config authority
          │
          ▼
         C43

new admissions → C43
existing R17   → remains C42
unless explicitly and safely rebound
```

Alltså **ingen delad, opportunistiskt muterbar agentkonfiguration mellan parallella workers**. Factory Room bör kunna säga exakt vilken policy/config-revision varje run exekverar under. En trasig eller okänd managed policy ska dessutom vara ett admission/runtime-fel — aldrig degradera tyst till mindre governance.

Anthropic fixade även två lifecycle-fel som stärker gårdagens `Run Closure Barrier`: Stop i remote-control kunde lämna background agents/processer levande, och resume kunde starta en ny workflow-kopia medan den stoppade generationen fortfarande höll på att avslutas. De låter nu dödade tasks ligga kvar synliga/re-stoppable tills processerna verkligen är borta och förhindrar duplicate execution vid sådan resume. citeturn761693view0 Det är främst **bekräftelse på gårdagens riktning**, så jag skulle inte öppna ett nytt designspår för det.

Dagens verkliga nya delta är därför **“permission prompt ≠ owner stop”**. Tillsammans med vår scoped Owner Attention-modell ger det en viktig egenskap för Nortropic: **unattended autonomy kan fortsätta fail-closed utan att antingen fastna på rutinfrågor eller behöva bli dangerously permissive.** urlClaude Code v2.1.259 releasehttps://github.com/anthropics/claude-code/releases/tag/v2.1.259 memcite

---

## Meddelande 19 — ChatGPT (assistent)

Ja — **tre saker är värda att flagga den här gången**. Den viktigaste är ett evidence-mönster som jag tycker passar Nortropic nästan direkt; de andra två skärper hur Planning Wall/Factory Room bör mäta värde och visa förändringar.

1. **Ett agent-system har börjat kunna bevisa i efterhand exakt vad modellen faktiskt såg.** Open Multi-Agent `v1.17.0`, släppt **28 augusti 2026**, introducerar en append-only `RunEvent`-journal som registrerar varje adapteranrop och dessutom lineage för varje model-visible content block. `verifyRun()` kan sedan cold-verifiera en avslutad journal och visa att modellens synliga context går att reproducera från exakt de events som blocken hänvisar till. Persistenta context-rewrites blir egna `context/replace`-events, checkpoints innehåller en journal-watermark, och resume återställer snapshoten och spelar därefter journalens tail — inklusive tool-results som hunnit journalföras men inte kommit med i checkpointen. citeturn145414view0

Det här går längre än vårt tidigare **Causal Trace Plane**. En trace kan säga *“agent A körde tool B efter event C”*, men den svarar inte nödvändigtvis på *“vilken exakt information såg modellen när den fattade beslutet?”*. Compaction, summarization, tool-result processing, retrieval och context replacement gör den skillnaden viktig.

Jag skulle därför lägga till ett separat **Model View Ledger / Context Lineage Journal** i Nortropic:

```text
IMMUTABLE EVIDENCE EVENTS
        │
        ▼
MODEL-VIEW ASSEMBLER
        │
        ├─ block B41 ← events 810,812,817
        ├─ block B42 ← context/replace 823
        └─ block B43 ← tool-result 829
        │
        ▼
MODEL INVOCATION

checkpoint = state + journal_watermark 829

resume
  = checkpoint
  + replay journal 830...
```

Den stora vinsten är incidentanalys och reproducibility. Om en Codex-worker fattar ett märkligt beslut kan Nortropic i princip bevisa **vad worker:n hade tillgång till**, inte bara rekonstruera en ungefärlig transcript i efterhand.

Jag skulle dock göra Nortropic starkare än referensimplementationens default. Open Multi-Agent gör journaling opt-in och best-effort som standard; Nortropic bör kunna ha exempelvis `lineage_required=true` för trust-kritiska lanes. Saknas lineage får Factory Room säga **EVIDENCE PARTIAL**, inte låtsas att observationen är komplett. Controller-state förblir fortfarande separat; journalen får aldrig mynta `DONE`. urlOpen Multi-Agent v1.17.0turn145414view0

2. **GitHub har lagt till ett explicit lager för “skapade arbetet faktiskt värde?” — separerat från både success och agentkvalitet.** `gh-aw v0.88.0`, släppt **1 september 2026**, introducerade operational-value history/reporting. Den underliggande specifikationen är ovanligt välgjord: evaluatorns bytes fryses och SHA-256-bindas, observationen har en explicit evidence cutoff och maturity, resultatet är absolut attainment `[0,1]`, och historisk regrading skapar en **ny observation** i stället för att skriva om det ursprungliga resultatet. Saknad evidens är `unavailable`, inte `0`, och GitHub varnar uttryckligen för att observationerna inte etablerar kausalitet. citeturn145414view1turn762157search1turn762157search2

Det fyller faktiskt ett tomrum i vår nuvarande modell. Vi har ungefär:

```text
Controller truth
→ gjorde runnen vad kontraktet krävde?

Trajectory Quality
→ arbetade agenten på ett bra sätt?

Factory Pattern Observatory
→ vilka återkommande beteendemönster finns?
```

Men ingen av dem besvarar ordentligt:

**“Var detta arbete faktiskt värt att göra?”**

Nortropic bör därför på sikt ha ett separat **Operational Value Plane**:

```text
RUN TERMINAL
     │
     ├── verified execution truth
     ├── trajectory-quality observations
     │
     └──────── time passes / evidence matures
                       │
                       ▼
              OPERATIONAL VALUE
              definition_digest
              evidence_cutoff
              maturity
              provenance
              value / unavailable
                       │
                       ▼
               PLANNING LEARNING
```

För exempelvis Digitala skulle en automation kunna vara mekaniskt perfekt men efter tre månader visa sig skapa nästan inget verkligt värde. En annan kanske kostar mer men konsekvent eliminerar verkligt underhållsarbete eller förbättrar kvaliteten. Planning Wall kan då börja lära sig **vilka sorters arbete fabriken bör prioritera**, inte bara vilka tasks den klarar av.

Detta får däremot aldrig innebära att låg senare operational value retroaktivt gör en korrekt run `FAILED`. Det är en senare observation över ett annat fenomen.

GitHubs nya Dashboard Language-specifikation innehåller dessutom ett litet guldkorn jag skulle kopiera rakt av: **data quality har tre oberoende axlar — Availability, Completeness och Freshness.** `empty ≠ unavailable`, `partial ≠ stale`, och `unknown ≠ zero`; varje view ska dessutom bära `as-of` och provenance. citeturn762157search0

Det ger ett mycket bättre Factory Room under exempelvis reconnect:

```text
Controller snapshot
AVAILABLE · COMPLETE · STALE
as_of 07:59:12

Activity overlay
AVAILABLE · PARTIAL · FRESH
as_of 08:05:58

Resource ledger
UNAVAILABLE · UNKNOWN · UNKNOWN
```

I stället för en enda grön/röd “connected”-indikator kan Nortropic alltså vara exakt om **vad vi vet, hur mycket vi vet och hur färskt det är**.

3. **En färsk Codex-bugg visar varför review-scope aldrig bör definieras som “last turn”.** Ett issue öppnat **3 september 2026** beskriver hur en delegated subagent först gjorde en funktionell refactor över 11 filer och därefter fick en liten whitespace-follow-up. Codex Apps `Last Turn`-review visade då bara whitespace-diffen; den huvudsakliga implementationen fanns kvar i worktree:t men försvann ur den review-yta som representerade subagentens arbete. Rapportören identifierar korrekt problemet som **review-boundary och attribution**, inte dataförlust. citeturn776572view0

Samtidigt skeppade Claude Code `v2.1.260` den **3 september** en live diff-panel som visar uncommitted changes medan Claude arbetar. Det är bra för foreground-observability, men tillsammans med Codex-fallet blir den viktiga Nortropic-regeln tydlig: **live diff och review diff är två olika produkter**. citeturn776572view1

Factory Room kan gärna visa:

```text
LIVE ACTIVITY DIFF
"vad förändras just nu?"
```

men ett approval/review måste bindas till:

```text
DELEGATED WORK UNIT / CANDIDATE
base_snapshot
candidate_snapshot
cumulative_patch_digest
attempt lineage

optional:
  turn_1_subdiff
  turn_2_subdiff
  turn_3_subdiff
```

En liten follow-up får alltså aldrig krympa den change-set som du förväntas granska. För Nortropic skulle jag formulera invarianten som:

> **Review scope follows the work/candidate lineage, never the conversational turn boundary.**

Det här är särskilt viktigt när Factory Room senare låter dig klicka på en worker, se arbetet och fatta owner-beslut. En UI-projektion som visar en tekniskt korrekt men semantiskt felaktig deldiff kan annars lura operatören trots att underlying evidence är korrekt. urlCodex issue #42441turn776572view0

Den samlade arkitekturdiffen jag skulle bära vidare är därför:

```text
Planning Wall
   │
   ├── intent / admission
   ├── historical operational value ──► prioritization
   │
   ▼
Factory Room
   ├── live activity diff
   ├── typed data-quality envelope
   │
   ▼
Execution
   ├── Context Lineage Journal        ← viktigast idag
   ├── Causal Trace
   └── Evidence
           │
           ▼
Candidate / Work-unit Review
cumulative, stable review boundary
           │
           ▼
Controller Truth
           │
           └──── later ───► Operational Value Plane
```

**Model View Ledger är dagens största guldkorn.** Det gör Nortropic kapabelt att verifiera inte bara *vad fabriken gjorde*, utan även den exakta informationskedja som formade agentens beslut. Operational Value Plane är därefter det mest intressanta långsiktiga tillskottet: det förvandlar Factory Room från ett system som bara driver arbetet korrekt till ett system som över tid kan lära sig **vilket arbete som faktiskt är värt att driva**.

---

## Meddelande 20 — ChatGPT (assistent)

Ja — **tre nya mönster från 4–5 september är tillräckligt starka för att påverka Nortropics Factory Room / Planning Wall-riktning**. Det första är viktigast: det löser ett problem som vår tidigare reconnect-modell ännu inte gick hela vägen på.

1. **Execution kan överleva control plane — och därefter adopteras av en ny controller utan att dupliceras.** Paperclip gjorde den 4 september ett ovanligt intressant recovery-arbete för sina lokala coding-agent runners. Vid en hot restart kan den gamla controllern uttryckligen släppa sin control authority **utan att stänga den pågående provider-turnen**. Den nya controllern återtar sedan exakt samma runner, run, provider-session och active turn först efter verifierad identitet; active turn återställs innan reconnect-events spelas upp, och recovery failar stängt om processfingerprint eller durable identity är tvetydig. I deras verkliga test byttes servern medan en Codex-turn körde, men samma runner-PID, run-ID, native session, provider session och active turn levde vidare och producerade exakt ett slutresultat utan retry- eller duplicate-run. fileciteturn5file0L2-L2 urlPaperclip: live hot-restart adoptionhttps://github.com/paperclipai/paperclip/commit/263f181fed709ae734f6f29f8d941317cade5e4b

Det här är **starkare än reconnect safety** som vi hittade tidigare. Reconnect safety svarar på vad UI:t gör när länken dör. Detta svarar på vad som händer när **själva controllern dör eller uppgraderas medan fabriken fortfarande arbetar**.

Jag skulle därför lägga till en riktig **Controller Adoption Protocol**:

```text
EXECUTION OWNERSHIP

Run R17
  executor_process_fingerprint
  provider_session_id
  active_turn_id
  controller_generation = C41
                │
         controller restart
                ▼
C41 DETACHES AUTHORITY
execution continues
                │
                ▼
C42 ADOPTION CLAIM
  exact run identity
  exact process identity
  authenticated runtime snapshot
  durable checkpoint identity
                │
          ambiguity?
          yes → BLOCKED
          no
                ▼
C42 OWNS CONTROL
then replay buffered events
```

Det viktiga Nortropic-kontraktet blir:

> **Controller lifetime ≠ execution lifetime.**

Men execution får aldrig bli “ownerless and free”. Den kan tillfälligt fortsätta under ett redan utfärdat execution lease, medan **nya mutationer, steering, spawn eller promotion authority är stängda tills en ny controllergeneration har gjort en exakt adoption**.

Detta passar mycket bra ihop med `Run Closure Barrier`, command reconciliation och unattended autonomy. Det innebär dessutom att vi senare skulle kunna uppgradera/restarta Factory Rooms backend mitt under en lång Codex/Claude-run utan att antingen döda arbetet eller riskera att starta det två gånger.

2. **Operator steering bör vara en egen durable queue — inte chatmeddelanden som råkar skickas medan agenten arbetar.** Paperclip fixade också den 4 september sin active-run steeringmodell. Follow-ups går nu direkt till en stabil kö där de kan ligga kvar, reorderas eller tas bort. Om runtime stöder live steering appliceras instruktionen på samma run; annars används en explicit interrupt-and-follow-up och instruktionen levereras till successor-runnen. UI:t skiljer dessutom på tidpunkten då instruktionen **köades** och när den faktiskt **steerades/delivererades**, och post-steer-segment markeras som fortsättning på samma run i stället för att se ut som ett nytt, orelaterat arbete. fileciteturn6file0L2-L2 urlPaperclip: stable active-run steering queuehttps://github.com/paperclipai/paperclip/commit/bf95a7eae255b390749fa5a4bda56de1127aa4e1

Detta fyller ett hål mellan våra tidigare två riktningar:

```text
Agent → Owner
OWNER ATTENTION / QUESTIONS

Owner → Agent
STEERING QUEUE                 ← saknades som explicit primitive
```

Jag skulle **inte** låta Factory Rooms framtida chattruta vara den mekaniska steeringmodellen. Ett owner-ingripande bör bli ett förstaklassobjekt:

```text
STEERING INTENT S91

issued_against:
  run R17
  attempt A4
  controller watermark W881

state:
  QUEUED
  → APPLIED_SAME_RUN
  → DELIVERED_SUCCESSOR_RUN
  → REMOVED
  → REJECTED

timestamps:
  queued_at
  applied_at

delivery:
  native_steer | interrupt_followup
```

Då kan du från mobilen skriva tre korrigeringar, ändra ordningen och ta bort nummer två utan att de blandas ihop med agentens transcript. Factory Room kan dessutom sanningsenligt visa:

`Queued 02:17:04 → Steered 02:19:31`

i stället för att bara placera texten någonstans i konversationen och få det att se ut som om agenten såg den när du skrev den.

OpenAI rör sig samtidigt åt samma håll på **5 september**: Codex TUI behåller nu async-question drafts, selections och handled-message IDs över reconnect/session refresh, låter queued messages och working-status vara synliga samtidigt, och blockerar själva submission när threaden är unavailable. Det stärker principen att **lokalt operatörsarbete kan överleva disconnect, men delivery authority måste vara separat från editability**. fileciteturn7file0L2-L2 urlCodex: persistent async-question statehttps://github.com/openai/codex/commit/be2684ede0c3aa3e7789c4d83ad6a98ff5fe5b87

3. **Owner authority bör vara uttryckligen icke-transitiv mellan agent-generationer.** OpenAI skärpte Guardian den 4 september så att ursprungliga user instructions behålls som **host-owned authorization evidence** även när compaction eller transcript selection tar bort dem ur aktuell model context. Två detaljer är särskilt viktiga: om instruktionen är för stor för evidence-budgeten utelämnas den **atomiskt** och systemet markerar evidence som incomplete, i stället för att exponera en trunkerad text som potentiellt kan feltolkas som en mindre restriktiv permission. Och när en agent forkas kan parentens user instructions fortfarande göras model-visible för barnet, men de markeras så att de **inte blir child-local authorization**. fileciteturn8file0L2-L2 urlCodex: retained authorization evidence across forkshttps://github.com/openai/codex/commit/9c4253ffc1b954337bf2f494aadc55e9cd132a48

Detta bör enligt mig bli en hård Nortropic-invariant:

> **Context may inherit. Authority does not.**

Exempel:

```text
OWNER
"Agent A får göra X"
        │
        ▼
AGENT A
context + authority(X)
        │ spawns
        ▼
AGENT B
context says:
  "Owner allowed A to do X"

authority:
  NOT X
unless controller issued
an explicit delegation to B
```

Det löser en subtil framtida risk. När Nortropic börjar köra agentträd får en child/reviewer naturligtvis behöva veta vilka beslut du har fattat. Men bara för att texten *“Johnny approved production deployment”* finns i dess context betyder det inte att **den agenten** har deployment authority.

Jag skulle därför låta delegation bära ett explicit scope:

```text
authority_grant G17
principal     = worker-A
capability    = promote-candidate
scope         = candidate-C31
revision      = owner-auth-42
delegable     = false
```

Om `delegable=false` kan en child se G17 som provenance men aldrig använda den. Om authorization evidence saknas eller måste trunkeras är resultatet `AUTHORITY_EVIDENCE_INCOMPLETE`, aldrig en approximativ permission.

Den samlade arkitekturdiffen blir därmed:

```text
PLANNING WALL
      │
      ▼
Admission
      │
      ▼
Factory Room
  ├── Owner Attention     agent → owner
  ├── Steering Queue      owner → agent          ← NY
  │
  ▼
Controller generation C41
      │
      ├── execution lease
      ▼
Workers / provider turns
      │
      │ controller restart
      ▼
Controller Adoption Protocol                        ← NY
      │
      ▼
generation C42

Agent delegation
      ├── context inheritance
      └── explicit authority grants only           ← SKÄRPT
```

**Controller Adoption Protocol är dagens största guldkorn.** Det tar Nortropic ett steg från ett robust agent-control-room till ett verkligt **continuously operating control plane**: fabriken behöver inte vara lika kortlivad som processen som övervakar den, men ingen ny controller får ta över ett levande arbete utan att mekaniskt bevisa exakt vad den adopterar. Det är precis den sortens egenskap jag skulle vilja ha innan Factory Room tillåts styra långa autonoma runs på riktigt. memcite

---

## Meddelande 21 — ChatGPT (assistent)

Ja — **ett nytt mönster från OpenAI Codex den 5–6 september är tillräckligt bra för att flagga**, och jag tycker det skärper en viktig del av Nortropics multi-agent-arkitektur:

## Typade lineage-transitions i stället för “ärv parent state”

Två färska Codex-förändringar pekar åt samma håll. Den **5 september** lade Codex till managed worktree-creation där en session kan startas fresh eller forkas till en ny checkout. Vid en fork laddas destinationens konfiguration först, history ärvs bara för en verklig fork, och Codex **vägrar forka om developer instructions i destinationen skiljer sig från källan**. Den tillåter inte heller övergången från en explicit untrusted source och kräver att primärsessionen är idle utan queued input. citeturn493012view0turn264401view0

Den **6 september** fixade Codex ett närliggande multi-agent-fel: fresh child sessions hade ärvt parentens experimental-context/token-budget-aktivering även när childen startade med en annan modell som kanske inte stödde capabilityn. Nu är modellcapability explicit (`supports_experimental_context`, fail-closed default `false`); en **fresh child** återgår till användarens konfigurerade preferenser och applicerar sin egen modells capability/defaults, medan en **history fork** behåller parentens aktivering. citeturn493012view1turn865097view3

Detta ger en bättre generell regel än bara vår tidigare **“Context may inherit; authority does not”**:

> **Inheritance must depend on the lineage transition.**

Jag skulle göra det till ett explicit `Lineage Transition Contract` i Nortropic:

```text
TRANSITION
                         context   runtime config   capabilities   authority
────────────────────────────────────────────────────────────────────────────
fresh_worker                no/relevant   recompute      negotiate      explicit only
child_worker                bounded       recompute      negotiate      delegated only
history_fork                inherit       compatible     revalidate     explicit only
workspace_fork              inherit*      destination    revalidate     explicit only
controller_adoption         preserve      pinned        preserve       adopt exactly
resume_same_run             preserve      pinned        preserve       preserve binding

* only if policy/developer-instruction identity is compatible
```

Det viktiga är att Factory Room **inte bör ha en generell `CLONE`, `FORK` eller `SPAWN` som semantiskt betyder “kopiera allt från parent”**.

En övergång bör först klassificeras:

```text
SPAWN REQUEST
     │
     ▼
transition_kind
 fresh_child
 history_fork
 workspace_fork
 resume
 adoption
     │
     ▼
LINEAGE COMPATIBILITY CHECK
     ├─ context inheritance
     ├─ policy/config compatibility
     ├─ model/provider capabilities
     ├─ resource-envelope rules
     └─ authority delegation
     │
     ▼
new execution identity
```

Det ger också en konkret Planning Wall/Factory Room-förbättring. När du klickar **“fork worker”** borde UI:t kunna visa exempelvis:

```text
Fork W17 → W23

History          INHERITED
Workspace        NEW /worktrees/w23
Policy revision  P42 → P42     ✓ compatible
Model            Sol → Luna
Capabilities     RECOMPUTED
Resource budget  NEW CHILD ALLOCATION
Authority        NOT INHERITED
```

Om destinationens policy har förändrats:

```text
FORK BLOCKED

Parent policy     P42
Destination       P47

History cannot safely cross this boundary.
Start fresh or explicitly reconcile.
```

Det är mycket bättre än att låta en agent få en gammal transcript tillsammans med nya instruktioner och anta att kombinationen fortfarande betyder samma sak.

En tredje Codex-förändring från **5 september** förstärker samma princip: när användaren aktiverar exempelvis subagents eller memory skrivs inställningen via app-servern **för nya threads**, medan den redan pågående threaden uttryckligen lämnas oförändrad. Systemet rapporterar dessutom om en managed config override gjorde att önskemålet inte faktiskt kunde gälla. citeturn865097view0 Det innebär i praktiken ännu en bra regel:

> **Configuration change ≠ retroactive execution mutation.**

För Nortropic passar detta mycket bra med idén om att runs binds till en config/policy revision. Om du ändrar exempelvis multi-agent capability från Planning Wall ska det normalt påverka **framtida admissions**, inte tyst förändra semantiken hos ett redan pågående execution tree.

urlCodex: managed worktree session transitionshttps://github.com/openai/codex/commit/f6976ab0369921a59e23416083587149807d8f93  
urlCodex: capability-aware child-session inheritancehttps://github.com/openai/codex/commit/6af345407d9c2a568da9d01b6c4b81a9e61495c0  
urlCodex: feature opt-ins apply to new threadshttps://github.com/openai/codex/commit/fc748ab8d55091e6b969929463b7e8084467358b

**Dagens guldkorn är alltså inte worktrees i sig — dem har Nortropic redan. Det är att göra varje agent/session/workspace-övergång till en explicit typad lineage-operation med egna inheritance-regler.** Det skulle knyta ihop Factory Rooms framtida spawn/fork UI med config revisions, provider-neutral capabilities, resource envelopes och authority delegation på ett betydligt säkrare sätt. memcite

---

## Meddelande 22 — ChatGPT (assistent)

Ja — **två nya mönster från 6–7 september är tillräckligt starka för att påverka Nortropics Factory Room / Planning Wall**, och ett tredje mindre fynd stänger en viktig state-semantisk lucka.

### Runtime Delegation Envelopes: authority som tidsbegränsad, mätbar resurs

GitHub Agentic Workflows mergade **7 september 2026** sin nya **dynamic enclave delegation controller**, ovanpå compiler-stödet för dynamic repository policies som mergades dagen före. Det intressanta är inte “enclave” i sig utan hur de har gjort delegation till ett **runtime-kontrakt**. En agent behöver inte få permanent GitHub-access eller alla möjliga repos definierade i förväg; controllern kan istället ge ett isolerat agent-enclave en dynamisk capability-envelope med exempelvis tillåtna repo-ägare, sensitivity, policytyp, max antal repositories, antal invocationer, output-bytes, execution-seconds och expiry. Dynamic mode failar stängt bakom versionsgates. fileciteturn8file0L2-L2

Implementationen från i morse gör modellen ännu bättre: delegation-controller-state ligger i skyddad persistent storage så att den kan överleva en restart, control-endpointen är **separat från agentens executor/data endpoint och endast lokalt nåbar**, controllerns generation härleds från run-identity, och delegation-capabilityn exponeras uttryckligen **inte för primary agent**. Den fixar också ett konkret privilege-leak där primary agent tidigare indirekt kunde få GitHub-backenden routad trots att bara delegated enclaves skulle ha access. Expiry klampas dessutom mot faktisk runtime i stället för att lita på en gammal compile-time timestamp. fileciteturn1file0L2-L2

urlGitHub Agentic Workflows — dynamic delegation controller PR #59046https://github.com/github/gh-aw/pull/59046  
urlDynamic repository enclave policies PR #58880https://github.com/github/gh-aw/pull/58880

Detta tycker jag är **dagens största guldkorn för Nortropic**. Vi har redan kommit fram till `Context may inherit; authority does not` och explicita grants. GitHubs arbete visar hur nästa nivå bör se ut: authority bör inte bara vara `worker A may do X`, utan ett förstaklassigt **Delegation Envelope**:

```text
DELEGATION ENVELOPE D73

principal
  worker W23

capability
  github.repository.read

scope
  owners: [nortropic]
  max_repositories: 3
  sensitivity: confidential

budget
  invocations: 12
  output_bytes: 64k
  execution_seconds: 900

lifetime
  issued_for: run R91
  controller_generation: C44
  expires_at: min(policy_expiry, run_deadline)

audit
  delegation_id: D73
  policy_digest: ...
  labels: [...]

delegable: false
```

Och själva arkitekturen bör separera:

```text
CONTROLLER
   │
   ├──── private delegation control plane
   │            │
   │        issue/revoke/expire
   │            │
   ▼            ▼
WORKER  ───►  CAPABILITY ENCLAVE
               │
               ▼
        external resource/tool
```

Primary worker behöver alltså inte ens **inneha credential/capabilityn** den behöver för en enskild sub-operation. Den får en begränsad execution-path genom ett enclave som controllern styr.

Det ger Factory Room något mycket bättre än dagens generiska “permissions”-vy. Du skulle kunna klicka på en worker och se:

```text
ACTIVE DELEGATIONS

GitHub read
nortropic/*
3 repositories max
8 / 12 calls remaining
11m 42s remaining
non-delegable
```

och `REVOKE` blir en typad controller-intention, inte manipulation av agentcontext.

Det passar också extremt bra med vårt **Hierarchical Resource Envelope**: compute-budget och authority-budget blir två parallella men separata resursträd.

---

### Approval ≠ fresh human presence

OpenAI mergade **7 september 2026** ett experimentellt Codex-kontrakt för **device-authenticated user verification**. Motiveringen är uttryckligen att vissa verifieringar behöver ett app-svar **utanför vanlig automated approval och review**. En typad verification challenge routas till exakt en anslutning som har aktiverats som trusted host; endast den ägaren får svara; requesten exkluderas från replay; den avbryts vid disconnect eller authentication/account changes; själva proof-materialet hålls borta från logging/analytics och realtime får bara ett generiskt verification-event. Ett MCP-tool kan hållas väntande tills verifieringen är klar. Funktionen är fortfarande experimentell och inte annonserad som stabil capability. fileciteturn3file0L2-L2

urlCodex — opt-in MCP user verificationhttps://github.com/openai/codex/commit/555b82afa9b6dab81ca034ac61a2c8892844d670

Detta ger Nortropic en viktig separation som vi ännu inte uttryckt lika explicit:

```text
AUTHORITY
"Owner has authorized operation X"

        ≠

PRESENCE
"The authorized owner is present,
on an accepted device,
right now"
```

För nästan allt ska Nortropic **inte** kräva båda — det skulle gå rakt emot vår riktning bort från onödiga ägarstopp.

Men för en mycket liten klass verkligt känsliga handlingar kan ett tidigare approval vara otillräckligt. Exempelvis en framtida policy skulle kunna säga:

```text
promotion to production
  authority: required
  fresh_presence: not required

rotate production credential
  authority: required
  fresh_presence: required

irreversible external deletion
  authority: required
  fresh_presence: required
```

Det bör bli ett smalt **Step-Up Verification Plane**, inte ännu en approval-mekanism:

```text
OWNER ATTENTION
      │
      │ approval given
      ▼
CONTROLLER
      │
 high-impact action?
      │
      ├─ no ─────────────► execute
      │
      └─ yes
          ▼
  PRESENCE CHALLENGE
          │
          ├─ exact command/run binding
          ├─ trusted host only
          ├─ non-replayable
          ├─ proof never enters transcript
          └─ disconnect → cancelled
                  │
                  ▼
               execute
```

Särskilt när Factory Room så småningom kan styras från mobil/Slack/remote clients är detta en bra säkerhetsprimitive. **Approval kan vara durable; presence-proof ska vara ephemeral och non-replayable.**

Och viktigt: verification bevisar inte authority. Den bevisar bara färsk presence för den identitet/policy som redan har authority.

---

### Ett mindre men bra state-kontrakt: policy refusal är inte execution failure

GitHubs veckorapport publicerad **7 september** lyfter dessutom en ändring som mergades 5 september: safe-output-operationer som stoppas därför att configured policy korrekt säger nej markeras nu `skipped: true` med ett reason code i stället för vanlig `success:false`. Tidigare kunde en helt korrekt policy-denial trigga fail-fast, stoppa efterföljande oberoende outputs och förorena failure-rate-statistiken. Däremot lämnas exempelvis parser-differentialer som kan indikera ett verkligt attackförsök som hårda failures. fileciteturn2file0L2-L2 fileciteturn7file0L2-L2

urlPolicy-driven declines as skipped — PR #58767https://github.com/github/gh-aw/pull/58767

Detta kopplar direkt till vår tidigare **Unattended Interaction Policy**. När Nortropic gör:

```text
ASK
  ↓ unattended
DENY
  ↓
agent replans
```

ska detta **inte automatiskt räknas som ett misslyckat execution attempt**.

Jag skulle frysa en distinktion ungefär:

```text
EXECUTION FAILED
tool/runtime/verifier gjorde inte vad kontraktet krävde

POLICY BLOCKED
kontrollsystemet fungerade exakt som avsett

SKIPPED BY POLICY
operationen var otillåten men runnen kan fortsätta

OWNER BLOCKED
fortsättning kräver owner authority

SECURITY FAILURE
något bröt mot säkerhets-/integritetsinvariant
```

Det kommer göra Factory Rooms statistik och Pattern Observatory betydligt sannare. Annars lär sig systemet felaktigt att “strikt policy = dålig reliability”.

Den samlade arkitekturdiffen från dagens bevakning blir därför:

```text
PLANNING WALL
   │
   ├── Intent
   ├── Resource Envelope
   ├── Delegation Envelope             ← NY
   └── Owner policy
             │
             ▼
CONTROLLER
   ├── execution control plane
   ├── private delegation plane         ← NY
   └── step-up verification plane       ← NY
             │
             ▼
FACTORY ROOM
   ├── workers
   ├── active delegated capabilities
   ├── remaining authority budgets
   ├── owner questions
   ├── rare presence challenges
   └── truthful outcome semantics
        FAILED
        POLICY_BLOCKED
        OWNER_BLOCKED
        DONE
```

**Dynamic Delegation Envelope är det jag absolut skulle bära vidare till Nortropic.** Det är en mycket konkret mekanism för den organisation vi försöker bygga: agents får inte “access”; de får **precis den temporära, scoped, metered capability som arbetet kräver**, medan controllern behåller själva delegationsmakten. Step-up presence verification är sedan ett bra komplement för den lilla mängd operationer där även korrekt authority behöver färsk mänsklig närvaro. memcite

---

## Meddelande 23 — ChatGPT (assistent)

Ja — dagens sweep gav **två verkligt nya Nortropic-mönster och en viktig korrigering av gårdagens fynd**. Korrigeringen är tillräckligt säkerhetsrelevant för att jag vill börja där.

### Korrigering: “private control plane” får aldrig betyda “nätverket skyddar den”

I går beskrev jag GitHubs nya delegation-controller som att dess control endpoint i praktiken var lokalt/private-only. **GitHub korrigerade själva exakt detta antagande sent den 7 september.** Att en Docker-port publiceras endast på hostens `127.0.0.1` innebär inte att andra containers på ett gemensamt bridge network inte kan nå containerns interna `0.0.0.0`-listener direkt. GitHub ändrade därför dokumentationen så att nätverkstopologin uttryckligen **inte** betraktas som isoleringsgränsen. Den verkliga kontrollen är i stället en separat 256-bit capability som inte läggs i agentmiljöerna och verifieras innan någon control-routing sker. fileciteturn3file0L3-L7

Det skärper gårdagens Nortropic-idé på ett bra sätt:

```text
WRONG ASSUMPTION

"only reachable locally"
        ↓
 therefore trusted


NORTROPIC INVARIANT

network placement
      ≠
authority boundary

every control mutation
      │
      ▼
authenticated capability
+ exact scope
+ controller generation
+ principal
+ replay protection
```

Vi bör alltså fortfarande ha ett **private Delegation Control Plane**, men “private” ska betyda *logiskt separerad och explicit autentiserad*, inte *vi tror att ingen annan process kan routa dit*.

Det är framför allt relevant när Nortropic senare har flera workers, sandboxes, HOST-01/HOST-02 och kanske containeriserade runtimes. Ett fel i nätverkskonfigurationen får då öka attackytan, men får **inte automatiskt skapa authority**.

Detta är en direkt korrigering av min formulering i går. GitHubs egen nya formulering är bättre och bör vara vår modell.  
urlGitHub gh-aw: corrected delegation-control reachability contracthttps://github.com/github/gh-aw/commit/e42a43e9cf3c993e0ccfe717034d5ce8e1076a38

### Nytt: Run Closure behöver en **Durable Terminalization Barrier**

OpenAI Agents SDK mergade den **7 september** en ovanligt viktig failure-semantik: en run kan ha producerat ett accepterat final output, fått output guardrails godkända och redan kört terminal lifecycle hooks — men därefter misslyckas när resultatet ska persisteras till Session.

Det farliga är att en vanlig `resume` då kan upprepa modellkörning eller lifecycle-effekter trots att caller redan såg resultatet.

OpenAI markerar därför nu runnen `terminal_unrecoverable` under exakt detta fönster. Markören sätts **efter att final output/guardrails/hooks accepterats men innan persistence är klar**, och tas bort först när terminalturnen faktiskt är durable. Om persistence misslyckades vägrar SDK:n senare resume **innan Session-, sandbox-, model-, tool-, guardrail- eller hook-arbete får utföras**. fileciteturn1file0L3-L7

Det här tycker jag fyller en verklig lucka i vår tidigare `Run Closure Barrier`.

Vi har sagt:

```text
descendants = 0
leases = 0
background work = 0
spawn gate = closed
        ↓
DONE
```

Men det räcker inte.

Det bör snarare vara:

```text
EXECUTION QUIESCENT
 descendants = 0
 leases = 0
 spawn gate = closed
        │
        ▼
OUTPUT ACCEPTED
        │
        ▼
TERMINAL COMMIT
 result
 evidence
 receipts
 usage
 lineage
 terminal state
        │
        ├── persistence fails
        │        ↓
        │   TERMINAL_UNRECOVERABLE
        │   reconcile / new run
        │   NEVER resume blindly
        │
        ▼
DURABLE TERMINAL
        │
        ▼
DONE
```

Alltså:

> **Execution closure ≠ durable completion.**

Det här är mycket Nortropic-kompatibelt. Factory Room kan visa ett resultat direkt som exempelvis `FINALIZING`, men controllern får inte mynta den starka terminala sanningen förrän terminal-receiptet är persistent.

Och framför allt: om Nortropic hamnar i det konstiga läget:

```text
external effect happened
final output existed
owner/UI may have seen it
terminal persistence failed
```

får vi aldrig låtsas att det bara är en vanlig failed run som kan köras igen.

Jag skulle lägga detta som en faktisk execution invariant bredvid `Run Closure Barrier`, inte som dashboardlogik.

urlOpenAI Agents SDK: fail closed on unpersisted accepted terminal outputhttps://github.com/openai/openai-agents-python/commit/e51633133e671e82df221e1f1713f7cb1cef9711

### Nytt: **Execution Provenance ska bindas både till den faktiska runtime:n och den människa vars instruktion exekveras**

Två separata projekt råkade under den 7 september angripa varsin halva av samma problem.

Codex har börjat registrera **launch-time executable identity**. Anledningen är konkret: en installer kan retargeta symlinken som heter exempelvis `current-codex` medan processen fortfarande körs. Om man senare bara tittar på sökvägen kan man därför tro att en levande process kör binary B trots att den faktiskt startades med binary A. Codex canonicaliserar nu binaryn före launch och sparar dess BLAKE3-identitet tillsammans med PID-recorden. citeturn871680view1

Codex lade dessutom till ett separat `providerId` för executor-builden baserat på **git commit + compiler target**, eftersom versionsnumret ensamt inte identifierar vilken runtime implementation som faktiskt körs. De är noga med att skilja på build identity och exakt binary identity. citeturn904297view0

Det förbättrar vår tidigare `Controller Adoption Protocol`:

```text
ADOPT RUN R17

run_id
process_id
process_start_time
provider_session
controller_generation

PLUS

executor_build_id
launched_binary_digest
```

En ny controller ska alltså inte bara fråga:

**“Är process 7124 fortfarande där?”**

utan:

**“Är detta exakt den runtime-artifact som R17 faktiskt startades med?”**

Det är särskilt viktigt om Nortropic på sikt automatiskt uppdaterar Codex/provider runtimes medan andra runs fortfarande arbetar.

urlCodex launch-time executable identityturn871680view1  
urlCodex stable executor build identityturn904297view0

Paperclip löste samtidigt den mänskliga halvan av provenanceproblemet. I en stor ändring mergad **7 september** skiljer de nu uttryckligen **task ownership från execution identity**. Om flera människor använder samma agent följer GitHub-identiteten den person vars instruktion agenten faktiskt har accepterat — genom queued messages, steering, retries, delegation, approvals och restart. Credentials hämtas först när den konkreta Git/GitHub-operationen börjar, och en redan startad operation behåller sin fångade identitet även om någon annan steer:ar agenten därefter. Vid osäker steering-acknowledgement stoppas ny credential acquisition tills identiteten reconciliats. fileciteturn2file0L3-L7

Det ger en väldigt elegant generell Nortropic-modell:

```text
TASK
"fix deployment pipeline"

ownership
  organizational responsibility

execution attempt A17
  │
  ├── instruction_principal
  │      owner/operator identity
  │
  ├── runtime_principal
  │      worker W7
  │
  ├── executor_identity
  │      provider/build/binary
  │
  ├── authority_grants
  │      exact delegated capabilities
  │
  └── causal lineage
```

Alltså:

> **Task identity, human principal, agent principal, runtime identity och authority är fem olika saker.**

De kan ofta råka sammanfalla, men Factory Room/Controller ska inte modellera dem som samma fält.

För Nortropic är det initialt mer foundation än UI, men den dag Factory Room används av flera personer eller organisationsfunktioner blir detta avgörande. Ett accepted steering-meddelande från person B ska kunna ändra principal för **framtida** operationer utan att retroaktivt byta identitet på en operation person A redan startade.

urlPaperclip: responsible-person execution identity for shared agentshttps://github.com/paperclipai/paperclip/commit/1cc45086d3b2f2710d4e161b0dc9ad1d3662a9a8

Den samlade förändringen jag skulle bära in i Recompile-korpusen är därför:

```text
PLANNING WALL
      │
      ▼
typed work / intent
      │
      ▼
CONTROLLER
 ├── authority ≠ topology
 ├── execution principal
 ├── runtime provenance
 │
 ▼
FACTORY
      │
      ▼
Run Closure Barrier
      │
      ▼
Durable Terminalization Barrier   ← viktigast idag
      │
      ▼
AUTHORITATIVE DONE
```

**`Durable Terminalization Barrier` är dagens största nya guldkorn.** Men GitHubs korrigering är nästan lika viktig eftersom den rättar vår egen modell: Nortropic ska aldrig vinna sin säkerhet på antagandet att ett control interface “nog inte går att nå”. Authority ska fortfarande hålla även den dag nätverkstopologin visar sig vara felkonfigurerad. memcite

---

## Meddelande 24 — ChatGPT (assistent)

Ja — **dagens sweep gav två nya mönster som jag tycker är starka nog för Nortropic, plus ett säkerhetskontrakt som bör följa med vår resume/adoption-modell.** Det mest intressanta är att OpenAI nu explicit löser själva **cutover-problemet** när kontroll över ett levande eventflöde byter ägare.

### 1. Event-stream handoff bör ha en explicit cutover-barriär

Codex lade den **8 september 2026** till `queued_event_count()` på en levande `CodexThread` av ett väldigt specifikt skäl: innan event-receivern överförs till en ny läsare tar den gamla läsaren en snapshot av hur många events som redan står i kön. Den gamla läsaren måste förbli **enda event-reader** medan exakt dessa events konsumeras; events som kommer in efter snapshoten lämnas kvar till nästa läsare. citeturn296736view1

Det ser litet ut i koden, men är en riktigt bra control-plane primitive:

```text
EVENT PRODUCER
      │
      ▼
old controller / reader
      │
      │ snapshot:
      │ queued_before_cutover = 17
      │
      ├── consume exactly 17
      │
      │ events arriving meanwhile
      │ remain queued
      ▼
CUTOVER
      │
      ▼
new controller / reader
```

Detta fyller en lucka i vår tidigare **Controller Adoption Protocol**. Vi hade identifierat hur en ny controller verifierar *vilken execution* den adopterar, men inte lika precist hur ownership av ett **pågående observability/eventflöde** ska flyttas utan dubbelläsning eller tappade events.

För Nortropic skulle jag göra detta starkare än Codex lokala queue-count-teknik och kalla det en **Event Ownership Cutover**. Varje canonical event bör ha monotont `event_seq` inom en `source_generation`, och adoptionen bör få en explicit watermark:

```text
old reader owns <= E1842

CUTOVER RECORD
run_id            R17
source_generation G9
last_old_event    E1842
new_reader_from   E1843

old reader:
  may finish <= E1842
  may never consume > E1842

new reader:
  may never consume <= E1842
  begins at E1843
```

Queue-count är en bra processlokal implementationsteknik; **watermark + generation är den Nortropic-version jag skulle frysa arkitektoniskt**.

Factory Room kan då byta controller, websocket, backend eller projection reader mitt under arbete utan att behöva stoppa producenten och utan att efteråt fråga “såg båda samma event?” eller “försvann något i bytet?”.

urlCodex: finite event drain before receiver transferhttps://github.com/openai/codex/commit/78932f4493995cb1236bcad411c926a9f5c179b2

### 2. Ett kommando lever längre än RPC-svaret som startade det

I dag, **9 september**, mergade Codex ytterligare en förändring som ligger väldigt nära detta. De upptäckte att thread startup, resume och rollback kunde **leva längre än request-handlern som initierade operationen**. Då kunde connection draining och request serialization tro att arbetet var klart för tidigt.

Nu väntar RPC-livscykeln på att det delegerade thread-arbetet faktiskt når sin completion point. De använder explicita completion-signaler, håller drain-admission aktiv tills svaret verkligen har producerats av den delegerade listenern, släpper lås/permits i rätt ordning så completion själv inte deadlockar, och rensar köade requests när deras connection har dött. citeturn488750view0

Det här ger en mycket bra generell Nortropic-regel:

> **Transport completion ≠ command completion.**

Vår tidigare `Run Closure Barrier` gäller hela runnen. Jag skulle nu lägga ett motsvarande mycket mindre kontrakt runt varje control-plane-operation: **Command Completion Lease**.

```text
Factory Room
    │
    │ RUN.RESUME C91
    ▼
Controller accepts
    │
    ├── acceptance receipt → UI
    │
    └── completion lease L91 remains ACTIVE
              │
              ▼
       delegated runtime work
              │
              ▼
       authoritative outcome
              │
              ▼
       lease L91 RELEASED
```

Det är alltså fullt möjligt att UI:t redan har fått:

`Command accepted`

samtidigt som controllern fortfarande måste betrakta operationen som **in flight**.

Det spelar direkt in i graceful shutdown, Controller Adoption, reconnect och rolling upgrades. Nortropic får inte säga:

```text
HTTP/WebSocket response sent
→ therefore safe to shut down controller
```

utan:

```text
all command completion leases settled
+ no new admission
+ event ownership cutover complete
→ safe control-plane drain
```

Det här är enligt mig dagens **största guldkorn** eftersom det knyter ihop flera saker vi redan hittat till ett sammanhängande control-plane-protokoll:

```text
RUN CLOSURE BARRIER
        │
execution tree

COMMAND COMPLETION LEASES
        │
control operations

EVENT OWNERSHIP CUTOVER
        │
observation stream

DURABLE TERMINALIZATION
        │
persisted truth
```

De fyra beskriver nu olika sorters “är det verkligen klart?” snarare än att allt reduceras till ett generiskt `DONE`.

urlCodex: keep thread RPCs alive through delegated completionhttps://github.com/openai/codex/commit/102e1763b90e70d79a0bba5d262cf71f904583c1

### 3. Resume-snapshots måste vara **credential-inert**

En annan Codex-ändring från **9 september** är säkerhetsmässigt väldigt relevant för vår persistent-runtime-riktning. OpenAI hittade att credentials kunde gömmas för naiva raw-text-kontroller genom shell quoting, aliases, functions, heredocs och Zsh-arrays. Ännu värre: även efter att credential broker ersatt riktiga credentials med dummy-värden kunde shell startup-filer **återställa de riktiga hemligheterna när snapshoten replayades**. citeturn296736view3

Codex gör nu bland annat literal decoding utan eval, avvisar snapshots där credentials göms i executable shell source, skyddar replay mot credential-rehydrering via startup files och rensar inherited environment innan escalated commands startas. citeturn296736view3

Det här kompletterar vår tidigare Delegation Envelope-idé med en mycket viktig invariant:

> **Execution state may persist. Credential authority must not persist inside that state.**

Alltså:

```text
RUN SNAPSHOT

workspace             YES
shell convenience     YES
session lineage       YES
tool state            YES
queued work           YES

credential secret     NO
delegated token       NO
stale authority       NO
```

Vid resume/adoption:

```text
snapshot
   │
   ▼
restore execution state
   │
   ▼
current controller authority check
   │
   ▼
re-broker fresh capability
for the exact principal / operation / envelope
```

Det vore farligt om Nortropic i framtiden hade fantastiskt bra `authority_grant D73` och samtidigt råkade bädda in en gammal GitHub-token i ett återspelbart shell-state. Då skulle persistent runtime-state i praktiken bli en **bakdörr runt authority-modellen**.

Jag skulle därför låta varje framtida resumable runtime-adapter deklarera något i stil med:

```text
snapshot_security:
  credentials_embedded: false
  authority_embedded: false
  replay_requires_rebroker: true
  sanitized_digest: ...
```

och faila stängt om detta inte kan bevisas för trust-kritiska lanes.

urlCodex: harden credential handling in shell snapshots and replayhttps://github.com/openai/codex/commit/ec512d23470c6afe30c975d570d181f34813b9a2

Den arkitekturdiff jag skulle bära in i Nortropic från dagens bevakning är därför:

```text
FACTORY ROOM
      │
      ▼
COMMAND
acceptance receipt
      │
Command Completion Lease
      │
      ▼
CONTROLLER / EXECUTION
      │
      ├──── persistent state
      │       └── credential-inert
      │
      └──── event stream
               │
        Event Ownership Cutover
               │
        controller generation N+1
```

**Event Ownership Cutover + Command Completion Lease hör enligt mig ihop och bör bli en del av samma framtida controller-lifecycle-kontrakt.** Det gör Nortropic robust inte bara mot agentfel utan mot de mycket mer subtila race conditions som uppstår när ett verkligt control room reconnectar, restartar, uppgraderas och byter ägare medan fabriken fortsätter arbeta. memcite

---

## Meddelande 25 — ChatGPT (assistent)

Ja — **dagens sweep gav tre fynd som är värda att bära vidare**, och två av dem fyller faktiska luckor i Factory Room-modellen snarare än att bara bekräfta tidigare riktning.

### Semantic Progress Lease: autonomi behöver en no-progress breaker

OpenAI landade sent **9 september** en förändring i Codex där automatiska goal-continuations inte längre får snurra obegränsat bara för att de tekniskt sett “lyckas”. Efter tre automatiska turns med tomt finalsvar och **ingen annan aktivitet** markeras målet `blocked`. Streaken nollställs när verklig aktivitet sker, när användaren ingriper eller när målet ändras. fileciteturn2file0L4-L6 fileciteturn2file0L58-L61

Detta är något annat än Nortropics Resource Envelope. Token-, tids- och kostnadsbudget svarar på *hur mycket* arbete agenten får göra. Här mäts i stället om autonomin **fortfarande gör framsteg**.

Jag skulle därför lägga till en **Semantic Progress Lease** för unattended goals:

```text
automatic continuation
        │
        ▼
did durable progress occur?
   │               │
  yes              no
   │               │
renew lease     no_progress += 1
                   │
             threshold reached
                   ▼
          BLOCKED_NO_PROGRESS
```

För Nortropic bör “progress” vara starkare än Codex enkla textsignal. Lease:n bör helst förnyas av controller-observerbara saker som ny verifierad evidens, faktiskt state-advance, löst blocker, accepterad artifact-delta eller en meaningful tool-result som senare konsumeras. **Agentens egen utsaga “jag gjorde framsteg” ska inte räcka.**

Det ger Factory Room en mycket sannare unattended-status:

`RUNNING → STALLED → REPLAN/ATTENTION`

i stället för att en agent kan se frisk ut medan den producerar tomma eller cirkulära continuation-turns och långsamt äter upp budgeten.

urlCodex: Block goals after three empty automatic continuation turnshttps://github.com/openai/codex/commit/0735c519789d300097554425cc3d7cf3f2d718a1

### Snapshot-then-Follow: historisk sanning och live-stream bör vara två olika kontrakt

Tidigt **10 september** ändrade OpenAI Codex Python-SDK:n sin eventmodell. En `thread.turn(...)`-handle får events från ögonblicket requesten skickas, medan andra consumers får **bara events från den punkt där de ansluter**. Codex slutade implicit replaya completed items, token usage och terminal-events till sena subscribers; vill klienten se det förflutna ska den uttryckligen läsa thread-history. fileciteturn3file0L3-L6 fileciteturn3file0L66-L69

Detta är ett litet SDK-beslut med stor betydelse för Factory Room. Jag skulle frysa principen:

> **Historical truth is read. Live activity is followed. Never confuse replay with observation.**

En Factory Room-klient bör alltså ansluta ungefär så här:

```text
1. READ authoritative snapshot/history
              │
              │ watermark W1842
              ▼
2. ATTACH live subscription
              │
              ▼
3. receive events > W1842 only
```

Det kompletterar vår tidigare Event Ownership Cutover. Cutover löste byte mellan controllers/readers; detta löser **semantiken för varje enskild observer**.

Det förhindrar subtila kontrollrumsfel: en mobil som reconnectar ska inte animera gammalt arbete som nytt, ett tidigare `DONE` ska inte se ut som en ny terminal transition, gamla owner-frågor ska inte återuppstå bara för att klienten ansluter sent, och två samtidiga Factory Room-klienter kan ha olika live-eventhistorik samtidigt som båda ser samma canonical state.

Jag skulle kalla detta **Observer Attachment Contract / Snapshot-then-Follow** och låta varje subscription bära explicit `attached_after_watermark`.

urlCodex: Start turn subscriptions at their attachment pointhttps://github.com/openai/codex/commit/ddea03ad049142943bdbf13e937b1d67e8c1ba0c

### Planning Wall bör ha heterogena execution-noder — inte göra allt till “agent work”

Microsoft Conductor landade också **10 september** en ny direkt MCP-step. Den anropar ett bestämt MCP-tool med bestämda argument **utan någon LLM i loopen**, kan ligga i vanliga flows, parallella grupper och `for_each`, producerar strukturerat routbart resultat och visas som en egen typ av nod i dashboarden. Lifecycle-events visar bara säker metadata snarare än tool-input/output. fileciteturn4file0L3-L6 fileciteturn4file0L206-L209

Deras implementation innehåller dessutom en bra säkerhetsdetalj: om ett side-effecting MCP-call avbryts och utfallet är okänt auto-replayas det inte bara därför att browsern försvann. Det blir ett explicit uncertain outcome som kräver en senare re-execution boundary. fileciteturn4file0L4-L6 Det senare har Nortropic redan fångat genom våra command/reconciliation-kontrakt; **det nya användbara här är node-arkitekturen**.

Planning Wall bör enligt mig inte bara visualisera:

```text
Agent A
→ Agent B
→ Reviewer
```

utan snarare den verkliga execution-topologin:

```text
AGENT / REASON
      │
      ▼
DETERMINISTIC ACTION
MCP / API / script
      │
      ▼
MECHANICAL GATE
      │
      ├── OWNER DECISION
      │
      └── AGENT / REASON
```

När tool och argument redan är beslutade finns inget värde i att låta en modell “välja” att göra samma anrop igen. Controllern kan utföra en typad deterministic action under dess Delegation Envelope. Det sparar tokens, minskar modellens authority-yta och gör Factory Room mycket lättare att förstå och replaya.

Det passar dessutom Nortropics grundidé ovanligt bra: **agentisk intelligens där omdöme behövs, determinism där omdöme inte behövs**.

urlMicrosoft Conductor: deterministic MCP workflow stepshttps://github.com/microsoft/conductor/commit/f7f444cedf9623943960d0b492824bf96dc52aba

Av dagens tre skulle jag prioritera **Semantic Progress Lease först**, sedan **Snapshot-then-Follow**. Tillsammans gör de Factory Room bättre på två av de svåraste aspekterna av verklig autonom drift: att veta när en agent fortfarande *gör framsteg*, och att veta skillnaden mellan *vad som redan hänt* och *vad som händer just nu*.

---

## Meddelande 26 — ChatGPT (assistent)

Ja — **dagens sweep gav två materiella mönster som jag tycker ska in i Nortropics framtida control-plane-design, och ett av dem nyanserar en princip vi redan har fryst.** Båda kommer från färska Codex-ändringar den **10–11 september 2026**. citeturn380675view0

### Control State behöver explicita uppdateringsgränser

Den 10 september ändrade OpenAI Codex hur globala instruktioner hanteras i långlivade sessions. Tidigare behöll en aktiv root-thread den version av globala `AGENTS.md`-instruktioner som fanns när threaden startades. Nu läses de om **vid varje model-request boundary — även efter tool calls inom samma turn**. En förändring träder alltså i kraft utan att hela sessionen behöver startas om. Samtidigt behåller systemet senaste kända goda instruktioner om en refresh misslyckas, rensar dem först när källan bekräftat tas bort/töms, serialiserar refresh-operationerna och låter nya subagents ärva den snapshot som faktiskt var applicerad hos parenten. Guardian-reviewers byts dessutom när den relevanta instruction-snapshoten ändras. citeturn502681view0

Det här **nyanserar vår tidigare regel** `Configuration change ≠ retroactive execution mutation`. Den regeln är fortfarande riktig för exempelvis vissa capabilities, providerinställningar och admission-bundna kontrakt. Men det börjar bli tydligt att Nortropic inte bör ha *en* enda config-update-semantik.

Jag skulle frysa ett **Control State Update Boundary** där varje typ av styrinformation deklarerar när en ny revision får börja gälla:

```text
CONTROL ITEM
────────────────────────────────────

RUN_PINNED
trust contract
execution identity
certain capability/config choices

REQUEST_BOUNDARY
operational guidance
organization-wide instructions
standards / working doctrine

ACTION_BOUNDARY
effective permission/grant evaluation
tool-specific constraints

IMMEDIATE_REVOKE
kill / revoke capability
security invalidation

EXPLICIT_STEERING
owner steering queue
```

Det viktiga är causal clarity. Om `guidance G18` publiceras medan en worker exekverar ett tool-call, får G18 **inte retroaktivt förändra betydelsen av det redan utsända tool-callet**. Den blir aktiv när nästa definierade boundary passeras.

Factory Room skulle då kunna visa något i stil med:

```text
Worker W23

run policy       P42   pinned
global guidance  G18   applied at request #91
authority grant  D73   expires 09:14
steering         S12   queued
```

och varje model invocation får `applied_control_revisions`.

Det här är en bättre modell för Nortropics framtida Evolution/Update-plane också: mindre förbättringar av arbetssätt kan börja påverka långlivade workers **utan att vi behöver döda dem**, samtidigt som trust- och authority-kontrakt inte råkar hot-reloadas bara för att en Markdown-fil ändrades.

Min Nortropic-regel skulle därför bli:

> **Every control datum declares its activation boundary. “Config changed” is not a sufficient execution semantic.**

urlCodex — refresh global instructions at model-request boundarieshttps://github.com/openai/codex/commit/935ac7710da6d33cf700b3fd953a878f9e1c4535

### Cached approval får bara återanvändas under monotont icke-vidgad authority

Den andra ändringen är ännu mer direkt kopplad till vår önskan att minska onödiga owner-stops.

Codex upptäckte den 10 september att Guardian kunde återanvända en tidigare approval/risk-score för ett `exec_command` trots att ett senare kommando begärde **ytterligare permissions som den gamla scoren aldrig hade bedömt**. De ändrade därför beteendet så att en oscorad permission-widening — i deras regressionstest extra network permissions — ogiltigförklarar cached approval och failar stängt med `scoring_failure`. Vanliga kommandon med oförändrad permission-scope får däremot fortsätta använda cache:n. citeturn454157view0

Det här ger oss en mycket bra generell regel för Nortropic:

> **Approval reuse is valid only under scope dominance. Any authority widening requires fresh evaluation.**

Det bör inte vara:

```text
"Owner approved shell earlier"
        ↓
reuse approval
```

utan ungefär:

```text
APPROVAL A17

principal
action class
argument/risk fingerprint
effective capability scope
policy revision
execution context
lifetime/run binding

new request R
      │
      ▼
same relevant semantics?
      │
      ├─ no → RE-EVALUATE
      │
      ▼
effective_scope(R)
    ⊆
approved_scope(A17)?
      │
      ├─ yes → MAY REUSE
      └─ no  → INVALIDATE / RE-EVALUATE
```

Det här är **väldigt användbart för Nortropics trust-baserade Owner Attention-modell**. Vi vill ju uttryckligen inte att du ska behöva svara på samma rutinfråga tjugo gånger. Då bör ett tidigare beslut kunna leva vidare — men bara medan systemet mekaniskt kan bevisa att den nya handlingen inte har fått större authority-yta.

Det gör det möjligt att vara både mindre störande **och** säkrare.

### Den viktiga detaljen från 11 september: jämförelsen måste göras mot den verkliga execution hosten

Codex gjorde i dag, 11 september, nästa närliggande förändring. Permission profiles kompileras nu med explicit **execution-host path context**: path grammar, faktisk `cwd`, home directory och workspace roots. Samma deklarerade policy kan alltså få olika effective semantics beroende på var den körs. Osäkra glob/path-resolutioner nekas konservativt, och profile-availability beräknas mot den efterfrågade exekveringsmiljön. citeturn221131view0

Det här blir viktigt när Nortropic går från en maskin till HOST-01/HOST-02, cloud workers eller olika sandbox-runtimes.

Jag skulle därför skilja på:

```text
DECLARED POLICY
build-worker-safe@P42
        │
        ▼
COMPILE AGAINST EXECUTION HOST

host              HOST-02
path convention   ...
workspace roots   ...
home              ...
runtime facts     ...
        │
        ▼
EFFECTIVE POLICY E91
digest: ...
```

Approval-cachen ovan bör bindas till **effective policy/context**, inte bara namnet `P42`.

Det förhindrar exempelvis att ett approval som var säkert för:

```text
/worktrees/project-a
```

återanvänds efter att arbetet flyttats till en host där samma symboliska workspace-policy faktiskt resolve:ar annorlunda.

Factory Room bör därför på sikt visa både **Declared** och **Effective permissions**, och den senare bör vara den som controllern verkligen fattar beslut mot.

urlCodex — resolve permission profiles against execution-host contexthttps://github.com/openai/codex/commit/9e22e74e8dcab53f8bf1799c0eed1f9834c32f1a

De tre bitarna går ihop ganska elegant:

```text
CONTROL STATE
     │
     ├── activation boundary
     │
     ▼
EXECUTION CONTEXT
host / workspace / principal
     │
     ▼
EFFECTIVE CAPABILITY SCOPE
     │
     ▼
approval exists?
     │
     ├── requested scope <= approved scope
     │          └── reuse
     │
     └── permission widening
                └── fresh evaluation
```

**Dagens största Nortropic-vinst är egentligen kombinationen.** Vi får en mer mogen modell där långlivade workers kan ta emot säkra organisatoriska uppdateringar utan restart, samtidigt som cached human/Guardian decisions aldrig “smittar” en operation som blivit mäktigare än den som faktiskt bedömdes.

Det är precis den balans vi vill åt i Factory Room: **färre onödiga owner-stops, men inget implicit authority creep.** memcite

