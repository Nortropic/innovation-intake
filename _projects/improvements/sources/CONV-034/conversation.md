# Brainstorma filsystem — fullständigt transkript

**Källprojekt:** Improvements (ChatGPT-projekt)
**Chatt:** Brainstorma filsystem
**URL:** https://chatgpt.com/c/6aa1785a-912c-83eb-adf2-a3d4041a217b
**Exportdatum:** 2026-09-11
**Antal meddelanden:** 3 (1 användare, 2 assistent)
**Syfte:** Fångad i PROJECT_SWEEP Improvements R39 (data-layer, WYSIWYG-filtrerad); syftet med samtalet avgörs av dess innehåll, inte av denna rubrik.

**Innehåll i korthet:** Samtalet öppnar med: ”Brainstorma Jake Van clief file system istället för kernels etc” och avslutas med: ”iturn457391image0  **Ja – Jakes filsystemsbaserade arbetssätt är ett relevant motförslag till delar av Nortropic, inte bara inspiration till en bättre mappstruktur.**  Jag tycker att vi ska ta din ”

> Notis: rader som ser ut som käll-/citat-chips från ChatGPT är en del av
> originaltexten och har bevarats ordagrant. Bilageinventering osäker: data-layer inventerade inga bilagor i de synliga meddelandena (noll poster), men texten bär filciteringar/uppladdningsfraser (lägsta observerade antal 1) — antalet är okänt och deklareras inte; innehållet ej infångat i svepet.

---

## Meddelande 1 — Johnny (användare)

Brainstorma Jake Van clief file system istället för kernels etc

---

## Meddelande 2 — ChatGPT (assistent)

Jag jämför Jakes filsystemsbaserade arbetssätt med Nortropic: vad vanliga filer kan ersätta, och vilka körande kärnfunktioner och skydd som ändå behövs.

---

## Meddelande 3 — ChatGPT (assistent)

iturn457391image0

**Ja – Jakes filsystemsbaserade arbetssätt är ett relevant motförslag till delar av Nortropic, inte bara inspiration till en bättre mappstruktur.**

Jag tycker att vi ska ta din fråga på allvar:

> **Behöver Nortropic verkligen så mycket egenbyggd infrastruktur, eller kan en stor del av organisationen bestå av välstrukturerade filer, tydliga arbetsflöden och bra AI-verktyg som redan finns?**

Min preliminära bedömning är:

**Filsystem först för kunskap och arbetsflöden. Befintlig körmiljö först för exekvering. Egen kärnkod bara där vi kan visa att något nödvändigt annars saknas.**

Det betyder inte att vi redan vet att nuvarande Kernel kan tas bort. Men vi ska heller inte utgå från att den måste behållas i sin nuvarande omfattning bara för att vi har byggt den.

## 1. Vad Jake faktiskt föreslår

I **Interpretable Context Methodology, ICM**, representerar numrerade mappar arbetsflödets steg. Markdown-filer beskriver vad agenten behöver läsa och göra, mellanresultat sparas som filer och lokala skript sköter mekaniska uppgifter. En orkestrerande agent kan byta arbetsroll genom att läsa rätt instruktioner i stället för att varje roll måste bli en separat agentimplementation. citeturn457391view1

Det intressanta är alltså inte:

> ”Spara information i mappar.”

Utan:

> **”Låt arbetsmiljön beskriva hur arbetet ska utföras, i stället för att bygga all samordning som specialiserad programvara.”**

I hans separata routingprojekt ligger dessutom en viktig princip: en liten orienteringskarta leder vidare till uppgiftsrouting, relevant arbetskontext och utvalda källfiler. Informationen har en bestämd hemvist; andra filer hänvisar dit i stället för att kopiera samma regler överallt. citeturn826699view6

**Min tolkning för Nortropic:** Vi kanske har beskrivit vissa behov som ”system som måste byggas”, när de i första hand är **kunskap och arbetssätt som behöver organiseras**.

En profession behöver exempelvis inte börja som ett subsystem. Den skulle kunna börja som en välgjord arbetsbeskrivning, referenser, verktyg, kvalitetskriterier och exempel på bra respektive dåligt arbete.

## 2. Den viktiga skillnaden: nödvändiga egenskaper är inte samma sak som nödvändig egen kod

Här behöver jag också vara självkritisk till hur vi ibland har pratat om Nortropic.

Resonemanget kan lätt bli:

> Vi behöver säker autonomi.  
> Därför behöver vi en Kernel.  
> Därför behöver vi allt som nu ligger under namnet Kernel.

**Det sista steget följer inte automatiskt.**

Att systemet behöver behörighetsgränser betyder inte att vi måste implementera varje behörighetsmekanism själva.

Att arbetet behöver kunna fortsätta efter ett avbrott betyder inte att varje återstartsproblem kräver en egen orkestreringsplattform.

Att vi behöver spårbarhet betyder inte att varje relation måste få en egen tjänst.

I ert äldre planunderlag används *Autonomy Kernel* för den autonoma arbetskedjan: uppgift, körning, resultat, verifiering, korrigering och säker avslutning/publicering. Det är alltså ett applikationslager vi diskuterar, inte datorns operativsystemskärna. fileciteturn0file1

Det gör följande fråga helt legitim:

> **Vilka av dessa ansvar måste Nortropic äga, och vilka kan Nortropic få från filsystemet, befintliga verktyg och en betydligt mindre mängd egen kod?**

Det går inte att avgöra vilka konkreta moduler som kan tas bort utan att granska aktuell kod. Men **arkitekturens omfattning ska vara prövbar**, inte skyddad av sitt namn.

## 3. Det här är inte Jake mot OpenAI och Anthropic

Tvärtom finns tydliga beröringspunkter.

Anthropics **Agent Skills** paketerar instruktioner, skript och resurser i mappar. Agenten läser först begränsad information om tillgängliga skills och laddar mer innehåll när uppgiften behöver det. Det är en filbaserad form av specialisering, inte ett krav på separata specialbyggda agenter för varje yrkesroll. citeturn826699view3

I Anthropics arbete med långvariga agentuppgifter används bland annat en framstegsfil, Git-historik, en strukturerad funktionslista och ett startskript för att nya sessioner ska kunna orientera sig och fortsätta arbetet. Filer är där en central del av körmiljön, inte något man först måste ersätta med en stor plattform. citeturn826699view0

Codex dokumenterar på motsvarande sätt hur `AGENTS.md` ger återkommande projektinstruktioner genom en hierarki av globala och projektspecifika filer. citeturn528715view3

**Min slutsats:** Nortropic behöver inte välja mellan ”enkla filer” och ”seriös agentarkitektur”. Frågan är snarare hur långt vi kommer genom att **kombinera genomtänkta filer med befintlig agentprogramvara**, innan ytterligare egen infrastruktur faktiskt ger ett mervärde.

Det passar också din ambition: du vill ge ett uppdrag och få arbete utfört, inte ägna livet åt att underhålla ett separat AI-ramverk.

## 4. Vad skulle kunna bli mycket enklare i Nortropic?

Det här är min förenklingshypotes, inte en inventering av vad som finns implementerat i dag:

| Nortropic-behov | Filbaserad utgångspunkt |
|---|---|
| Organisationens identitet och riktning | En kort huvuddefinition, mål och beslut med källhänvisningar. |
| Professioner och kompetenser | Skills, referenser, arbetsmetoder, kvalitetskriterier och verifieringsverktyg. |
| Projekt- och innovationsarbete | Projektmappar med problem, evidens, hypoteser, experiment och beslut. |
| Arbetsflöden | Begripliga steg med definierade indata, utdata och villkor för fortsatt arbete. |
| Institutionellt minne | Bevarade råkällor, accepterad kunskap och tydligt markerade härledningar. |
| Överblick | Genererade vyer över verkliga projekt, resultat och körningar. |

Det skulle exempelvis kunna innebära att **Projekt- och innovationskontoret i sin första användbara form är en arbetsmiljö**, inte en ny organisation av chefsagenter.

Ett projekt kan då innehålla:

```text
project/
  brief.md          Vad försöker vi åstadkomma?
  sources/          Vad bygger arbetet på?
  hypotheses.md     Vad tror vi, men har inte visat?
  experiments/      Hur prövar vi det?
  decisions.md      Vad har faktiskt beslutats?
  outputs/          Vad har producerats?
```

Det här är bara en illustration av principen, inte ett förslag att skapa ännu en konkurrerande struktur bredvid dagens Intake.

**Poängen är att en fungerande innovationsprocess kanske inte kräver ett ”Innovation Office-system” innan den kan börja skapa värde.**

### Samma sak gäller Digitala

I underlaget om Webbförvaltningen är den starkaste idén att kunna känna igen, producera, verifiera och förbättra en bra webbupplevelse. Kvalitet knyts till användarnytta, teknisk integritet, upplevelse och verkliga utfall. fileciteturn0file0

Det uppdraget försvinner inte med en enklare arkitektur.

En tänkbar startpunkt är en projektbrief, relevant kvalitetsstandard, ett arbetsflöde, bra referenser och verktyg för att testa resultatet. En separat permanent ”SEO-agent” eller ”Head of Web” bör då behöva visa att den förbättrar arbetet jämfört med att samma kapacitet aktiveras när den behövs.

**Vi kan behålla den professionella ambitionen och samtidigt ifrågasätta hur mycket organisationsmaskineri den kräver.**

## 5. Men vi ska inte romantisera ”bara filer”

Här finns en viktig begränsning i Jakes eget material.

ICM beskrivs huvudsakligen för **sekventiella arbetsflöden där en människa granskar mellanresultat**. Författarna pekar själva ut begränsningar kring hög samtidighet och komplex automatisk förgrening. De anger också att kontrollerad jämförelse mellan deras stegvisa kontextladdning och monolitisk prompting saknas; erfarenheterna är huvudsakligen praktikerbaserade. citeturn457391view0

Det betyder inte att metoden är svag. Det betyder att vi inte får smuggla in slutsatsen:

> ”Jake visar att mappar ersätter en autonom organisation som arbetar utan mänsklig handpåläggning.”

Det har de inte visat.

Dessutom körs deras exempel genom Claude Code, och vissa använder delegering till underagenter. **Körmiljön finns alltså kvar även när ett separat orkestreringsramverk försvinner.** citeturn826699view5

För Nortropic blir därför den ärliga jämförelsen:

> **Filer + befintlig körmiljö**  
> mot  
> **filer + befintlig körmiljö + Nortropics egen infrastruktur.**

Inte ”mappar mot all programvara”.

### Tre saker jag inte skulle förväxla

**En instruktion är inte en behörighetsgräns.**  
En fil som säger ”ändra inte något utanför projektet” är inte samma sak som att körmiljön faktiskt förhindrar det. Codex skiljer uttryckligen mellan sandboxens tekniska begränsningar och policyn för när agenten behöver be om godkännande. citeturn966674view0

**Ett påstående om kvalitet är inte ett verifierat resultat.**  
Att agenten skriver `approved: true` bevisar inte att leveransen är korrekt. I Anthropics långtidsexperiment var för tidig färdigmarkering ett uttryckligt problem; ordentlig testning behövde byggas in i arbetssättet. citeturn614623view0

**Läsbara instruktioner är inte automatiskt betrodda instruktioner.**  
Anthropic varnar själva för att skills kan innehålla skadliga instruktioner eller kod. För vår filbaserade hypotes innebär det att hämtade researchkällor inte automatiskt får bli instruktioner som styr verktygsanvändningen. citeturn614623view1

Min slutsats är därför inte ”behåll all Kernel”. Den är:

> **Behåll de nödvändiga garantierna. Pröva vilken minsta implementation som faktiskt kan ge dem.**

## 6. Den mest intressanta Nortropic-varianten: filer som arbetsyta, en liten exekverande grund

Jag skulle utforska en modell där Nortropic känns mer som **en välorganiserad arbetsplats** än som ett nytt operativsystem som först måste byggas färdigt.

Den logiska strukturen skulle kunna vara:

```text
NORTROPIC

Riktning och beslut
        ↓
Kunskap + kompetenser + arbetsflöden
        ↓
Projekt med tydliga uppdrag
        ↓
Befintliga agentverktyg utför arbetet
        ↓
Resultat + kontroller + observerade utfall
        ↓
Förbättrad kunskap och bättre arbetssätt
```

Under detta behövs de verkliga begränsningar och mekanismer som uppgifterna kräver. Men jag skulle i första hand försöka **återanvända dem**, inte automatiskt bygga en Nortropic-version av allt.

OpenAI dokumenterar redan en modell där agenten kan arbeta självständigt inom en tekniskt avgränsad miljö utan bekräftelse för varje rutinåtgärd. Samtidigt behöver verktyg utanför kommandosandboxen, exempelvis vissa connector- och MCP-ytor, bedömas utifrån sina egna kontroller. Det är alltså en konkret återanvändningsmöjlighet, inte ett generellt bevis på att alla Nortropics behov redan täcks. citeturn966674view0turn966674view1

### Det viktiga för dina ägarstopp

Jag skulle skilja på:

> **Resultatet går att inspektera.**

och:

> **Johnny måste inspektera resultatet innan arbetet får fortsätta.**

För vår hypotes vill jag behålla det första utan att göra det andra obligatoriskt överallt.

Agenten ska kunna fortsätta inom sitt mandat, lämna läsbara mellanresultat och påkalla din uppmärksamhet när det finns ett faktiskt vägval eller en avvikelse. En mappgräns ska inte i sig bli en ny ägargräns.

### Och Aquarium behöver inte försvinna

Min designhypotes är att Verkstadsgolvet och Aquarium fortfarande kan vara fönster mot den här arbetsmiljön.

Men ett projektkort får inte bli grönt bara för att en agent skrivit en optimistisk sammanfattning. Vyn behöver skilja mellan planerat arbete, agentens egen rapport och observerade kontrollresultat.

**Läsbarhet är värdefullt. Sanningshalten måste fortfarande prövas.**

## 7. För vår researchsammanställning är detta särskilt relevant – redan nu

Här vill jag uttryckligen skilja på två frågor:

**Att ordna, komplettera och analysera researchmaterialet behöver inte vänta på färdig Kernel. Att låta ett nytt upplägg ersätta operativ infrastruktur är ett annat beslut.**

I Recompile-underlaget finns redan en kompatibel tanke: råchattar ska bevaras som evidens, sammanställningar ska vara härledda och utbytbara, och bearbetningen ska ske i inspekterbara pass i stället för i en jättestor prompt. fileciteturn0file2

För just detta är en filbaserad arbetsmiljö en stark kandidat:

> **Råkällor → extraktion → källkoppling → motsägelser och överlapp → sammanställning → översiktskarta.**

Min föreslagna tillämpning är att låta befintlig Nortropic Intake förse arbetet med källmaterial, inte att uppfinna en parallell intake.

Därefter kan väl avgränsade arbetssteg bearbeta materialet. Den ursprungliga chatten förblir källa; en ny slutsats måste kunna peka tillbaka till vad som faktiskt stödjer den.

Det här skulle också kunna vara ett konkret första prov för **Projekt- och innovationskontoret som Customer Zero**: använda en minimal arbetsmiljö för att lösa vårt eget problem med att hålla ihop researchen.

Inte först bygga kontoret i full skala och sedan undersöka om det behövdes.

## 8. Hur vi avgör om förenklingen håller

Jag skulle inte fatta beslut efter vilken arkitekturbild som känns mest elegant. Jag skulle pröva en avgränsad uppgift:

> **Ta ett bestämt researchunderlag, inför nya källor och uppdatera sammanställningen utan att tappa ursprung, blanda hypoteser med beslut eller dölja motsägelser.**

Jämför två utföranden: en filbaserad arbetsmiljö med befintlig agentkörning, och motsvarande körbara Nortropic-flöde. Samma källversioner, modell, verktyg, behörigheter och acceptanskriterier.

Lägg sedan in verkliga störningar: avbryt mitt i arbetet, starta med en ny session, ändra en källa och lämna en bilaga saknad. Facit och kontrollkriterier ska inte kunna skrivas om av den som producerar resultatet.

Det som ska avgöra är **korrekthet, återhämtning, din arbetsinsats, kostnad och hur mycket specialkod som måste underhållas**.

En filbaserad variant vinner inte om den bara flyttar orkestreringen till dig. En avancerad variant vinner inte om dess extra kontroller inte förbättrar resultat eller minskar relevant risk.

**Och befintligt Nortropic måste få förlora jämförelsen.** Annars är det ingen verklig prövning.

## Min slutsats

Jag skulle flytta Jakes arbetssätt från kategorin **”bra kontextidéer”** till **”seriös alternativ implementation att jämföra mot”**.

Inte för att allt bör bli Markdown. Inte för att säker autonomi är oviktig. Utan för att vi behöver skilja Nortropics syfte från den mängd infrastruktur vi hittills har föreställt oss.

Den centrala frågan blir:

> **Hur mycket av Nortropic kan vara välorganiserad kunskap och återanvändbara arbetssätt – och hur liten kan den egenbyggda exekverande delen bli utan att vi tappar något viktigt?**

**Nästa rimliga steg är att formulera och pröva den minsta filbaserade varianten på researchsammanställningen, inte att starta ännu ett stort arkitekturprojekt eller riva nuvarande Kernel på antaganden.**

