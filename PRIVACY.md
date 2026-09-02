# Zásady ochrany soukromí – aplikace Okolník

*Platné od 2. 9. 2026*

Aplikace **Okolník – vyhledávač míst v okolí** (dále „aplikace") respektuje
vaše soukromí. Tento dokument popisuje, jaké údaje aplikace zpracovává, proč
a jaká máte práva. Zpracování probíhá v souladu s nařízením (EU) 2016/679
(GDPR). Provozovatelem je **Stanislav Mudra**, e-mail: stamu.apps@gmail.com.

## Shrnutí

Základní aplikace **nevyžaduje účet a neshromažďuje osobní údaje spojené
s vaší osobou** a nemá vlastní servery pro vaše data. Volitelně si můžete
zapnout **žebříček na okolnik.cz** nebo hrát **týmovou hru Dobyvatel** –
obojí vyžaduje přihlášení (Google, nebo e-mail a heslo) a teprve tím
začne aplikace odesílat herní údaje popsané níže; výchozí stav je
vypnuto a dá se kdykoli zrušit. Poloha, trasa, deník, výpravy
i fotky zůstávají uložené jen ve vašem telefonu. Na server správce posíláte
to, co sami odešlete (návrh místa, hlasování, zpětná vazba) – bez jména či
e-mailu; aplikace navíc odesílá **souhrnné statistiky používání**
(lze vypnout v nastavení). Některé funkce se dotazují veřejných služeb
třetích stran (mapy, OpenStreetMap, Wikipedie). Hlášení „místo už neexistuje"
se zveřejní jako veřejná poznámka v OpenStreetMap. Bezplatná verze zobrazuje
reklamy Google AdMob, které v EU vyžadují váš souhlas.

## Poloha

Aplikace používá polohu zařízení (GPS) k zobrazení vaší pozice a míst
v okolí na mapě a v seznamu a k hernímu „vybarvování" navštívených oblastí.
**Poloha se zpracovává ve vašem zařízení** a neukládá se na servery správce.
Některé funkce ale potřebují poslat přibližnou polohu veřejné službě třetí
strany, aby fungovaly: načtení mapových dlaždic, načtení veřejných poznámek
OpenStreetMap v hrubém okolí (~±30 km) kolem vás a načtení popisku
zobrazovaného místa z Wikipedie.

Volitelně lze v nastavení zapnout **zaznamenávání trasy na pozadí** (např.
při zhasnutém displeji). Funkce je ve výchozím stavu vypnutá, běží jako
viditelná služba s trvalým oznámením a zaznamenaná trasa zůstává jen ve
vašem zařízení. Oprávnění k poloze můžete kdykoli odebrat v nastavení
systému; aplikace pak nabídne omezený režim.

**Navigace:** při volbě „Navigovat" aplikace předá cíl (a u služby Mapy.com
i vaši výchozí polohu) navigační aplikaci či webu dle vaší volby (Google
Mapy, Mapy.com / Seznam.cz, Waze). Tyto služby mají vlastní zásady.
U nádraží a zastávek lze obdobně otevřít odjezdovou tabuli ve službě
**IDOS** – předá se jen název zastávky, nikoli vaše poloha.

## Data, která zůstávají jen ve vašem zařízení

Zaznamenaná trasa a „objevené" oblasti, turistický deník a výpravy (zápisy,
poznámky, fotografie), vlastní a oblíbená místa, úspěchy i nastavení se
ukládají **pouze lokálně ve vašem zařízení** a nikam se neodesílají. Smažete
je v aplikaci, vymazáním dat aplikace nebo její odinstalací. Systém Android
může data aplikace zálohovat do vašeho účtu Google (lze vypnout v nastavení
telefonu); aplikace navíc umí ruční export zálohy (ZIP).

## Reklamy (Google AdMob)

Bezplatná verze zobrazuje reklamní banner služby **Google AdMob**. Google
a partneři mohou v souvislosti s reklamami zpracovávat reklamní
identifikátory zařízení, IP adresu a údaje o interakci s reklamou dle svých
zásad: https://policies.google.com/privacy a
https://support.google.com/admob/answer/6128543.

V zemích EU/EHP se před zobrazením personalizovaných reklam zobrazí
**formulář souhlasu (GDPR)**, kde můžete personalizaci odmítnout. Volbu lze
později změnit v nastavení aplikace, případně omezit personalizaci a
resetovat reklamní ID v nastavení systému Android.

## Údaje, které sami odešlete

- **Do databáze správce (Google Firebase / Firestore):** návrh nového místa
  (název, kategorie, poznámka, souřadnice, verze aplikace, pseudonymní
  kód instalace proti spamu), hlas o aktuálnosti místa (+1 k počítadlu)
  a dobrovolná zpětná vazba (text + verze aplikace). Neodesílá se jméno,
  e-mail, telefon ani vaše poloha. Kód instalace lze obnovit smazáním dat
  aplikace (viz vysvětlení níže).
- **Veřejně do OpenStreetMap:** hlášení „místo už neexistuje / je mimo
  provoz" vytvoří po vašem potvrzení **veřejnou anonymní poznámku** trvale
  dohledatelnou na openstreetmap.org (obsahuje název a souřadnice místa),
  aby mapu opravili dobrovolníci OpenStreetMap.
- **Plán výletu po cestách (Mapy.com):** když uložíte plán se dvěma
  a více zastávkami, odešlou se **souřadnice zastávek plánu** přes náš
  server službě Mapy.com (Seznam.cz, a.s.) k výpočtu trasy po cestách.
  Posílají se jen body plánu, nikdy vaše poloha ani jméno; služba má
  vlastní zásady (https://www.seznam.cz/ochrana-udaju). Bez přihlášení
  nebo bez sítě zůstane plán vzdušnou čarou a nic se neodesílá.
- **Sdílení:** obsah (např. karta výpravy) předáte přes systémovou nabídku
  tam, kam sami zvolíte.


**Co je identifikátor instalace.** Náhodně vygenerovaný kód, který vznikne
při prvním spuštění a zůstává stejný, dokud aplikaci nesmažete. Neobsahuje nic
o vás ani o telefonu a sami k němu nemáme žádné jméno ani e-mail. Protože je
ale *trvalý* a odlišuje jednu instalaci od druhé, považujeme ho podle GDPR
(recitál 26) za **pseudonymizovaný osobní údaj** – ne za anonymní. Slouží jen
k tomu, abychom u zpětné vazby dohledali váš případ, omezili spam u návrhů
a hlasování a mohli ručně přiznat prémiový přístup konkrétní instalaci
(testeři, výherci). K ničemu jinému ho nepoužíváme.

## Žebříček a účet na webu (dobrovolné)

Mapa, objevování, deník i výpravy fungují bez účtu a bez připojení
k webu. Žebříček, hra Dobyvatel a soutěže vyžadují **přihlášení** –
účtem Google, nebo e-mailem a heslem (spravuje služba Firebase
Authentication společnosti Google; z účtu Google aplikace dostává jen
přihlašovací identifikátor, heslo e-mailového účtu nikdy nevidíme).
Pokud si v aplikaci („Více → Můj Okolník“) zapnete účast v žebříčku,
platí navíc toto:

- **Co je veřejné.** Na stránce okolnik.cz/zebricek se zobrazí vaše
  **přezdívka**, počet ušlých kilometrů, počet nových obcí a počet
  fotovýprav za aktuální měsíc, případně kraj, pokud si ho zvolíte.
  Přezdívku si volíte sami – nemusí to být vaše jméno.
- **Co se neodesílá nikdy.** Vaše poloha, trasa, deník, fotky, seznam
  navštívených míst ani e-mail. Z těchto dat vznikají jen výše uvedená
  souhrnná čísla, která se počítají přímo v telefonu.
- **Identita hráče.** Výsledky jsou svázané s vaším přihlášeným
  účtem. Navenek vystupujete jen pod zvolenou přezdívkou a náhodným
  kódem účtu, který podle GDPR považujeme za pseudonymizovaný údaj
  (viz vysvětlení identifikátoru instalace výše); jméno ani e-mail se
  nikde nezobrazují.
- **Krokoměr.** Se zapnutou účastí si aplikace vyžádá přístup
  k čítači kroků telefonu. Slouží jen k tomu, aby šlo odlišit chůzi
  od jízdy – do žebříčku se posílá pouze **měsíční počet kroků**
  a příznak „podloženo kroky“, ne jednotlivá měření ani časy.
  Souhlas můžete kdykoli odvolat v nastavení Androidu.
- **Stejný účet na webu.** Na okolnik.cz/ucet se přihlásíte tímtéž
  účtem jako v aplikaci a uvidíte svůj **soukromý profil** (úroveň,
  souhrnná čísla, úspěchy); ten je čitelný jen pro vás, ne veřejně.
- **Odhlášení.** Vypnutím přepínače v „Můj Okolník“ se váš řádek
  z žebříčku smaže a další čísla se už neposílají. O smazání profilu
  i spárování lze kdykoli požádat na stamu.apps@gmail.com.

## Hra Dobyvatel a soutěže (dobrovolné)

Dobyvatel je týmová hra: krajské týmy obsazují vlajky (významná místa)
po celém Česku. Režim vyžaduje přihlášení a jeho zapnutí je vaše volba.
Když ho hrajete, platí toto:

- **Přítomnost u vlajky.** Při obsazování nebo bránění vlajky odesílá
  aplikace na server hry (Google Firebase) krátkodobý záznam
  o přítomnosti: číslo vlajky, váš tým, čas a polohu telefonu
  v okamžiku boje (kvůli ověření, že u vlajky opravdu stojíte).
  Záznam slouží jen rozhodčímu hry k vyhodnocení boje a **krátce po
  vyhodnocení se maže** (řádově minuty). Vaše průběžná poloha ani
  trasa se neodesílají – mimo boj o vlajku neodchází o poloze nic.
- **Co je veřejné.** Herní stav soutěže: která místa drží který tým,
  kdy byla dobyta, skóre týmů a bodování hráčů vedené pod přezdívkou
  či pseudonymním kódem účtu (bez jména a e-mailu). Tyto údaje se
  zobrazují v aplikaci i na okolnik.cz/dobyvatel.
- **Členství v týmu.** U vašeho účtu se ukládá zvolený tým (kraj)
  a případná účast ve vlastní soutěži. Tým jde po uplynutí ochranné
  lhůty změnit.
- **Konec účasti.** Hru kdykoli opustíte přepnutím režimu; o smazání
  herních dat účtu lze požádat na stamu.apps@gmail.com.

## Záloha do účtu Google (služba Androidu)

Android umí sám zálohovat data aplikací do zálohy telefonu ve vašem
účtu Google. Okolník to má povolené a od verze 1.531 posílá do téhle
zálohy **jen postup ve hře** (odkrytá mapa, ušlé kilometry, deník,
výpravy, návštěvy, úspěchy a nastavení) — **fotky se nezálohují**.
Po přeinstalování nebo na novém telefonu se postup obnoví sám.

Zálohu provádí systém, ne my: data putují do úložiště Googlu
svázaného s vaším účtem, jsou šifrovaná a **správce aplikace k nim
nemá přístup**. Vypnout je lze v nastavení Androidu
(*Google → Zálohování*). Nezávisle na tom si můžete kdykoli udělat
vlastní zálohu do souboru ZIP přímo v aplikaci — ta obsahuje i fotky
a nikam se neodesílá.

## Souhrnné statistiky používání

Aby bylo možné aplikaci zlepšovat a odhalovat chyby, odesílá aplikace do služby
Google Firebase základní **souhrnné** statistiky používání – počet
spuštění, denní počet aktivních zařízení, verzi aplikace, orientační stáří
instalace, počty použití funkcí a počty pádů. Zapisují se pouze jako souhrnná
počítadla („dnes +1"); neodesílá se žádné jméno, identifikátor, poloha ani
obsah, takže je nelze přiřadit ke konkrétní osobě. Sběr lze kdykoli vypnout
v nastavení aplikace (přepínač „Anonymní statistiky používání").

## Hlášení chyb a pádů

Když aplikace spadne nebo přestane reagovat, vytvoří o tom technický záznam
a při dalším spuštění ho odešle vývojáři, aby šlo chybu opravit. Takové
hlášení obsahuje:

- technický popis chyby (tzv. stack trace / ANR trace) — tedy které části
  programu selhaly,
- **model zařízení** a verzi Androidu,
- verzi aplikace a údaj o využité paměti,
- **náhodně vygenerovaný identifikátor zařízení**, aby šlo poznat, že několik
  hlášení pochází z jednoho telefonu (není odvozený z žádného vašeho údaje
  ani z reklamního ID a nelze podle něj zjistit, kdo jste).

Hlášení **neobsahuje** vaši polohu, deník, fotky ani obsah, který jste
v aplikaci vytvořili. Ukládá se do služby Google Firestore a slouží výhradně
k opravě chyb.

Odesílání pádů vypíná **týž přepínač** jako souhrnné statistiky („Anonymní
statistiky používání") — když je vypnutý, neodešle se nic. Podrobný záznam
zůstává navíc uložený v telefonu a můžete ho sami sdílet z obrazovky
„O aplikaci".

## Data stahovaná do aplikace

Aplikace stahuje z veřejného repozitáře na GitHub.com datový kanál
s aktualizacemi, které nevyžadují novou verzi – např. průměrné ceny paliv
(zdroj: Český statistický úřad) a provozní nastavení. Jde o stažení obsahu;
poskytovateli se předá jen běžný síťový požadavek (IP adresa), žádné vaše
osobní údaje.

**Počasí:** pro atmosférické efekty v Objevování (mraky, mlha) stahuje
aplikace aktuální počasí ze služby **Open-Meteo**. Dotaz obsahuje **pevný
seznam bodů** rozmístěných po ČR, stejný pro všechny uživatele – vaše poloha
ani výřez mapy se neodesílají. Počasí pro vaše okolí se vybere z už
stažených dat přímo v telefonu.

**Srážkový radar:** protože předpověď se občas mýlí, ověřuje aplikace déšť
ještě podle **radarových snímků služby RainViewer**. Stahuje se seznam
dostupných snímků a obrázkové dlaždice radaru; jde o běžné stažení obsahu,
vaše poloha se neodesílá.

## Nákupy v aplikaci

Prémiové funkce (předplatné Okolník Premium, zvýraznění podniku, vlastní
místo na mapě) lze zakoupit přes **Google Play**. Platbu zpracovává výhradně
Google – správce nemá přístup k údajům o platební kartě a od Googlu obdrží
pouze informaci, zda je nákup aktivní, a token nákupu (ten se u žádosti
o zvýraznění podniku nebo o vlastní místo uloží do Firestore, dokud správce
žádost nevyřídí; slouží ke kontrole platby a případnému vrácení peněz).

Máte-li přihlášený účet, aplikace k němu zapíše příznak, zda je Premium
aktivní (bez částek a údajů o platbě). Podle něj web okolnik.cz skryje
reklamy a povolí zakládání soutěží v Dobyvateli.


## Komu údaje předáváme

Údaje nikomu neprodáváme. Příjemci / poskytovateli služeb jsou:

- **Google** – AdMob (reklamy), Firebase/Firestore (návrhy, hlasy, zpětná
  vazba, souhrnné statistiky, žebříček), Firebase Auth (anonymní identita
  hráče a přihlášení účtem Google na webu), Google Play (nákupy
  a distribuce).
- **OpenStreetMap** – mapové dlaždice a komunitní poznámky (načítání
  i veřejné hlášení zaniklých míst).
- **OpenTopoMap** a **Esri** – mapové podklady (turistická mapa, letecké
  snímky).
- **Wikimedia / Wikipedia** – popisek zobrazovaného místa.
- **GitHub** (Microsoft) – stažení datového kanálu.
- **Open-Meteo** – aktuální počasí pro pevné body v ČR (bez odeslání vaší
  polohy).
- **RainViewer** – snímky srážkového radaru (bez odeslání vaší polohy).
- **Navigační služby dle vaší volby** – Google Mapy, Mapy.com / Seznam.cz,
  Waze (jen když spustíte navigaci).
- **IDOS** (CHAPS) – odjezdové tabule zastávek a nádraží, jen když je sami
  otevřete (předá se název zastávky).

Tito příjemci obdrží běžné síťové požadavky (zejména IP adresu a případně
souřadnice podle konkrétní funkce).

## Oprávnění aplikace

- **Poloha (přesná/přibližná)** – pozice na mapě, hledání v okolí,
  vybarvování navštívených oblastí.
- **Poloha na pozadí** – pouze pro volitelný záznam trasy na pozadí; do
  jeho zapnutí se nepoužívá.
- **Oznámení** – trvalé oznámení, že běží záznam trasy na pozadí.
- **Internet** – mapy, reklamy, odeslání návrhů, hlášení a zpětné vazby.
- **Fotoaparát** – pořizování fotek k výpravám a do deníku přímo v aplikaci
  (vlastní hledáček). Zvuk se nenahrává, fotky zůstávají v zařízení.
- **Galerie / soubory** – výběr už pořízených fotek a načtení či uložení
  zálohy (ZIP) přes systémový výběr souborů.
- **Rozpoznání tělesné aktivity** – čtení čítače kroků telefonu pro
  počítání kroků ve výpravě a pro odlišení chůze od jízdy v žebříčku.
  Aplikace o něj požádá až při spuštění výpravy nebo při zapnutí
  žebříčku; bez něj vše ostatní funguje dál.

## Data míst

Databáze míst pochází z projektu **OpenStreetMap**
(© přispěvatelé OpenStreetMap, licence ODbL 1.0). Průměrné ceny pohonných
hmot pocházejí z otevřených dat **Českého statistického úřadu** a jsou
celorepublikovým průměrem, nikoli cenou konkrétní čerpací stanice.

## Smazání účtu a dat

Účet v Okolníku vzniká jen tehdy, když si sami zapnete žebříček nebo
propojíte hru s webem — hra samotná ho nepotřebuje.

**Smazat ho jde dvěma způsoby:**

- **v aplikaci:** *Více → Můj Okolník → Smazat účet a data ze serveru*.
  Zmizí řádek v žebříčku za **všechna období**, profil pro web
  i anonymní identita hráče.
- **bez aplikace:** na stránce
  [okolnik.cz/smazani-uctu](https://okolnik.cz/smazani-uctu/), kde je
  i adresa pro žádost e-mailem. Žádost vyřídíme nejpozději do 30 dnů.

Data ve hře — odkrytá mapa, ušlé kilometry, deník, výpravy a fotky —
smazáním účtu **nezmizí**, protože na serveru nikdy nebyla. Odstraníte
je vymazáním dat aplikace nebo její odinstalací.

## Vaše práva

Podle GDPR máte právo na přístup, opravu, výmaz, omezení zpracování,
přenositelnost a námitku. Data uložená v telefonu máte plně pod kontrolou
(smazání dat / odinstalace). U údajů odeslaných na server nás
kontaktujte e-mailem a přiložte svůj **kód instalace** (najdete ho v aplikaci
v „O aplikaci"). Podle něj vaše záznamy dohledáme a na požádání smažeme.
Bez toho kódu je k vaší osobě přiřadit neumíme (čl. 11 GDPR) – jiný údaj
o vás nemáme. Pro údaje zpracovávané společností Google (reklamy)
využijte nástroje Google. Máte také právo podat stížnost u Úřadu pro
ochranu osobních údajů (uoou.gov.cz). S dotazy se obraťte na správce:
**Stanislav Mudra**, e-mail: stamu.apps@gmail.com.

## Děti

Aplikace není určena dětem mladším 15 let (hranice souhlasu se zpracováním
osobních údajů podle § 7 zákona č. 110/2019 Sb.) a vědomě neshromažďujeme
jejich údaje. Pokud zjistíte, že nám dítě odeslalo osobní údaje, napište nám
a my je smažeme.

## Změny

Aktuální verze těchto zásad je vždy dostupná na této adrese. O podstatných
změnách budeme informovat v popisu aktualizace aplikace.
