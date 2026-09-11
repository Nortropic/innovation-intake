# Brainstorma hårdvarusetsning — fullständigt transkript

**Källprojekt:** Improvements (ChatGPT-projekt)
**Chatt:** Brainstorma hårdvarusetsning
**URL:** https://chatgpt.com/c/6a9948f8-91d8-83ed-a3fb-e81a5d7410c3
**Exportdatum:** 2026-09-11
**Antal meddelanden:** 22 (8 användare, 14 assistent)
**Syfte:** Fångad i PROJECT_SWEEP Improvements R39 (data-layer, WYSIWYG-filtrerad); syftet med samtalet avgörs av dess innehåll, inte av denna rubrik.

**Innehåll i korthet:** Samtalet öppnar med: ”Jag vill diskutera hårdvara för våra setup, just nu har jag min frus MacBook Pro. Brainstorma kring nu läge, vad framtida setup kan eller bör vara etc. Jag är rätt nybörjare på AI setups och hårdvara ” och avslutas med: ”Ja. För **HOST-01 i den Nortropic-arkitektur vi har beskrivit** hade jag valt en väldigt specifik konfiguration:  product["turn521059product0","Mac mini M6 12-core / 32 GB / 1 TB",{"render_as":"hero”

> Notis: rader som ser ut som käll-/citat-chips från ChatGPT är en del av
> originaltexten och har bevarats ordagrant. 0 bilagor inventerade (data-layer: distinkta plattforms-fil-id ur metadata.attachments + icke-textdelar; en bild som adaptern listar två gånger räknas en gång); bytes registreras separat via register-attachment där plattformen exponerar dem.

---

## Meddelande 1 — Johnny (användare)

Jag vill diskutera hårdvara för våra setup, just nu har jag min frus MacBook Pro. Brainstorma kring nu läge, vad framtida setup kan eller bör vara etc. Jag är rätt nybörjare på AI setups och hårdvara generellt

---

## Meddelande 2 — ChatGPT (assistent)

Jag skulle tänka på hårdvaran som **Nortropics fysiska lager**, inte som “vilken dyr AI-dator ska jag köpa?”. För ert nuvarande arbetssätt är den viktigaste frågan först **vad som faktiskt kör lokalt kontra i molnet** — det förändrar nästan hela köpbeslutet.

---

## Meddelande 3 — ChatGPT (assistent)

Den första stora slutsatsen är redan tydlig: **Codex är inte en lokal 100-miljardersmodell som din MacBook måste “orka köra”.** Codex-klienten arbetar på datorn och kör filer/kommandon där, medan den tunga modellinferensen ligger hos OpenAI. En snabbare dator gör alltså framför allt builds, tester, worktrees, webbläsare, containers och många parallella agentprocesser bättre — den gör inte automatiskt själva GPT-modellen smartare.

---

## Meddelande 4 — ChatGPT (assistent)

För Nortropic blir den framtida frågan därför snarare **“hur många samtidiga arbetare och tjänster ska den fysiska maskinen bära?”** än “hur stor AI-GPU behöver vi?”. Och där börjar 8 GB-klassen bli trång långt innan processorn egentligen är gammal: flera Codex-sessioner, VS Code, webbläsare, Node, tester, worktrees och eventuella containers konkurrerar om samma minne.

---

## Meddelande 5 — ChatGPT (assistent)

Ja — och jag tror faktiskt att det här är ett ganska viktigt Nortropic-spår, eftersom **“AI-hårdvara” lätt får en nybörjare att köpa helt fel saker**. För er bör vi börja med systemarkitekturen och först därefter välja dator.

Utifrån vår tidigare setup arbetar du fortfarande från en äldre M1 MacBook Pro med 8 GB minne, och dessutom är den din frus dator. Det första problemet är därför nästan mer **ägande, minne och driftsäkerhet** än rå processorprestanda. memcite

## Först: vad datorn egentligen gör

När du sitter med ChatGPT och Codex kan man förenklat tänka:

```text
DIN MAC
────────────────────────
VS Code
Git
Nortropic-repot
worktrees
Node/Python
tester
webbläsare
lokala servrar
Codex-klienten
containers
filer/secrets
────────────────────────
        ↕ internet
────────────────────────
OPENAI / ANDRA PROVIDERS
Den enorma AI-modellen
Det tunga "tänkandet"
────────────────────────
```

Codex är en lokal agent som kan läsa, ändra och köra saker på din dator, men den stora modellinferensen levereras av OpenAI. OpenAI beskriver också Codex som ett system där flera agenter kan arbeta parallellt i separata worktrees. citeturn983440search0turn983440search1turn983440search2

Det betyder något viktigt:

> **En dator för 70 000 kr gör inte GPT-5.6 Sol dubbelt så smart som en dator för 20 000 kr.**

Men den kan göra det möjligt att ha:

```text
Codex A
Codex B
Supervisor
tester
webbserver
Playwright
flera worktrees
browser
databas
Docker
observability
Nortropic services
```

igång samtidigt utan att maskinen går på knäna.

Och **det är där jag tror Nortropics hårdvarubehov kommer växa.**

---

# Vad som är viktigt i en dator för Nortropic

På 5-åringsnivå:

**CPU** = hur snabbt datorn gör vanligt arbete. Builds, tester, kompilering osv.

**RAM/minne** = hur mycket den kan hålla igång samtidigt. För er är detta väldigt viktigt.

**GPU** = framför allt intressant om vi själva börjar köra stora AI-modeller, bild-/videomodeller osv lokalt.

**SSD** = hur mycket kod, worktrees, Docker-images, modeller, cache och data vi kan lagra.

För **Nortropic idag** skulle jag rangordna:

```text
1. RAM
2. stabilitet / dedikerad maskin
3. SSD
4. CPU
5. GPU
```

Inte GPU först.

### 8 GB → det är den verkliga svagheten

En M1 är fortfarande en helt användbar processor.

Men 8 GB för:

- macOS
- VS Code
- Chrome
- flera Codex-processer
- Node
- Git worktrees
- testsviter
- lokala tjänster

är ganska lite.

Jag skulle sätta ungefär:

```text
16 GB   = fungerar
24 GB   = bra
32 GB   = min rekommenderade Nortropic-bas
48–64 GB = mycket bekvämt / lokal-AI-redo
128 GB+ = specialiserad lokal AI
```

---

# Så jag tror inte första köpet bör vara en monster-PC

Min **sweet spot för Nortropic just nu** är mycket mer odramatisk:

## Mac mini M6, 32 GB, 1 TB

Den nya Mac mini presenterades faktiskt **25 augusti 2026**, alltså för bara några dagar sedan. Den går att förbeställa nu och släpps **22 september 2026**. M6-modellen börjar på 11 995 kr; en 32 GB/1 TB-konfiguration ligger just nu runt 23 700 kr hos svenska återförsäljare. citeturn456816search1turn456816search4

product["turn456816product0","Mac mini, M6 12-Core, grafik 12-Core, 32GB, 1TB SSD",{"render_as":"hero"}]

Jag tycker att den är väldigt intressant därför att den kan bli något annat än bara **Johnnys dator**.

Den kan bli:

> **Nortropic Host 01.**

Alltså:

```text
NORTROPIC-HOST-01
Mac mini
32 GB RAM
1 TB SSD
Ethernet
always-on

├── nortropic-system
├── worktrees
├── Codex executor A
├── Codex executor B
├── supervisor
├── local tests
├── browser automation
├── development services
└── observability
```

Och då kan din laptop mer och mer bli:

```text
JOHNNYS COCKPIT

ChatGPT
VS Code
Verkstadsgolvet
review
owner decisions
communication
```

Det tycker jag är mycket mer framtidsriktigt.

---

# Den framtida Nortropic-setupen jag ser framför mig

Inte en superdator.

Utan **lager**.

```text
                  JOHNNY
                     │
              MacBook / cockpit
                     │
                     ▼
             NORTROPIC HOST
          Mac mini / Mac Studio
             always-on 24/7
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Codex A    Codex B    Supervisor
          │          │          │
          └──────────┼──────────┘
                     ▼
              Nortropic Kernel
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      GitHub       Vercel       Cloud APIs
        │
        ▼
    production
```

Och **senare**:

```text
                     │
                     ▼
             LOCAL AI NODE
          Mac Studio / NVIDIA
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
    local LLM    embeddings    cheap workers
```

Det är där hårdvaran börjar bli riktigt spännande.

---

# Varför en stationär Nortropic-maskin är attraktiv

Din laptop behöver då inte:

- vara påslagen hela natten,
- vara hemma,
- bära all execution,
- ha alla secrets,
- köra varenda service,
- samtidigt vara din privata arbetsmaskin.

Nortropic får en **egen fysisk identitet**.

Det passar faktiskt väldigt fint med allt vi bygger kring authority, reproducibility och autonomous execution.

Istället för:

> "Codex råkar köra på fruns MacBook."

får vi:

> `nortropic-host-01` är en definierad execution environment.

Det kan så småningom finnas:

```text
host identity
hardware inventory
OS version
installed capabilities
secrets boundary
allowed network access
available resources
health
disk
memory
load
execution slots
```

Och Nortropic själv kan förstå:

> `HOST-01: healthy · 3/6 execution slots occupied`.

Det är **Organization OS ända ner till metallen**.

---

# När skulle jag istället köpa MacBook Pro?

Om du säger:

> "Jag vill bara äga EN riktigt bra dator och kunna ta med mig Nortropic."

då hade jag tittat på en 14-tums MacBook Pro.

Nuvarande MacBook Pro har M5/M5 Pro/M5 Max och kan konfigureras hela vägen upp till 128 GB unified memory. M5 Pro kan få 48 eller 64 GB. citeturn160701search9turn925496search0

En M5 Pro 24 GB/1 TB ligger runt 33 000 kr i aktuell svensk handel:

product["turn456816product6","MacBook Pro 14\" M5 Pro 15-core CPU, 16-core GPU/24GB/1TB SSD",{"render_as":"block"}]

Men för **Nortropic per spenderad krona** skulle jag hellre lägga ungefär 24k på en stark Mac mini än ~33–45k på en laptop om du inte behöver mobiliteten.

---

# Sedan kommer Mac Studio

Här börjar vi komma in på nästa nivå.

Apple presenterade samtidigt nya Mac Studio:

```text
M5 Max
36 → 128 GB unified memory
från 32 995 kr

M5 Ultra
96 → 512 GB unified memory
från 72 995 kr
```

De släpps också 22 september. citeturn885690search1turn160701search0

En aktuell M5 Max-konfiguration med 48 GB/1 TB ligger ungefär i 45k-klassen:

product["turn456816product5","Mac Studio/M5 Max 18-kärnig CPU & 40-kärnig GPU/48GB RAM/1TB",{"render_as":"block"}]

För **Nortropic idag** tycker jag detta är onödigt.

För **Nortropic senare** tycker jag däremot den är väldigt intressant.

---

# Här kommer lokal AI in

Säg att vi längre fram tänker:

> Varför ska Nortropic skicka varenda liten klassificering, sammanfattning och rutinuppgift till en dyr frontier-modell?

Då kanske vi kör:

```text
GPT-5.6 / frontier cloud
↓
svår arkitektur
svår reasoning
kritiska beslut
komplex kod

LOCAL MODEL
↓
klassificering
triage
embeddings
enklare extraction
routing
billiga workers
background processing
privacy-sensitive tasks
```

Apple Silicon har blivit betydligt mer användbart för det här. Ollamas nuvarande MLX-motor använder Apples unified memory för lokal modellkörning, och deras egen exempelsetup för en Qwen 35B-codingmodell rekommenderar **mer än 32 GB unified memory**. citeturn443295search0turn443295search1

Därför ser jag ungefär:

```text
32 GB
bra Nortropic development host

48–64 GB
börjar bli en intressant AI-development host

128 GB
seriös lokal LLM-lab

256–512 GB
mycket stora lokala modeller / specialiserad AI-infrastruktur
```

Det betyder **inte** att vi behöver detta nu.

Men det betyder att Mac Studio kan bli relevant längre fram av en helt annan anledning än “Codex går snabbare”.

---

# Och vad är allt snack om NVIDIA 5090?

Här finns den andra vägen.

En riktig AI-PC kan exempelvis innehålla RTX 5090. Det kortet har **32 GB GDDR7 VRAM** och Nvidias CUDA/Tensor-ekosystem. citeturn443295search9

Den typen av maskin är fantastisk om Nortropic börjar behöva:

- CUDA,
- lokal modellträning/fine-tuning,
- tung bildgenerering,
- tung videogenerering,
- hög lokal inference-throughput,
- specifik ML-programvara byggd för NVIDIA.

Men det innebär också mer:

```text
Linux/Windows
drivers
CUDA
värme
ström
fläktar
VRAM-management
ytterligare platform att administrera
```

Och just nu hade vi i princip köpt en Formel 1-bil för att köra till ICA.

### Dessutom finns en intressant skillnad

RTX 5090:

```text
32 GB mycket snabbt dedikerat GPU-minne
```

Mac Studio:

```text
upp till 128 / 512 GB unified memory
CPU + GPU delar minnet
```

Så NVIDIA kan ha mycket hög prestanda på arbetslaster som passar det, medan en stor Mac kan **få plats med modeller som inte ens ryms i 32 GB VRAM**.

Vilket som är bäst beror därför helt på vad Nortropic faktiskt behöver göra.

Det är därför jag **inte skulle fatta det beslutet före behovet existerar**.

---

# Min tänkta utvecklingsbana för er

### Fas 0 — nu

```text
Fruns M1 MacBook Pro
8 GB
+
cloud AI
```

**Status:** fungerar för att färdigställa Bootstrap/Digitala.

Jag hade inte avbrutit arbetet för att köpa hårdvara.

---

### Fas 1 — Nortropic får en egen dator

Min kandidat:

```text
Mac mini M6
32 GB
1 TB

≈ 24k
```

Den blir:

> **Nortropic Host 01**

Det tycker jag ger väldigt mycket per krona.

Och eftersom den nya modellen släpps den **22 september 2026**, skulle jag definitivt inte köpa en gammal Mini till normalt pris under de kommande veckorna.

---

### Fas 2 — Johnny får en egen cockpit

När det finns anledning:

```text
MacBook Pro 14"
M5 Pro
48 GB
1 TB
```

Den behöver inte vara Nortropics server.

Den är din:

```text
owner console
research
ChatGPT
Codex interaction
review
design
management
```

Och om du är hemma kan du knappt märka vilken maskin arbetet faktiskt exekveras på.

---

### Fas 3 — Nortropic blir always-on

Då kompletterar vi hosten med:

```text
Ethernet
UPS
automatisk backup
extern SSD
secure remote access
monitoring
host health
separata credentials
```

1 TB intern SSD tycker jag är bra som baseline. Externa Thunderbolt/NVMe-diskar kan senare ta modeller, arkiv och backups mycket billigare än att köpa enorm Apple-intern SSD.

---

### Fas 4 — lokal AI blir en riktig capability

Då gör vi **inte ett hobbyköp**.

Nortropic kan i princip göra en capability evaluation:

```text
NEED:
Local inference

WHY?
cost?
privacy?
latency?
availability?
provider independence?

WORKLOAD:
what models?
how large?
requests/sec?
context?
multimodal?

BENCHMARK:
Mac Studio
vs
NVIDIA
vs
cloud GPU

TCO:
purchase
power
maintenance
tokens saved

↓
DECISION
```

Och först därefter köper vi:

```text
Mac Studio 64/128 GB

eller

Linux workstation
RTX 5090 / framtida GPU

eller

ingen lokal maskin alls
```

Det tycker jag är **väldigt Nortropic**.

---

# Jag skulle alltså inte bygga ett “AI gaming rig” idag

Min preliminära hårdvaru-roadmap blir:

```text
                    NU
                     │
          M1 / 8 GB MacBook
                     │
                     ▼
            ┌────────────────┐
            │ Mac mini M6    │
            │ 32 GB / 1 TB   │
            │ Host 01        │
            └────────────────┘
                     │
              växer Nortropic
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
  Johnny behöver mobilitet   Local AI behövs
          │                     │
          ▼                     ▼
  MacBook Pro M5 Pro       Mac Studio / NVIDIA
     48 GB / 1 TB              AI node
```

Och det finns en ännu viktigare arkitekturprincip här:

> **Vi ska inte behöva köpa en ny dator varje gång vi skaffar ytterligare en Codex-agent.**

Codex A + Codex B är två **execution/provider lanes**, inte nödvändigtvis två fysiska datorer. En ordentligt dimensionerad host kan bära många separata worktrees/processer. Fysiska noder lägger vi till när mätbar CPU-, minnes-, isolation- eller availability-belastning kräver det.

## Därför skulle jag sätta en Nortropic-princip redan nu

> **Cloud intelligence, local execution, hardware as scalable infrastructure.**

Vi använder frontier compute från molnet där det är bäst. Vi använder lokala resurser där de ger verklig nytta. Och vi bygger inte dyr AI-infrastruktur spekulativt.

För just den Nortropic vi bygger idag tycker jag att **Mac mini M6 32 GB / 1 TB som första dedikerade Nortropic-host är en ovanligt ren sweet spot**. Sedan skulle jag låta själva systemets utveckling avgöra om nästa krona ska gå till en MacBook Pro, mer RAM, Mac Studio, NVIDIA-server eller molncompute.

---

## Meddelande 6 — Johnny (användare)

Brainstorma ett scenario och förklara som jag vore 5 när mer hårdvara blir aktuellt och hur Nortropic skulle växa för att det skulle behövas, jag ser många bygger AI riggar men jag vill förstå hur hårdvaran kan växa tillsammans med Nortropic för goda förutsättningar, tex när vi gör de här sakerna, hypotes scenarion nu och framledes

---

## Meddelande 7 — ChatGPT (assistent)

Ja — jag tror bästa sättet är att **sluta tänka “vilken AI-rigg behöver Nortropic?” och istället följa Nortropics livscykel**. Jag ska göra ett par konkreta framtidsscenarion där varje ny hårdvarubit dyker upp först när ett verkligt problem uppstår, och förklara vad maskinen faktiskt gör i vardagen.

---

## Meddelande 8 — ChatGPT (assistent)

En viktig skillnad redan nu: **mer Nortropic betyder inte automatiskt större GPU**. Om Nortropic går från 2 till 20 Codex-workers kan det först ge behov av mer RAM, CPU, disk och flera hosts — medan lokal AI-GPU fortfarande kan vara helt onödig. GPU-riggen blir intressant först när vi väljer att flytta själva *modellberäkningen* hem.

---

## Meddelande 9 — ChatGPT (assistent)

Det är också här en “AI-rigg” kan vara missvisande. En **RTX 5090 har 32 GB GPU-minne**, medan en professionell RTX PRO 6000 har 96 GB; Apples nya Mac Studio går upp till 512 GB unified memory, och Nvidias lilla DGX Spark har 128 GB unified memory och är byggd specifikt för lokal modellutveckling. Det är tre helt olika verktyg för tre olika problem — inte en enkel stege “dyrare = bättre Nortropic”.

---

## Meddelande 10 — ChatGPT (assistent)

Ja. Det här blir mycket lättare om vi tänker **“Nortropic är en liten verkstad som långsamt blir en fabrik”**.

Och en viktig princip från början:

> **Vi köper inte maskiner för att Nortropic *kanske* blir stort. Vi låter Nortropic växa tills det själv börjar slå i ett fysiskt tak — och då bygger vi ut just den delen.**

### Först: förklara datorn som om du vore 5

Tänk att Nortropic bygger LEGO.

```text
GPT / Codex i molnet
= den jättesmarta ingenjören du ringer på telefon

CPU
= arbetarnas händer

RAM
= hur stort arbetsbordet är

SSD
= lagret med alla LEGO-bitar

GPU
= en egen väldigt snabb AI-hjärna i huset

Nätverk
= vägarna mellan byggnaderna

Backup/NAS
= reservlagret

UPS
= reservström om lamporna slocknar
```

Just nu **hyr vi nästan alla riktigt smarta hjärnor över internet**.

Din Mac behöver därför framför allt kunna:

```text
hålla projekten
köra programmen
köra tester
öppna många worktrees
köra browsers
hantera filer
låta flera agenter arbeta samtidigt
```

Inte tänka alla AI-tankar själv.

---

# Scenario 0 — Nortropic idag

Tänk:

> Johnny sitter vid köksbordet och bygger sin första robotfabrik.

Vi har ungefär:

```text
FRUNS MACBOOK
M1
8 GB

        │

ChatGPT
Codex A
Codex B
VS Code
Git
Node/Python
tester
browser

        │
        ▼

OpenAI
"de stora hjärnorna"
```

Och vi håller fortfarande på att färdigställa själva autonoma motorn, Digitala och senare Organization OS.

Det är fascinerande egentligen: **en liten gammal laptop kan vara kontrollcentral för enorma frontier-modeller.**

Det är därför din nuvarande dator fortfarande fungerar.

Problemet är främst:

```text
8 GB bordsyta
```

När fem arbetare försöker lägga sina LEGO-bitar på samma lilla bord börjar de knuffa undan varandra.

macOS börjar flytta saker mellan RAM och SSD.

Program behöver vänta.

Browsern äter minne.

Tester äter minne.

VS Code äter minne.

Flera agenter arbetar samtidigt.

Därför är nästa hårdvaruproblem sannolikt **inte “vi behöver mer AI”**.

Det är:

> **“Vi behöver ett större arbetsbord.”**

---

# Scenario 1 — Nortropic får sin första riktiga verkstad

Tänk att Bootstrap är färdig.

Autonomy Kernel fungerar.

Digitala kan börja arbeta.

Codex A och Codex B kan arbeta parallellt.

Nortropic behöver inte längre bara köras när Johnny råkar ha laptopen öppen.

Då börjar det bli rimligt med:

```text
            JOHNNY
          MacBook/iPhone
               │
               ▼
       NORTROPIC HOST 01
        Mac mini M6
        32 GB / 1 TB
               │
       ┌───────┼────────┐
       ▼       ▼        ▼
    Codex A  Codex B   Kernel
       │       │
       └───┬───┘
           ▼
       Tester
       Browser
       Git
       Builds
```

Apple råkar faktiskt ha positionerat nya M6 Mac mini, presenterad 25 augusti, specifikt mot bland annat **always-on agentic computing**. M6-modellen kan konfigureras med upp till 32 GB minne, medan M5 Pro-varianten går till 64 GB. citeturn151584search0turn434492view1

Det betyder inte att Apple automatiskt är rätt för Nortropic.

Men **formen passar väldigt väl**.

Den är liten.

Strömsnål.

Kan stå på.

macOS matchar utvecklingsmiljön vi redan använder.

### Vad får vi egentligen för pengarna?

Inte:

> GPT blir smartare.

Utan:

> Nortropic får **ett eget hus**.

Nu kan din dator vara kontrollrummet medan Host 01 arbetar.

---

# Scenario 2 — Digitala börjar producera på riktigt

Nu gör vi hypotesen lite roligare.

Anta att Nortropic är Customer Zero och Digitala är färdig.

Sedan kommer tre riktiga företag in.

Digitala arbetar samtidigt med:

```text
Nortropic.se
Kund A
Kund B
Kund C
```

För varje hemsida kanske Nortropic gör:

```text
research
↓
copy
↓
design
↓
implementation
↓
build
↓
browser testing
↓
mobile testing
↓
accessibility
↓
screenshots
↓
visual evaluation
↓
SEO validation
↓
deployment
```

Plötsligt kanske vi har 8–15 faktiska processer igång.

Två browsers.

Flera Node-servrar.

Tre testsviter.

Fyra worktrees.

Databas.

Observability.

Codex-agenter.

### Vad händer då?

Inte nödvändigtvis:

> "Köp RTX 5090!"

Istället kanske Host 01 säger:

```text
RAM: nästan fullt
CPU: upptagen
browser tests: väntar
worker queue: 6 tasks
```

Då har Nortropic fått sitt första verkliga **capacity problem**.

Och här finns två lösningar.

### Lösning A — större maskin

```text
Mac mini M5 Pro
64 GB
```

Ett större bord.

### Lösning B — en maskin till

```text
HOST 01
build / code / kernel

HOST 02
browser / QA / tests
```

Två arbetsbord.

Jag tror att **B blir väldigt intressant för Nortropic**.

För då lär vi själva organisationen att förstå:

```text
CAPABILITY: browser-testing
HOST: qa-01

CAPABILITY: mac-build
HOST: build-01

CAPABILITY: orchestration
HOST: core-01
```

Nu börjar hårdvaran bli en del av Nortropics Organization OS.

---

# Och här händer någonting riktigt Nortropic

Föreställ dig Verkstadsgolvet senare:

```text
INFRASTRUCTURE

Host             Load       Workers
────────────────────────────────────
core-01          21%        2/4
build-01         77%        4/4
qa-01            96%        8/8 ⚠

QUEUE
browser-test     17 jobs ⚠
```

Nortropic kan själv konstatera:

> Browser-capacity är flaskhalsen.

Inte:

> Johnny tycker att den nya Nvidia-riggen ser cool ut på YouTube.

Och kanske föreslår organisationen:

```text
CAPACITY PROPOSAL

Problem:
QA jobs queue > policy threshold.

Cause:
Browser execution saturation.

Candidate:
Add QA execution node.

Expected effect:
+8 concurrent browser lanes.

Owner attention:
Recommended purchase.
```

**Det där är min idealbild av hur du ska köpa hårdvara.**

Systemet kan till slut säga till dig när det faktiskt behöver mer.

---

# Scenario 3 — Nortropic blir en liten fabrik

Nu har vi kanske:

```text
Digitala
Research
Market Radar
Organization OS
Knowledge
Evolution
Observability
```

och flera verkliga kunder.

Nortropic arbetar dygnet runt med vissa saker.

Nu börjar ett annat problem dyka upp.

### Data.

Vi får:

```text
screenshots
logs
build artifacts
website snapshots
raw research
customer material
backups
databases
evaluation corpora
Git
video
images
model caches
```

Plötsligt är 1 TB inte särskilt mycket.

Och nu gör många AI-entusiaster misstaget:

> "Dags för större GPU."

Nej.

Vi kanske snarare behöver:

```text
Nortropic Storage 01
```

Exempel:

```text
                HOSTS
             │    │    │
             └────┼────┘
                  ▼
             10 Gb network
                  │
                  ▼
          STORAGE / BACKUP
           8–20 TB usable
                  │
             backup copy
```

Plus:

```text
UPS
Ethernet
backup
monitoring
```

Det är inte lika sexigt som en RTX 5090.

Men för en **riktig autonom organisation** är det sannolikt mycket viktigare.

---

# Scenario 4 — den första gången en riktig AI-rigg blir rationell

Nu kommer punkten du egentligen är nyfiken på.

Anta att Nortropic gör enormt mycket AI-arbete.

Men vi tittar på vad GPT-5.6 används till och upptäcker:

```text
1000 jobb/dag

600 = enkel klassificering
150 = extraction
100 = embeddings/retrieval
50  = enkel bildanalys
50  = triage
30  = enklare summaries
20  = riktigt svår reasoning
```

Och vi tänker:

> Behöver verkligen världens bästa frontiermodell läsa varenda liten loggrad?

Nej.

Nu kan vi skapa:

```text
NORTROPIC MODEL HIERARCHY
```

Ungefär:

```text
                  svårast
                     │
                     ▼
             GPT-5.6 / frontier
          architecture / coding /
          difficult judgment
                     ▲
                     │
             medium cloud model
                     ▲
                     │
               LOCAL MODEL
          cheap repetitive work
                     ▲
                     │
            deterministic code
                  enklast
```

### Nu får den lokala GPU:n ett jobb.

Inte:

> "Vi vill ha en AI-rigg."

Utan:

> **“Vi har en definierad workload som vi vill köra lokalt.”**

Det är helt annorlunda.

---

# Vad skulle Nortropic kunna köra lokalt?

Exempelvis:

```text
classify incoming findings
extract structured fields
deduplicate research
embeddings
basic retrieval
simple coding tasks
log analysis
basic visual QA
screenshot classification
document classification
routine summaries
routing
low-risk evaluations
```

Och GPT får de svåra fallen.

Det kan bli extremt kraftfullt.

Anta:

```text
10 000 små AI-jobs
              │
              ▼
         LOCAL MODEL
              │
       9 300 solved
              │
              ├─────────────┐
              ▼             ▼
          accepted      uncertain
                           700
                            │
                            ▼
                        GPT-5.6
```

Nu fungerar din lokala AI ungefär som **kommunens handläggare**, medan frontiermodellen är specialistläkaren.

Specialisten behöver inte öppna varje kuvert.

---

# Då blir Mac Studio relevant

Nu behöver vi ett stort **AI-bord**.

Apples nya Mac Studio med M5 Max kan konfigureras med upp till 128 GB unified memory, medan M5 Ultra når 512 GB. Apple anger också Thunderbolt-baserad klustring för distribuerad AI-inferens mellan flera Mac Studio-maskiner. citeturn380720search2turn380720search6

Varför spelar minnet roll?

Väldigt förenklat:

```text
liten modell
=
liten låda

stor modell
=
stor låda
```

Modellen måste få plats i minnet.

Så:

```text
32 GB
│
├─ många mindre modeller
└─ vissa större komprimerade modeller

64 GB
│
└─ betydligt större modeller

128 GB
│
└─ stora lokala LLM-arbetslaster

256–512 GB
│
└─ enorm modellkapacitet / specialfall
```

Exakt vilken modell som ryms beror på precision, kvantisering, context/KV-cache och runtime, så parameterantal ensamt berättar inte hela sanningen.

Men principen räcker:

> **RAM/VRAM är ungefär rummets storlek där AI-hjärnan måste få plats.**

---

# Scenario 5 — varför folk bygger RTX-riggar

Nu antar vi att Digitala utvecklas.

Nortropic börjar kanske själv göra:

```text
image generation
video generation
vision models
visual QA
fine-tuning
local multimodal models
large batches
model experiments
```

Nu kommer NVIDIA-ekosystemet in.

En RTX 5090 har 32 GB GDDR7 och mycket hög GPU-prestanda. citeturn784182search0

Tänk:

```text
MAC STUDIO
= enorm lastbil

RTX 5090
= väldigt snabb sportbil
```

Macens unified memory kan vara enormt.

5090:ans GPU-minne är mycket mindre men extremt snabbt och CUDA-ekosystemet är enormt.

Om jobbet är:

> Kör en modell som ryms i 32 GB **så snabbt som möjligt**.

kan 5090 vara extremt attraktiv.

Om jobbet är:

> Få plats med en modell som behöver 100 GB minne.

kan 5090 helt enkelt säga:

> Jag får inte in den.

---

# Och sedan finns riktiga professionella Nvidia-maskiner

NVIDIA RTX PRO 6000 Blackwell har **96 GB GDDR7 ECC-minne och 1 792 GB/s minnesbandbredd**, och NVIDIA positionerar den uttryckligen för bland annat lokal inference, fine-tuning och agentiska AI-system. Den kan dra upp till 600 W. citeturn784182search1

Det här är ungefär:

```text
RTX 5090
    ↓
enthusiast / powerful workstation

RTX PRO 6000
    ↓
serious professional AI workstation
```

Men då pratar vi helt andra pengar och helt andra workloads.

---

# Ett ännu roligare Nortropic-scenario: DGX Spark

NVIDIA har nu även DGX Spark.

Den är ungefär stor som en liten desktopmaskin och har:

```text
128 GB unified memory
Grace Blackwell
10 Gb Ethernet
ConnectX-7
```

och NVIDIA anger stöd för att utveckla/köra modeller upp till omkring 200B parametrar på en Spark, beroende på modell/runtime. Två Spark kan användas för vissa arbetslaster upp till 405B. citeturn380720search5

Det är betydligt mer:

> **AI appliance**

än vanlig PC.

Jag skulle kunna föreställa mig:

```text
NORTROPIC HOST 01
Mac
orchestration

NORTROPIC HOST 02
Mac
build/test

NORTROPIC AI 01
DGX Spark
local models
```

Och Nortropic vet:

```text
job:
classify 50,000 documents

required:
local-llm
CUDA
128GB-memory

route:
ai-01
```

Det är mycket mer intressant än:

> “Johnny SSH:ar in på sin GPU-rigg.”

---

# Scenario 6 — Nortropic har kanske 10 förvaltningar

Nu börjar vi få något riktigt spännande.

Föreställ dig framtida Nortropic:

```text
                  NORTROPIC
                     │
        ┌────────────┼────────────┐
        │            │            │
     Digitala     Research     Software
        │            │            │
        ├────────┐   │   ┌────────┤
        ▼        ▼   ▼   ▼        ▼
      tasks     tasks tasks      tasks
        │        │    │            │
        └────────┴────┴────────────┘
                     │
                     ▼
                SCHEDULER
                     │
        ┌────────────┼─────────────┐
        ▼            ▼             ▼
     CORE-01       BUILD-01       AI-01
     Mac mini      Mac mini       GPU
        │            │             │
 orchestration      tests       local LLM
 git/state          browser       vision
 databases          builds       inference
```

Det viktiga är:

> **Agenten ska inte behöva veta vilken dator som finns.**

Den begär en capability.

Exempel:

```text
I need:
browser-chrome
macos-arm
16GB free
network-isolated
```

Scheduler:

```text
QA-01 matches.
```

Eller:

```text
I need:
cuda
80GB VRAM
local-model-x
```

Scheduler:

```text
AI-02 matches.
```

### Det är Kubernetes-idén på 5-åringsnivå

Arbetaren säger:

> Jag behöver en hammare.

Nortropic bestämmer:

> Hammaren ligger i verkstad nummer 3.

---

# Och då förändras betydelsen av “köpa dator”

Det blir inte längre:

> Johnny behöver en ny dator.

Det blir:

```text
NORTROPIC CAPACITY PLANNING
```

Systemet kanske ser:

```text
CUDA capacity:
82% average

AI queue:
growing

P95 wait:
11 minutes

Forecast:
capacity exhausted within 4 weeks
```

och producerar:

> `CAPACITY EXPANSION CANDIDATE: AI-02`

Då kan Nortropic i princip börja **planera sin egen fysiska expansion**.

Det är ett ganska häftigt slutmål.

---

# Scenario 7 — vi får fler kunder

Anta sedan att Nortropic inte längre bara är Nortropic Customer Zero och några lighthouse-kunder.

Vi har:

```text
10 kunder
50 kunder
500 kunder
```

Här händer något kontraintuitivt.

Man skulle kunna tro:

> Då behöver Johnny ett rum fullt med RTX-kort.

Förmodligen inte.

Nu börjar det istället bli mer rationellt med:

```text
AWS
Azure
Google Cloud
specialiserad GPU cloud
Vercel
managed databases
regional infrastructure
```

För en dator hemma hos dig i Luleå är en dålig produktionsdatacenterlösning för 500 kunder.

Så utvecklingen kan bli:

```text
START
local everything possible

        ↓

GROWTH
local development infrastructure

        ↓

MORE GROWTH
hybrid local + cloud

        ↓

PRODUCT SCALE
cloud/datacenter production
+
local R&D / secure compute
```

Det betyder att hårdvarukurvan **inte behöver gå till oändligheten**.

Det kan bli:

> mer cloud istället för mer garage.

---

# Därför ser jag två helt olika sorters tillväxt

### Organisationstillväxt

Fler:

```text
agents
services
browsers
tests
repos
worktrees
databases
```

kräver främst:

```text
CPU
RAM
SSD
fler hosts
```

### AI-compute-tillväxt

Fler:

```text
local LLMs
vision
image generation
video
fine-tuning
high-volume inference
```

kräver:

```text
GPU
VRAM
memory bandwidth
CUDA / MLX
AI nodes
```

**De två behöver inte inträffa samtidigt.**

Det är kanske den viktigaste saken att förstå.

---

# Ett konkret framtida dygn i Nortropic

Säg att vi spolar framåt.

03:00.

Johnny sover.

Market Radar hittar 4 800 nya saker.

```text
AI-01
local cheap model

4800
 ↓
dedupe
 ↓
classify
 ↓
score
 ↓
123 interesting
```

Sedan:

```text
GPT frontier

123
 ↓
deep reasoning
 ↓
7 important findings
```

Research skapar ett förslag.

Samtidigt:

```text
BUILD-01
```

bygger en ny Digitala-release.

```text
QA-01
```

startar 40 browser journeys.

```text
AI-01
```

analyserar screenshots.

En test misslyckas.

Kernel skapar remediation.

Codex fixar det.

Independent verifier kontrollerar.

På morgonen öppnar du Verkstadsgolvet:

```text
NORTROPIC

Digitala       HEALTHY
Research       HEALTHY
Kernel         HEALTHY

Overnight
42 tasks completed
3 remediated
0 owner blockers

Owner attention
2 items
```

### Datorerna har då helt olika yrken.

Det är nyckeln.

---

# Och nu kan vi beskriva hela hårdvaruresan

| Nortropic-stadium | Vad som händer | Flaskhals | Hårdvara som kan bli relevant |
|---|---|---|---|
| **Nu** | Vi bygger Kernel/Digitala | 8 GB RAM, personlig laptop | Befintlig Mac |
| **Egen organisation** | Always-on + Codex A/B | Tillgänglighet/minne | Mac mini 32 GB |
| **Digitala producerar parallellt** | Flera builds/tests/browser workers | RAM/CPU | 64 GB host eller Host 02 |
| **Flera förvaltningar** | Mycket state/artifacts/loggar | Storage/reliability | NAS/NVMe, UPS, backup |
| **Hög AI-volym** | Tusentals enkla AI-jobb | Cloud cost/latency | Local AI node |
| **Stora lokala modeller** | Local inference/private AI | AI memory | Mac Studio 128–512 GB / DGX Spark |
| **Tung ML/media** | Vision/video/fine-tuning | GPU throughput/CUDA | RTX 5090 / RTX PRO |
| **Många kunder** | Production måste skala | Availability/global scale | Cloud/datacenter |
| **Stor Nortropic** | Blandade workloads | Resource orchestration | Hybrid compute fabric |

---

# Jag skulle därför göra Nortropics hårdvarufilosofi så här

Inte:

```text
"Buy the best AI rig."
```

Utan:

```text
WORK
↓
OBSERVE
↓
BOTTLENECK
↓
CLASSIFY

memory?
cpu?
storage?
availability?
network?
AI compute?
privacy?
latency?

↓
BENCHMARK OPTIONS

bigger host?
another host?
local GPU?
cloud?
managed service?

↓
COST / BENEFIT
↓
ADD CAPABILITY
```

Och samma princip som vi använder i resten av Nortropic:

> **capability först, implementation sedan.**

---

# När skulle jag själv trycka på köpknappen?

Inte när Activity Monitor visar 75 % RAM en gång.

Jag skulle vilja att Nortropic gradvis får riktiga **capacity signals**.

Exempel:

```text
MEMORY PRESSURE
repeated sustained saturation

WORK QUEUE
workers routinely waiting for compute

UTILIZATION
specific capability consistently saturated

AVAILABILITY
work stops because Johnny's machine is unavailable

LATENCY
local resource materially slows mission completion

CLOUD COST
routine inference becomes economically meaningful

PRIVACY
some data should not leave our trust boundary

CAPABILITY
required workload simply cannot be executed today
```

Först då:

> ny hårdvara.

---

# Det finns en sak jag skulle undvika hårt

Att vi nu säger:

> “AI är framtiden. Köp en 5090 med 128 GB RAM och bygg en server.”

Det är **hardware-driven architecture**.

Jag tycker Nortropic bör göra precis motsatsen:

```text
MISSION
     ↓
CAPABILITY
     ↓
WORKLOAD
     ↓
MEASURE
     ↓
COMPUTE REQUIREMENT
     ↓
HARDWARE
```

Inte:

```text
RTX 5090
     ↓
"vad kan vi hitta på att göra med den?"
```

---

# Min nuvarande hypotes för oss

Om jag skulle gissa Nortropics naturliga resa från exakt där vi står nu:

```text
NU
Fruns M1 / 8 GB
        │
        │ Kernel blir färdig
        ▼
HOST-01
Mac mini M6
32 GB / 1 TB
        │
        │ Nortropic + Digitala börjar arbeta på riktigt
        ▼
CAPACITY OBSERVABILITY
        │
        ├──── behov av fler vanliga workers
        │              │
        │              ▼
        │          HOST-02
        │
        ├──── mycket data
        │              │
        │              ▼
        │        STORAGE/BACKUP
        │
        └──── stor repetitive AI workload
                       │
                       ▼
                     AI-01
                Mac Studio/DGX/NVIDIA
                       │
                       ▼
                  HYBRID FABRIC
                       │
                local + cloud
```

**Jag tror faktiskt att en jättedyr AI-rigg sannolikt är minst två eller tre arkitekturella steg bort för oss.**

Men en **dedikerad Nortropic-host** är betydligt närmare, eftersom den löser ett problem som vi redan håller på att skapa: autonomt arbete, flera executors, always-on execution och separation mellan ägarens cockpit och organisationens maskin. memcite

Och den riktigt intressanta slutbilden är inte att Johnny har världens fetaste dator.

Det är:

> **Nortropic vet vilka beräkningsresurser organisationen har, kan routa rätt arbete till rätt maskin, kan observera när en capability blir mättad och kan påkalla din uppmärksamhet när organisationen faktiskt har ett välgrundat behov av att bygga ut sin egen fysiska infrastruktur.**

Då har hårdvaran vuxit **tillsammans med organisationen**, istället för före den.

---

## Meddelande 11 — Johnny (användare)

Beskriv denna bild för mig NU
Fruns M1 / 8 GB
        │
        │ Kernel blir färdig
        ▼
HOST-01
Mac mini M6
32 GB / 1 TB
        │
        │ Nortropic + Digitala börjar arbeta på riktigt
        ▼
CAPACITY OBSERVABILITY
        │
        ├──── behov av fler vanliga workers
        │              │
        │              ▼
        │          HOST-02
        │
        ├──── mycket data
        │              │
        │              ▼
        │        STORAGE/BACKUP
        │
        └──── stor repetitive AI workload
                       │
                       ▼
                     AI-01
                Mac Studio/DGX/NVIDIA
                       │
                       ▼
                  HYBRID FABRIC
                       │
                local + cloud

---

## Meddelande 12 — ChatGPT (assistent)

Absolut. Bilden visar egentligen **hur Nortropic går från “ett projekt på en laptop” till “en liten datoriserad organisation med egen infrastruktur”**.

Tänk på det som att Nortropic först bor hemma hos er, sedan får ett eget kontor, därefter fler rum, ett lager och till sist en egen maskinpark.

### 1. `NU — Fruns M1 / 8 GB`

Det här är där vi befinner oss idag.

```text
Fruns MacBook
      │
      ├── Johnny arbetar
      ├── Codex arbetar
      ├── tester körs
      ├── Git/worktrees finns
      ├── webbläsaren körs
      └── Nortropic byggs
```

Allt bor i princip i samma lilla hus.

MacBooken är både:

**din arbetsplats + Nortropics byggarbetsplats + testmaskin + exekveringsmaskin.**

Det fungerar eftersom den riktigt tunga AI-hjärnan fortfarande huvudsakligen finns hos OpenAI.

Problemet är inte primärt att M1 är för långsam.

Problemet är snarare:

> **8 GB är ett litet skrivbord för allt vi börjar lägga på det.**

---

# 2. `Kernel blir färdig`

Det här är den viktiga tröskeln.

Idag är vi fortfarande ganska mycket:

```text
Johnny
  ↓
Codex
  ↓
bygger Nortropic
```

När Autonomy Kernel fungerar blir det mer:

```text
Johnny
  ↓
ger mål
  ↓
Nortropic
  ↓
organiserar arbete
  ↓
workers arbetar
  ↓
verifiering
  ↓
remediation
  ↓
resultat
```

Datorn går då från att vara:

> en dator Johnny programmerar på

till:

> **en plats där en autonom organisation arbetar.**

Det är därför nästa steg blir intressant.

---

# 3. `HOST-01 — Mac mini M6 32 GB / 1 TB`

Nu säger vi:

> Nortropic ska få en egen dator.

Den kanske står hemma hos dig och är inkopplad dygnet runt.

Inte en skärm framför dig.

Bara en liten låda.

```text
        INTERNET
           │
           │
    ┌─────────────┐
    │  HOST-01    │
    │             │
    │ Nortropic   │
    │ Kernel      │
    │ Codex       │
    │ Git         │
    │ tester      │
    │ browsers    │
    │ services    │
    └─────────────┘
           ▲
           │
      Johnny
     MacBook/iPhone
```

Din laptop behöver inte längre vara fabriken.

Den blir mer:

> **kontrollpanelen till fabriken.**

Och Mac mini blir:

> **själva verkstadsgolvet.**

Det är en ganska stor konceptuell förändring trots att det bara är en liten dator.

---

# 4. `Nortropic + Digitala börjar arbeta på riktigt`

Nu antar vi att Nortropic faktiskt börjar producera.

Digitala kanske gör:

```text
Kund A
Kund B
Kund C
Nortropic själv
```

Samtidigt kanske Nortropic har:

```text
research
kod
tester
browser automation
visual QA
deployments
monitoring
Codex A
Codex B
```

Nu börjar datorn få **riktigt arbete**, inte bara utvecklingsarbete.

Och då händer något viktigt.

Vi behöver inte längre gissa:

> Behöver vi bättre hårdvara?

Vi kan **mäta det**.

---

# 5. `CAPACITY OBSERVABILITY`

Det här är hjärtat i bilden.

Orden betyder ungefär:

> **Nortropic kan se hur mycket datorkraft organisationen använder.**

Som en bil har:

```text
hastighetsmätare
bensinmätare
temperatur
varningslampor
```

får Nortropic:

```text
CPU
RAM
disk
köer
antal workers
AI-jobb
browser jobs
storage
network
```

Verkstadsgolvet skulle exempelvis kunna visa:

```text
HOST-01

CPU             37%
RAM             26 / 32 GB
SSD             430 / 1000 GB

Workers
3 / 6 active

Browser queue
2 jobs

Status
HEALTHY
```

Det är då vi börjar fatta hårdvarubeslut på riktigt.

---

# Sedan delar bilden upp sig i tre olika problem

Det är viktigt.

Den säger **inte**:

> Nortropic växer → köp större GPU.

Den säger:

> Nortropic växer → ta reda på *vad* som blivit för litet.

---

## Gren A — `behov av fler vanliga workers`

Anta att Digitala plötsligt har mycket att göra.

HOST-01 kör:

```text
Codex worker
Codex worker
browser
tester
Node server
database
build
another build
```

och Nortropic ser:

```text
CPU 95%
RAM fullt
workers väntar
```

Problemet är då:

> Vi behöver fler vanliga händer.

Inte mer AI-hjärna.

Då lägger vi till:

# `HOST-02`

Exempelvis ännu en Mac mini.

Nu kanske det blir:

```text
           NORTROPIC
               │
       ┌───────┴───────┐
       ▼               ▼
    HOST-01          HOST-02

Kernel              Browser tests
Git/state           Builds
Supervisor          Workers
Workers             Workers
```

Tänk:

> Första verkstaden blev full, så vi hyrde lokalen bredvid.

Nu kan Nortropic fördela arbete mellan datorerna.

---

# Gren B — `mycket data`

Ett helt annat problem kan uppstå.

Kanske CPU:n är lugn.

Men efter två år har vi:

```text
kundprojekt
screenshots
logs
backups
research
videos
bilder
datasets
evals
model files
historiska builds
```

Och disken säger:

```text
970 GB / 1 TB
```

Då behöver vi **inte en snabbare dator**.

Vi behöver ett lager.

# `STORAGE / BACKUP`

Exempelvis:

```text
        HOST-01
            │
        HOST-02
            │
            ▼
    ┌──────────────┐
    │   STORAGE    │
    │              │
    │  10–20 TB    │
    │              │
    │ projects     │
    │ backups      │
    │ artifacts    │
    │ datasets     │
    └──────────────┘
```

Och kanske ytterligare backup utanför huset.

Tänk:

> Verkstaden fungerar bra, men kartongerna får inte längre plats.

Så vi bygger ett förråd.

---

# Gren C — `stor repetitive AI workload`

Det är här **AI-riggen** äntligen kommer in.

Anta att Nortropic börjar göra:

```text
50 000 klassificeringar
20 000 embeddings
10 000 dokumentanalyser
5 000 screenshots
massor av logganalys
massor av enkel extraction
```

Och allting skickas till OpenAI.

Nortropic kanske upptäcker:

```text
Det här kostar mycket.
Det här behöver inte frontier-AI.
Det här skulle kunna göras hemma.
```

Nu har vi ett verkligt argument för lokal AI.

---

# `AI-01`

Då köper vi något som faktiskt är byggt för AI.

Exempelvis:

```text
Mac Studio

eller

NVIDIA workstation

eller

DGX-liknande system
```

Och vi kallar den:

```text
AI-01
```

Dess jobb kanske endast är:

```text
local LLM
embeddings
vision
classification
image generation
inference
```

Då ser organisationen kanske ut:

```text
             NORTROPIC
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
    HOST-01   HOST-02     AI-01

    Kernel     Builds     Local AI
    State      Tests      Vision
    Git        Browser    Embeddings
    Workers    Workers    LLM
```

### Detta är alltså AI-riggen.

Men lägg märke till när den kom.

Inte dag 1.

Den kom när Nortropic faktiskt kunde säga:

> **“Vi har så mycket AI-arbete av denna specifika typ att en lokal AI-maskin skulle göra organisationen bättre.”**

Det är den stora skillnaden.

---

# Till sist: `HYBRID FABRIC`

Det låter avancerat men betyder något väldigt enkelt.

> **Nortropic använder både egna datorer och datorer vi hyr på internet.**

Exempel:

```text
                    NORTROPIC
                        │
       ┌────────────────┼─────────────────┐
       │                │                 │
       ▼                ▼                 ▼
    HOST-01          HOST-02           AI-01
      hemma            hemma             hemma
       │
       │
       ├─────────────────────────────┐
       │                             │
       ▼                             ▼
    OpenAI                         Cloud
 GPT-5.6 etc.                Vercel/AWS/GPU
```

Det är **hybrid**.

---

# Nortropic behöver då inte bry sig om var datorn står

Det är slutmålet jag tycker är riktigt intressant.

En worker kanske säger:

```text
Jag behöver:
- Chrome
- 8 GB RAM
- Node
```

Nortropic:

> HOST-02 passar.

En annan säger:

```text
Jag behöver:
- lokal LLM
- 80 GB AI-minne
```

Nortropic:

> AI-01 passar.

En annan säger:

```text
Jag behöver:
- GPT-5.6 Sol
```

Nortropic:

> Skicka till OpenAI.

En fjärde:

```text
Jag behöver:
- 8 GPU:er i tio minuter
```

Nortropic:

> Hyr dem i molnet.

Det är vad:

# `local + cloud`

betyder.

---

# Så hela bilden berättar egentligen denna historia

```text
ETAPP 1

Johnny har en dator.
Nortropic bor på den.


ETAPP 2

Nortropic får en egen dator.
HOST-01.


ETAPP 3

Nortropic börjar se hur mycket resurser
organisationen faktiskt använder.


ETAPP 4

När ett visst problem uppstår
bygger vi just den kapaciteten.

Fler workers?
→ HOST-02

För mycket data?
→ STORAGE

För mycket lokaliserbart AI-arbete?
→ AI-01


ETAPP 5

Alla resurser kopplas ihop.

Nortropic väljer själv vilken resurs
som passar varje jobb.

→ HYBRID FABRIC
```

Och det är därför jag tycker bilden är viktigare än ett förslag på en viss AI-rigg.

Den säger att **Nortropics hårdvara själv kan bli modulär**:

> en vanlig dator för vanligt arbete, en annan för parallellt arbete, lagring för data, specialiserad AI-hårdvara för AI och molnet för sådant som inte är rationellt att äga själv.

Det riktigt stora slutmålet är därför inte **“en fet AI-PC”**.

Det är snarare:

> **Nortropic får ett eget litet datacenter där varje maskin har ett yrke — och Organization OS förstår vilka resurser som finns, hur belastade de är och vart varje arbetsuppgift ska skickas.**

Då blir nästa Mac mini, SSD eller GPU inte bara en pryl vi köper. Den blir **en ny fysisk capability som Nortropic kan använda som en del av organisationen**.

---

## Meddelande 13 — Johnny (användare)

vad sa du host01 och 02 skulle vara

---

## Meddelande 14 — ChatGPT (assistent)

Jag beskrev dem ungefär så här:

- **HOST-01 = Nortropics kärnmaskin**  
  Den första dedikerade, always-on datorn. Tanken var exempelvis en **Mac mini M6, 32 GB / 1 TB**. Den kör sådant som Kernel, supervisor/orchestration, Git/state, vissa workers och grundläggande Nortropic-tjänster.

- **HOST-02 = extra exekveringskapacitet när HOST-01 blir full**  
  Troligen ytterligare en Mac mini eller liknande. Den kan specialiseras på mer resurskrävande men “vanligt datorarbete”: **builds, tester, browser/Playwright, fler Codex-workers, parallella worktrees**.

Alltså ungefär:

```text
HOST-01
= hjärta / samordning / grunddrift

HOST-02
= extra händer / builds / tester / browser-workers
```

Och separat senare:

```text
AI-01
= lokal AI-maskin
  Mac Studio / NVIDIA / DGX-typ
```

Så **HOST-02 var inte tänkt som AI-riggen**. Den är främst nästa vanliga arbetsmaskin när Nortropic har fler samtidiga workers än HOST-01 bekvämt kan bära.

---

## Meddelande 15 — Johnny (användare)

**Mac mini M6, 32 GB / 1 TB** är alltså tillräckligt?

---

## Meddelande 16 — ChatGPT (assistent)

**Ja — för den HOST-01 vi har beskrivit tycker jag att Mac mini M6, 32 GB / 1 TB är tillräcklig.** Jag skulle till och med säga att den är en väldigt vettig startpunkt snarare än en kompromiss.

product["turn191068product0","Mac mini M6 12-Core, 32GB, 1TB SSD",{"render_as":"hero"}]

Det viktiga är att förstå **vad vi ber den göra**:

```text
HOST-01
│
├── Autonomy Kernel
├── Supervisor / orchestration
├── Git + worktrees
├── Codex A
├── Codex B
├── Node/Python-tjänster
├── builds och tester
├── viss browser automation
├── Nortropic observability
└── Digitalas vanliga arbete
```

Själva GPT/Codex-modellerna kör fortfarande huvudsakligen sin tunga inferens i molnet. Därför behöver HOST-01 inte 128 GB RAM och ett monster-GPU.

M6 har 12 CPU-kärnor och kan konfigureras till **32 GB unified memory**, vilket är max för M6-versionen. Apple positionerar dessutom just den nya Mini-generationen för always-on agentiska arbetsflöden. citeturn191068search0turn191068search1

### Jag skulle tänka på 32 GB så här

Din nuvarande:

```text
8 GB
████████

Litet bord.
Vi klarar redan Nortropic-utveckling på det.
```

HOST-01:

```text
32 GB
████████████████████████████████

4× arbetsbordet.
+
mycket snabbare CPU
+
snabbare SSD
+
dedikerad maskin
+
du behöver inte använda den som personlig laptop.
```

Det är ett **enormt steg** från där vi står.

Och framför allt behöver vi inte dimensionera HOST-01 för all framtida Nortropic.

Det är precis därför arkitekturen såg ut så här:

```text
HOST-01
32 GB
   │
   │ växer
   ▼
capacity observability
   │
   ├── vanligt compute fullt?
   │        ↓
   │      HOST-02
   │
   ├── storage fullt?
   │        ↓
   │      STORAGE
   │
   └── mycket lokal AI?
            ↓
          AI-01
```

### Det finns en större Mini

M5 Pro-versionen kan konfigureras med **64 GB RAM**, och en 64 GB/1 TB-konfiguration ligger just nu betydligt högre i pris. citeturn191068search0

product["turn191068product5","Mac mini M5 Pro 64GB, 1TB SSD",{"render_as":"block"}]

Jag skulle **inte köpa den bara av rädsla för framtiden**.

För om vi når punkten:

```text
32 GB HOST-01
är konstant full
```

är det inte självklart att lösningen är:

```text
ersätt HOST-01 med större dator
```

Det kan vara mycket bättre:

```text
HOST-01              HOST-02
Kernel               workers
orchestration        Playwright
state                builds
services             tester
Codex A              Codex B/C/D
```

Då får Nortropic **64 GB total fysisk arbetsyta plus två CPU:er och riktig arbetsfördelning**, istället för en enda jättemaskin.

Det är också en mycket bättre proving ground för den distribuerade Nortropic-arkitektur vi vill kunna ha senare.

## Och 1 TB?

**Ja, även det räcker bra för HOST-01.**

Jag skulle inte betala Apple-priser för 4–8 TB intern disk nu.

När vi faktiskt börjar samla enormt med:

```text
screenshots
artifacts
datasets
backups
video
model files
logs
kundhistorik
```

vill jag hellre att arkitekturen går mot:

```text
HOST-01   HOST-02   AI-01
     \       |       /
      \      |      /
       STORAGE-01
          8–20 TB
```

än att varje Mac sitter med jättestor dyr intern SSD.

### En liten sak jag skulle fundera på

Mac mini M6 har **2,5 Gbit Ethernet som standard och 10 Gbit som konfigurationsval**. citeturn191068search1

För HOST-01 behöver vi inte 10 Gbit idag. Men om merkostnaden är rimlig när du beställer är just **10 Gb Ethernet** en framtidsuppgradering jag tycker är mer intressant än exempelvis att köpa enorm intern SSD, eftersom HOST-01 senare kan prata väldigt snabbt med `STORAGE-01`, `HOST-02` och `AI-01`.

---

Så min bild är:

> **M6 / 32 GB / 1 TB är inte tänkt att vara “Nortropics slutgiltiga superdator”. Den är tänkt att vara en väldigt kapabel första fysisk nod.**

För **Kernel + Digitala + Codex A/B + vanliga workers + builds/tester + always-on Nortropic**: **ja.**

För **70B/100B+ lokala AI-modeller, tung bild/video-inference, fine-tuning och tusentals lokala AI-jobb**: **nej — men det är `AI-01:s` framtida jobb, inte HOST-01:s.**

Och den nya M6 Mini börjar levereras **22 september 2026**, så vi är faktiskt precis i rätt fönster om vi skulle välja att göra detta efter Kernel-checkpointen. citeturn191068search1

---

## Meddelande 17 — Johnny (användare)

Ge mig ett scenario hur det ser ut med fruns Mac och styra h1 h2 på distans

---

## Meddelande 18 — ChatGPT (assistent)

Absolut. Tänk att **fruns Mac blir din fjärrkontroll**, medan H1 och H2 är två små fabriker som står någonstans hemma och arbetar.

```text
                    DU
             Fruns MacBook M1
                  8 GB
              "COCKPITEN"
                    │
                    │ privat anslutning
                    ▼
        ┌──────────────────────┐
        │       HOST-01        │
        │   Nortropics hjärta  │
        │                      │
        │ Kernel               │
        │ Supervisor           │
        │ state / Git          │
        │ scheduler            │
        │ observability        │
        └──────────┬───────────┘
                   │
             skickar arbete
                   │
                   ▼
        ┌──────────────────────┐
        │       HOST-02        │
        │  extra arbetskraft   │
        │                      │
        │ Codex workers        │
        │ browser / Playwright │
        │ builds               │
        │ tester               │
        │ worktrees            │
        └──────────┬───────────┘
                   │
              resultat tillbaka
                   ▼
                HOST-01
                   │
                   ▼
             Fruns MacBook
```

### Som om du vore 5

Fruns MacBook är **chefens walkie-talkie**.

H1 är **arbetsledaren på fabriken**.

H2 är **verkstaden med fler arbetare**.

Du sitter alltså inte och gör allting på fruns Mac längre. Du använder den för att säga:

> "Nortropic, bygg det här."

H1 hör dig och tänker:

> "Okej. Det här behöver tre arbetare, två tester och en browser."

H1 skickar då en del av arbetet till H2.

H2 jobbar.

H2 skickar tillbaka resultatet.

H1 kontrollerar vad som hänt och håller reda på organisationens state.

Du ser resultatet från fruns Mac.

---

## Ett konkret framtida scenario

Det är klockan 21:45.

Barnen har lagt sig och du öppnar fruns MacBook.

Du behöver inte ha hela Nortropic lokalt.

Du kanske öppnar:

```text
Verkstadsgolvet
```

och ser:

```text
NORTROPIC

HOST-01
Healthy
2 workers active
Kernel healthy

HOST-02
Healthy
4 workers active
2 browser jobs

Digitala
3 active missions

Owner attention
1 item
```

Du klickar på Digitala och säger ungefär:

> Gör nästa iteration av Nortropic-webbplatsen enligt den nya standarden.

Fruns M1 skickar bara själva instruktionen.

---

# H1 tar över därifrån

H1 kanske skapar:

```text
MISSION #482

Research
Design review
Implementation
Browser verification
Accessibility
Visual QA
Deployment candidate
```

H1 kanske själv kör små koordinationssaker.

Men sedan ser den:

```text
Behöver:
4 parallella browser-workers
```

H1 har kanske inte lämplig kapacitet.

Då säger scheduler:

```text
HOST-02
available
```

och arbetet skickas dit.

---

# H2 börjar arbeta

H2 kanske samtidigt kör:

```text
Worker 1
desktop browser test

Worker 2
mobile browser test

Worker 3
build + TypeScript

Worker 4
visual screenshots
```

Din frus laptop gör **ingenting av detta**.

Den kan nästan stå helt stilla.

Du kan till och med stänga locket.

H1 och H2 fortsätter.

Det är en väldigt viktig förändring.

---

# Nästa morgon

Du tar fram fruns Mac igen.

H1 har under natten fått tillbaka:

```text
HOST-02

Build          PASS
Desktop        PASS
Mobile         FAIL
Accessibility  PASS
Visual         PASS
```

H1 har redan sett felet.

Kanske:

```text
Mobile navbar overlaps CTA
```

Kernel startar remediation.

Ny worker på H2 fixar.

Ny verifiering körs.

PASS.

När du kommer tillbaka ser du:

```text
Mission #482

COMPLETED

14 tasks
1 failure
1 autonomous remediation
Final verification PASS

Owner attention:
none
```

Det här är den typ av Nortropic vi försöker komma till.

---

# Och du kan fortfarande gå in manuellt

Säg att något ser konstigt ut.

Från fruns Mac kan du öppna Terminal och ansluta direkt:

```text
Johnny
  ↓
Fruns Mac
  ↓
HOST-01
```

och få en riktig terminal på H1.

Eller:

```text
Johnny
  ↓
Fruns Mac
  ↓
HOST-02
```

och titta på H2.

Tekniskt kan det senare exempelvis göras genom en **privat nätverksanslutning + SSH**, så att vi inte behöver öppna maskinerna direkt mot internet.

Och VS Code kan på samma sätt användas så att det känns ungefär som om filerna låg på din Mac trots att koden faktiskt finns/körs på H1/H2.

---

# Det fina är att M1:ans 8 GB plötsligt spelar mycket mindre roll

Idag:

```text
M1 / 8 GB

Chrome
VS Code
Codex
tester
Node
build
Git
Nortropic
allt samtidigt

😵
```

Senare:

```text
M1 / 8 GB

ChatGPT
browser
VS Code / remote
Verkstadsgolvet
terminal

🙂
```

Det tunga arbetet ligger här:

```text
H1  32 GB
+
H2  32/64 GB
```

Så din gamla M1 kan faktiskt bli **mer användbar när Nortropic blir större**, eftersom den slutar vara fabriken.

---

# Och H1/H2 behöver egentligen inga skärmar

Föreställ dig ett litet skåp eller skrivbord hemma:

```text
┌────────────────────────┐
│   NORTROPIC RACK MINI  │
│                        │
│  HOST-01   ● Healthy   │
│  HOST-02   ● Healthy   │
│                        │
│  Router                │
│  Storage senare        │
│  UPS senare            │
└────────────────────────┘
```

Ingen skärm.

Inget tangentbord.

Ingen mus.

Ethernet in.

Ström in.

Klart.

Du sitter någon annanstans med laptop.

---

# Du skulle också kunna vara borta

Säg att du är på jobbet, hotell eller hos någon annan.

Så länge du har en säker privat väg hem:

```text
Fruns Mac
     │
   internet
     │
private tunnel
     │
     ▼
   HOST-01
     │
     ▼
   HOST-02
```

kan du fortfarande öppna Verkstadsgolvet.

Nortropic kan alltså stå hemma i Luleå och arbeta medan du befinner dig någon helt annanstans.

Och längre fram kan din telefon räcka för mycket:

```text
iPhone

"Nortropic behöver attention"

↓ tap

Digitala:
Deployment candidate ready.
No blocker.
Confidence high.

[inspect]
```

Du behöver inte ens öppna terminalen för normalt ägararbete.

---

# En viktig arkitekturdetalj

Jag skulle helst inte göra:

```text
Laptop
├── styr H1
├── styr H2
├── styr Worker A
├── styr Worker B
├── styr Worker C
└── styr tester
```

För då är **du fortfarande supervisor**.

Hellre:

```text
        JOHNNY
          │
          ▼
        HOST-01
     CONTROL PLANE
          │
          ▼
      NORTROPIC
          │
     ┌────┴────┐
     ▼         ▼
   H1 work    H2 work
```

Du talar primärt med **Nortropic**.

Nortropic talar med maskinerna.

Det är mycket mer i linje med vad vi bygger.

---

## Så jag ser första riktiga hemmasetupen

```text
                  JOHNNY
                     │
              Fruns M1 / 8 GB
              OWNER COCKPIT
                     │
                     │ secure remote
                     ▼
                HOST-01
          Mac mini M6 32/1TB
           CONTROL + CORE
                     │
           ┌─────────┴─────────┐
           │                   │
           ▼                   ▼
      vanligt arbete       HOST-02
                         EXECUTION NODE
                              │
                       builds / browser
                       workers / tests
```

Och senare kopplar vi bara på:

```text
               HOST-01
                  │
       ┌──────────┼───────────┐
       ▼          ▼           ▼
    HOST-02    STORAGE      AI-01
```

Det är därför jag gillar denna utvecklingsväg så mycket: **du behöver inte ersätta fruns M1 bara för att Nortropic blir kraftfullt.**

M1:an kan fortsätta vara den lilla terminalen du håller i handen, medan Nortropics faktiska muskler successivt flyttar över till dess egna maskiner.

---

## Meddelande 19 — Johnny (användare)

Ja m1an eller min iPhone ?

---

## Meddelande 20 — ChatGPT (assistent)

**Båda**, men de får olika roller.

Jag skulle se det så här:

```text
               NORTROPIC
                   │
             HOST-01 / H1
                   │
             HOST-02 / H2
                   │
          verkligt arbete körs här
                   ▲
          ┌────────┴────────┐
          │                 │
       M1 Mac            iPhone
     "cockpit"          "fjärrkontroll"
```

**M1:an** blir din riktiga cockpit när du vill arbeta: ChatGPT, VS Code remote, terminal/SSH, läsa diffar, granska kod, se logs, göra större owner-beslut och vid behov gå direkt in på H1/H2. Den behöver inte längre vara kraftfull eftersom den mest visar och styr saker som körs någon annanstans.

**iPhonen** kan bli Nortropics vardagliga ägarinterface. Där skulle jag på sikt vilja att du kan öppna Verkstadsgolvet och se något i stil med:

```text
NORTROPIC

● Kernel healthy
● H1 healthy
● H2 healthy

Digitala
4 missions active

Overnight
27 tasks completed
2 autonomously remediated

OWNER ATTENTION
1 item

Deploy new Nortropic site?
Recommendation: APPROVE
Evidence: PASS
```

Och därifrån kanske du kan läsa sammanfattningen, titta på screenshots, ge ett mål, svara på en verklig owner-fråga eller godkänna något när authority faktiskt kräver dig.

Så en vanlig framtida dag skulle kunna vara:

```text
07:15
iPhone
↓
"Kolla Nortropic"
↓
allt grönt
↓
1 owner-attention
↓
du svarar

12:30
iPhone
↓
"Digitala, undersök detta"
↓
mission går till H1

21:30
M1 MacBook
↓
djupare arbete
↓
ChatGPT + Verkstadsgolvet + remote VS Code
↓
H1/H2 gör själva jobbet
```

Det riktigt fina slutmålet är alltså att **du normalt inte ska behöva SSH:a in i H1 för att driva Nortropic**. SSH/terminal är serviceluckan när vi bygger, felsöker eller behöver gå på djupet.

Normalläget bör snarare vara:

> **iPhone för att leda och följa organisationen. M1 för att arbeta nära organisationen. H1/H2 för att göra arbetet.**

Så ja: även om Nortropic längre fram har flera Mac minis, en AI-rigg och lagring kan **din iPhone i princip vara huvudfjärrkontrollen till hela organisationen**. M1:an blir då bara det större skrivbordet du tar fram när mobilen inte räcker.

---

## Meddelande 21 — Johnny (användare)

okej, vilken spec skulle jag ha på mac mini

---

## Meddelande 22 — ChatGPT (assistent)

Ja. För **HOST-01 i den Nortropic-arkitektur vi har beskrivit** hade jag valt en väldigt specifik konfiguration:

product["turn521059product0","Mac mini M6 12-core / 32 GB / 1 TB",{"render_as":"hero"}]

### Min H1-spec

| Del | Jag skulle välja | Varför |
|---|---|---|
| **Chip** | **M6, 12-core CPU / 12-core GPU** | Mer än tillräckligt för Kernel, Codex-workers, builds, tester och services |
| **Minne** | **32 GB unified memory** | Viktigaste uppgraderingen; max för M6 och bra marginal för parallellt arbete |
| **SSD** | **1 TB** | Bra lokal arbetsyta utan att överinvestera i Apples dyra storage |
| **Ethernet** | **10 Gbit/s om prispåslaget känns rimligt** | Inte nödvändigt idag, men attraktivt när H2/NAS/AI-01 kommer |
| **Wi-Fi** | Wi-Fi 7 ingår | Bra, men jag skulle köra H1 på kabel |
| **AppleCare** | Valfritt | Inte arkitekturmässigt nödvändigt |

Apple bekräftar att M6 Mini kan konfigureras med **32 GB RAM, 1 TB/2 TB SSD och 10 Gb Ethernet**. Standard-Ethernet är redan 2,5 Gb/s. citeturn521059search0turn521059search2

Så på beställningssidan skulle jag i princip klicka:

```text
Mac mini

M6
12-core CPU
12-core GPU

32 GB unified memory
1 TB SSD

10 Gigabit Ethernet  ← min enda "future-proof"-extra
```

## Vad jag INTE skulle köpa

Jag skulle inte lägga pengar på:

```text
❌ 2 TB SSD
❌ M5 Pro bara "för säkerhets skull"
❌ 64 GB redan på H1
❌ dyr extern GPU
❌ tangentbord/mus/skärm specifikt för H1
```

H1 ska i vårt scenario ändå vara **headless**:

```text
ström
+
Ethernet
+
Mac mini
=
Nortropic H1
```

Du styr den från:

```text
iPhone
eller
fruns M1
       │
       ▼
      H1
```

Och när H1 en dag verkligen inte räcker vill jag hellre att vi får:

```text
H1                     H2
M6 / 32 GB             nästa node
core/control     +      execution
```

än att vi idag försöker köpa en enda monstruös dator som ska klara fem års okända behov.

### En detalj: köpdatum

Den nya M6 Mac mini presenterades **25 augusti 2026**, men börjar levereras **22 september 2026**. Så eftersom det idag är 6 september skulle jag hellre förbeställa/rikta in mig på M6 än köpa föregående generation för nästan samma syfte. citeturn521059search2

**Kortversionen: `M6 / 32 GB / 1 TB / helst 10GbE`. Det är den H1 jag hade byggt Nortropics första egna hem runt.**

