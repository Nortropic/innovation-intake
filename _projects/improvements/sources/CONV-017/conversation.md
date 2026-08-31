# Brainstorma jämförelser — fullständigt transkript

**Källprojekt:** Improvements (ChatGPT-projekt)
**Chatt:** Brainstorma jämförelser
**URL:** https://chatgpt.com/c/6a8ab602-de90-83eb-a238-c82bd35f4b10
**Exportdatum:** 2026-08-31
**Antal meddelanden:** 9 (3 användare, 6 assistent)
**Syfte:** Brainstorm om vad Nortropic-bygget kan jämföras med och hur planen bör delas upp efter bootstrap.

**Innehåll i korthet:** Samtalet öppnar med: ”Det vi bygger här, vad kan det jämföras med? Längden för bygget gör ibland att jag ifrågasätter vad detta är och om det kommer funka. Brainstorma” och avslutas med: ”Efter bootstrap skulle jag dela upp vår plan i **fyra tydliga faser**. Det viktiga är att vi inte fortsätter “bygga bootstrap” efter att den gjort sitt jobb. ### 1. Freeze + första”

> Notis: rader som ser ut som käll-/citat-chips från ChatGPT är en del av
> originaltexten och har bevarats ordagrant. Inga bilagor.

---

## Meddelande 1 — Johnny (användare)

Det vi bygger här, vad kan det jämföras med? Längden för bygget gör ibland att jag ifrågasätter vad detta är och om det kommer funka. Brainstorma

---

## Meddelande 2 — ChatGPT (assistent)

Ja — och jag tror att just **längden på bygget lurar intuitionen**. Det känns som att ni “bygger en agent”, men i praktiken har ni glidit upp flera abstraktionsnivåer och bygger mer av ett **kontrollsystem för autonom mjukvaruproduktion**. Jag jämför det mot några etablerade systemlager och försöker samtidigt avgöra om komplexiteten är motiverad eller om Nortropic håller på att överbygga.

---

## Meddelande 3 — ChatGPT (assistent)

En första viktig validering: det ni gör ligger **inte utanför vad frontier-teamen själva beskriver som problemet**. OpenAI skriver 2026 att när agenter tar över mer kodning flyttar ingenjörsarbetet till *environment design, feedback loops, guardrails och control systems*; Anthropic beskriver samtidigt långkörande agentbyggen som ett harness-problem med persistenta artefakter, specialiserade roller och evaluatorer. 

Men det betyder inte automatiskt att varje lager i Nortropic är värt kostnaden. Det är precis den gränsen jag vill dra nu.

---

## Meddelande 4 — ChatGPT (assistent)

Det mest intressanta jag hittar är en **varningssignal som faktiskt talar för att just nu omvärdera gränsen**, inte själva visionen: Anthropic skriver efter sina egna containment-incidenter att de mest beprövade primitivesen — hypervisorer, seccomp/gVisor osv. — höll, medan deras **egenbyggda mellanlager** var det som brast. De rekommenderar uttryckligen containment i miljölagret först och att vara försiktig med custom security components. 

Det gör R112–R116-typen av arbete väldigt intressant: det är legitimt ingenjörsarbete, men frågan är om **Nortropic ska äga just den nivån**, eller använda ett hårdare standardiserat exekveringssubstrat och lägga sin unika komplexitet högre upp.

---

## Meddelande 5 — ChatGPT (assistent)

Ja. Jag tror faktiskt att det är nyttigt att göra den här jämförelsen nu, för **antalet rundor gör att bygget ser mycket konstigare ut än det egentligen är**.

Min huvudtes är:

> **Nortropic håller inte längre på att bli “en agent som kan bygga hemsidor”. Det håller på att bli ett AI-native engineering control plane — ett operativsystem för autonomt ingenjörsarbete.**

Och det är en väsentligt större sak.

OpenAI använder nästan exakt språket *control systems, environments, feedback loops och harness engineering* för den typ av problem ni har hamnat i. Deras eget agent-first-projekt tog omkring fem månader, växte till ungefär en miljon rader och ~1 500 PR:er innan de hade ett system där Codex kunde driva en feature end-to-end från problem till verifiering, PR, reparation och merge. citeturn296867search0

## Vad Nortropic egentligen kan jämföras med

Inte en enskild befintlig produkt. Snarare en kombination:

| Nortropic | Närmaste etablerade motsvarighet |
|---|---|
| Task/spec → desired outcome | Kubernetes `desired state` |
| Supervisor/backlog-loop | Kubernetes controller/reconciliation loop |
| Claude/Codex/provider-routing | Agent harness / Codex Core / Claude Agent SDK |
| Långlivade runs + checkpoints | Temporal Durable Execution |
| `allowed_write`, explicit inputs/outputs | Bazel hermetic actions |
| Provider confinement / sandbox | Codex/Claude Code sandbox |
| TEST_AUTHOR → BUILDER → VERIFIER | Anthropic planner/generator/evaluator |
| Immutable evidence + gates | CI/CD + policy/evaluation system |
| Verkstadsgolvet | execution/data plane |
| Nortropic | control plane |

Kubernetes är en särskilt bra analogi. Ett Kubernetes-controller får ett **önskat tillstånd**, observerar verkligheten, agerar, mäter igen och fortsätter tills verkligheten motsvarar specen. citeturn192257search0

Det är nästan exakt den abstraktion vi har försökt bygga:

**“Jag vill ha X” → Nortropic tar ansvar för att verkligheten faktiskt blir X.**

Inte:

**“Här är en prompt, hoppas Claude löser det.”**

Och Temporal är en annan bit av pusslet: långa processer ska kunna krascha, återupptas och fortsätta från dokumenterat tillstånd i stället för att människan måste rekonstruera vad som hänt. citeturn269146search1turn269146search2

Sedan har du Bazel-likheten. Bazels hermeticity bygger på idén att en action bara ska få de inputs den behöver och bara producera de outputs den deklarerat. Det är anmärkningsvärt nära varför vi överhuvudtaget hamnat i `allowed_write`, staging roots, identitetskontroller och explicit effektauktoritet. citeturn192257search1

### Den kanske allra närmaste publika motsvarigheten

OpenAI släppte i april 2026 **Symphony**, där ett projektledningssystem fungerar som ett *control plane for coding agents*: uppgifter blir arbete, agenter arbetar kontinuerligt, människor hanterar styrning och review. citeturn296867search3

Det jag skulle säga är:

**Symphony ≈ en del av Nortropic.**

Nortropic försöker dessutom äga saker som Symphony-artikeln inte är fokuserad på: provider-neutralitet, explicit verifieraroberoende, capability boundaries, resumability, immutable checkpoints, execution confinement och så småningom R&D/knowledge-feedback.

Så begreppet jag skulle använda framöver är:

### **Autonomous Engineering Control Plane**

Eller mer visionärt:

### **AI-native Software Factory OS**

“Agent harness” är egentligen för litet som begrepp.

---

# Varför tar det då så förbannat lång tid?

Här är den psykologiskt viktiga biten.

Om vi hade satt målet:

> Claude ska själv bygga en hemsida.

…då hade det varit absurt att arbeta så här länge innan den började bygga hemsidor.

Men målet blev successivt:

> Claude/Codex ska kunna utföra godtyckligt ingenjörsarbete under lång tid, utan kontinuerlig mänsklig övervakning, överleva fel, lämna verifierbar evidens, inte kunna ändra otillåtna saker, kunna bytas ut som provider och bara eskalera när människans omdöme faktiskt behövs.

Det är **plattformsteknik**.

Och frontier-världen har upptäckt samma sak.

Anthropic konstaterade att frontier-modeller fortfarande misslyckas på långkörande arbeten om man bara loopar dem. De behövde explicit initialisering, progressartefakter, git-historik, feature lists och rena överlämningar mellan sessioner. citeturn531224search0

Sedan gick de vidare till planner → generator → evaluator för lång autonom application development. citeturn531224search3

Och för att stresstesta multi-agent autonomy lät Anthropic 16 Claude-instanser bygga en C-kompilator. Det tog närmare **2 000 Claude Code-sessioner**, kostade cirka **$20 000**, och producerade ungefär 100 000 rader Rust. citeturn442348search2

Så:

**att ett autonomt system tar många hundra eller tusen agentiterationer är inte i sig ett tecken på att något gått fel.**

---

# Men här kommer min stora reservation

Jag tror **visionen är betydligt mer validerad idag än när vi började**.

Jag är däremot mindre säker på att Nortropic bör bygga hela den nuvarande *execution-security stacken själv*.

Det här är den viktigaste nya slutsatsen jag skulle dra från det vi sett.

Anthropic publicerade i maj en omfattande genomgång av sina containment-system. Deras kanske viktigaste lärdom är:

> deras beprövade primitives — hypervisorer, seccomp, gVisor och liknande — fungerade bra; det var deras egna specialbyggda komponenter runt dessa primitives som skapade de farliga felen.

De rekommenderar därför att containment görs deterministiskt i miljölagret och varnar för custom security components. citeturn442348search1

OpenAI beskriver också hur Codex-sandboxen reducerar processers faktiska OS-behörigheter och låter begränsningarna följa hela processträdet. citeturn296867search4 Anthropic använder samma princip i Claude Code: OS-baserad filesystem- och nätverksisolering gör att agenten kan få **mer autonomi eftersom blast radius är hårt begränsad**. citeturn442348search0

Och det leder oss rakt tillbaka till de senaste R112–R116-problemen.

När vi diskuterar inode-binding, dirfds, symlink races, staging-root moves, process-group identity och exakt unlink-auktoritet så bygger vi inte längre en agentorkestrerare.

Vi bygger delar av en **security/runtime kernel**.

Det kan vara rätt.

Men det är inte självklart att **Nortropics konkurrensfördel ska ligga där**. memcite

---

# Jag ser därför fyra möjliga tolkningar av nuläget

**1. “Det tar lång tid för att idén är fel.”**  
Jag tycker evidensen talar ganska tydligt emot detta. OpenAI och Anthropic rör sig snarare *mot* samma problemklass: harnesses, evaluators, control planes, durable agents, containment och agent-native repositories. citeturn296867search0turn531224search3turn442348search1

**2. “Det tar lång tid eftersom vi bygger en mycket större sak än vi först förstod.”**  
Det här tror jag är huvudanledningen.

**3. “Arkitekturen är rätt, men vi har gått för djupt i vissa lager.”**  
Det här betraktar jag som en verklig risk nu.

**4. “Vi har gjort bootstrapen till själva produkten.”**  
Det här är risken jag vill aktivt förhindra.

Nummer fyra är den farligaste.

---

# Tänk på Nortropic som en fabrik

Du ville tidigare använda kommun-/Verkstadsgolvet-metaforen. Jag tycker fabriksversionen gör dagens läge ännu tydligare.

I början trodde vi ungefär att vi byggde en robotarbetare.

Sedan insåg vi att roboten behöver instruktioner.

Sedan kvalitetskontroll.

Sedan arbetsledning.

Sedan ett skiftsystem.

Sedan loggböcker.

Sedan reservkraft.

Sedan säkerhetsburar.

Sedan behörighetskontroll.

Sedan system som kan upptäcka att kvalitetskontrollanten själv gör fel.

Till slut står man där och inser:

**“Oj. Vi bygger inte en robot. Vi bygger fabriken.”**

Och Nortropic går ytterligare ett steg:

**vi bygger fabriken som senare ska kunna förbättra fabriken.**

Det är därför det känns enormt.

---

# När vet vi då att vi inte har byggt ett forskningsprojekt som aldrig blir klart?

Här skulle jag ändra vår mentala definition av “bootstrap färdig”.

Den får **inte** betyda:

> Vi har inte längre lyckats uppfinna någon teoretisk failure mode.

För det målet existerar inte.

Den bör istället betyda att följande egenskaper demonstrerats i verklig drift:

1. En människa uttrycker ett riktigt mål.
2. Systemet bryter ned det.
3. Agenten arbetar utan handholding.
4. Körningen kan dö och återupptas.
5. Agenten kan inte överskrida sin deklarerade blast radius.
6. Verifieraren kan verkligen underkänna buildern.
7. Misslyckande leder till remediation/retry eller mänsklig eskalering.
8. Slutresultatet kan reproduceras och auditeras.
9. Claude kan vara primär provider och Codex alternativ — utan att kärnan måste byggas om.
10. Vi kan göra samma sak igen med en annan riktig task.

**När det fungerar ska bootstrapen frysas.**

Därefter blir nya fynd vanliga kernel/runtime-issues — inte en anledning att fortsätta hålla hela fabriken stängd.

---

# Det förändrar hur jag ser på R116

Tidigare hade jag lätt kunnat säga:

> Fortsätt tills alla gates är gröna.

Nu skulle jag säga något mer sofistikerat:

**Slutför den invariantfamilj vi redan har öppnat. Men efter den måste vi göra en explicit architectural exit review innan vi öppnar ytterligare en djup hardening-familj.**

Frågan där ska inte vara:

> “Kan vi hitta ännu en edge case?”

Utan:

> **“Ligger den här risken inom Nortropics threat model, och är Nortropic rätt lager att lösa den i?”**

Om svaret är att en battle-tested sandbox/container/VM/capability primitive kan äga det bättre, ska vi förmodligen **radera komplexitet**, inte addera R117–R140.

Det är inte att backa från ambitionen.

Det är mer mogen systemarkitektur.

---

# Min bedömning av om det kommer fungera

Jag skulle separera tre frågor.

**Kan ett sådant system fungera tekniskt?**  
Ja. Jag tycker det är mycket väl belagt nu. OpenAI har demonstrerat ett agent-first repository där en agent kan gå från task till merge; Anthropic har demonstrerat långkörande harnesses och agent teams; durable execution, hermeticity och reconciliation är dessutom sedan länge beprövade distribuerade systemidéer. citeturn296867search0turn442348search2turn269146search1turn192257search0

**Kan Nortropic fungera?**  
Jag ser inget fundamentalt arkitekturproblem som får mig att tänka “det här kommer aldrig gå”. Tvärtom har många av designvalen konvergerat mot frontier-praktik.

**Är exakt den implementation vi bygger idag rätt slutarkitektur?**  
Det är där jag är mer kritisk. Troligen inte. Och den behöver inte vara det.

Bootstrap v1 behöver bli **tillräckligt robust för att Nortropic ska börja arbeta**. Sedan kan Nortropic hjälpa till att ersätta sina egna primitiva delar med bättre generationer.

---

## Det mest spännande scenariot

Det finns egentligen en punkt där payoff-kurvan kan vända dramatiskt.

Idag:

**Du → ChatGPT → Claude/Codex → massor av kontroll → nästa kontroll → nästa kontroll.**

Efter bootstrap:

**Du → Nortropic → 10–50 arbeten fortgår → endast exceptioner kommer tillbaka till dig.**

Och senare:

**Omvärldsbevakning → upptäckt → hypotes → eval → task → implementation → verifiering → deployment → observation → förbättring.**

Då börjar fabriken använda sig själv.

Det är först där all denna investering kan börja **compounda**.

OpenAI beskriver just den övergången: de började långsamt därför att miljön var underspecificerad, men när verktyg, invariants och feedbackloopar byggts upp ökade agenternas leverage kraftigt. De beskriver även återkommande agenter som automatiskt letar efter arkitekturdrift och teknisk skuld — i praktiken “garbage collection” för agentgenererad mjukvara. citeturn296867search0

Det är väldigt nära slutbilden vi har diskuterat för Nortropic.

---

### Så om jag skulle sammanfatta hela brainstormen i en mening:

**Jag skulle inte avbryta Nortropic därför att bygget blivit långt. Jag skulle däremot använda just längden som signal för att nu hårt skilja mellan “fundamental autonomi som Nortropic måste äga” och “infrastrukturproblem som ett beprövat underliggande system borde äga”.**

Det kan vara den viktigaste arkitekturella förenklingen vi gjort hittills.

Och kanske den mentala omställning som gör hela projektet lättare att förstå:

**Vi har inte ägnat månader åt att bygga en långsam AI-agent. Vi har ägnat månader åt att konstruera kontrollplanet som ska göra tusentals framtida agentarbeten billiga, parallella, återupptagbara och pålitliga.**

Den tesen ska vi nu bevisa genom **verkligt arbete**, inte genom oändligt fler bootstrap-gates. memcite

---

## Meddelande 6 — Johnny (användare)

Missförstå mig rätt, jag vill inte ta någon genväg eller bli klar snabbare, bara få en förståelse för vad vi bygger och vi är väl nära slutmålet så detta kommer bli magi

---

## Meddelande 7 — ChatGPT (assistent)

Ja — då förstår jag dig rätt. **Jag tycker inte att vi ska förenkla bort det vi bygger eller forcera fram ett “klart”.** Du försöker snarare få rätt mental modell för varför något som från början kunde låta som “en autonom Claude-loop” har vuxit till ett så omfattande system.

Och där tror jag att den viktigaste distinktionen är:

> **Vi är nära slutet på bootstrapen. Vi är inte nära slutet på Nortropic.**

Det är en enorm skillnad.

Bootstrapen är ungefär som att bygga **motorn, transmissionen, bromsarna, styrningen, instrumentpanelen och säkerhetssystemet**. Hittills har nästan all energi gått åt till att säkerställa att bilen faktiskt kan köra själv utan att vi behöver hålla i ratten.

När det arbetet är färdigt börjar vi använda bilen.

Och det är där det potentiellt börjar kännas som “magi”.

### Vad vi egentligen har byggt

Om man zoomar ut från alla R-rundor, gates, dirfds, provider boundaries och verifieringar ser arkitekturen ungefär ut så här:

**Du**
→ uttrycker intention

**Nortropic**
→ förstår vilket arbete som behöver göras  
→ skapar rätt arbetskontext  
→ väljer rätt agent/provider  
→ begränsar vad den får göra  
→ låter den arbeta  
→ observerar resultatet  
→ verifierar det oberoende  
→ reparerar när något är fel  
→ fortsätter över agent/session/context-gränser  
→ dokumenterar vad som hänt  
→ eskalerar endast när mänskligt omdöme behövs

Det där är väldigt långt från:

> “Claude, implementera den här funktionen.”

Det är snarare:

> **“Nortropic, se till att den här förändringen blir korrekt genomförd.”**

Det är den abstraktionsnivån vi försöker nå.

---

## Och ja: jag tycker att vi är nära en väldigt viktig tröskel

Det som gör den nuvarande fasen lite bedräglig är att de sista problemen är extremt tekniska och ser små ut.

R113, R115, R116 och liknande handlar om saker som staging-identitet, processgrupper, filesystem-races och exakt write-authority. Sett isolerat känns det nästan absurt:

> “Har vi verkligen hållit på så här länge för att diskutera `unlink()`?”

Men de problemen ligger **längst ned i pyramiden**.

De översta lagren finns redan i någon form:

```text
             INTENTION
                 ↓
          Work / Backlog
                 ↓
        Supervisor / Loop
                 ↓
       Builder / Verifier
                 ↓
        Provider Routing
                 ↓
      Durable Run / Resume
                 ↓
     Execution Boundaries
                 ↓
       OS / Process Effects
```

Just nu arbetar vi mycket nära botten.

Och det är en intressant egenskap hos systembyggen: **de sista 5 procenten av infrastrukturen kan kännas som 50 procent av arbetet**, eftersom man då möter de invariants som allt annat vilar på.

När den delen fryses behöver vi inte fortsätta bygga den varje gång.

---

# “Magi” är faktiskt ett ganska bra ord för nästa fas

Inte för att systemet plötsligt blir intelligent på något mystiskt sätt.

Utan därför att **komplexiteten börjar döljas bakom en enklare abstraktion**.

Idag kan en förbättring innebära något i stil med:

> brainstorming → spec → Claude → Codex → test-author → builder → verifier → remediation → gate → checkpoint → ny runda → osv.

Du ser hela maskineriet.

Målet är att du senare ska kunna säga något mycket närmare:

> **“Undersök varför våra hemsidor har sämre Core Web Vitals än de bästa konkurrenterna. Ta fram en förbättring, bevisa att den fungerar och implementera den om evidensen håller.”**

Sedan arbetar maskineriet under ytan.

Du kanske får tillbaka:

> Hypotes H3 vann evalueringen.  
> 17 sidor påverkades.  
> Median LCP förbättrades 18 %.  
> Regression suite: PASS.  
> Independent verification: PASS.  
> PR #481 redo för owner review.

Det är den upplevelsen vi investerar i.

### Det verkligt stora steget kommer dock efter det

När Nortropic inte bara exekverar sådant **du hittar på**, utan börjar mata sig själv med arbete:

```text
               OMVÄRLD
                  ↓
          Research / Signals
                  ↓
             Knowledge
                  ↓
             Hypotheses
                  ↓
                Evals
                  ↓
                Tasks
                  ↓
             Nortropic
                  ↓
          Implementation
                  ↓
           Verification
                  ↓
             Production
                  ↓
             Telemetry
                  ↓
           New knowledge
                  ↺
```

Där får vi den självförbättrande loop vi har pratat om.

Då blir exempelvis en ny Anthropic-artikel, ett intressant GitHub-repo eller en ny agentteknik inte bara något du och jag läser.

Systemet kan i princip fråga:

> Har detta någon relevans för oss?

Sedan:

> Kan vi falsifiera eller validera idén?

Sedan:

> Ger den mätbar förbättring?

Och om ja:

> Implementera den under våra regler.

**Det är den Nortropic jag tror du egentligen har varit på väg mot hela tiden.**

---

## En annan sak jag tror kommer överraska

Den stora vinsten kommer förmodligen inte vara att Claude “kodar snabbare”.

Det är för litet.

Den stora vinsten är att **din egen uppmärksamhet slutar vara systemets scheduler**.

Idag finns mycket implicit tillstånd i dig:

- vad som ska göras härnäst,
- vad som är blockerat,
- vad Codex väntar på,
- vad Claude borde fortsätta med,
- vilken verifiering som saknas,
- vilken idé vi diskuterade,
- vad som behöver följas upp.

Det är ett enormt osynligt arbete.

När Nortropic är fungerande flyttas det till systemet.

Du går från:

**operator**

till:

**owner / architect / governor.**

Det är förmodligen den största transformationen.

---

# Och därför tycker jag att längden börjar bli begriplig

Tänk om någon 2025 hade sagt:

> “Jag ska bygga ett script som anropar Claude.”

Då hade månader varit vansinne.

Men om beskrivningen istället hade varit:

> “Jag ska bygga ett provider-neutralt, resumable, fail-closed autonomous engineering control plane som kan köra långvarigt mjukvaruarbete, separera produktion från verifiering, hålla exakt execution authority, återhämta sig efter fel och så småningom kontinuerligt förbättra företagets egna system.”

Då hade man från början tänkt:

**det här är ett riktigt infrastruktursystem.**

Det är den senare beskrivningen som har blivit sann.

---

Och jag vill lägga till en sista nyansering till ditt **“vi är väl nära slutmålet”**:

### Ja:
Vi verkar vara nära **bootstrapens avgörande slutpunkt** — där vi kan gå från att bevisa själva maskinen till att använda den för riktigt autonomt arbete.

### Nej:
Vi är inte nära någon punkt där Nortropic är “färdigutvecklat”.

Men det är bra.

Efter bootstrap behöver förbättringar ske **genom Nortropic**, inte genom att vi fortsätter bootstrappa Nortropic.

Det är den fasövergången jag väntar på.

Och om den fungerar som arkitekturen är tänkt, tror jag faktiskt att upplevelsen kan bli ganska dramatisk:

> **Under månader har vi matat arbete *in i maskinen*.**
>
> **Efter tröskeln börjar maskinen ge oss arbete tillbaka som redan är genomfört, testat, verifierat och dokumenterat.**

Då blir alla dessa märkliga R-rundor plötsligt väldigt begripliga i backspegeln. memcite

---

## Meddelande 8 — Johnny (användare)

Hur ser våran planering ut efter bootstrap

---

## Meddelande 9 — ChatGPT (assistent)

Efter bootstrap skulle jag dela upp vår plan i **fyra tydliga faser**. Det viktiga är att vi inte fortsätter “bygga bootstrap” efter att den gjort sitt jobb.

### 1. Freeze + första riktiga autonoma arbetet
Direkt när bootstrapen är grön:

- frys bootstrap v1 som en referensbaseline,
- dokumentera exakt vilka invariants den garanterar,
- kör **supervisor-resume**,
- gör den första riktiga autonoma produkt-runnen,
- låt systemet gå hela vägen: task → builder → verifier → remediation → färdigt resultat,
- mät hur mycket mänsklig handpåläggning som faktiskt behövdes.

Det här blir ögonblicket då vi går från **“kan maskinen fungera?”** till **“kan maskinen producera värde?”**

### 2. Gör Claude till normal arbetsmotor
När första riktiga runnen fungerar skulle jag gå vidare med providerlagret:

- Claude Code som primär/default worker,
- Codex som alternativ, verifierare eller specialist där den ger bättre resultat,
- provider-neutral result core,
- routing utifrån tasktyp, kostnad, kvalitet och tillgänglig usage,
- samma Nortropic-kontrakt oavsett vilken modell som arbetar.

Det är viktigt eftersom Nortropic då inte blir “ett Claude-system” eller “ett Codex-system”.

Det blir ett **agent operating layer** där modellerna är utbytbara motorer.

### 3. Börja använda Nortropic på riktigt
Sedan skulle jag medvetet sluta göra bootstrap-taskar och mata systemet med verkligt Nortropic-/Verkstadsgolvet-arbete.

Exempelvis:

- förbättringar av våra webbprodukter,
- UX,
- SEO,
- performance,
- interna verktyg,
- dokumentation,
- tester,
- refactors,
- buggar,
- nya capabilities.

Här börjar vi bygga upp en faktisk **production history**.

Och varje run ger oss data:

`Task → plan → actions → failures → remediation → verifiering → outcome`

Det materialet blir senare enormt värdefullt för att förbättra själva systemet.

---

## 4. Bygg den självförbättrande Nortropic-loopen

Det här ser jag egentligen som **Nortropic Phase 2**.

Vi har redan börjat bygga komponenterna runt omkring genom knowledge-repot, innovation intake och vår frontier-bevakning.

Målet blir att koppla ihop dem:

```text
Omvärldsbevakning
        ↓
Signal / idé
        ↓
Research
        ↓
Hypotes
        ↓
Eval / experiment
        ↓
Backlog task
        ↓
Nortropic execution
        ↓
Independent verification
        ↓
Production
        ↓
Telemetry / outcome
        ↓
Knowledge
        ↺
```

Det är här Nortropic börjar bli något mycket mer än en kodagent.

En ny Anthropic-paper, ett intressant GitHub-projekt eller en observation från våra egna system kan automatiskt bli:

> “Den här tekniken skulle potentiellt minska våra agent failures med 15 %. Kör ett isolerat experiment.”

Om experimentet inte håller → parkera.

Om det håller → skapa implementation.

Om implementationen passerar verification → inför.

Det är den **autonoma R&D-motorn** vi har pratat om.

---

# Sedan kommer skalningen

När vi bevisat att en workstream fungerar skulle jag inte omedelbart lägga på 50 agenter.

Jag skulle skala kontrollerat:

**1 autonom lane**

→ **3 parallella lanes**

→ **flera förvaltningar**

→ **hela Nortropic**

Där kommer din kommunmetafor tillbaka.

Nortropic kan då se ungefär ut så här:

```text
                         OWNER
                           │
                     NORTROPIC
                   CONTROL PLANE
                           │
          ┌────────────────┼────────────────┐
          │                │                │
      WEB / UX          R&D / AI        INTERNAL OPS
          │                │                │
    Verkstadsgolvet    Research Loop     Automation
          │                │                │
       Agents            Agents            Agents
```

Varje “förvaltning” kan ha:

- egen backlog,
- egna policies,
- egna evals,
- egna agentspecialister,
- egna kvalitetskrav,

men styrs av samma Nortropic-kärna.

---

## Och därefter kommer det jag tycker är mest intressant

**Nortropic förbättrar Nortropic.**

Men med samma regler som allt annat.

Inte:

> Agenten får skriva om sitt eget system hur som helst.

Utan:

> Research upptäcker förbättring → experiment → verifiering → candidate → independent review → kontrollerad promotion.

Då får vi en säker form av rekursiv förbättring.

Det skulle exempelvis kunna upptäckas att:

- en viss promptstruktur orsakar retries,
- en modell är bättre för frontendarbete,
- en annan är bättre som verifierare,
- vissa tasks borde delas mindre,
- ett nytt Claude Code-feature minskar context waste,
- en open-source harness har en bättre scheduling-algoritm.

Och systemet kan självt föreslå och testa förbättringen.

---

# Så jag ser roadmapen ungefär så här

```text
NU
│
├── Bootstrap closeout
│
▼
Autonomous Kernel v1
│
├── First real autonomous run
│
▼
Production Autonomy
│
├── Claude-default / provider neutrality
│
├── Real Nortropic work
│
├── Metrics + evals
│
▼
Multi-lane Autonomy
│
├── Web / Verkstadsgolvet
├── Internal tooling
├── Knowledge
├── R&D
│
▼
Continuous Improvement Loop
│
├── Frontier monitoring
├── Research
├── Experiments
├── Automated proposals
│
▼
Self-improving Nortropic
```

Och sedan finns en ännu senare nivå:

### **Nortropic som företagets operativsystem**

Då handlar det inte längre primärt om kod.

Samma kontrollplan kan potentiellt orkestrera:

research, produktutveckling, design, QA, dokumentation, kundarbete, marknadsanalys, drift och interna förbättringar.

Det är därför jag tycker att **Verkstadsgolvet är första förvaltningen**, snarare än själva slutprodukten.

Den stora planen efter bootstrap är alltså inte att börja bygga ännu ett enormt fundament.

Det är att börja **lägga verksamhet ovanpå fundamentet**.

Och därifrån ska varje nytt lager helst göra systemet mer användbart och mer självgående — inte bara mer tekniskt sofistikerat. memcite

