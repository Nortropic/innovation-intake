# Brainstorma Capability Atlas — fullständigt transkript

**Källprojekt:** Improvements (ChatGPT-projekt)
**Chatt:** Brainstorma Capability Atlas
**URL:** https://chatgpt.com/c/6a9be39e-4d24-83ed-9f41-7525718eb8f5
**Exportdatum:** 2026-09-11
**Antal meddelanden:** 2 (1 användare, 1 assistent)
**Syfte:** Fångad i PROJECT_SWEEP Improvements R39 (data-layer, WYSIWYG-filtrerad); syftet med samtalet avgörs av dess innehåll, inte av denna rubrik.

**Innehåll i korthet:** Samtalet öppnar med: ”Jag gillar kategoriseringen av verktyg, brainstorma” och avslutas med: ”Ja — och jag tror faktiskt att **det mest värdefulla i de här bilderna inte är de 275 reporna**, utan sättet han gör landskapet begripligt.  Han har i praktiken skapat ett litet **“AI capability catal”

> Notis: rader som ser ut som käll-/citat-chips från ChatGPT är en del av
> originaltexten och har bevarats ordagrant. 8 bilagor inventerade (data-layer: distinkta plattforms-fil-id ur metadata.attachments + icke-textdelar; en bild som adaptern listar två gånger räknas en gång); bytes registreras separat via register-attachment där plattformen exponerar dem.

---

## Meddelande 1 — Johnny (användare)

Jag gillar kategoriseringen av verktyg, brainstorma

---

## Meddelande 2 — ChatGPT (assistent)

Ja — och jag tror faktiskt att **det mest värdefulla i de här bilderna inte är de 275 reporna**, utan sättet han gör landskapet begripligt.

Han har i praktiken skapat ett litet **“AI capability catalog”**:

- Claude Code & harnesses
- Agent skills
- MCP & connectors
- AI tools & apps
- AI design & visuals
- Prompts & context
- “Charlie’s own”
- plus en separat vy: **“The 6 I use every day”**

Det sista är nästan ännu viktigare. Han skiljer implicit mellan **hela ekosystemet** och **den operativa standardstacken**.

För Nortropic skulle jag ta den idén betydligt längre.

# Nortropic Capability Atlas

Jag skulle inte kalla det *Tool Library*, eftersom mycket av det vi använder inte egentligen är “verktyg”.

Vi har:

```text
Models
Harnesses
Skills
Agents
Connectors
APIs
MCP servers
Prompt/program systems
Memory/context systems
Browsers
Computer-use systems
CLI tools
Infrastructure
Evaluation systems
Observability
Applications
Nortropic-native capabilities
```

Det gemensamma är snarare:

> **De är capabilities Nortropic kan använda för att åstadkomma något.**

Så jag ser framför mig:

```text
NORTROPIC
   │
   ▼
CAPABILITY ATLAS
   │
   ├── Execution & Harnesses
   ├── Models & Routing
   ├── Skills
   ├── Connectors & MCP
   ├── Context & Knowledge
   ├── Research & Discovery
   ├── Browser & Computer Use
   ├── Code & Engineering
   ├── Design & Media
   ├── Data & Documents
   ├── Automation & Orchestration
   ├── Evaluation & Assurance
   ├── Observability & Operations
   ├── Infrastructure & Deployment
   └── Nortropic Native
```

## Men här finns en viktig arkitekturdetalj

Charlies kategorisering är **utmärkt för människor**, men lite för lös för ett autonomt system.

Exempelvis kan:

`hermes-agent`

vara både:

- agent
- harness
- learning system
- automation tool

Och:

`spec-kit`

är inte riktigt samma sorts objekt som:

`OpenCut`.

Så Nortropic bör ha **två taxonomier samtidigt**.

### 1. Människans taxonomi

Precis som bilderna.

> “Visa mig designverktyg.”

> “Visa mig agent skills.”

> “Vad använder Digitala?”

### 2. Maskinens taxonomi

Strukturerad metadata.

```text
NAME
hermes-agent

TYPE
agent-framework

CAPABILITIES
workflow-learning
task-execution
memory

DOMAIN
general

EXECUTION
local/cloud

SIDE EFFECTS
filesystem
network

AUTHORITY
write/execute

DATA ACCESS
...

COST
...

LATENCY
...

TRUST
evaluated

STATUS
candidate

LAST VERIFIED
2026-09-...

EVIDENCE
...

ALTERNATIVES
...

REPLACES
...
```

Det här är **mycket mer Nortropic**.

---

# Och då kommer en idé jag gillar ännu mer

## Discovery → Candidate → Admitted → Preferred → Default

Vi ska absolut inte göra:

```text
GitHub cool
↓
install
```

Capability Atlas kan ha en riktig lifecycle:

```text
DISCOVERED
    ↓
RADAR
    ↓
CANDIDATE
    ↓
EVALUATION
    ↓
ADMITTED
    ↓
PREFERRED
    ↓
DEFAULT
```

Och åt andra hållet:

```text
DEGRADED
DEPRECATED
QUARANTINED
SUPERSEDED
RETIRED
```

Det passar nästan perfekt ihop med mycket av det vi redan har kommit fram till kring capability lifecycle.

Då skulle `superpowers`, till exempel, inte automatiskt bli del av Nortropic bara för att det är populärt.

Det skulle vara:

```text
Source:
external GitHub

Status:
DISCOVERED

Potential:
high

Relevant capability:
agent skill framework

Requires evaluation:
yes
```

---

# “The 6 I use every day” är också en kanonidé

Men jag skulle göra den dynamisk.

Inte:

> Nortropic har sex favoritverktyg.

Utan:

## Default Stacks

Exempel:

```text
DIGITALA
Default Stack

Harness
Model
Browser
Design capability
Implementation capability
Verifier
Deployment capability
Observability
```

Research kanske har:

```text
RESEARCH
Default Stack

frontier search
deep research
browser
GitHub
source verifier
knowledge compiler
```

Kernel kan ha en annan.

Och en specifik mission kan få:

```text
MISSION EXECUTION PROFILE

Model        GPT-5.6 Sol
Executor     Codex B
Environment  HOST-02
Skills       web-audit-v3
              accessibility-review
Tools        browser
              lighthouse
              axe
Verifier     independent-web-reviewer
Context      customer/project capsule
```

Det här knyter direkt ihop med det vi nyligen diskuterade kring **RouteLLM**.

Fast Nortropic ska inte bara route:a:

```text
prompt → model
```

utan så småningom:

```text
TASK
 ↓
CAPABILITY ROUTER
 ↓
model
+harness
+skills
+tools
+connectors
+runtime
+context
+verification strategy
```

Det är mycket mer kraftfullt.

---

# Jag skulle därför lägga till en särskild kategori

## Models & Routing

Den saknas egentligen i hans struktur.

```text
MODELS & ROUTING

GPT
Claude
Gemini
Grok
local models
specialist models

model routers
cost routers
quality routers
fallback systems
ensemble systems
```

Nortropic ska helst inte tänka:

> “Vilken AI använder vi?”

utan:

> **Vilken execution configuration är bäst för den här uppgiften?**

---

# “Charlie’s own” tycker jag är briljant

Det är egentligen:

> **egen IP kontra externa byggblock.**

Nortropic behöver definitivt motsvarigheten:

# Nortropic Native

Där skulle med tiden kunna ligga saker som:

```text
Nortropic Intake

Improvements Recompile

Capability Qualification

Website Quality Standard

Owner Attention Fusion

Context Compiler

Organization Projection

Aquarium Projection

Evidence / Verification machinery

Profession Qualification

Experience Compiler
```

Det är viktigt kommersiellt också.

Vi kan använda 500 open-source-verktyg utan att låtsas att de är vårt värde.

Atlasen kan tydligt visa:

```text
ECOSYSTEM CAPABILITY
versus
NORTROPIC NATIVE
```

Och den senare kategorin blir successivt Nortropics verkliga differentiering.

---

# Jag skulle också dela upp “AI tools & apps”

Det är den enda kategorin i bilderna jag tycker är för bred.

Jag hade hellre gjort:

```text
Automation & Orchestration
Data & Documents
Communication
Media
Developer Utilities
Knowledge
```

Exempel från bilderna, bara utifrån hur de presenteras:

```text
markitdown
→ Data & Documents

spec-kit
→ Engineering / Specification

OpenCut
→ Media

Dify
→ Automation & Orchestration

UI-TARS
→ Computer Use

browser
→ Browser Automation

Composio
→ Connectors / Action Layer

meetily
→ Capture / Knowledge

DSPy
→ Context / Model Programming
```

Det gör systemet lättare att förstå.

---

# Skills förtjänar dessutom en mycket stark definition

Bilderna använder “skill” ganska löst.

För Nortropic skulle jag vilja kunna skilja:

```text
TOOL
kan göra något

SKILL
vet hur ett resultat ska åstadkommas med hjälp av tools/capabilities

ROLE
ett arbetsmässigt ansvar/perspektiv

AGENT
en temporär exekverande instans

HARNESS
miljön som låter agenten arbeta

MODEL
den kognitiva motorn

CONNECTOR
ger åtkomst till extern värld

CAPABILITY
det Nortropic som organisation faktiskt kan åstadkomma
```

Detta är en **väldigt viktig distinktion**.

För annars blir hela agentvärlden snabbt:

> agent = skill = tool = MCP = repo = capability

och sedan går det knappt att resonera om arkitekturen.

---

# Och Atlasen kan bli levande

Föreställ dig Verkstadsgolvet:

```text
CAPABILITIES
────────────────────────────────

All       437
Admitted   81
Default    24
Radar     192
Testing    17
Deprecated 13
```

Sedan kategorier som i bilderna.

En capability-card:

```text
┌──────────────────────────────────────┐
│ UI-TARS                              │
│ Computer-use agent                   │
│                                      │
│ COMPUTER USE · EXTERNAL              │
│ ● EVALUATING                         │
│                                      │
│ Privacy      Medium risk             │
│ Side effects High                    │
│ Local        Yes                     │
│ Cost         —                       │
│                                      │
│ Used by: Digitala Lab                │
│ Last eval: 3 days ago                │
└──────────────────────────────────────┘
```

Trycker man på den:

```text
WHAT IT DOES
WHY WE CARE
HOW IT WORKS
TRUST BOUNDARY
BENCHMARKS
EVIDENCE
ALTERNATIVES
KNOWN FAILURES
USED BY
VERSION HISTORY
```

Nu börjar det bli Organization OS snarare än en bookmarks-sida.

---

# Sedan kan vi få automatiska “stack recommendations”

Exempel:

> **“Bygg och förvalta en modern restaurangwebb.”**

Nortropic ser:

```text
required capabilities

business research
competitive analysis
content
design
image generation
frontend
browser testing
accessibility
SEO
deployment
analytics
```

Capability Router frågar Atlasen:

```text
Vilka admitted capabilities löser dessa?

Vilka är preferred?

Vilka har bäst outcome-data?

Vilka får användas inom authority?

Vilka kostar minst utan kvalitetsförlust?
```

Och konstruerar execution profile.

Det är nästan **package management för organisatorisk kompetens**.

---

# Ännu mer intressant: capability gaps blir synliga

Mission kräver:

```text
3D product visualization
```

Atlas:

```text
AVAILABLE CAPABILITY
NONE QUALIFIED
```

Då får vi:

```text
CAPABILITY GAP
      ↓
discover ecosystem
      ↓
evaluate candidates
      ↓
buy / integrate / build
      ↓
verify
      ↓
admit
      ↓
execute mission
```

Det är exakt den sorts mekanism som gör att Nortropic kan **lära sig nya yrkesförmågor** utan att vi förhandsspecificerar alla framtida agenter.

---

# Och popularitet ska inte vara kvalitet

Stjärnorna i bilderna är bra för discovery:

```text
★272k
★231k
...
```

Men Nortropic borde istället börja bygga sin egen signal:

```text
NORTROPIC SCORECARD

Task success       96%
Verification pass  98%
Cost                low
Latency             medium
Reliability         high
Security            B
Maintenance         active
Integration burden  low
Outcome evidence    strong
```

GitHub stars blir bara:

```text
EXTERNAL POPULARITY SIGNAL
```

inte:

```text
QUALITY = 272k
```

Det här är viktigt.

---

# Fyra vyer snarare än en enda katalog

Jag tror slutprodukten egentligen har fyra sätt att titta på samma capability graph:

### **Explore**
Den snygga kategoriseringen från bilderna.

För människor.

### **Operate**
Vad är installerat, aktivt, trasigt och faktiskt använt?

### **Govern**
Vad får göra vad? Vilken authority, dataåtkomst och risk har det?

### **Learn**
Vilka capabilities fungerar bäst? Vad håller på att ersättas? Vad förbättrar outcomes?

Och Aquarium kan senare visa vissa delar mer ambient:

```text
Digitala
12 capabilities active
2 experimenting
1 degraded
No owner attention required
```

---

## Jag tycker dessutom att vi har hittat ännu en potentiell first-class Nortropic primitive:

# **Capability Registry**

Inte nödvändigtvis ett stort system eller en service.

Men konceptuellt:

```text
CAPABILITY
+
SOURCE
+
QUALIFICATION
+
STATUS
+
AUTHORITY
+
EVIDENCE
+
USAGE
+
OUTCOMES
+
LIFECYCLE
```

Det kan bli den institutionella katalogen över:

> **vad organisationen faktiskt kan göra.**

Det är mycket mer betydelsefullt än en lista över installerade tools.

Och det passar extremt bra med vår tidigare princip:

> **Capabilities persist. Workers are ephemeral.**

---

### Min preliminära Nortropic-kategorisering

```text
01  Models & Routing
02  Harnesses & Runtimes
03  Skills & Methods
04  Connectors & MCP
05  Browser & Computer Use
06  Context, Memory & Knowledge
07  Research & Discovery
08  Engineering & Code
09  Design, Visuals & Media
10  Data & Documents
11  Automation & Orchestration
12  Evaluation & Assurance
13  Observability & Operations
14  Infrastructure & Deployment
15  Communication & Collaboration
16  Nortropic Native
```

Och ovanpå allt:

```text
MY / DEPARTMENT DEFAULTS
RECENTLY USED
RECOMMENDED
EXPERIMENTING
FRONTIER RADAR
```

Det ger både **den tilltalande enkla katalogen du reagerade på i bilderna** och den betydligt djupare capability-arkitektur Nortropic behöver.

Jag skulle därför inte kopiera “Vault”. Jag skulle ta idén och göra den till **Nortropic Capability Atlas + Capability Registry + Execution Profiles**. Det känns väldigt nära en central bit i den Organization OS-arkitektur vi håller på att konvergera mot — och något som bör få komma med som kandidat i Improvements Recompile snarare än att vi börjar bygga ett nytt sidoprojekt nu. memcite

