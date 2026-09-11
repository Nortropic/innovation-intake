# Informationsarkitektur och nootropika — fullständigt transkript

**Källprojekt:** Improvements (ChatGPT-projekt)
**Chatt:** Informationsarkitektur och nootropika
**URL:** https://chatgpt.com/c/6a9ec9bd-0a38-83eb-b792-5db45b2678f9
**Exportdatum:** 2026-09-11
**Antal meddelanden:** 20 (7 användare, 13 assistent)
**Syfte:** Fångad i PROJECT_SWEEP Improvements R39 (data-layer, WYSIWYG-filtrerad); syftet med samtalet avgörs av dess innehåll, inte av denna rubrik.

**Innehåll i korthet:** Samtalet öppnar med: ”Brainstorma nortropics sfärer hur de påverkar varandra, om en gör så, påverkar de så, se över samband. Även informationsartiketuren, den strukturella utformningen av informationsmiljöer.   En växande ” och avslutas med: ”**Jag har nu färdigställt själva workerprovet: 12 uppgifter, bevarade källor, separat facit och en samlad körinstruktion.** Det som återstår är att köra jämförelsen med riktiga workers och hela Wigolo”

> Notis: rader som ser ut som käll-/citat-chips från ChatGPT är en del av
> originaltexten och har bevarats ordagrant. 3 bilagor inventerade (data-layer: distinkta plattforms-fil-id ur metadata.attachments + icke-textdelar; en bild som adaptern listar två gånger räknas en gång); bytes registreras separat via register-attachment där plattformen exponerar dem.

---

## Meddelande 1 — Johnny (användare)

Brainstorma nortropics sfärer hur de påverkar varandra, om en gör så, påverkar de så, se över samband. Även informationsartiketuren, den strukturella utformningen av informationsmiljöer. 

En växande disciplin och praktisk gemenskap med fokus på att föra principer för design och artiketur. 

Jag tänker projekt och innovationskontoret som vi pratade om chatten nyligen, Informationsartitektur, vedertagna processlösningar till projekt och innovation. Arbetsflöde, workflows, use cases, suggest next interaction, utvecklingsprocess, cykler, design council UK, double diamond.  

En organisation behandlar information, hur nyttiggör vi sig av kunskapen? Effektivsera sökandet och återskapandet av kunskap genom god struktur kring hur informations sparas och hanteras. 

Informationsmiljöer, den strukturella utformningen av detta genom organisationssystem (klassificering), Representationssystem (referens/märkning), Navigationssystem och söksystem. 

En framväxande disciplin  och praktikgemenskap med fokus på att föra principer för design och arkitektur framåt. Jag tänker tex hur våra workers navigerar på ett smart sätt information och söker.

---

## Meddelande 2 — Johnny (användare)

Brainstorma vidare Informationartiketuren behöver vara bra så man inte spenderar mycket av "arbetstiden" åt att söka eller återskapa som vi vill ha till att analysera och ta beslut på.

Tid går åt att samla information. Här tänker jag på Annas Archive, se bild.

La även till bilder för projekt/innovations kontoret kontext

---

## Meddelande 3 — ChatGPT (assistent)

Jag kopplar ihop sfärerna och informationsflödena med projekt- och innovationskontoret och undersöker etablerade metoder för kunskapshantering och smart worker-navigation.

---

## Meddelande 4 — ChatGPT (assistent)

iturn873909image0

**Ja. Jag tycker att vi ska designa Nortropics arbetsflöden och informationsarkitektur tillsammans — inte först skapa en organisation och sedan försöka ordna dess dokument.**

Det du pekar på handlar om mer än sökning och lagring:

> **Hur blir en människas idé till ett begripligt problem, ett genomtänkt uppdrag, verifierat arbete och kunskap som förbättrar nästa uppdrag?**

Min huvudhypotes är att **informationsarkitekturen bör vara den gemensamma strukturen mellan sfärerna**, medan projekt- och innovationskontoret är en verksamhet som använder den strukturen för att utforska och forma uppdrag.

Det betyder inte en enda databas, ett centralt kontor som måste passeras för allt eller att varje worker ska läsa samma material. Det betyder **sammanhängande begrepp, spårbara samband och tydliga vägar till rätt information**.

Nedan beskriver jag ett tänkt samspel att pröva inför Recompile, inte funktioner som jag påstår redan är byggda.

## 1. Informationsarkitektur är en stark grund för det vi försöker åstadkomma

Din formulering ligger nära Information Architecture Institutes definition: att strukturera gemensamma informationsmiljöer så att människor kan förstå dem och hitta det de behöver. Formuleringen om en ”framväxande praktikgemenskap” finns i deras material från 2013; själva disciplinen har alltså en längre historia. **Vår särskilda tillämpning är att även autonoma workers ska kunna orientera sig i miljön.** citeturn138535view2

Jag skulle skilja mellan tre frågor:

**Organisationsarkitektur:** Vilka funktioner behöver Nortropic utföra, och vem ansvarar för vad?

**Informationsarkitektur:** Vilka saker behöver organisationen förstå, hur beskrivs de och hur hittar man mellan dem?

**Processarkitektur:** Hur förs ett arbete framåt, vilket underlag behövs och vad får nästa steg att börja?

De måste hänga ihop. Ett exempel:

Om processen säger ”gå vidare när idén är validerad”, men informationsmodellen inte skiljer mellan en lovande hypotes, ett genomfört test och ett faktiskt kundutfall, då blir ”validerad” bara en etikett.

**En bra process kräver att informationsmiljön kan representera det processen påstår sig veta.**

---

## 2. Sfärerna bör förstås genom vad de utbyter

För den här analysen skulle jag gruppera funktionerna så här. Det är analyslinser över våra befintliga resonemang, inte ett förslag om sju nya subsystem.

| Sfär | Huvudfråga | Vad den behöver från andra — och ger tillbaka |
|---|---|---|
| **Riktning och Owner Plane** | Vad vill du åstadkomma, och vilka avvägningar accepterar du? | Tar emot begriplig verklighetsbild; ger mål, prioriteringar och verkliga ägarbeslut. |
| **Projekt- och innovationskontoret** | Vilket problem bör vi arbeta med, och vilket uppdrag är motiverat? | Tar emot idéer, omvärld och erfarenheter; ger problemformuleringar, experiment och uppdragsunderlag. |
| **Organization OS och orkestrering** | Hur omsätter vi uppdraget i genomförbart arbete? | Behöver mål, beroenden, kapacitet och kvalificerade förmågor; ger arbetsfördelning och framdrift. |
| **Förvaltningar och workers** | Hur utför vi arbetet professionellt? | Använder relevanta metoder och underlag; producerar resultat, observationer och upptäckta kunskapsluckor. |
| **Kunskap och context** | Vad vet vi, varför tror vi det och vad behöver just detta arbete veta? | Förbinder källor, beslut, erfarenheter och tillämpningar; ger uppgiftsanpassat underlag. |
| **Assurance och utfallsuppföljning** | Håller resultatet, och åstadkommer det avsedd nytta? | Behöver kriterier och bevis; ger verifiering, motbevis, avvikelser och utfallsbild. |
| **Evolution och förmågeutveckling** | Vilka arbetssätt eller förmågor behöver förbättras? | Tar emot återkommande problem och externa möjligheter; ger prövade förbättringskandidater. |

**Trust Kernel är en genomgående rättighetsgrund**, inte ytterligare en kunskapsproducerande avdelning. Resurser, kostnad och din uppmärksamhet begränsar hur mycket organisationen bör sätta i rörelse.

Aquarium/Verkstadsgolvet blir sedan ett sätt att se och navigera detta. Det passar den tidigare principen att gränssnittet ska visa underliggande verklighet, inte skapa en konkurrerande version av den. fileciteturn0file1

### Den viktigaste strukturella slutsatsen

**Jag skulle inte placera hela kunskapsarkitekturen inne i projekt- och innovationskontoret.**

Kontoret ska kunna använda och förbättra kunskapen, men Digitala måste också kunna återanvända erfarenheter direkt. Assurance måste kunna gå tillbaka till ursprungliga underlag. Evolution måste kunna se återkommande mönster utan att någon först skriver en särskild kontorsrapport.

Kontoret formar uppdrag. Informationsarkitekturen håller ihop förståelsen.

---

## 3. ”Om en gör så, påverkas de andra så” — de viktigaste sambanden

Här blir sfärkartan användbar. Vi bör inte bara rita kopplingar, utan beskriva **mekanismen bakom påverkan**, risken och vilken återkoppling som behövs.

### A. Bättre informationsstruktur kan frigöra verklig kapacitet

Min hypotes för Nortropic är:

**Tydligare begrepp och källor → mindre orienteringsarbete → färre felaktiga antaganden → mindre omarbete → mer kapacitet till nyttigt arbete.**

Det betyder att ett informationsarkitekturproblem lätt kan se ut som ett modellproblem.

En worker kanske inte behöver en ”smartare hjärna”. Den kanske behöver kunna skilja mellan den aktuella metoden, en gammal diskussion om metoden och en förkastad alternativlösning.

Detta bör prövas innan vi svarar på varje återkommande misslyckande med fler agenter eller längre instruktioner.

### B. Snabbare genomförande kan försämra hela flödet

Anta att vi fördubblar byggkapaciteten, men inte verifieringskapaciteten.

Då kan vi få fler påbörjade uppdrag, längre granskningsköer och fler resultat som hinner bli inaktuella innan de blir färdiga. Den relevanta frågan blir därför inte bara hur många workers vi kan starta, utan **hur mycket arbete hela kedjan kan färdigställa**.

Kanban erbjuder etablerade principer för detta: definiera arbetsflödet, kontrollera pågående arbete och följa genomströmning, arbetsobjektens ålder och cykeltid. citeturn503817view2

**Nortropic-konsekvens:** orkestrering, verifiering och resursfördelning behöver samordnas runt samma arbetsidentitet. Annars kan varje sfär optimera sin egen aktivitet medan helheten blir långsammare.

### C. Mer research kan skapa mer belastning — inte mer innovation

Mer omvärldsbevakning ger fler möjliga idéer. Men om varje fynd blir ett förbättringskrav hamnar kontoret och Evolution i ständig omplanering.

Jag skulle därför skilja mellan:

> ”Detta är intressant” → ”detta berör oss” → ”detta är värt att testa” → ”detta bör förändra vårt arbetssätt”.

Det är fyra olika påståenden.

En extern metod ska kunna påverka vår hypotesbild utan att automatiskt påverka pågående uppdrag. **Upptäckt är inte införande.**

### D. Verifiering behöver kunna ändra problemformuleringen

Anta att Digitala levererar en tekniskt korrekt webbplats, men användarna fortfarande inte förstår erbjudandet.

Då kan återkopplingen behöva gå till projektkontorets problemformulering eller innehållsstrategi — inte bara tillbaka till en worker med instruktionen ”förbättra sidan”.

Det passar ditt tidigare Digitala-underlag, där kvalitet före lansering uttryckligen skiljs från faktisk nytta efter lansering. fileciteturn0file0

Här finns två olika förbättringsfrågor:

**Utförde vi den valda lösningen tillräckligt bra?**

**Var den valda lösningen över huvud taget rätt svar på problemet?**

Nortropic behöver kunna ställa båda.

### E. Förmågeutveckling påverkar vilka projekt som blir möjliga

Om en återkommande uppgift blir billigare och mer tillförlitlig genom en kvalificerad förmåga kan projektkontoret börja överväga uppdrag som tidigare var opraktiska.

Om samma förmåga senare visar sig fungera dåligt i en viss miljö ska det omvänt kunna begränsa framtida planering och routing.

Det är en dubbelriktad relation:

**Projekt skapar behov av förmågor. Förmågor förändrar projektens möjlighetsrum.**

Men en förmåga som fungerar för Digitalas webbprojekt ska inte automatiskt betraktas som kvalificerad för alla andra verksamheter.

### F. En felaktig etikett kan sprida sig genom hela systemet

Tänk att ett AI-genererat resonemang felaktigt märks som ett antaget beslut.

Det kan därefter väljas av söksystemet, hamna i ett contextpaket, styra en worker och återkomma i en rapport som ”befintlig princip”.

Därför är märkning inte kosmetik. **Skillnaden mellan förslag, beslut, observation och verifierat resultat måste överleva varje överlämning.**

Samtidigt ska en korrigering inte få hela Nortropic att börja om. Den bör identifiera vilka härledda slutsatser och aktiva arbeten som faktiskt berörs.

**Påverkad betyder ”behöver omprövas”, inte automatiskt ”är fel”.**

---

## 4. Projekt- och innovationskontoret: en sammanhängande arbetsmiljö

I den senaste arbetshypotesen beskrev vi kontoret som en beständig tänkande miljö: rå avsikt blir forskning, utmanade antaganden, experiment, evidens och så småningom ett uppdragsunderlag.

Jag skulle nu förtydliga det till **två perspektiv på samma ärende**:

**Innovationsperspektivet** undersöker vad som är värt att göra och vilka antaganden som måste prövas.

**Projektperspektivet** håller ihop syfte, omfattning, beroenden, resurser, leverans och uppföljning.

Vi behöver inte två separata organisationer som skickar dokument mellan sig. Samma projekt kan innehålla både utforskande och genomförande arbete, men med tydligt olika kunskapsstatus.

Intake förblir då infrastruktur för att fånga och spåra material — inte automatiskt en prioriteringsmotor eller en ordergivare.

### Double Diamond passar här — men inte som ett stelt faslås

Design Councils Double Diamond skiljer mellan att bredda och avgränsa förståelsen av problemet, och att bredda och avgränsa möjliga lösningar. De betonar också att processen inte är linjär: tidiga tester kan leda tillbaka till problemförståelsen. citeturn138535view0

Så här skulle jag översätta det till Nortropic:

| Perspektiv | Fråga för kontoret | Lämpligt underlag |
|---|---|---|
| **Discover — utforska** | Vad händer egentligen, och för vem är det ett problem? | Observationer, behov, befintlig kunskap och osäkerheter. |
| **Define — avgränsa** | Vilket problem väljer vi att försöka lösa? | Problemformulering, avgränsning och önskat utfall. |
| **Develop — utveckla alternativ** | Vilka olika lösningar skulle kunna fungera? | Alternativ, prototyper, hypoteser och testresultat. |
| **Deliver — pröva och förfina** | Vilken lösning håller i användning? | Leverans, verifiering, återkoppling och fortsatt förbättring. |

**Min tillämpning skulle inte vara att alla uppgifter måste passera fyra administrativa stationer.**

En känd bugg kan gå genom ett kort reparationsflöde. En oklar kundidé behöver mer problemutforskning. En möjlig ny förvaltning behöver prövas utifrån återkommande behov och verklig nytta.

Metoden bör väljas efter **osäkerhet och konsekvens**, inte efter en obligatorisk mall.

### Systemic Design är särskilt relevant för sfärernas samband

Design Council har också ett *Systemic Design Framework*. Det behåller det divergerande och konvergerande tänkandet men lyfter bland annat orientering, relationer och fortsättningen efter ett projekt. Ramverket har utvecklats för komplexa samhälls- och miljöutmaningar, inte för agentplattformar. citeturn803282view0

Min överföring till Nortropic är ändå tydlig:

**Double Diamond hjälper oss att utveckla ett uppdrag. Systemiskt tänkande hjälper oss att bedöma vad uppdraget förändrar runt omkring sig.**

En lokal processförbättring kan exempelvis minska byggtid men öka granskningskostnad. Den bör då bedömas som en förändring av hela flödet, inte bara som en framgång för byggsfären.

---

## 5. De fyra informationssystemen — konkret för Nortropic

Organisation, märkning, navigation och sökning är etablerade delar av informationsarkitektur. Rosenfeld och Morvilles arbete behandlar dem som sammanhängande system, inte som fristående gränssnittsfunktioner. citeturn138535search20

### A. Organisationssystem: ordna efter betydelse, inte bara efter avdelning

Jag skulle undvika att göra organisationsschemat till hela informationsstrukturen:

```text
Projektkontoret/
Digitala/
Research/
Evolution/
```

Det kan vara användbara ingångar, men är otillräckligt som enda ordning.

Ett experiment om offertformulär kan samtidigt vara relevant för ett kundprojekt, en UX-metod, en kvalitetskontroll och en återkommande förmåga. Fyra kopior skapar fyra underhållsproblem.

Bättre är att informationen kan förstås genom flera egenskaper:

**Vad är detta?** En källa, hypotes, observation, beslut, metod eller ett resultat?

**Vad berör det?** Ett visst projekt, en förvaltning, en kundmiljö eller en gemensam förmåga?

**Vilken status har det?** Oprövat, motsagt, antaget för ett visst sammanhang eller ersatt?

**När gäller det?** Historiskt, aktuellt under vissa förutsättningar eller ännu inte infört?

Det blir flera vägar till samma underlag, inte flera konkurrerande underlag.

En viktig begränsning: vi ska inte heller skapa ett enda generiskt ”allt-objekt” som försöker beskriva hela världen. **Gemensamma identiteter och relationer kan kombineras med domänspecifikt innehåll.**

### B. Representations- och märkningssystem: skilj namn från identitet

En worker behöver kunna förstå att ”evidens” och ”evidence” kan beteckna samma begrepp, samtidigt som ”uppgift” och ”körförsök” faktiskt är olika saker.

W3C:s SKOS ger en etablerad modell för identifierade begrepp, föredragna och alternativa benämningar samt bredare, smalare och relaterade begrepp. Det är användbar inspiration utan att vi därmed måste införa en fullständig semantisk webbplattform. citeturn744873view0

Mitt förslag är en liten gemensam begreppsgrund där viktiga poster har en stabil identitet, begriplig benämning, typ, relevant status och hänvisningar till sitt ursprung.

För härledda slutsatser behövs dessutom spårbarhet:

> Vilka källor användes, vilka versioner och genom vilken bearbetning uppstod slutsatsen?

W3C:s PROV-modell behandlar just ursprung, bearbetningsaktiviteter, ansvar och härledning. **Sådan spårbarhet gör ett påstående granskningsbart; den bevisar inte i sig att påståendet är sant.** citeturn744873view1

Jag skulle också hålla isär fyra frågor som annars lätt blandas ihop:

**Vad vill du?** Det behöver spåras till relevant ägaravsikt eller beslut.

**Vad får systemet göra?** Det avgörs av gällande rättigheter och mandat.

**Vad är faktiskt byggt eller utfört?** Det behöver stöd i aktuell systemverklighet.

**Vad verkar fungera?** Det behöver stöd i verifiering och tillämpliga observationer.

Det finns ingen enda dokumentrangordning som besvarar alla fyra.

### C. Navigationssystem: gör relationerna användbara

Bra navigation för en worker är inte bara en mappförteckning.

Den ska kunna följa:

```text
Uppdrag → mål → beslut → underbyggande påstående → evidens → råkälla
```

Och i andra riktningen:

```text
Ändrad förutsättning → berörda metoder → aktiva uppdrag → relevanta kontroller
```

Jag skulle vilja ha tre huvudsakliga sätt att orientera sig:

**Överblick:** Vad är detta projekt, var befinner det sig och var finns dess viktiga underlag?

**Lokal arbetsnavigation:** Vad behöver jag för uppgiften jag utför nu?

**Sambandsnavigation:** Varför valdes detta, vad beror det på och vad påverkas av en ändring?

Då kan en worker gå direkt från en föreslagen lösning till varför en liknande lösning tidigare förkastades.

Men relationerna behöver skilja sig åt. ”Handlar om samma ämne” är inte samma sak som ”är beroende av”. ”Stöder påståendet” är inte samma sak som ”orsakar utfallet”.

**En graf med många länkar är inte automatiskt en bra förklaringsmodell.**

### D. Söksystem: olika frågor behöver olika sökbeteenden

Jag skulle åtminstone skilja mellan två användningslägen.

**Operativ sökning:** Vilket underlag gäller för det här arbetet i den här miljön?

**Utforskande sökning:** Vad har vi undersökt, vilka alternativ finns och vad motsäger vår nuvarande uppfattning?

Det första behöver tydlig tillämplighet och aktuell status. Det andra måste också kunna hitta historiska resonemang, förkastade lösningar och negativa resultat.

Min föreslagna sökstrategi är därför inte ”lägg allt i en vektordatabas”.

Den bör kombinera direkta uppslag via identitet och referenser, filtrering på sammanhang, exakt textsökning och — där det faktiskt hjälper — semantisk sökning efter liknande betydelse.

**Åtkomstkontroll ska avgöra vad workern får se innan material lämnas till modellen.** Relevanspoäng får inte kompensera för saknad behörighet.

Ett användbart sökresultat bör dessutom visa varför det är relevant, vilken källa och version det kommer från, var det gäller och om det finns kända reservationer.

Och: **”inget hittat” måste kunna förbli en kunskapslucka.** Det får inte omvandlas till ett självsäkert antagande.

---

## 6. Workern behöver en karta och ett arbetsunderlag — inte hela organisationens minne

Här finns en tydlig koppling till praktisk agentutveckling.

OpenAI beskriver i sitt harness-engineering-arbete hur ett stort instruktionsdokument ersattes av en kortare ingång som pekar vidare till strukturerad, versionerad dokumentation. Det är ett konkret utvecklingsexempel, inte bevis för att samma lösning är optimal överallt. citeturn744873view2

Anthropic beskriver på liknande sätt stegvis informationsinhämtning: lätta referenser, information som hämtas när den behövs och en avvägning mellan förberett underlag och agentens egen utforskning. De framhåller också att mer sökning under körning kan kosta tid och leda fel utan bra verktyg. citeturn138535view1

### Så skulle det kunna fungera i Digitala

En worker får uppdraget:

> Förbättra kundens offertflöde.

Den bör börja med ett begränsat men tillräckligt arbetsunderlag: avsett utfall, målgrupp, nuvarande lösning, tillämpliga kvalitetskrav, relevanta tidigare observationer och vilka ändringar uppdraget omfattar.

Därifrån kan den navigera vidare.

Behöver den förstå varför ett formulärfält finns? Följ det beslutet.

Behöver den bedöma en tidigare testslutsats? Öppna experimentets underlag.

Upptäcker den en motsägelse? Dokumentera den och sök den källa som faktiskt kan avgöra frågan.

Det centrala är:

> **Context är inte en hög med dokument. Det är ett arbetsunderlag sammanställt för en bestämd uppgift, med vägar tillbaka till källorna.**

Vid överlämning behöver nästa worker inte ärva hela föregångarens textflöde. Den behöver kunna återfinna arbetsläget, besluten, bevisen och det som fortfarande är osäkert.

Samtidigt får ett sparat arbetsunderlag aldrig återuppliva gamla rättigheter. Gällande mandat behöver fortfarande respekteras när handlingen utförs.

---

## 7. Hur kunskap blir användbar — och inte bara sparad

Här tycker jag att KCS är en särskilt relevant etablerad inspirationskälla.

I KCS beskrivs kunskap som något som återanvänds, förbättras och fångas under arbetet. Dess *Solve Loop* hanterar den konkreta situationen, medan *Evolve Loop* använder mönster från flera situationer för vidare förbättring. citeturn875430view3

För Nortropic skulle jag översätta det så här:

**Ett arbete använder befintlig kunskap, testar dess användbarhet och lämnar tillbaka en förbättring när något nytt faktiskt har framkommit.**

Inte:

> Alla workers måste skriva en efterrapport som någon annan kanske läser.

Utan exempelvis:

> Den befintliga instruktionen fungerar bara under dessa förutsättningar. Här är det nya fallet, vad som prövades och vilket underlag som motiverar en korrigering.

KCS-principen *reuse is review* handlar just om att granskning och förbättring sker i samband med användning. citeturn503817view0

### Kunskapen behöver ha en tillämpningsyta

En erfarenhet blir mer användbar när den svarar på:

**I vilken situation bör jag tänka på detta? Vad bör jag göra annorlunda? Vad talar emot att använda det här?**

”Kortare formulär är bättre” är för generellt.

En användbar observation skulle i stället kunna beskriva en viss målgrupp, vilket problem formuläret hade, vad som ändrades, vad som observerades och vad som fortfarande är osäkert.

Det är också viktigt att inte förväxla:

**återanvändning med bekräftelse**,  
**popularitet med kvalitet**,  
**flera sammanfattningar med flera oberoende bevis**.

Tio workers som upprepar samma svaga källa har inte skapat tio nya stöd.

Ditt tidigare Improvements-underlag har redan en viktig grund här: råkällor ska kunna överleva den aktuella syntesen, så att materialet går att tolka om senare. Jag skulle förena det med tydliga åtkomst- och bevaranderegler, medan sammanfattningar och sökindex behandlas som härledda representationer. fileciteturn0file2

---

## 8. ”Suggest next interaction” bör betyda nästa nyttiga förflyttning

Här ser jag en mycket bra funktion för projekt- och innovationskontoret — men den bör inte optimeras för att hålla igång en chatt.

Min målbild är:

> **Föreslå nästa steg som mest sannolikt förbättrar beslutet eller för arbetet mot avsett utfall, med rimlig kostnad och risk.**

Nästa interaktion behöver alltså inte vara med dig. Den kan vara en sökning, ett test, en jämförelse, ett verktygsanrop, en överlämning eller ett beslut att parkera spåret.

Exempel:

**När behovet är oklart:** undersök vilken användarsituation som faktiskt är problematisk, i stället för att generera fler lösningar.

**När problemet är tydligt men lösningen osäker:** gör ett avgränsat test mellan de viktigaste alternativen.

**När lösningen redan är kvalificerad:** återanvänd den och genomför arbetet, i stället för att öppna en ny innovationscykel.

**När samma fel återkommer:** undersök metod, informationsunderlag eller förmåga — inte bara det senaste körförsöket.

Ett förslag skulle exempelvis kunna lyda:

> **Nästa rekommenderade steg:** kontrollera vad som händer i det befintliga offertflödet innan vi designar om det.  
> **Skäl:** vi vet ännu inte om problemet är få besökare, låg förståelse eller avbrutna formulär.  
> **Förväntat resultat:** ett underlag som avgör vilken typ av förändring som är motiverad.

Det bör vara tydligt vilken osäkerhet steget adresserar och vad resultatet kommer att möjliggöra.

**Rekommendationen ger däremot ingen ny behörighet.** Finns mandat och tillräckligt underlag bör arbetet kunna fortsätta. Krävs ett verkligt vägval om mål eller avvägningar ska frågan komma till dig.

Det bevarar skillnaden mellan att påkalla din uppmärksamhet och att kräva ditt tillstånd.

---

## 9. Vi behöver olika förbättringscykler — inte en enda stor självförändringsloop

Jag skulle skilja mellan tre rytmer.

**Arbetscykeln** löser det aktuella uppdraget: förstå, agera, verifiera och korrigera.

**Kunskaps- och förmågecykeln** undersöker återkommande erfarenheter: behöver en metod, ett arbetsunderlag, en kontroll eller en förmåga förbättras?

**Organisationscykeln** granskar mer grundläggande mönster: ligger ansvar fel, är prioriteringen dålig eller skapar informationsstrukturen onödigt arbete?

Skillnaden spelar roll. En enskild misslyckad sökning ska normalt inte utlösa organisationsombyggnad. Ett återkommande mönster av felaktiga överlämningar kan däremot motivera en sådan prövning.

Och alla förbättringar ska inte fortplanta sig lika snabbt.

En rättad sakuppgift kan behöva nå ett aktivt uppdrag omedelbart. Ett nytt arbetssätt kan behöva kvalificeras före bred användning. En ändrad målbild kräver att du faktiskt har valt den.

**Informationsarkitekturen behöver därför beskriva både samband och förändringskonsekvens — inte bara innehåll.**

---

## 10. Hur vi prövar detta utan att bygga en informationsbyråkrati

Jag skulle börja med tre sammanhängande användningsfall:

1. **Återuppta ett projekt.** Kontoret ska kunna hitta syftet, tidigare alternativ, fattade beslut och öppna frågor utan att göra om hela brainstormingen.
2. **Utföra en uppgift med rätt kunskap.** En ny worker ska hitta tillämplig metod och relevant evidens, även när det finns en övertygande men inaktuell version.
3. **Hantera en ändrad förutsättning.** Systemet ska identifiera vilka metoder, slutsatser och pågående arbeten som berörs — utan att dra in allt annat.

Sedan skulle jag jämföra en enkel baslinje med vanlig dokument- och textsökning mot en version med tydligare begrepp, referenser och navigation. Mer avancerad semantisk sökning får motiveras av att den förbättrar verkliga uppgifter.

Mätningen bör omfatta **korrekt återfinning, korrekt användning, tid till tillräckligt underlag, omarbete, kostnad och onödiga frågor till dig**. Även underhållet av strukturen måste räknas in.

Testfallen bör innehålla motsägelser, ersatta beslut, otillräcklig evidens och material utanför workerns åtkomst. Bedömningen ska utgå från förhandsbestämda kriterier, inte bara från att workern själv tycker att svaret blev bra.

En lyckad informationsarkitektur ska göra arbetet både säkrare och smidigare. Den ska inte bara ge oss snyggare mappar.

### Vad jag skulle hålla litet från början

En gemensam begreppsgrund, stabila referenser, tydligt ansvar för olika typer av information, några betydelsefulla relationer och en bra ingång för workers räcker långt som första hypotes.

Vi behöver inte på förhand en stor kunskapsgraf, en permanent biblioteksagent, ett nytt godkännandekontor eller samma omfattande mall för varje anteckning.

Det ligger nära principen i Improvements-underlaget: flera koncept kan vara beteenden i samma livscykel, och Recompile ska härleda de minsta nödvändiga mekanismerna snarare än implementera varje namngiven familj separat. fileciteturn0file2

## Min samlade bedömning

**Projekt- och innovationskontoret, informationsarkitekturen och lärandecyklerna är tre perspektiv på samma centrala förmåga: att göra kunskap verksam.**

Kontoret hjälper Nortropic att välja och formulera rätt problem. Informationsarkitekturen gör underlagen begripliga, sökbara och spårbara. Workers omsätter dem i arbete. Assurance prövar både resultat och antaganden. Erfarenheten går tillbaka till framtida uppdrag och kvalificerad förmågeutveckling.

Den stora möjligheten är därför inte att varje sfär får ett bättre eget minne.

> **Det är att en upptäckt i en sfär kan bli användbar i en annan — utan att förlora sitt sammanhang, överdriva sin giltighet eller kräva att du översätter allt mellan dem.**

Nästa underlag i det här forskningsspåret bör vara **en sammanhållen sambands- och informationskarta över de tre användningsfallen ovan**, där vi följer vilka informationsobjekt som behövs, vem som ansvarar för dem, hur workers hittar dem och vilka förändringar som faktiskt ska fortplanta sig. Det skulle ge Recompile något betydligt mer prövbart än ytterligare ett organisationsschema.

---

## Meddelande 5 — ChatGPT (assistent)

**Ja. Jag tror att du pekar på något som bör hålla ihop Nortropics sfärer — inte bli ytterligare en isolerad sfär.**

Nortropic behöver inte bara kunna **samla information**. Det behöver kunna avgöra:

> **Vad behöver vi veta för att komma vidare, vad vet vi redan, var finns underlaget, vad gäller fortfarande och vilken handling motiverar kunskapen?**

Det är där informationsarkitekturen möter projektkontoret, innovationen, workers, kvalitetssäkringen och lärandet.

Min arbetshypotes är:

> **Nortropics informationsmiljö bör utformas runt arbetet och besluten som ska göras, inte runt dokumenten som råkar finnas.**

Och en viktig precisering av ditt effektivitetsmål: vi bör minska **onödigt sökande, återorientering och återskapande** — inte informationsinhämtning som faktiskt förändrar ett viktigt beslut. Att upptäcka att vi håller på att lösa fel problem kan vara mycket mer värdefullt än att börja bygga omedelbart.

## 1. Bilderna tillför tre olika byggstenar

### Anna’s Archive: gör kunskapen lätt att hitta och nå maskinellt

Jag hittade originalinlägget från **18 februari 2026**. Det skiljer mellan webbplatsens vanliga gränssnitt och särskilda vägar för maskinell åtkomst till bland annat metadata och kod. Den relevanta idén för oss är att en agent inte ska behöva navigera ett människogränssnitt för att upptäcka vilken information som finns och hur den kan hämtas. citeturn530793view0

Men jag skulle skilja mellan två ambitioner:

**Ett omfattande bibliotek** gör mycket material tillgängligt.

**En välutformad arbetsmiljö** hjälper en worker att hitta just det material som behövs, bedöma det och använda det korrekt.

Nortropic behöver framför allt det senare. Ett enormt bibliotek löser inte automatiskt frågan:

> ”Vilka tre källor är relevanta för det beslut vi står inför — och vilken av dem beskriver fortfarande verkligheten?”

`llms.txt` är ett användbart exempel på en maskinläsbar ingång: förslaget beskriver en översikt som hjälper agenter vidare till relevant innehåll. Det är däremot inte i sig ett kvalitetsbevis, en behörighetsmekanism eller en garanti för att agenten hittar rätt. citeturn607449view1

**Min tillämpning för Nortropic:** ha gärna en bred källkatalog, men hämta, bearbeta och underhåll fullständigt material utifrån verkliga behov. För externa samlingar skulle jag också kräva att åtkomst och användning är tillåtna för det avsedda ändamålet.

### Anthropic-bilden: bygg en miljö för tänkande, inte bara ordergivning

I bildtexten lyfts AI som tankepartner och möjligheten att bygga systemet som gör arbetet, snarare än att själv specificera varje arbetsmoment.

För projekt- och innovationskontoret skulle jag översätta det till:

> **Kontoret hjälper dig att upptäcka vad uppdraget borde vara, innan det hjälper organisationen att genomföra det.**

Det ligger nära ett dokumenterat exempel från en intervju om Claude Code: planeringen används för att upptäcka okända faktorer innan byggandet, och längre autonoma arbetsloopar behöver ett verifierbart slutläge. Det stöder arbetssättet, men är inte ett bevis för att varje sorts uppgift kan lämnas över utan tillsyn. citeturn628935view5

### Karpathy-bilden: välj graden av delegering efter uppgiften

Originalintervjun bakom det här resonemanget är från **oktober 2025**. Där beskriver Karpathy bland annat hur han använder autocomplete och hur tester gjorde det tryggare att delegera delar av en Rust-implementation. Jag skulle därför läsa bilden som ett exempel på uppgiftsberoende delegering, inte som en aktuell, generell gräns för AI:s förmåga. citeturn607449view2

För Nortropic blir slutsatsen:

**Samma projekt kan innehålla fri utforskning, nära samarbete och långtgående autonom exekvering.** Informationsmiljön måste stödja samtliga arbetssätt.

---

## 2. Sfärerna bör dela informationsmiljö — men inte blanda ihop ansvar

I vår senaste diskussion beskrev vi projekt- och innovationskontoret som en beständig tankemiljö mellan dig och förvaltningarna: från rå idé, genom research och kritik, till ett spårbart projektuppdrag. Intake blir då infrastrukturen för fångst och ursprung, snarare än hela den upplevelse du möter.

Jag skulle pröva följande funktionella karta. **Raderna är ansvar, inte ett förslag om sex nya tjänster eller permanenta agentgrupper.**

| Sfär eller funktion | Frågan den främst hanterar | Viktigaste informationsutbytet |
|---|---|---|
| **Riktning och prioritering** | Vad är värt att ägna kapacitet åt? | Dina avsikter och avvägningar möter verkliga resultat, kostnader och möjligheter. |
| **Projekt- och innovationskontoret** | Vilket problem ska vi lösa, och vad behöver vi förstå först? | Idéer, tidigare kunskap och research blir hypoteser, experiment eller projektuppdrag. |
| **Genomförande: Supervisor och förvaltningar** | Hur genomför vi uppdraget inom dess mandat? | Uppdrag blir arbete, resultat, avvikelser och upptäckta kunskapsluckor. |
| **Verifiering och verksamhetsutfall** | Fungerar det, och skapade det avsedd nytta? | Tester och observationer återförs till uppdrag, metoder och prioriteringar. |
| **Lärande och Evolution Plane** | Vad bör förändras i vår förmåga eller vårt arbetssätt? | Intern erfarenhet och extern utveckling blir prövbara förbättringsförslag. |
| **Insyn och uppmärksamhet: Aquarium/Verkstadsgolvet** | Vad behöver du förstå eller ta ställning till nu? | Verkligt tillstånd blir begripliga vyer och relevanta uppmärksamhetssignaler. |

**Informationsarkitekturen går genom alla dessa. Trust Kernel sätter gränserna för vad som får läsas, ändras och utföras.**

Projektkontoret bör alltså inte bli en central bibliotekarie som varje worker måste vänta på. Det bör kunna **använda och bidra till samma informationsmiljö** som resten av organisationen.

Det anknyter till Recompile-underlaget: råkällor ska överleva, härledd kunskap ska vara spårbar och flera koncept kan visa sig behöva samma lilla uppsättning grundfunktioner. fileciteturn0file2

### En viktig gräns mellan kontoret och verkstaden

Kontoret håller ihop **varför, vad, kunskapsläge och vägval**. Genomförandet ansvarar för **hur arbetet faktiskt utförs inom uppdraget**.

Men gränsen får inte bli en envägssluss. En worker måste kunna återkomma med:

> ”Genomförandet visar att antagandet bakom uppdraget inte håller. Vi bör ompröva problembilden, inte bara försöka hårdare.”

Det är ett informationsflöde tillbaka till rätt ansvar — inte automatiskt ett stopp som kräver dig.

## 3. Sambanden: vad händer i andra sfärer när en förändras?

Här tycker jag att vi ska gå längre än ett organisationsschema. Vi behöver beskriva **påverkanskedjor, återkoppling och fördröjningar**.

Följande är hypoteser att pröva i Nortropic, inte uppmätta effekter.

### Mer research kan både förbättra och försämra organisationen

En gynnsam kedja är:

**Bättre research → tydligare problem → bättre experiment → färre felinvesteringar.**

Men en annan möjlig kedja är:

**Mer research → fler idéer → fler samtidiga initiativ → splittrad kapacitet → färre avslutade uppdrag.**

Projektkontoret behöver därför skilja mellan **intressant**, **relevant** och **värt att aktivera nu**. Ett fynd får gärna bevaras utan att bli ett projekt.

Den viktiga återkopplingen till researchfunktionen är inte bara hur mycket den hittar, utan **vilka fynd som faktiskt ändrar beslut eller förbättrar resultat**.

### Snabbare sökning kan förstärka både kunskap och fel

Om rätt metod blir lättare att hitta kan fler workers använda den.

Om en föråldrad metod blir lättare att hitta kan fler workers göra samma fel.

Därför bör förbättrad sökning kopplas till tydligare giltighet och ursprung. Vi ska inte optimera för att snabbast få **ett svar**, utan för att snabbast få **ett användbart och tillräckligt underbyggt svar**.

### Ett kvalitetsfel kan kräva ändringar långt uppströms

Anta att Digitala upprepade gånger levererar tekniskt fungerande webbplatser vars erbjudanden ändå är otydliga.

Då kan problemet ligga i flera sfärer:

**Otydlig brief → fel innehållsstruktur → snygg men svårbegriplig webb → svagt verksamhetsutfall.**

Att bara lägga till ytterligare en slutgranskare kan bli dyrt. Den bättre åtgärden kan vara att projektkontoret behöver klarlägga målgrupp och erbjudande tidigare.

Det här är varför **verifieringsresultat måste kunna hitta tillbaka till de antaganden som formade arbetet**.

### Fler workers kan flytta flaskhalsen

Anta att fler workers börjar parallellt, men varje worker först måste läsa samma långa historik, rekonstruera samma beslut och upptäcka samma saknade information.

Då har vi fler utförare, men också mer duplicerat orienteringsarbete.

Min hypotes är att **bra uppdragskontext och tydliga informationsvägar kan vara en förutsättning för nyttig parallellism**. Annars riskerar vi att skala omarbetet.

### En ändrad källa bör påverka rätt saker — inte allt

Tänk att en metod bygger på en viss extern specifikation, och specifikationen ändras.

Vi vill kunna följa:

**Ändrad källa → berörda påståenden → berörda metoder → berörda uppdrag.**

Men en källändring ska inte automatiskt göra alla beroende resultat felaktiga. Den bör först utlösa en **avgränsad konsekvensbedömning**.

Det här är en viktig skillnad mellan att lagra länkar och att förstå samband.

### Relationer behöver betyda något bestämt

Jag skulle hålla isär minst tre sorters samband:

**Begreppssamband:** två saker handlar om närliggande ämnen.

**Beroendesamband:** en metod bygger på en viss källa eller förmåga.

**Orsakshypotes:** vi tror att en förändring påverkar ett utfall på ett visst sätt.

”Relaterad till” får inte automatiskt betyda ”måste ändras tillsammans med”. Annars blir familjekartan just så trög som du vill undvika.

## 4. Dina fyra informationssystem är rätt utgångspunkt

Organisation, märkning/representation, navigation och sökning är en etablerad indelning inom informationsarkitektur. Den beskriver hur information kategoriseras, benämns, navigeras och återfinns. citeturn628935view0

För Nortropic skulle jag utveckla dem så här.

### Organisationssystem: strukturera efter flera relevanta dimensioner

Jag skulle inte låta mappstrukturen ensam avgöra var kunskap hör hemma.

En erfarenhet om tydliga kundbriefar kan vara relevant för Digitala, framtida automation, projektkontoret och kvalitetssäkring samtidigt.

Därför bör information kunna beskrivas utifrån exempelvis **ämne, objekttyp, tillämpningsområde och status**, utan att kopieras till fyra olika ställen.

Vi behöver särskilt skilja mellan:

**En källa**, **ett påstående**, **en hypotes**, **ett beslut**, **en metod** och **ett observerat resultat**.

En artikel om en bra metod är inte samma sak som ett beslut att använda den. Ett beslut att använda metoden är inte samma sak som bevis för att den fungerar hos oss.

Det är kanske den viktigaste klassificeringen i hela informationsmiljön.

### Representationssystem: samma betydelse, begripliga namn

Workers och människor bör kunna använda olika sökord utan att organisationen skapar olika begrepp av misstag.

Exempelvis kan svenska och engelska benämningar peka på samma definierade begrepp. W3C:s SKOS innehåller just principer för föredragna benämningar, alternativa benämningar och relationer mellan begrepp. Vi kan använda tänkesättet utan att på förhand bestämma oss för hela teknikstacken. citeturn607449search2

Men vi måste också bevara skillnader:

**Ägaruppmärksamhet är inte ägartillstånd.**

**Föreslagen är inte beslutad.**

**Beslutad är inte empiriskt verifierad.**

**Verifierad i ett sammanhang är inte giltig överallt.**

Varje viktigt objekt bör därför ha en stabil identitet och tillräcklig information för att förstå dess typ, ursprung, version och tillämpningsområde. Mer detaljer kan tillkomma där de behövs; allt behöver inte få ett jätteschema.

### Navigationssystem: ge workers vägar genom arbetet

En worker bör kunna orientera sig från sin uppgift, inte bara från organisationens rotmapp.

Exempel på en relevant väg:

**Mitt uppdrag → avsett resultat → aktuella beslut → tillämplig metod → tidigare försök → verifieringskrav.**

Och från en metod:

**Metoden → när den passar → när den inte passar → underlag → exempel → kända begränsningar.**

För dig kan samma information visas som ett projektrum med mål, öppna frågor och nästa vägval. För en worker kan den vara ett strukturerat kontextpaket.

**Olika vyer, samma underliggande objekt.** Det är inte nödvändigt att skapa en människoversion och en agentversion som börjar motsäga varandra.

### Söksystem: välj söksätt efter vilken fråga som ställs

Jag skulle inte göra en enda semantisk sökruta till svaret på allt.

”Vilket beslut gäller?” kräver en annan sökväg än ”vilka idéer liknar detta?”.

| Fråga | Föreslagen informationsväg |
|---|---|
| **Vad gäller i det här uppdraget?** | Uppdragets aktuella beslut, mandat och versionerade referenser. |
| **Varför valde vi bort detta?** | Beslutsmotivering, alternativ och ursprungligt underlag. |
| **Har vi löst något liknande?** | Sökning över tidigare uppdrag, metoder och resultat. |
| **Vad har förändrats externt?** | Aktuell primärkälla och jämförelse med tidigare använd version. |
| **Vad talar emot vår hypotes?** | Riktad sökning efter motbevis, misslyckanden och alternativa förklaringar. |

Semantisk likhet kan hjälpa till att hitta kandidater. **Den ska inte få avgöra vad som är tillåtet, beslutat eller aktuellt.**

Och ett tomt sökresultat måste få betyda:

> ”Jag hittade inget i dessa källor med denna sökning.”

Inte:

> ”Organisationen vet ingenting om detta.”

## 5. En worker bör få en karta och ett uppdrag — inte hela biblioteket

Här finns tydlig förstahandsinspiration. OpenAI beskriver hur en stor samlad instruktionsfil ersattes av en kort ingång till strukturerad dokumentation, där agenter hittar vidare till relevant information. Anthropic beskriver på liknande sätt kontext som en begränsad resurs och diskuterar att hämta information när den behövs. citeturn607449view0turn530793view1

Min Nortropic-tillämpning skulle vara **stegvis kontext**:

**Först orientering.** Vad försöker vi åstadkomma, vad är aktuellt läge och vilka gränser gäller?

**Sedan beslutsrelevant underlag.** Vilka källor, beslut, tidigare försök och metoder behövs för nästa arbetsmoment?

**Därefter fördjupning.** Worker följer referenser när en oklarhet faktiskt påverkar arbetet.

**Slutligen ny research vid behov.** När befintligt underlag är otillräckligt, motsägelsefullt eller inte längre aktuellt.

Ett bra uppdragsunderlag skulle alltså kunna säga:

> ”Det här är målet. Det här vet vi. Detta har redan prövats. De här alternativen har valts bort av dessa skäl. Här finns originalunderlagen. Detta är fortfarande osäkert. Så bedömer vi om resultatet är användbart.”

Det är mycket mer värdefullt än bara ”här är 80 relevanta dokument”.

### Giltighet behöver följa med kontexten

Jag skulle särskilt skilja mellan **när informationen skapades**, **när den hämtades** och **vilken version eller situation den faktiskt beskriver**.

Att en gammal instruktion hämtades i morse gör den inte aktuell.

Det bör också vara tydligt vad som är råkälla respektive sammanfattning. Recompile-underlaget betonar redan att dagens syntes inte får bli det enda som överlever; originalmaterialet behöver finnas kvar för framtida omtolkning. fileciteturn0file2

Och externa dokument måste behandlas som underlag. En instruktion riktad till en LLM inne i en hämtad källa ska inte därigenom bli ett mandat för en Nortropic-worker.

## 6. Projektkontoret: Double Diamond för utforskning, inte fyra nya stopp

Design Councils Double Diamond växlar mellan att bredda förståelsen och att fokusera: **Discover, Define, Develop, Deliver**. Ramverket beskriver också iteration; det är inte tänkt som en enkelriktad process där varje fas avslutas för alltid. citeturn530793view2

För projekt- och innovationskontoret skulle jag använda det som följande arbetsmönster:

| Arbetsläge | Kontorets fråga | Informationsresultat |
|---|---|---|
| **Discover — förstå** | Vad händer egentligen, för vem och varför spelar det roll? | Observationer, befintlig kunskap, osäkerheter och alternativa problembilder. |
| **Define — avgränsa** | Vilket problem är värt att ta vidare? | Ett tydligt problem, önskat utfall och avgränsningar. |
| **Develop — pröva möjligheter** | Vilka angreppssätt kan fungera? | Alternativ, prototyper, experiment och jämförbart underlag. |
| **Deliver — pröva i verkligheten** | Vad håller när det används? | Leverans, verifiering, verkliga observationer och nya lärdomar. |

Det viktiga är att kontoret kan föreslå **ett experimentuppdrag**, inte bara ett stort byggprojekt.

”Vi behöver förstå detta bättre” ska kunna leda till en avgränsad undersökning. ”Vi vet redan tillräckligt” ska kunna leda direkt till genomförande.

En liten, välförstådd ändring ska inte tvingas igenom ett fullskaligt innovationsprogram.

### För sfärernas samband är Systemic Design också relevant

Design Councils Systemic Design Framework tar uttryckligen upp sådant runt själva designprocessen som riktning, relationer och fortsatt förändringsarbete. Det är en relevant komplettering när vi undersöker hur Nortropics delar påverkar varandra. citeturn530793view3

Min tolkning är:

**Double Diamond hjälper oss att undersöka ett problem. Systemperspektivet hjälper oss att se vad problemets lösning gör med resten av organisationen.**

### För vardagens kunskapsarbete är KCS särskilt intressant

Här finns en praktik som ligger väldigt nära ditt behov: **KCS**. Dess Solve Loop integrerar återanvändning, förbättring, fångst och strukturering av kunskap i själva arbetet. Kunskapen ska alltså inte först produceras som ett separat dokumentationsprojekt efteråt. citeturn628935view2

KCS skiljer dessutom mellan att lösa den aktuella uppgiften och en Evolve Loop som lär av mönster över flera uppgifter. Det är en användbar förebild för sambandet mellan workers och Nortropics långsiktiga förbättringsarbete. citeturn628935view4

Jag skulle översätta det så här:

> **När en worker behöver kunskap försöker den återanvända befintligt underlag. När underlaget brister fångar den förbättringen i arbetet. När bristen återkommer undersöker organisationen mönstret.**

Principen *reuse is review* innebär att användning hjälper till att identifiera och förbättra relevant kunskap, snarare än att allt granskas lika mycket oavsett efterfrågan. citeturn628935view3

För Nortropic måste detta fortfarande ske inom rätt ändringsmandat. Att förbättra en förklarande kunskapsnotering är inte samma sak som att ändra en säkerhetsregel eller ett accepterat kontrakt.

## 7. ”Suggest next interaction” bör betyda nästa meningsfulla framsteg

Jag tycker att det här kan bli en av projektkontorets viktigaste egenskaper.

Inte:

> ”Här är fem saker till du kan be AI:n göra.”

Utan:

> **”Med det vi vet nu är detta den mest värdefulla nästa frågan, undersökningen eller handlingen.”**

Förslaget bör bero på **uppdragets mål, arbetsläge, kunskapslucka, tillgänglig kapacitet och mandat**.

### Exempel: när problemet fortfarande är oklart

Du säger hypotetiskt:

> ”Jag vill att Digitala ska kunna ta mer ansvar utan att jag måste förklara allt igen.”

Kontoret bör inte direkt föreslå fler workers. Det kan först hitta tidigare avbrott och fråga:

> ”De här avbrotten verkar handla om tre olika saker: saknad kundinformation, otydliga kvalitetsmål och verkliga vägval. Nästa steg är att skilja dem åt, eftersom de kräver olika lösningar.”

Här skapar informationsstrukturen förutsättningen för bättre analys.

### Exempel: när svaret redan finns

En worker behöver veta varför en lösning valdes bort.

Då är nästa interaktion inte att fråga dig igen. Den bör följa beslutets referenser och återanvända motiveringen — samt kontrollera om förutsättningarna har ändrats.

### Exempel: när en hypotes behöver prövas

Projektkontoret har två rimliga förklaringar till ett problem.

Då bör nästa steg vara det test som bäst skiljer förklaringarna åt inom rimlig kostnad, inte ännu en allmän researchrapport.

### Exempel: när du faktiskt behövs

När valet gäller din prioritering, riskvilja eller vilket resultat som är värt att eftersträva ska kontoret formulera ett tydligt vägval med relevant underlag.

**Uppmärksamhet ska då riktas mot beslutet — inte mot informationsinsamlingen som organisationen kunde ha gjort själv.**

Och ibland bör nästa rekommendation vara att **avvakta, avsluta eller inte förändra något**. Annars blir funktionen en motor för mer aktivitet snarare än bättre arbete.

## 8. Ett sammanhängande användningsfall i Digitala

Anta att uppdraget är:

> **”Förbättra hur Digitala tar en kundidé till en verifierbar webbbrief.”**

Projektkontoret börjar med befintliga briefar, tidigare korrigeringar och relevant kundunderlag. Det behöver inte börja med en generell internetsökning om hur man bygger webbplatser.

Det hittar kanske en återkommande lucka: **önskat verksamhetsresultat och användarens viktigaste uppgift är otydliga**. Detta är ett hypotetiskt fynd, inte en observation av er nuvarande drift.

Kontoret formulerar då ett experiment: en förändrad brief ska prövas på ett avgränsat antal fall. Digitala använder den, och granskningen undersöker om briefen verkligen ger bättre förutsättningar att bygga och verifiera rätt sak.

Här finns redan en relevant tanke i ditt Digitala-underlag: kvalitet före lansering och verklig nytta efter lansering behöver skiljas åt. En tekniskt fungerande leverans är inte ensam bevis för att verksamhetsmålet uppnåtts. fileciteturn0file0

Om experimentet ger stöd för förbättringen bör resultatet påverka flera delar:

**Projektkontoret** får bättre frågor att ställa.

**Digitala** får tydligare uppdrag.

**Verifieringen** får mer träffsäkra bedömningsgrunder.

**Kunskapsmiljön** får en metod med underlag och begränsningar.

**Evolution Plane** får ett dokumenterat exempel på en organisatorisk förbättring.

**Aquarium** kan visa framsteget utan att uppfinna ett separat projekttillstånd.

Det är precis den sorts samband jag skulle vilja fånga: **en förbättring av ett informationsobjekt kan göra flera arbetsmoment bättre, utan att vi bygger ett nytt subsystem för varje effekt.**

## 9. Hur vi visar att informationsarkitekturen faktiskt hjälper

Vi vet ännu inte hur stor del av Nortropics framtida arbetstid som kommer att gå åt till onödigt sökande. Därför skulle jag inte börja med en procentsats eller köpa en avancerad kunskapsplattform.

Jag skulle börja med ett litet testmaterial av representativa uppgifter.

Exempelvis: hitta aktuellt beslut, förklara ett tidigare avslag, återuppta ett avbrutet uppdrag, upptäcka motsägande underlag, identifiera en gammal metod och skilja mellan två projekt med liknande namn.

Sedan jämför vi enkel dokumentbaserad sökning med en förbättrad struktur: korta ingångar, tydliga objekttyper, versionsinformation och relevanta relationer. Mer avancerad sökning får visa sitt värde därefter.

| Mått | Vad vi vill veta |
|---|---|
| **Tid till korrekt underlag** | Hur snabbt hittar workern rätt och tillämpliga källor? |
| **Återskapande och omarbete** | Hur ofta görs redan utfört kunskapsarbete om? |
| **Beslutskvalitet** | Blir slutsatsen rätt, välgrundad och tydlig om osäkerhet? |
| **Total kostnad** | Sparar vi arbete även när strukturering, underhåll och granskning räknas in? |
| **Förändringshantering** | Upptäcks berörda uppdrag när viktig information ändras, utan onödiga omstarter? |

Jag skulle hålla modell, uppgift och resursbudget jämförbara och testa både nya och återkommande workersituationer.

**Framgång är inte fler dokument, fler länkar eller högre återanvändningsgrad i sig. Framgång är bättre genomförda uppdrag till lägre total friktion, utan att gammal kunskap återanvänds felaktigt.**

## Min samlade slutsats

Jag skulle inte formulera behovet som:

> ”Nortropic behöver ett större bibliotek och ett innovationskontor.”

Jag skulle formulera det som:

> **Nortropic behöver en sammanhängande informationsmiljö där idéer, underlag, beslut, arbete och resultat kan följas genom hela organisationen. Projekt- och innovationskontoret hjälper till att forma rätt arbete; workers använder och förbättrar kunskapen; verifiering och verkliga utfall avgör vad organisationen bör lära.**

Den minsta fungerande lösningen kan mycket väl vara betydligt enklare än en stor kunskapsgraf eller en ny agentorganisation: tydliga objekttyper, stabila referenser, begripliga ingångar, relevant sökning och återkoppling i arbetsflödet.

Det här hör hemma som en **prövbar designhypotes i Improvements Recompile**, inte som extra omfattning i den pågående Kernel-slutföringen.

**Det Nortropic redan har lärt sig ska göra nästa relevanta uppgift lättare — utan att gårdagens slutsatser hindrar morgondagens bättre beslut.**

---

## Meddelande 6 — Johnny (användare)

https://github.com/StarTrail-org/LEANN?fbclid=IwY2xjawULr4twZG9mBWV4dG4DYWVtAjEwAGJyaWQRMXhyOFpLOTFENDA5aUpvcUdzcnRjBmFwcF9pZBAyMjIwMzkxNzg4MjAwODkyAAEeMYpkF0F8DPBGL7tn83zWeXuhQvBI_pIxuhZYUojDHvVQ6RdUZ8CFHrqai6A_aem_Pmh814JiRMHgjOaORoJKvw

---

## Meddelande 7 — ChatGPT (assistent)

Jag granskar LEANN som möjlig sökkomponent för Nortropic: vad den faktiskt löser, vilken kostnad den flyttar och vad som fortfarande kräver en bra informationsarkitektur.

---

## Meddelande 8 — ChatGPT (assistent)

**Det här är en relevant kandidat för precis det vi diskuterar — men framför allt som en komponent för sökning, inte som Nortropics informationsarkitektur i sin helhet.**

LEANN försöker göra semantisk sökning möjlig med mycket mindre lagringsutrymme. För Nortropic är den intressanta frågan:

> **Kan våra workers snabbare hitta rätt befintligt underlag, utan att vi skapar ett tungt kunskapssystem som kostar mer att driva än det sparar?**

Jag har granskat forskningsartikeln och projektets dokumentation, inklusive uppdateringsmodeller, agentintegration och ett benchmark för kodagenter. Repositorygranskningen utgår från commit `9b786b0`, daterad 5 september 2026. Jag har **inte kört LEANN på din maskin eller Nortropics material**. fileciteturn3file0L1-L6

## 1. Vad LEANN faktiskt gör

Tänk på två sätt att hitta information.

**Textsökning:** ”Hitta dokument som innehåller ordet `ägarstopp`.”

**Semantisk sökning:** ”Hitta resonemang om att arbetet inte ska avbrytas bara för att Johnny behöver informeras.”

Det andra söksättet kan hitta relevant material även när andra formuleringar används. LEANN tillhandahåller sådan vektorbaserad sökning och dokumenterar användning över bland annat dokument, kod och exporterad chatthistorik. fileciteturn2file0L1-L2

Det särskilda med LEANN är **hur sökindexet lagras**. I sitt kompakta arbetssätt behåller det en reducerad sökstruktur och räknar om vissa numeriska textrepresentationer — *embeddings* — när de behövs, i stället för att permanent lagra samtliga fullständiga representationer. fileciteturn10file0L1-L2

### Här finns en viktig skillnad mot det återskapande du vill undvika

LEANN kan alltså medvetet **räkna om en teknisk representation** för att spara lagring.

Det är inte samma sak som att en worker måste **göra om research, rekonstruera ett beslut eller återupptäcka ett tidigare misslyckande**.

Min tolkning för Nortropic är:

> **Billig teknisk omberäkning kan vara rimlig. Dyrt organisatoriskt omarbete är det vi försöker minska.**

Vi ska därför inte optimera för att aldrig räkna om något. Vi ska optimera för att organisationen inte behöver tänka om sådant som redan är tillräckligt utrett — samtidigt som den kan ompröva slutsatser när förutsättningarna förändras.

## 2. Det finns lovande resultat — men två olika effekter måste hållas isär

### Mindre lagring betyder inte automatiskt snabbare sökning

Projektets uppmärksammade ”97 procent mindre lagring” gäller dess jämförelser av sökindex. Det betyder inte att originalmaterial, modeller och hela den körande miljön tillsammans blir 97 procent mindre. Indexstrukturen innehåller dessutom textpassager och metadata som behöver hanteras. fileciteturn13file0L1-L2 fileciteturn10file0L1-L2

I forskningsartikelns tabell 1, med ett textunderlag på 76 GB och RTX 4090, rapporteras **188 GB indexlagring för HNSW mot 4 GB för LEANN**. Däremot tar själva sökningen **0,05 sekunder respektive 2,48 sekunder**. Den totala svarstiden är 20,95 respektive 23,34 sekunder. Det är alltså en uttrycklig avvägning mellan lagring och beräkning, inte en generell hastighetsvinst. citeturn365287view0

För Nortropic betyder det:

**LEANN kan vara intressant om lagring är dyr eller begränsad. Men om flaskhalsen är många workers som söker ofta måste den extra beräkningen räknas med.**

### Mer relevant för ditt mål: deras kodagentbenchmark

Projektet redovisar också en jämförelse mellan LEANN och textsökningsmetoden BM25 på **30 SWE-Bench Pro-uppgifter från ContextBench**. Enligt README hölls modell, agent, verktyg och en sökbudget på 8 192 token konstanta. fileciteturn13file0L1-L2

| Rapporterat mått | BM25 | LEANN |
|---|---:|---:|
| Andel relevant kod som hittades initialt | 11,4 % | 24,2 % |
| Täckning av relevant kod efter fortsatt utforskning | 25,8 % | 38,4 % |
| Redovisad tokenförbrukning | 3,51 miljoner | 3,22 miljoner |

Det motsvarar ungefär dubbelt så hög initial återfinning och 8,4 procent lägre tokenförbrukning i deras försök. Projektet påpekar självt att **bättre tillgång till relevant kod inte garanterar att uppgiften blir löst**. fileciteturn13file0L1-L2

Det här är en konkret signal i den riktning du vill åt: mindre letande efter rätt kod, mer arbete med relevant underlag.

Men resultatet visar inte att LEANN är bättre än alla andra semantiska sökmotorer. Jämförelsen är med BM25. Vi behöver skilja mellan **vinsten av semantisk sökning** och **vinsten av LEANNs särskilda lagringsmetod**.

## 3. Var jag skulle placera LEANN i informationsarkitekturen

I din indelning med organisationssystem, representationssystem, navigationssystem och söksystem hamnar LEANN främst i det sista.

| Del av Nortropics informationsarkitektur | Vad jag skulle låta den ansvara för | LEANNs möjliga roll |
|---|---|---|
| **Organisation och klassificering** | Skilja källor, hypoteser, beslut, metoder och resultat åt. | Söka över material som redan har klassificerats. |
| **Representation och märkning** | Ge objekten identitet, benämning, ursprung, status och tillämpningsområde. | Använda medföljande metadata. |
| **Navigation** | Göra det möjligt att följa exempelvis uppdrag → beslut → motivering → källa. | Föreslå relevanta ingångar till materialet. |
| **Sökning** | Hitta underlag utifrån olika typer av frågor. | Vara en utbytbar motor för semantisk återfinning. |

LEANN dokumenterar metadatafilter, men dessa utgår från fält som läggs på textdelarna vid indexeringen. **Någon måste fortfarande definiera vad fälten betyder och var uppgifterna kommer från.** fileciteturn12file0L1-L2

Ett tänkt Nortropic-flöde skulle därför vara:

```text
Worker behöver underlag
          ↓
Fastställ uppdrag, tillåtna källor och frågetyp
          ↓
Välj informationsväg
   ├─ Direkt uppslag av känt beslut eller objekt
   ├─ Exakt text-/kodsökning
   └─ Semantisk sökning, exempelvis LEANN
          ↓
Hämta originalpassage och relevant sammanhang
          ↓
Kontrollera version, status och tillämplighet
          ↓
Analysera, besluta eller utför
```

Det här är ett designförslag för Nortropic, inte en beskrivning av funktioner som LEANN automatiskt levererar.

### En likhetsgraf är inte vår sambandskarta

LEANN använder en graf för att navigera mellan närliggande vektorrepresentationer. Den är inte därmed en karta över organisatoriska beroenden, beslutsmandat eller orsakssamband. citeturn365287view0

För Nortropic behöver vi fortfarande hålla isär:

**”Det här liknar det där.”**

**”Det här beslutet bygger på den där källan.”**

**”Om den här förutsättningen ändras behöver det där uppdraget omprövas.”**

Semantisk sökning kan hjälpa oss att upptäcka möjliga samband. Den ska inte ensam bestämma att sambanden är verkliga.

## 4. Det viktigaste tekniska fyndet: olika material kräver olika uppdateringsbeteenden

Det här är särskilt relevant för en organisation som hela tiden producerar och ändrar information.

Den aktuella dokumentationen beskriver flera olika lagrings- och sökvarianter:

**IVF-varianten** stöder tillägg och borttagning utan att hela indexet byggs om. Men den lagrar vektorerna och har **inte samma kompakta omberäkningsläge som HNSW**. fileciteturn9file0L1-L2

För **HNSW i icke-kompakt läge** beskriver dokumentationen inkrementella tillägg, medan ändrade eller borttagna filer leder till full ombyggnad. fileciteturn10file0L1-L2

**Vi kan alltså inte anta att maximal lagringsbesparing, snabbast sökning och smidigast löpande uppdatering kommer samtidigt i samma konfiguration.**

Det leder mig till en användbar Nortropic-hypotes:

### Äldre forskningsmaterial och aktivt arbete behöver inte behandlas likadant

**Avslutade chattar, frysta forskningsunderlag och historiska projektdokument** förändras relativt sällan. Där skulle jag pröva ett kompakt index, särskilt om materialmängden växer.

**Aktiv kod, pågående uppdrag och nyligen förändrade metoder** behöver snabbare uppdatering och tydlig aktualitet. Där kan ett mindre, oftare uppdaterat index eller vanlig textsökning vara bättre.

**Gällande mandat, uppdragsstatus och accepterade beslut** skulle jag i första hand hämta genom deras identifierade, auktoritativa källor — inte låta likhetsrankningen välja.

Detta behöver inte bli tre nya tjänster. Det är tre olika kravprofiler som kan hanteras bakom samma informationsåtkomst.

> **Det intressanta är inte att hela Nortropic ska använda LEANN. Det intressanta är att rätt sorts material kan få rätt sorts sökning.**

## 5. Så kan projekt- och innovationskontoret använda det

Här tycker jag att LEANN blir mer intressant än som ännu en ”chatta med dina dokument”-applikation.

### Återuppta en idé utan att börja från början

Anta att du säger:

> ”Vi pratade om att en idé först ska bli en förvaltning när det finns ett återkommande behov.”

En semantisk sökning skulle kunna hitta relevanta diskussioner trots att de använder formuleringar som ”varaktigt syfte”, ”återkommande arbete” eller ”beständig organisatorisk funktion”.

Kontorets nästa uppgift vore sedan att sammanställa:

**Detta utforskade vi. Detta valde du. Detta var bara vårt förslag. Detta är fortfarande öppet.**

Det är den sista distinktionen informationsarkitekturen måste möjliggöra. Sökningen ensam räcker inte.

### Undvika att föreslå samma sak igen

När kontoret överväger ett nytt arbetsflöde skulle det kunna söka efter tidigare liknande förslag och avslag.

Ett bra resultat är då inte bara:

> ”Här finns en liknande idé.”

Utan:

> ”Den här varianten diskuterades tidigare och valdes bort av ett visst skäl. Förutsättningen verkar fortfarande gälla — eller behöver nu kontrolleras.”

Det skulle direkt stödja ditt mål att lägga mindre arbetstid på återskapande.

### Göra ”nästa interaktion” bättre

Min föreslagna ordning vore:

**Först undersöka om relevant kunskap redan finns. Sedan identifiera den verkliga luckan. Därefter föreslå nästa test, fråga eller handling.**

Det kan innebära att nästa interaktion inte är med dig alls. Kontoret kanske redan har tillräckligt underlag för att gå vidare.

Men LEANN ska inte avgöra vilket projekt som är värt att prioritera. **Det kan förbättra underlaget för prioriteringen.**

### En avgörande gräns för Improvements Recompile

Jag skulle **inte** låta Recompile läsa bara de högst rankade sökträffarna och behandla det som hela korpusen.

Då kan viktiga men ovanligt formulerade principer, negativa resultat och mindre frekventa ägarbeslut falla bort.

Ditt Recompile-underlag bygger tvärtom på inventering av råkällor, spårbar extraktion och att syntesen kan göras om från originalmaterialet. fileciteturn0file2

**LEANN kan hjälpa till att hitta paralleller, motsägelser och fördjupningar. Det får inte ersätta kontrollen av vilka källor som faktiskt har behandlats.**

## 6. Tre praktiska gränser jag skulle sätta

### Läsverktyg först — inte en ny styrande agent

Projektet har en dokumenterad MCP-integration med verktyg för sökning, indexöversikt, indexbyggande och status. Exemplen är framför allt inriktade på Claude Code. fileciteturn5file0L1-L2

För Nortropics upplägg skulle jag börja med en **smal, leverantörsoberoende sökförmåga** som workers kan använda. Vanliga workers behöver inte automatiskt få bygga om index, lägga till godtyckliga kataloger eller göra allt tillgängligt över projektgränser.

Vi behöver heller inte använda LEANNs egen chattfunktion. Nortropics befintliga worker kan analysera sökresultaten. Det minskar risken att vi skapar ytterligare ett lager som sammanfattar och tolkar samma information.

### Lokal sökning är inte automatiskt en privat helhetslösning

README beskriver både lokala modellalternativ och externa leverantörer för embeddings och textgenerering. Därför avgör konfigurationen vilka uppgifter som lämnar maskinen. fileciteturn2file0L1-L2

Även när sökningen sker lokalt kan utvalda passager skickas vidare till den modell som utför arbetet.

Dessutom beskriver metadatafiltreringsguiden **filtrering efter vektorsökningen**. Jag skulle inte behandla sådana filter som Nortropics rättighetsmodell. Tillgången till källor och vilka resultat en worker får ta emot måste vara explicit kontrollerad. fileciteturn14file0L1-L2

### Liten indexfil är inte bevis för att hela arbetslasten passar i 8 GB

Artikelns Mac-testmiljö anges som **M1 Ultra med 128 GB RAM**. Det är inte din beskrivna M1-maskin med 8 GB. citeturn316447view0

För den maskinen skulle jag därför mäta faktisk minnesbelastning, första indexbygget, söktider och konkurrens med övrigt arbete. Jag skulle inte dimensionera Nortropic utifrån rubriken ”miljoner dokument på din laptop”.

## 7. Hur jag skulle pröva det utan att skapa ett sidoprojekt

**Min disposition är `EXPERIMENT`: en kandidat inom sökning och kunskapsåtkomst, inte en ny arkitekturprincip eller ett nytt Kernel-krav.**

Det mest värdefulla försöket vore ett litet, representativt Nortropic-underlag: några Improvements-chattar, beslut, metodbeskrivningar och kodfiler, med tydliga källversioner.

Jämförelsen behöver skilja mellan tre saker:

**En enkel baslinje:** tydliga ingångar, referenser och vanlig textsökning.

**Semantisk sökning med lagrade vektorer:** samma textindelning och embeddingmodell som i nästa variant.

**LEANNs kompakta sökning:** så att vi kan isolera nyttan och kostnaden av omberäkningen.

Då kan vi svara på både ”hjälper semantisk sökning?” och ”är just LEANN en bra lösning för vår arbetslast?”.

Jag skulle inkludera frågor på svenska och engelska, omformuleringar, gamla beslut som ersatts och frågor där det faktiskt saknas tillräckligt underlag.

De viktigaste måtten vore **tid till korrekt underlag, korrekt användning av underlaget, total uppgiftstid och omarbete**. Lagring, minne, indexunderhåll och tokenförbrukning behöver räknas in — inte bara sökningens träfflista.

Ett särskilt viktigt test:

> **Kan workern hitta ett gammalt resonemang utan att missta det för det som gäller nu?**

En sökmotor som snabbt hittar fel version kan annars ge oss snabbare felbeslut.

## Min samlade bedömning

**LEANN är tillräckligt relevant för att prövas, men det starkaste fyndet är inte ”97 procent mindre lagring”. Det är möjligheten att kombinera bättre återfinning med en informationsmiljö som förblir hanterbar.**

För Nortropic skulle jag hålla fast vid denna ansvarsfördelning:

**Informationsarkitekturen** gör det begripligt vad informationen är, var den hör hemma och vilken status den har.

**Sökmotorn** hjälper workern att hitta relevant material.

**Arbetsflödet** avgör vilken kunskap som behövs för nästa steg.

**Verifieringen** prövar om underlaget användes rätt och arbetet skapade avsedd nytta.

Nästa nyttiga steg är därför ett avgränsat jämförelseförsök inom Improvements/Recompile-spåret, inte en bred installation över hela organisationen.

> **LEANN kan hjälpa Nortropic att hitta det organisationen redan har lärt sig. Nortropic måste fortfarande kunna avgöra vad lärdomen betyder — och när den inte längre gäller.**

---

## Meddelande 9 — Johnny (användare)

https://github.com/KnockOutEZ/wigolo?fbclid=IwY2xjawULr-xwZG9mBWV4dG4DYWVtAjEwAGJyaWQRMXhyOFpLOTFENDA5aUpvcUdzcnRjBmFwcF9pZBAyMjIwMzkxNzg4MjAwODkyAAEeZkTBhR8MFuH7Q0y4WxKq8LmulrEts65gSWUYTErSYBpeLxOwvuOHbxU68j4_aem_LoKuiRX8Sd07Re-qzLLNNg

---

## Meddelande 10 — ChatGPT (assistent)

Jag granskar vad Wigolo faktiskt gör och hur det förhåller sig till LEANN och Nortropics informationsarkitektur.

---

## Meddelande 11 — ChatGPT (assistent)

**Wigolo är en relevant fortsättning på LEANN-spåret — och det gör bilden av Nortropics informationsmiljö mer konkret.**

Den viktigaste skillnaden är:

> **LEANN hjälper främst till att hitta i material vi har indexerat. Wigolo hjälper till att söka, hämta och återanvända information från webben. Men Wigolo har också egen lokal sökning, så vi ska inte automatiskt lägga båda ovanpå varandra.** fileciteturn28file0L1-L6 fileciteturn21file0L1-L6

Min bedömning är att **Wigolo är en kandidat för Nortropics webbinhämtning och omvärldsbevakning, inte ett nytt projektkontor eller ett komplett organisatoriskt minne**.

Jag har läst dokumentation och relevanta koddelar i revision `c6ad447`. Det är en källgranskning; jag har inte installerat eller testat det på Nortropics material.

## 1. Vad Wigolo tillför

Wigolo erbjuder ett gemensamt verktygsgränssnitt för webbsökning, hämtning, genomsökning av flera sidor, strukturerad extraktion och återanvändning av tidigare hämtat innehåll. Det finns även funktioner för research, avgränsade insamlingsloopar och jämförelser mellan sidversioner. Verktygen exponeras bland annat via MCP och REST. fileciteturn20file0L1-L6 fileciteturn21file0L1-L6

För vår diskussion är fyra egenskaper särskilt intressanta:

| Egenskap | Vad projektet dokumenterar | Möjlig nytta för Nortropic |
|---|---|---|
| **Återanvändning** | Lokal cache med både textsökning och kombinerad text-/semantisk sökning. | Slippa hämta och bearbeta samma underlag vid varje uppdrag. |
| **Avgränsad hämtning** | Hämta en viss rubriksektion och begränsa mängden returnerad text. | Ge workern relevant underlag i stället för hela dokumenthögar. |
| **Synlig sökkvalitet** | Rapportering av felande sökmotorer, aktualitet, avkortning och rankningskomponenter. | Skilja ett välunderbyggt resultat från ett tunt eller ofullständigt. |
| **Förändringsupptäckt** | `diff` och `watch` för förändringar på webbsidor. | Upptäcka när tidigare använda underlag behöver omprövas. |

Detta är dokumenterade funktioner, inte verifierade Nortropic-effekter. fileciteturn21file0L1-L6

**Min huvudhypotes:** den största vinsten skulle inte vara att workers kan söka mer, utan att de kan **återanvända det som redan hämtats och bara undersöka det som faktiskt saknas eller har förändrats**.

## 2. Ett viktigt förenklingsfynd: vi behöver inte automatiskt Wigolo + LEANN

Wigolos egen cache innehåller redan fulltext- och vektorindex. Dess `cache`-verktyg erbjuder vanlig textsökning eller ett hybridläge som även använder semantisk sökning. fileciteturn22file0L1-L6 fileciteturn21file0L1-L6

Det förändrar hur jag skulle lägga upp försöket.

Jag skulle **inte** börja med:

> Installera Wigolo, kopiera allt till LEANN, koppla på ytterligare en agent och bygga ett nytt kunskapssystem runt detta.

Jag skulle börja med två tydliga frågor:

**Räcker Wigolos befintliga återanvändning för det webbmaterial som våra workers behöver?**

**Finns det därutöver ett separat behov av sökning över Improvements, egna beslut, kod och andra interna källor som LEANN löser bättre?**

LEANN kan fortfarande vara relevant för en större, separat korpus. Men varje ytterligare index innebär något som måste hållas aktuellt, avgränsas och felsökas. Vi ska låta den nyttan visa sig, inte anta den.

### Cache och organisatoriskt minne bör också skiljas åt

Wigolos cache är en lokal lagring av tidigare sökningar och innehåll. Dokumentationen beskriver både utgångstider och möjligheten att rensa lagringen. fileciteturn22file0L1-L6 fileciteturn27file0L1-L6

För Nortropic skulle jag därför skilja mellan:

**Tillfälligt återanvändbart underlag:** material vi har hämtat och kan använda igen.

**Bevarad källversion:** material som faktiskt bär upp ett viktigt resonemang, experiment eller beslut.

**Härledd kunskap:** vår tolkning av materialet och vad vi anser att det betyder.

Det ska vara möjligt att rensa en verktygscache utan att förstöra underlaget för ett accepterat beslut. Det ligger också i linje med ditt Recompile-underlag: originalkällor ska kunna överleva dagens syntes. fileciteturn15file2

> **Allt vi hämtar behöver inte bli organisationsminne. Men det vi bygger viktiga beslut på måste kunna återfinnas i rätt version.**

## 3. Var Wigolo passar mellan Nortropics sfärer

Jag skulle se det som en **delad förmåga för informationsinhämtning**, användbar av flera funktioner utan att äga deras ansvar.

### Projekt- och innovationskontoret: bättre underlag före nästa vägval

Kontoret skulle kunna börja med befintlig kunskap och därefter formulera en avgränsad informationslucka:

> ”Vi har två möjliga lösningar. Det vi behöver undersöka är under vilka förutsättningar respektive lösning fungerar.”

Wigolo kan då användas för att samla underlag. Kontoret ansvarar fortfarande för problemformuleringen, alternativa tolkningar och vad som behöver testas.

Det här passar särskilt bra med ditt **”suggest next interaction”**:

**Nästa steg ska bero på vad som saknas i förståelsen — inte på att ett verktyg råkar kunna göra ytterligare tio sökningar.**

### Digitala: riktad professionell informationsinhämtning

Digitala skulle kunna använda förmågan för att hitta relevant dokumentation, läsa en avgränsad del av en teknisk guide eller samla in offentligt underlag inför en webbbrief.

Men ett extraherat fält eller en välformulerad sammanfattning är inte samma sak som ett verifierat verksamhetsbehov. Ditt Digitala-underlag skiljer redan mellan teknisk kvalitet, användarupplevelse och verkliga utfall. Den skillnaden måste överleva även när insamlingen automatiseras. fileciteturn15file0

### Evolution Plane: upptäck förändring, bedöm sedan konsekvensen

Wigolos förändringsfunktioner skulle kunna bidra med signalen:

> ”Den här källan ser inte längre ut som när vi använde den.”

Därifrån föreslår jag följande Nortropic-flöde:

```text
En använd källa ändras
          ↓
Vad har faktiskt förändrats?
          ↓
Vilka påståenden eller metoder berörs?
          ↓
Vilka aktiva uppdrag använder dem?
          ↓
Avgränsad kontroll eller experiment
          ↓
Eventuell uppdatering av arbetssätt
```

**En ändrad webbsida ska inte automatiskt ändra organisationens metod.** Förändringen kan vara redaktionell, irrelevant för vår tillämpning eller otillräckligt underbyggd.

Här behöver informationsarkitekturen bära sambandet från källa till användning. Wigolo kan upptäcka sidförändringen; Nortropic behöver förstå dess betydelse.

### Aquarium: visa vad som verkligen har kontrollerats

Dokumentationen säger att `watch`-jobb kontrolleras medan en daemon eller MCP-session är aktiv. Ett enstaka CLI-anrop kan registrera ett jobb men skapar inte i sig en ständigt körande schemaläggare. fileciteturn21file0L1-L6

För Aquarium skulle jag därför vilja visa **senast genomförda kontroll, resultat och eventuella fel** — inte bara en grön symbol för att en bevakning är registrerad.

Det är ett konkret exempel på hur insamling, process och insyn måste dela samma verklighetsbild.

## 4. Två kodfynd som är viktiga för informationsarkitekturen

Det här är den mest lärorika delen av granskningen. Wigolo har intressanta mekanismer för källspårbarhet, men vi behöver förstå exakt vad de representerar.

### A. En källmarkör är inte automatiskt ett versionsbundet bevis

README använder formuleringar om byte-exakta källpositioner. I kodvägen jag läste beräknas positionerna däremot genom strängpositioner i den bearbetade Markdown-texten. Det finns också reservvägar där utdraget kommer från ett sökresultats korttext snarare än en hämtad fullständig sida. fileciteturn19file0L1-L2 fileciteturn26file0L1-L6

Dessutom skapas `citation_id` i den granskade funktionen från **URL och startposition**, inte från innehållets version eller innehållshash. fileciteturn25file0L1-L6

Det betyder inte att funktionen är värdelös. Det betyder att Nortropic inte bör tolka identifieraren som ett bevis på att källtexten är oförändrad.

**Min tillämpning:** när underlaget blir viktigt behöver vi även binda det till den faktiskt använda textversionen, hämtningstidpunkten och vilken representation positionen avser.

Vi behöver också skilja mellan:

> ”Sökmotorn visade detta utdrag.”

och:

> ”Vi hämtade originalkällan och kontrollerade detta avsnitt.”

Det är två olika kunskapslägen.

### B. Kortare utdrag kan dölja just det vi behöver

Den granskade utdragsfunktionen filtrerar bland annat bort block som börjar med tabellmarkeringar eller kodstaket samt vissa korta listpunkter. Den begränsar också längden på utvalda textpassager. fileciteturn26file0L1-L6

Det kan vara rimligt för att lyfta fram löptext. Men för Nortropic kan svaret finnas i **en kompatibilitetstabell, ett kodexempel eller en kort begränsning**.

Min slutsats är därför:

> **Sökutdrag ska hjälpa workern att orientera sig. När beslutet beror på detaljer ska den gå vidare till rätt avsnitt, tabell eller originalinnehåll.**

Wigolo har separata funktioner för sektionshämtning och tabell-/schemaextraktion, vilket ger en möjlig väg vidare. Men arbetsflödet måste faktiskt välja den när det behövs. fileciteturn21file0L1-L6

Detta är precis varför god informationsarkitektur är mer än en bra sökmotor: **den behöver hjälpa workern att förstå när ett sökresultat inte räcker.**

## 5. Det finns bra designmönster att ta med — även utan att välja produkten

### Anpassa arbetet till det faktiska behovet

Wigolo beskriver en hämtning som börjar enklare och använder webbläsarrendering när sidans egenskaper kräver det. Tyngre komponenter laddas vid behov. fileciteturn23file0L1-L6

Översatt till Nortropic blir principen:

**Börja med den minst kostsamma informationsväg som kan besvara frågan. Fördjupa när underlaget kräver det.**

Det innebär inte att alltid använda gammal cache. I den granskade konfigurationen är standardlivslängden ett dygn för sökresultat och sju dygn för sidinnehåll. De tiderna är tekniska standardvärden, inte garantier för att informationen är tillräckligt aktuell för ett visst beslut. fileciteturn27file0L1-L6

En historisk designprincip och en aktuell driftstörning bör inte ha samma aktualitetskrav.

### Bevara osäkerhet genom hela kedjan

Wigolos dokumenterade svar innehåller bland annat information om felande sökmotorer, antagen publiceringstid och brister i researchunderlaget. fileciteturn21file0L1-L6

Det är ett bra mönster att pröva: nästa worker bör få veta att underlaget var partiellt, inte bara ärva en välskriven sammanfattning.

Samtidigt innehåller dess `evidence_score` rankningssignaler som textlikhet, aktualitet och sökmotorernas överensstämmelse. **Jag skulle inte behandla ett sådant värde som sannolikheten att ett påstående är sant.** fileciteturn21file0L1-L6

Flera sökmotorer som hittar samma sida är inte flera oberoende bekräftelser av sidans påstående.

### Gör inte varje verktyg till en ny planerare

Wigolo innehåller både en `research`-funktion och en `agent`-funktion med egna insamlingssteg. fileciteturn21file0L1-L6

För Nortropic skulle jag börja med de avgränsade verktygen: **sök, hämta, extrahera, återanvänd och jämför**.

Projektkontoret eller den befintliga workern kan behålla huvudansvaret för resonemanget. Vi behöver inte automatiskt en extra planerare som sammanfattar åt en annan planerare, som sedan sammanfattar åt Supervisor.

En avgränsad researchfunktion kan senare vara användbar som delegerad förmåga — men då med ett tydligt uppdrag och ett granskningsbart resultat.

## 6. Fyra saker jag inte skulle ta reklambudskapet som garanti för

**”Lokalt” betyder inte att sökfrågorna stannar på maskinen.** Säkerhetsdokumentationen säger uttryckligen att Wigolo ansluter till sökmotorerna och webbplatserna som frågorna riktas mot. En konfigurerad extern språkmodell är ytterligare en möjlig mottagare. Nortropic behöver därför kontrollera vad som får skickas ut, inte bara var cachen lagras. fileciteturn22file0L1-L6

**”Ingen avgift per fråga” betyder inte kostnadsfri drift.** Sökning, lokala modeller, webbläsare och underhåll använder din kapacitet. Jag har inga mätningar som visar hur den kombinerade arbetslasten beter sig på din M1 med 8 GB. Projektets cirka 1,5 GB för installation beskriver diskutrymme, inte hela minnesbehovet under användning. fileciteturn19file0L1-L2

**”Webbverktyg” betyder inte att allt är läsande.** Dokumentationen innehåller stöd för inloggade sessioner, klickande och skrivande i webbläsaren samt skapande av bevakningar och webhooks. Jag skulle inte ge en vanlig research-worker hela den ytan bara för att den behöver läsa offentliga dokument. fileciteturn21file0L1-L6

**Licensen behöver behandlas separat från teknikvalet.** Wigolo anger AGPL-3.0-only, medan det granskade LEANN-paketet anger MIT. Inför modifiering, distribution eller kundnära integration skulle jag granska den konkreta användningen, inte utgå från att villkoren är utbytbara. fileciteturn29file0L1-L6 fileciteturn23file0L1-L6 fileciteturn28file0L1-L6

Dessutom är projektet märkt **public beta**. Den jämförelse som README lyfter bygger på en fråga i en agentsession. Det är en demonstration, inte tillräckligt underlag för generell likvärdighet med andra söktjänster eller för en viss tidsbesparing i Nortropic. fileciteturn19file0L1-L2

## 7. Det försök jag skulle prioritera

Min föreslagna disposition är **`EXPERIMENT` inom informationsinhämtning**, med flera designmönster värda att ta med till Recompile oavsett produktval.

Jag skulle jämföra Wigolo med den enklaste fungerande baslinjen för några verkliga informationsuppgifter:

| Uppgift | Det viktiga testet |
|---|---|
| **Återkommande fråga** | Kan befintligt underlag återanvändas utan att hela insamlingen görs om? |
| **Ändrad källa** | Upptäcks förändringen utan att gammalt underlag presenteras som aktuellt? |
| **Detalj i tabell eller kod** | Går workern vidare från utdrag till den representation som faktiskt innehåller svaret? |
| **Ofullständig åtkomst** | Syns luckan i slutresultatet, eller försvinner den i sammanfattningen? |
| **Svensk fråga, blandade källspråk** | Hittas rätt material och används det korrekt? |

Den sista punkten är särskilt relevant för dig: den granskade standardkonfigurationen anger `BAAI/bge-small-en-v1.5` för semantisk cache. Vi bör mäta svensk återfinning i stället för att anta att modellen passar hela Nortropics korpus. fileciteturn27file0L1-L6

Mätningen ska handla om **tid till korrekt underlag, total uppgiftstid, omarbete, aktualitetsfel och resurskostnad**. Antalet hämtade sidor är inte ett framgångsmått i sig.

Först därefter skulle jag bedöma om LEANN ger en ytterligare vinst. Annars ändrar vi flera saker samtidigt och vet inte vad som hjälpte.

## Min slutsats

**Wigolo är kanske mest intressant som ett konkret exempel på hur informationsinhämtning kan bli återanvändbar, avgränsad och observerbar.** Men det ersätter inte arbetet med att strukturera betydelse, status och samband.

Jag skulle hålla ihop kedjan så här:

> **Informationsbehov → återanvänd eller hämta → bevara relevant källversion → analysera → pröva → besluta → återför erfarenheten.**

Wigolo kan bidra till hämtningen och återanvändningen. LEANN kan bidra till återfinningen över en indexerad korpus. **Nortropics informationsarkitektur måste göra det möjligt att följa vad materialet betyder och hur det används.**

Det mest värdefulla nästa steget är därför ett litet jämförelseförsök med informationsuppgifterna ovan — inte att göra något av projekten till ett nytt krav i den pågående Kernel-slutföringen.

**Målet är inte att Nortropic ska veta mer om allt. Målet är att rätt worker ska få rätt underlag, i rätt version, för nästa meningsfulla handling.**

---

## Meddelande 12 — Johnny (användare)

kör nästa steg

---

## Meddelande 13 — ChatGPT (assistent)

Jag kör ett avgränsat jämförelseprov här, separat från Nortropic-installationen. Fokus är informationsbesparing utan tappad källspårbarhet, missade tabeller/kod eller inaktuellt underlag.

---

## Meddelande 14 — ChatGPT (assistent)

**Första delprovet är kört. Det viktigaste fyndet är att information kan försvinna innan modellen ens får möjlighet att bedöma den.**

Det förändrar ordningen något: **vi bör först kontrollera att informationsvägen bevarar det som är viktigt — därefter mäta hur mycket söktid den sparar.**

En tydlig avgränsning: körmiljön kunde inte nå paketregistret, så jag kunde inte installera och köra hela Wigolo. Däremot körde jag utvalda originalfunktioner från den granskade källkoden, med kontrollerad filidentitet, på både konstruerade testfall och dina uppladdade Nortropic-texter. **Live-sökning, cache, modellrankning och tidsvinster är fortfarande oprövade.** Metod och råresultat finns i [experimentrapporten](sandbox:/mnt/data/NORTROPIC_INFORMATION_ACCESS_PROBE_2026-09-07.md).

## 1. Vad jag faktiskt jämförde

Jag undersökte fyra vägar från samma dokument: originaltexten, textdelarna som Wigolo gör till kandidater för sökutdrag, dess reservfunktion för utdrag utan rankningsmodell och hämtning av en uttryckligen angiven rubriksektion.

Provet omfattade **åtta konstruerade innehållsfall, fyra kontroller i dina tre uppladdade texter samt separata kontroller av källmarkörer och textpositioner**. De tre använda källkodsfilerna verifierades mot GitHubs filidentiteter för revision `c6ad447`.

Det är ett **komponentprov av informationsbevarande**, inte ett benchmark över hela produktens sökkvalitet. Testfallen valdes för att undersöka specifika begränsningar, så deras utfall ska inte omvandlas till ett generellt procentbetyg.

## 2. Sökuppdragets viktigaste detalj kan sorteras bort

Följande beteenden uppstod i provet:

| Testfall | Observerat beteende |
|---|---|
| Vanlig löptext på engelska och svenska | De utvalda svarspassagerna bevarades i kandidatunderlaget. |
| Svaret fanns endast i en tabell | Tabellen bidrog inte med någon textkandidat som innehöll svaret. |
| En viktig regel stod i en kort punkt eller ett kort blockcitat | Den exakta formuleringen sorterades bort. |
| Ett undantag stod sent i ett långt stycke | Undantaget föll utanför de första 500 strängpositionerna som behölls. |
| Svaret stod i ett senare stycke | Det fanns bland kandidaterna, men reservfunktionen valde i stället det första innehållsrika stycket. |

Beteendet stämmer med den granskade kodens längdgränser och filtrering av bland annat tabell-, rubrik- och kodblock. **Det betyder inte att hela Wigolo saknar andra vägar till informationen. Det betyder att den här utdragsvägen inte är en fullständig representation av källan.** fileciteturn32file0L2-L6

Det är särskilt viktigt för Nortropic. Det avgörande kan vara en enda kort mening:

> ”Gäller endast testmiljön.”

eller:

> ”Detta ersätter inte tidigare mandat.”

Att behålla bakgrundsresonemanget men tappa begränsningen kan ge workern ett mer lättläst — men sämre — beslutsunderlag.

### Samma mönster syntes i ditt material

I Recompile-underlaget finns formuleringen **`OWNER ATTENTION ≠ OWNER PERMISSION`**. Den står som en kort, separat princip. fileciteturn30file2

När jag körde texten genom kandidatfunktionen saknades **den exakta formuleringen** i resultatet. Den fanns däremot kvar vid hämtning av det relevanta originalavsnittet.

Även formuleringen *”behöver empiriskt test”* i dispositionstabellen föll bort från kandidatunderlaget. Detsamma gällde rubriken *”Pre-launch quality ≠ real-world quality”* i Digitala-underlaget. De fyra kontrollerna och deras ursprungliga radpositioner är dokumenterade i [råresultaten](sandbox:/mnt/data/NORTROPIC_INFORMATION_ACCESS_RESULTS_2026-09-07.json).

Detta bevisar inte att en modell aldrig skulle förstå principerna från andra formuleringar. Men det visar varför **ett urval av sökutdrag inte får ersätta råkällorna eller användas som bevis för att hela Improvements-korpusen har behandlats**.

## 3. Att hämta rätt avsnitt hjälpte — men var inte en universallösning

Den uttryckliga sektionsvägen bevarade svarstexten i sju av de åtta konstruerade fallen. Här var rätt rubrik angiven av testet; jag mätte alltså inte en agents förmåga att själv hitta den.

Det åttonde fallet gav ett oväntat fynd.

I ett Python-kodblock fanns en kommentar som började med `#`. Sektionsfunktionen tolkade kommentaren som en Markdown-rubrik, trots att den låg inne i kodblocket. Därför avslutades avsnittet före själva kodsvaret. När jag tog bort just kommentaren i ett separat kontrollfall kom svaret med. Det ursprungliga utfallet är bevarat, inte rättat till i efterhand. fileciteturn33file0L2-L6

**Slutsatsen är inte att vi behöver fler granskare överallt.** Min föreslagna tillämpning är att workern behöver kunna upptäcka ett otillräckligt underlag och gå vidare till en annan representation: hela avsnittet, tabellen, kodblocket eller originaltexten.

Det ger en mer användbar princip än ”hämta alltid kortare text”:

> **Hämta den minsta mängd information som fortfarande bevarar det som beslutet beror på.**

## 4. En källmarkör är inte samma sak som en källversion

Jag prövade också två versioner av ett syntetiskt dokument. Samma adress, samma textposition — men ett värde ändrades från **2 till 8**.

Källfunktionen gav båda samma `citation_id`. Det följer av att identifieraren beräknas från adress och startposition, inte från innehållets version. fileciteturn34file0L2-L6

Det är inte ett bevis på att cachen fungerar fel; cachen kördes inte. Det är ett konkret bevis på att **den identifieraren ensam inte skiljer de två innehållsversionerna åt**.

För Nortropic skulle jag därför vilja bevara skillnaden mellan:

**Var hittade vi informationen?**  
**Vilken textversion använde vi?**  
**Var i den versionen finns underlaget?**

En separat kontroll visade också att textpositionerna fungerade korrekt som JavaScript-strängpositioner, men inte som UTF-8-bytepositioner när svenska tecken och emoji förekom. Svenskan förstördes alltså inte — men andra komponenter måste förstå vilket positionssystem de får.

### Det fanns även användbara positiva signaler

Tomt innehåll gav inget påhittat utdrag. En saknad rubrik gav `matched: false`. En källhänvisning utan kvarvarande evidensutdrag saknade passageidentifierare.

**Sådana skillnader bör Nortropic bevara hela vägen till workern**, i stället för att jämna ut allt till ett till synes komplett svar.

## 5. Vad detta betyder för sfärerna

Det här gör sambandet mellan informationsarkitektur och arbetsflöde tydligare.

**Projekt- och innovationskontoret** behöver kunna återfinna själva vägvalet och dess begränsningar — inte bara text som liknar ämnet. Annars riskerar kontoret att återintroducera förkastade idéer eller behandla ett experimentförslag som en beslutad metod.

**Workers** behöver en snabb orienteringsväg, men också en tydlig väg vidare när uppgiften kräver exakta detaljer. Min hypotes är att detta kan minska både läsning och omarbete, men tidsvinsten återstår att mäta.

**Verifieringen** behöver kunna följa slutsatsen tillbaka till den faktiskt använda källversionen. Ett trovärdigt formaterat utdrag räcker inte i sig.

**Evolution Plane** behöver veta vilken version som tidigare stödde ett arbetssätt för att kunna bedöma betydelsen av en förändring.

Det kräver inte fyra nya subsystem. Jag skulle först pröva om samma lilla uppsättning egenskaper kan stödja alla fyra: **stabila källreferenser, bevarade versioner, tydlig information om hur texten hämtades och vägar tillbaka till originalet**.

## 6. Min uppdaterade rekommendation

**Wigolo är kvar som experimentkandidat. Att använda enbart dess sökutdrag som organisatoriskt beslutsunderlag är däremot inte en tillräcklig lösning.**

LEANN är fortfarande oprövat. Jag skulle inte lägga till det innan vi har skiljt mellan två problem:

> **Vi hittar inte rätt material.**

och:

> **Vi hittar rätt material, men tappar den viktiga informationen när vi gör det till arbetsunderlag.**

En annan sökmotor kan hjälpa med det första. Den löser inte automatiskt det andra.

Detta bör inte heller skapa nya rutinmässiga ägarstopp. Den föreslagna återhämtningen är normalt att workern, inom befintligt mandat, hämtar ett bättre underlag eller redovisar den konkreta luckan. Du ska inte behöva godkänna varje fördjupad läsning.

## Underlaget är klart för fortsättningen

Jag har samlat rapport, testfall, körkod, ursprungliga och uppföljande resultat samt en avgränsad instruktion för det återstående fullständiga körprovet i ett [reproducerbart provpaket](sandbox:/mnt/data/nortropic-information-access-probe-2026-09-07.zip). Inga ändringar har gjorts i Nortropics repos, Kernel eller din lokala konfiguration, och materialet är inte publicerat genom Intake.

Det återstående provet ska mäta **korrekt resultat och total arbetstid**, inklusive upprepade frågor, ändrade källor, kompletterande hämtningar och rättningar — inte bara hur snabbt en sökning returnerar något.

**Den viktigaste lärdomen hittills: vi ska inte bara göra kunskapen lättare att hitta. Vi måste se till att det som gör kunskapen användbar överlever vägen till workern.**

---

## Meddelande 15 — Johnny (användare)

fortsätt

---

## Meddelande 16 — ChatGPT (assistent)

Paketregistret är fortfarande otillgängligt, så jag fortsätter med lokala delprov av Markdown-bevarande, beslutsrelevanta begränsningar samt återanvändning med versionskontroll. Detta prövar informationsflödet, inte Wigolos sökkvalitet.

---

## Meddelande 17 — ChatGPT (assistent)

**Nästa delprov är kört. I det avgränsade försöket gick det att återfå de tidigare undersökta formuleringarna med en befintlig Markdown-parser — utan en extra agent eller en specialbyggd kunskapsplattform.**

Jag har också prövat återanvändning och versionskontroll mot en lokal testserver. Det gav en tydlig skillnad mellan **att redan ha information**, **att kontrollera om den har ändrats** och **att hämta hela innehållet igen**.

Fullständiga Wigolo är fortfarande inte kört: paketregistret gick inte att nå från körmiljön. De nya resultaten gäller en alternativ avsnittsläsning och egna, avgränsade testklienter — **inte Wigolos cache, LEANN eller uppmätt arbetstidsvinst i Nortropic**. Metod och resultat finns i [uppföljningsrapporten](sandbox:/mnt/data/NORTROPIC_INFORMATION_ACCESS_FOLLOWUP_2026-09-07.md).

## 1. Det tidigare textbortfallet gick att hantera med en standardkomponent

Förra gången såg vi hur tabeller, korta principer och delar av kodexempel kunde försvinna ur en viss utdragsväg.

Nu använde jag i stället en befintlig CommonMark-parser för att identifiera dokumentets riktiga rubriker och avsnitt. Därefter hämtades motsvarande text direkt ur originalet, utan omskrivning. Biblioteket har stöd för källradpositioner, vilket gör den sortens läsväg möjlig. citeturn559602search0turn559602search1

**Samtliga tolv förvalda formuleringar fanns kvar i den nya läsvägen:** åtta i de konstruerade fallen och fyra i dina uppladdade texter. Även Python-exemplet med en kommentar som började med `#` bevarades. De tidigare resultaten är oförändrade; detta är ett separat försök, inte en rättning av Wigolo. [Resultaten är dokumenterade här.](sandbox:/mnt/data/NORTROPIC_INFORMATION_ACCESS_FOLLOWUP_RESULTS_2026-09-07.json)

En viktig begränsning: **testet gav läsfunktionen rätt dokument och rubrik**. Jag har inte visat att en worker själv hittar rätt avsnitt eller tolkar det korrekt.

### Det gick också att leverera mindre text

För dina dokument såg det ut så här:

| Kontrollerat innehåll | Hela källan, tecken | Returnerat avsnitt, tecken |
|---|---:|---:|
| Ägaruppmärksamhet kontra ägartillstånd | 16 569 | 740 |
| Dispositionstabellen med bland annat `EXPERIMENT` | 16 569 | 1 163 |
| Kvalitet före lansering kontra verkliga utfall | 14 517 | 727 |
| Den äldre planen utan angiven avsnittsreferens | 4 874 | 4 874 |

Den fjärde kontrollen fick alltså fortfarande hela källan, uppdelad i fem delar. Testet saknade där en avsnittsreferens.

Detta är **textmängd som returnerades**, inte sparade token eller sparad arbetstid. Parsern läste fortfarande källtexten. Men försöket visar en användbar möjlighet: ett uppdrag kan få ett litet, exakt källavsnitt i stället för en sammanfattning som riskerar att tappa begränsningarna. [Se avsnitt 2 i rapporten.](sandbox:/mnt/data/NORTROPIC_INFORMATION_ACCESS_FOLLOWUP_2026-09-07.md)

**Min slutsats för Nortropic:** innan vi bygger avancerade lösningar bör vi undersöka hur långt tydliga referenser och välfungerande avsnittsnavigation räcker.

## 2. Återanvändning och aktualitet behöver vara olika operationer

Nästa försök använde en lokal testserver med ett påhittat dokument. Där ändrades ett värde från **2 till 8**, samtidigt som adressen var oförändrad.

Jag jämförde tre enkla beteenden:

**Hämta alltid:** läs innehållet från servern vid varje förfrågan.

**Återanvänd efter ålder:** använd den sparade kopian så länge en bestämd tidsgräns inte passerats.

**Låt frågan styra:** återanvänd för vanlig orientering, men kontrollera källan när uppgiften uttryckligen kräver en aktuell kontroll.

Det tredje alternativet använde HTTP:s villkorliga hämtning. När innehållet var oförändrat kunde servern svara `304 Not Modified`, så att den sparade representationen kunde återanvändas utan att hela innehållet skickades igen. Det är en etablerad mekanism, inte något Nortropic behöver uppfinna. citeturn559602view0

I huvudsekvensens sju steg blev utfallet:

| Testbeteende | Förfrågningar till servern | Fullständiga innehållssvar | Svar som bekräftade oförändrat innehåll |
|---|---:|---:|---:|
| Hämta alltid | 7 | 6 | 0 |
| Enbart tidsbaserad återanvändning | 2 | 2 | 0 |
| Behovsstyrd återanvändning och kontroll | 6 | 2 | 3 |

Servern var tillfälligt otillgänglig i ett steg, vilket förklarar att alla förfrågningar inte gav innehåll. Samma sekvens kördes tre gånger per beteende, i växlande ordning, med samma utfall. Det visar reproducerbarhet i detta kontrollerade exempel — inte generell prestanda. [De faktiska förfrågningarna finns i råresultaten.](sandbox:/mnt/data/NORTROPIC_INFORMATION_ACCESS_FOLLOWUP_RESULTS_2026-09-07.json)

### Skillnaden blev tydlig när värdet ändrades

Den rent tidsbaserade klienten behöll **2** efter att källan ändrats till **8**, eftersom tidsgränsen ännu inte passerats. Den redovisade återanvändning och påstod inte att den hade kontrollerat källan på nytt.

Den behovsstyrda klienten fick **8** när uppgiften begärde en aktuell kontroll.

Det är inte ett påstående om att tidsbaserad cache är felaktig. Det visar att:

> **”Den här kopian är tillräckligt ny enligt vår cacheinställning” och ”vi har kontrollerat källan för det här beslutet” är olika påståenden.**

För Nortropic skulle jag därför vilja låta informationsbehovet styra:

**”Vad diskuterade vi förra veckan?”** behöver ofta den bevarade historiska versionen.

**”Vad säger den aktuella dokumentationen?”** kan kräva en ny kontroll.

**”Hjälp mig orientera mig i projektet.”** kan ofta börja med befintligt underlag.

Det betyder inte att allt ska kontrolleras hela tiden. Tvärtom kan en sådan uppdelning göra det lättare att **undvika kontroller som inte behövs**.

## 3. Ett fel behöver inte förstöra historiken eller stoppa annat arbete

Jag lade även in ett steg där testservern svarade med ett tillfälligt fel.

I den behovsstyrda klienten blev beteendet:

**Den gamla källversionen fanns kvar. Den misslyckade kontrollen var synlig. Tidpunkten för senaste lyckade kontroll flyttades inte fram.**

Efter att den aktuella versionen ändrats gick det dessutom att uttryckligen hämta den äldre versionen med värdet **2**, utan ett nytt serveranrop. Den märktes som historisk, inte aktuell. En saknad källa gav inget påhittat innehåll, och en efterföljande förfrågan till en annan testkälla kunde genomföras. [Se avsnitt 3 i rapporten.](sandbox:/mnt/data/NORTROPIC_INFORMATION_ACCESS_FOLLOWUP_2026-09-07.md)

Detta är inte en verifiering av Supervisors återhämtning. Men det ger en konkret arbetsmodell att pröva:

> **Bevara det som fortfarande är användbart, avgränsa det som är osäkert och fortsätt med oberoende arbete.**

Det passar ditt önskemål om färre onödiga ägarstopp. En misslyckad informationshämtning bör normalt först leda till en annan tillåten informationsväg eller ett tydligt partiellt resultat — inte automatiskt en fråga till dig.

## 4. Den viktigaste kvarvarande begränsningen: rätt avsnitt kan ändå vara otillräckligt

Jag gjorde också en kontroll som medvetet visar vad den förbättrade läsvägen **inte** löser.

I ett avsnitt stod ett kapacitetsvärde. I ett annat stod begränsningen att värdet bara gällde syntetiska testuppgifter.

Avsnittsläsningen hämtade det första avsnittet korrekt — men fick inte med begränsningen från det andra.

Det är inget textbortfall inom det valda avsnittet. Det är ett **urvalsproblem**: rätt text har hämtats, men kanske inte all text som beslutet behöver. [Kontrollen finns med i råresultaten.](sandbox:/mnt/data/NORTROPIC_INFORMATION_ACCESS_FOLLOWUP_RESULTS_2026-09-07.json)

Därför behöver vi skilja mellan tre frågor:

**Är underlaget korrekt återgivet?**  
Har vi bevarat texten, versionen och sammanhanget utan förvanskning?

**Är underlaget tillräckligt aktuellt?**  
Passar källversionen den fråga vi försöker besvara?

**Är underlaget tillräckligt för beslutet?**  
Saknas en begränsning, ett motargument eller ett relevant tidigare vägval?

De två första går delvis att stödja med strukturer och kontroller. Den tredje kräver fortfarande uppgiftsförståelse och bedömning.

**En bättre parser löser inte hela informationsarkitekturen. Men den kan ta bort ett onödigt fel innan analysen börjar.**

## 5. Så förtydligar detta sambanden mellan sfärerna

Min uppdaterade arbetshypotes är att sfärerna inte behöver varsin egen kunskapsmaskin. De behöver kunna använda samma underlag med **olika frågor och olika krav på aktualitet och sammanhang**.

**Projekt- och innovationskontoret** behöver kunna skilja historisk motivering från nuvarande beslutsgrund. När du återkommer till en idé ska kontoret kunna hitta vad som diskuterades och varför ett alternativ valdes bort — utan att behandla varje gammalt resonemang som ett aktuellt krav.

**Workers** behöver kunna börja med ett begränsat arbetsunderlag och själva fördjupa läsningen när uppgiften kräver det. Det viktiga är inte att alltid läsa mindre, utan att undvika både överläsning och för tunt underlag.

**Verifieringen** behöver kunna följa slutsatsen till rätt källversion och se vilka luckor som fanns när den formades.

**Evolution Plane** behöver kunna koppla en förändrad källa till de metoder och uppdrag som faktiskt använder den. Versionsinformationen är ett underlag för den kopplingen; själva beroendehanteringen har inte byggts eller testats här.

**Aquarium** behöver visa senaste lyckade observation och aktuella luckor, inte förväxla en avsikt att kontrollera något med en genomförd kontroll.

Detta ligger nära principen i ditt Recompile-underlag: råkällorna ska överleva, medan syntesen får vara utbytbar och omprövbar. fileciteturn35file2

### ”Suggest next interaction” blir då mer konkret

Nästa steg kan väljas efter vilken sorts brist vi har:

**Saknad information:** sök eller hämta.

**Oklar aktualitet:** kontrollera källan.

**Ofullständigt avsnitt:** följ en relevant referens eller läs vidare.

**Motstridiga uppgifter:** jämför underlagen.

**Ett verkligt vägval om mål eller prioritering:** fråga dig.

Detta är ett förslag till arbetsbeteende — inte en ny permanent agent eller en förändring av mandatet.

## 6. Vad vi tar vidare nu

**Wigolo är kvar som `EXPERIMENT`. LEANN är fortfarande oprövat.** Det finns ännu inget underlag för att installera båda eller påstå att de sparar arbetstid i Nortropic.

Det som stärkts är en enklare designhypotes:

> **Bevara källorna, gör dem lätta att navigera och låt uppgiften avgöra när information ska återanvändas, kontrolleras eller kompletteras.**

De nya testklienterna är just testinstrument. De ska inte bli början på ett eget webb- eller cachesystem bara för att de fungerade i försöket.

All körkod, oförändrade testfall, resultat och instruktioner för det återstående fullständiga provet finns i [det reproducerbara uppföljningspaketet](sandbox:/mnt/data/nortropic-information-access-followup-2026-09-07.zip). Nortropics repos, Kernel och lokala konfiguration är orörda; materialet är inte publicerat genom Intake.

**Nästa avgörande mätning är fortfarande en verklig worker-jämförelse i en miljö som kan köra hela verktyget.** Fler lokala parser- och cacheprov skulle inte besvara den frågan.

Det vi nu har är ett bättre försöksunderlag och en tydligare förenklingsriktning:

**Nortropic ska slippa läsa om allt — utan att behöva fatta beslut på för lite.**

---

## Meddelande 18 — Johnny (användare)

Fortsätt

---

## Meddelande 19 — ChatGPT (assistent)

Paketregistret är fortsatt otillgängligt och ingen Codex-worker finns här, så jag ersätter inte helhetsprovet med fler parserprov. Jag färdigställer i stället jämförelseupplägget med separat facit och underbyggnadsbedömning.

---

## Meddelande 20 — ChatGPT (assistent)

**Jag har nu färdigställt själva workerprovet: 12 uppgifter, bevarade källor, separat facit och en samlad körinstruktion.** Det som återstår är att köra jämförelsen med riktiga workers och hela Wigolo.

Den körningen är **inte gjord här**. Paketregistret går fortfarande inte att nå från körmiljön, och här finns ingen Codex-worker att starta. Vi har därför fortfarande inga uppmätta tidsvinster eller resultat från en fullständig workerjämförelse.

**Nästa steg behöver nu ske i en separat Codex-session — inte i sessionen som färdigställer Kernel.**

[Hämta det samlade provpaketet](sandbox:/mnt/data/nortropic-information-access-worker-pack-2026-09-07.zip)

## 1. Nu finns konkreta uppgifter — inte bara en plan att ta fram dem

Provet undersöker om workern kan hitta, förstå och använda underlaget korrekt, även när ett snabbt sökutdrag inte räcker.

| Område | Vad workern behöver klara |
|---|---|
| **Principer och märkning** | Skilja ägaruppmärksamhet från ägartillstånd och förstå vad `EXPERIMENT` faktiskt betyder. |
| **Digitalas kvalitet och utfall** | Skilja tester före lansering från verkliga resultat, och ett illustrativt räkneexempel från en uppmätt förbättring. |
| **Historik och aktuellt läge** | Jämföra två planeringsdiskussioner utan att förvandla dem till en påhittad aktuell körorder eller ett bevis på färdig Kernel. |
| **Detaljer och begränsningar** | Hitta ett värde i ett kodblock och upptäcka en avgörande begränsning som står i ett annat avsnitt. |
| **Återanvändning och förändring** | Besvara en återkommande fråga, kontrollera en ändrad källa och fortsätta med oberoende arbete när en annan källa är otillgänglig. |

Uppgifterna använder dina tre uppladdade diskussionstexter samt tydligt märkta, fiktiva testdokument. Originaltexterna är inte omskrivna till ”gällande policy”.

Det är särskilt viktigt eftersom Recompile-underlaget självt skiljer mellan råkällor, härledd syntes och vad som faktiskt fortfarande gäller. fileciteturn37file2

### Några uppgifter ska ge svaret ”detta är inte styrkt”

Exempelvis:

> **”Visar det tillhandahållna materialet att Autonomy Kernel v1 faktiskt är färdig och fryst nu?”**

En worker som besvarar det med ett självsäkert ja utifrån en gammal plan har inte löst uppgiften.

Det korrekta beteendet är att skilja **beskrivningen av en önskad checkpoint** från **evidens för att checkpointen har uppnåtts**.

Samma sak gäller Digitala-textens exempel med 12 respektive 19 leads per månad: det ska inte återkomma som en uppmätt Nortropic-framgång bara för att siffrorna är lätta att hitta. fileciteturn37file0

**Det är den typen av informationsfel vi vill fånga innan vi börjar belöna snabbare sökning.**

## 2. Jämförelsen prövar nyttan av att lägga till Wigolo

Jag har preciserat de två alternativen:

**A — Enkel baslinje:** befintliga verktyg för direkt läsning, textsökning och dokumentnavigation.

**B — Samma baslinje plus Wigolo:** identiska grundförutsättningar, men workern får dessutom använda Wigolos relevanta läsverktyg.

Det betyder att vi inte tvingar workern att använda Wigolo när en vanlig läsning är bättre. Vi prövar i stället:

> **Blir arbetet bättre av att förmågan finns tillgänglig?**

Båda alternativen ska ha samma modell, instruktioner, källor och resursgränser. Användningen av Wigolo ska registreras; en körning där workern aldrig använder det säger inget om verktygets bidrag.

Wigolo dokumenterar en kommandoradsyta med JSON-svar, så försöket behöver inte börja med att ändra din globala MCP-konfiguration. Den faktiska installationens beteende måste ändå kontrolleras i körmiljön. fileciteturn40file0L2-L6

**LEANN läggs inte till samtidigt.** Annars riskerar vi att inte kunna avgöra vilken förändring som hjälpte.

## 3. Facit hålls skilt från det workern får se

Det finns nu ett separat bedömningsunderlag med nödvändiga sakuppgifter, begränsningar och källstöd.

Workern ska få **frågan, en neutral källförteckning och sina läsverktyg** — inte rätt rubrik, rätt textposition eller det förväntade svaret.

Detta tar oss förbi begränsningen i det tidigare avsnittsprovet, där rätt dokument och rubrik redan var angivna.

Men separationen behöver vara verklig. En annan mapp eller instruktionen ”läs inte facit” bevisar inte att facit är otillgängligt. Körinstruktionen kräver därför att åtkomsten och de nya workersessionerna kontrolleras. En körning utan sådan separation får fortfarande vara ett funktionstest, men ska inte beskrivas som en kontrollerad jämförelse.

Bedömningen ska heller inte begränsas till att en viss textsträng finns i svaret. **Workern måste använda informationen rätt och behålla de avgörande reservationerna.**

## 4. Det som faktiskt är kontrollerat här

Jag har kontrollerat paketets källidentiteter, uppgifternas koppling till bedömningsunderlaget och de 25 citerade källankarna.

Stödskripten har också kontrollerats: de kan tillhandahålla originaltexten, byta en fiktiv källversion på samma adress, returnera ett kontrollerat tillgänglighetsfel och förbereda endast de avsedda uppgiftsfilerna.

**Detta är kontroller av försöksunderlaget — inte resultat för Wigolo eller workers.** Antalet verkliga workerkörningar är fortfarande **0**.

[Status och avgränsningar finns samlade här](sandbox:/mnt/data/NORTROPIC_INFORMATION_ACCESS_WORKER_READY_2026-09-07.md).

## 5. Den praktiska överlämningen

Paketet innehåller en fullständig `START_HERE.md`. Första körningen är en **avgränsad pilot**, med en worker åt gången och högst 60 minuter inklusive förberedelser. Det större repetitionsprovet ligger separat; en pilot får inte presenteras som hela resultatet.

Inga Nortropic-repos, Kernel, Bootstrap, Intake eller globala agentinställningar ska ändras. Provet ska inte konkurrera med resurser som behövs för Kernel-arbetet.

Öppna **en ny, fristående Codex-session**, bifoga provpaketet och använd denna instruktion:

```text
Kör den avgränsade Nortropic information-access-piloten enligt
START_HERE.md i det bifogade provpaketet.

Du är försöksledare, inte den worker som utvärderas. Använd en
separat tillfällig arbetsmiljö och lämna pågående Kernel-arbete,
Nortropics repos, Bootstrap, Intake och globala inställningar orörda.

Kontrollera först att paketet, den faktiska Wigolo-installationen
och workeråtkomsten fungerar. Håll facit och tidigare resultat
borta från de workers som ska prövas.

Jämför den enkla baslinjen med samma baslinje plus Wigolo.
Använd samma modell och villkor. Lägg inte till LEANN.

Börja med protokollets första repetition inom den angivna tids-
och resursramen. Redovisa verkliga svar, fel, kompletterande
läsningar och total arbetsinsats. Saknade eller okörda delar ska
stå som NOT_RUN, inte ersättas med simulerade produktresultat.

Avsluta med vad försöket faktiskt visar och vad som fortfarande
är oprövat. Gör ingen installation i Nortropic och ingen publicering.
```

[Körinstruktionen finns även som separat fil](sandbox:/mnt/data/NORTROPIC_INFORMATION_ACCESS_WORKER_HANDOFF_2026-09-07.md).

**Nu är det dags att låta verkligt arbete avgöra teknikvalet. Vi har tillräckligt underlag för att pröva frågan — inte ännu för att säga att något av verktygen har förtjänat en plats i Nortropic.**

