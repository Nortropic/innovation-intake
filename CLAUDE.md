# Nortropic innovation-intake — idékorpusen

Detta repo är korpusen/idébanken som skillen `nortropic-intake`
(`~/.claude/skills/nortropic-intake/`) levererar till. Varje idé är en låda med tre
papper: byggritningen (briefen = VAD), designrationalen (= VARFÖR) och dagboken
(transkriptet = RÅ BEVISNING). Briefen styr; rationalen förklarar designlogiken vid
behov; transkriptet slås upp i riktade meddelandeintervall.

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
- `INDEX.md` — en rad per idé (aldrig per fil): `slug | title | status | created | links`.
  Upsertas vid varje leverans och statusbyte. Börja där för att se vad som finns.
- Idémappen ligger **direkt i repo-roten** (`<slug>/`, inte `ideas/<slug>/`).

## Progressiv exponering & auktoritet

Läsordning efter roll: implementerare → briefen; arkitekt/planerare/granskare → briefen,
+ rationalen när den gör materiell nytta; exakt proveniens → riktade transkriptintervall,
inget mer. Auktoritetsordning (högst vinner): gällande kanonisk repo-auktoritet
(konstitution, regelverk, godkänd arkitektur) → senare ägargodkänd spec/arkitektur/plan →
brief → rationale → transkript. Inom ett intake-paket tolkas brief > rationale >
transkript. Intake bevarar intention och proveniens — det är aldrig exekveringsauktoritet.

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
  plan mode → bygg i färsk session → adversariell granskning.

## Trust-lagret (invarianter)

Det ingen brief får bryta ägs av konstitutionen och regelverket:
`~/nortropic/nortropic-system/docs/07-konstitution.md` och
`~/nortropic/nortropic-system/docs/03-regelverk.md` — trust-kontrakt, frusna grindar,
§-regler. Briefer **pekar** dit (en rad i §2 och §6); de kopierar aldrig innehållet.

## Vad som INTE händer här

Skillen skriver filer och indexrader — den committar inte, pushar inte och laddar inte
upp till Drive. Git-historik är Johnnys explicita beslut.
