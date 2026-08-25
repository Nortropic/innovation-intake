# Nortropic innovation-intake — idékorpusen

Detta repo är korpusen/idébanken som skillen `nortropic-intake`
(`~/.claude/skills/nortropic-intake/`) levererar till. Varje idé är en låda med tre
papper: byggritningen (briefen = VAD), designrationalen (= VARFÖR) och dagboken
(transkriptet = RÅ BEVISNING). Briefen styr; rationalen förklarar designlogiken vid
behov; transkriptet slås upp i riktade meddelandeintervall.

Efter att ägaren godkänt en plan i Plan Mode läggs ett fjärde papper i lådan: den
godkända planen (= HUR och i vilken ordning). Paketmodellen:

    FÖRE PLAN    VAD (brief) / VARFÖR (rationale) / RÅ (transkript)
    EFTER PLAN   VAD / VARFÖR / RÅ / GODKÄND PLAN (exekveringsordning)

## Struktur

- `<slug>/idea-<slug>.md` — briefen: beslut (inkl. förkastade vägar) med proveniens
  `(← msg N)`, EARS-acceptanskriterier, öppna frågor. Det agenten planerar och bygger
  från — den enda intake-fil en byggsession laddar som standard.
- `<slug>/<slug>-design-rationale.md` — designrationalen: resonemangskedjor, förkastanden
  med vilket haveri de skulle skapa, avvägningar, hämtkarta (ämne → meddelandeintervall).
  Läses på begäran när designlogik behövs; aldrig förladdad. (Idéer fångade före
  trekontraktet saknar den — det flaggar backfill, inte fel.)
- `<slug>/<slug>-full-chat.md` — det ordagranna transkriptet, fail-closed-verifierat och
  orörligt efter verifierad capture. Riktade meddelandeintervall hämtas via subagent när
  rationalen inte räcker eller exakt formulering spelar roll; aldrig förladdat.
- `<slug>/<slug>-approved-plan.md` — den godkända planen: exakt den plan ägaren godkände
  i Plan Mode, i sin helhet (exekveringsordning, avgränsningar, beslut, uppskjutet,
  förkastat, ägaröverlämningar, stoppvillkor, acceptanskriterier, nuvarande/nästa
  skiva, precedensplåster). Skapas **aldrig** före godkännandet och aldrig ur briefen.
  Version N≥2 heter `<slug>-approved-plan-v<N>.md`. Läses tillsammans med briefen i en
  exekveringssession.
- `INDEX.md` — en rad per idé (aldrig per fil): `slug | title | status | created | links`.
  Upsertas vid varje leverans och statusbyte. Börja där för att se vad som finns.
  Planfilen får **ingen egen rad** — indexet är inte en filförteckning.
- Idémappen ligger **direkt i repo-roten** (`<slug>/`, inte `ideas/<slug>/`).

## Progressiv exponering & auktoritet

Läsordning efter roll: implementerare → briefen (+ den godkända planen när en sådan
finns); arkitekt/planerare/granskare → briefen, + rationalen när den gör materiell nytta;
exakt proveniens → riktade transkriptintervall, inget mer. Auktoritetsordning (högst
vinner): gällande kanonisk repo-auktoritet (konstitution, regelverk, godkänd arkitektur) →
senare ägargodkänd spec/arkitektur/plan → godkänd intake-plan → brief → rationale →
transkript. Inom ett intake-paket tolkas godkänd plan > brief > rationale > transkript.
Intake bevarar intention och proveniens — det är aldrig exekveringsauktoritet.

Den godkända planen är den starkaste intake-artefakten och ändå inte auktoritet: den kör
aldrig över konstitutionen, regelverket, frusna grindar, gällande publicerad
produktionssanning eller en senare ägargodkänd övergång. Den är inte en andra runtime,
inte en andra sanningskälla och inget exekveringstillståndsregister. Går plan och
gällande repo-sanning isär vinner repot och avvikelsen rapporteras till ägaren — den
löses aldrig tyst till planens fördel.

## Konventioner

- Statuslivscykel i briefens frontmatter: `idea → clarified → planned → building →
  verified`; terminal: `superseded`. (`ready-for-clarification` i äldre briefer är det
  gamla namnet på `idea`.) `idea` = ligger i banken med öppna frågor intakta; `clarified`
  = ägarintervjun är gjord och idén är redo att planeras.
- Korslänkar i frontmatter, satta av korpus-kollen (Phase 2.8 i skillen):
  `supersedes: [slug]`, `superseded_by: <slug>` (på den gamla briefen, tillsammans med
  `status: superseded`), `related: [slug, …]`. Aldrig tysta dubbletter — vid trolig
  dubblett/evolution frågas ägaren.
- En idé dras till bygge via skillens implementera-nu-flöde, startat från den lagrade
  briefen: korpus-omkoll → Phase 2.5-intervju (öppna frågor) → `status: clarified` →
  plan mode → **ägaren godkänner planen** → planen sparas, valideras och binds →
  `status: planned` → bygg i färsk session → adversariell granskning.

## `planned` är ett mekaniskt tillstånd

`status: planned | building | verified` är giltigt **endast** när briefen är bunden till
en giltig godkänd plan: filen finns, dess sha256 matchar `approved_plan_sha256`, den bär
rätt slug och ägargodkännandemetadata, och den är den aktuella (ej ersatta) versionen.
Saknas det får statusen inte gå förbi `clarified`. Det är inte en regel på papperet —
den valideras:

```bash
python3 ~/.claude/skills/nortropic-intake/scripts/plan_contract.py validate
```

Samma kontroll finns som commit-grind i `hooks/pre-commit`, så att ett obevisbart
tillstånd inte når git-historiken. Git spårar inte `.git/hooks`, så installationen är ett
steg per klon (och `--no-verify` är ägarens uttryckliga val, aldrig ett default):

```bash
chmod +x hooks/pre-commit
ln -sf ../../hooks/pre-commit .git/hooks/pre-commit
```

Grinden är en grind, inte en mur: `--no-verify` går förbi den, och den släpper igenom om
skillen inte är installerad på maskinen — båda är ägarens uttryckliga val. Den upptäcker
tillståndet men kan inte tvinga fram att Phase 4 körs alls, och kan inte bevisa att
planens text är trogen det ägaren godkände. Det första är skillens instruktion, det andra
är disciplin.

Bindningen står i briefens frontmatter (`approved_plan`, `approved_plan_sha256`,
`plan_version`, `plan_approved_at`). Briefen **pekar** på planen — den kopierar den
aldrig. En kort exekveringsprompt är inte planen; den får peka på planen, aldrig ersätta
den.

Planen skrivs aldrig om tyst efter godkännande. Vid medvetet omtag: den gamla filen
behålls med `status: superseded` + `superseded_by_plan`, den nya får
`supersedes_plan` + nästa `plan_version`, och briefens pekare flyttas medvetet.

**Saknad plan på `planned`/`building`** rapporteras som `LEGACY_PLAN_ARTIFACT_MISSING`
och är ett fel, inte en varning. Enda tillåtna vägen tillbaka är avgränsad och manuell:
ägaren pekar ut den kända källan, planen sparas med
`plan_source: recovered-from-known-source` och `fidelity: partial`, ägaren verifierar,
sedan binds den. Transkriptet skrapas aldrig automatiskt, och en modellrekonstruktion
godtas aldrig som plan. Finns ingen känd källa är det ärliga utfallet `status: clarified`
och en ny planering.

## Efter komprimering och i en färsk session

Den varaktiga planen ligger på disk; minnet behöver bara hitta tillbaka till den.
En återupptagande session — efter `/compact`, automatisk komprimering, eller helt ny —
kör:

```bash
python3 ~/.claude/skills/nortropic-intake/scripts/plan_contract.py \
    resume --slug <slug> --target-repo <repo>
```

och får `PLAN_IDENTITY=<sökväg>@sha256:<hash>`, `PLAN_STATUS`, brief-sökväg och
repo-evidens. **Läs sedan om den godkända planen från disk innan du härleder framtida
arbete**, och stäm av den mot repots faktiska tillstånd. Rekonstruera aldrig en saknad
plan ur samtalsminne, ur ett utkast eller ur transkriptet; kan planen eller dess
registrerade identitet inte bevisas: STOPPA med `PLAN_IDENTITY_UNAVAILABLE`.

En eventuell pekare i målrepots `CLAUDE.md` (`ACTIVE_INTAKE_SLUG`,
`ACTIVE_APPROVED_PLAN_PATH`, `ACTIVE_APPROVED_PLAN_SHA256`, `TARGET_REPO`,
`CURRENT_EXECUTION_POINTER`) är en **cache, inte tillstånd**. Nuvarande position räknas
om genom att jämföra planen med repots tillstånd. Krockar pekaren med repo-evidens vinner
repot och avvikelsen rapporteras.

## Trust-lagret (invarianter)

Det ingen brief får bryta ägs av konstitutionen och regelverket:
`~/nortropic/nortropic-system/docs/07-konstitution.md` och
`~/nortropic/nortropic-system/docs/03-regelverk.md` — trust-kontrakt, frusna grindar,
§-regler. Briefer **pekar** dit (en rad i §2 och §6); de kopierar aldrig innehållet.

## Vad som INTE händer här

Skillen skriver filer och indexrader — den committar inte, pushar inte och laddar inte
upp till Drive. Git-historik är Johnnys explicita beslut.
