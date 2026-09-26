# Zásady ochrany soukromí – aplikace Okolník

*Platné od 25. 9. 2026*

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
vypnuto a dá se kdykoli zrušit. Poloha, přesná trasa a fotky zůstávají
uložené jen ve vašem telefonu; po přihlášení se **postup ve hře** (odkrytá
mapa, kilometry, deník a výpravy bez fotek, úspěchy, plány) ukládá i pod
vaším účtem, aby přežil výměnu telefonu a šel zobrazit na okolnik.cz –
jen pro vás, nikdy veřejně. Na server správce posíláte
to, co sami odešlete (návrh místa, hlasování, zpětná vazba) – bez jména či
e-mailu; aplikace navíc odesílá **souhrnné statistiky používání**
(lze vypnout v nastavení). Některé funkce se dotazují veřejných služeb
třetích stran (mapy, OpenStreetMap, Wikipedie). Hlášení „místo už neexistuje"
se zveřejní jako veřejná poznámka v OpenStreetMap. Bezplatná verze zobrazuje
reklamy Google AdMob, které v EU vyžadují váš souhlas.

## Poloha

Aplikace používá polohu zařízení (GPS) k zobrazení vaší pozice a míst
v okolí na mapě a v seznamu a k hernímu „vybarvování" navštívených oblastí.
**Poloha se zpracovává ve vašem zařízení** a neukládá se na servery správce;
jedinou výjimkou je hrubá odkrytá mapa (buňky o velikosti stovek metrů)
ukládaná po přihlášení pod vaším účtem, viz „Postup ve hře pod účtem".
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
ukládají **ve vašem zařízení**. Bez přihlášení se nikam neodesílají; po
přihlášení se jejich část ukládá i pod vaším účtem (viz „Postup ve hře pod
účtem"). Přesná trasa (jednotlivé body polohy), fotografie a nastavení
zůstávají vždy jen v telefonu. Smažete
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
- **Co je a co není veřejné.** Veřejná jsou jen výše uvedená souhrnná
  čísla pod přezdívkou; počítají se přímo v telefonu. Vaše poloha,
  přesná trasa, fotky ani e-mail se do žebříčku neposílají. Deník,
  navštívená místa a odkrytá mapa se ukládají jen soukromě pod vaším
  účtem (viz „Postup ve hře pod účtem"), nikdy veřejně.
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
  souhrnná čísla, úspěchy) a od verze 1.608 i **svou mapu** (odkrytá
  místa, fotovýpravy, zápisy); obojí je čitelné jen pro vás, ne veřejně.
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

## Hra na míru – akce (dobrovolné)

Organizátor (firma, škola, oddíl, rodina) může v Okolníku založit akci – společnou výpravu nebo hru.
Připojíte se kódem nebo odkazem od organizátora a **před připojením vám aplikace ukáže, co přesně se
bude sdílet, s kým a do kdy**. Bez vašeho souhlasu se nic neodešle. Pro akci se ukládá:

- **Účast:** přezdívka, kterou si pro akci zvolíte, tým a čas vašeho souhlasu. Organizátor může
  účast schvalovat – do schválení se nic nesdílí – a účastníka z akce vyřadit.
- **Poloha během akce**, pokud ji pravidla akce zapínají **a vy sdílení povolíte** (přepínačem při
  připojení, jde kdykoli vypnout): aktuální poloha telefonu, přesnost a čas, nejvýš jednou za minutu
  (i se zhasnutou obrazovkou, dokud jste v akci). Podle nastavení akce ji vidí jen organizátor, jen
  váš tým, váš tým a organizátor, nebo všichni účastníci – organizátor ji tedy nemusí vidět vůbec –
  a **vždy jen do konce akce**. Sdílení nemusí běžet pořád – stačí při plnění úkolů a na trase jako
  doklad, kde a kdy jste byli. Nic se neděje automaticky; o účasti rozhoduje organizátor.
- **Trasa**, pokud ji organizátor zapnul a vy máte sdílení zapnuté (týž přepínač jako u polohy):
  záznam vaší cesty během akce po kouscích. Vidí ji organizátor, nebo všichni účastníci (až po
  skončení akce, nebo už během ní – podle nastavení).
- **Smazání:** sdílení skončí samo po skončení akce nebo po odstoupení z akce. Polohy, trasy a účast se smažou po době uchování,
  kterou organizátor zvolí (0 až 90 dní po akci, uvidíte ji v textu souhlasu). Když z akce odejdete,
  vaše účast a poloha se smažou hned.

Kdo z účastníků co vidí, hlídají pravidla serveru (Google Firebase), ne jen aplikace. Po založení
akce už organizátor sdílení nemůže rozšířit – ukázat polohu nebo trasu dalším lidem, prodloužit dobu
uchování ani běžící akci; smí je jen zúžit nebo akci zkrátit. Organizátor
odpovídá za to, k čemu údaje z akce použije; správce Okolníku je zpracovává jen pro provoz akce.

## Postup ve hře pod účtem (synchronizace)

Od verze 1.608 aplikace po přihlášení ukládá váš **postup ve hře** pod váš
účet do databáze správce (Google Firebase / Firestore), aby přežil výměnu
nebo ztrátu telefonu a abyste ho viděli i na okolnik.cz. Synchronizace je
součástí přihlášeného účtu – kdo se nepřihlásí, neposílá nic a hra běží
jen v telefonu.

- **Co se ukládá.** Odkryté oblasti mapy (mřížka buněk o velikosti zhruba
  200 × 130 m, kterými jste prošli), dokončené obce a denní kilometry,
  zápisy deníku a fotovýpravy **bez fotografií** (u výprav včetně
  zaznamenané trasy výpravy a časů), soukromá a oblíbená místa, poznámky
  k místům, hlasy o aktuálnosti míst, úspěchy a časy jejich získání, časy
  objevení míst a doložené návštěvy, plány v kalendáři.
- **Co se neukládá.** Fotografie, přesná průběžná trasa („trasa dne"),
  aktuální poloha, kroky ani nastavení. Poloha se ani tady neodesílá
  průběžně – odchází jen souhrn po skončení aktivity nebo při odchodu
  z aplikace, ručně pak tlačítkem v „Můj Okolník".
- **Kdo to vidí.** Jen vy: data jsou svázaná s vaším účtem a čitelná
  pouze po přihlášení tímtéž účtem (v aplikaci i na okolnik.cz). Nejsou
  veřejná, nepředáváme je a nepoužíváme je k reklamě ani k profilování.
  Správce má k databázi technický přístup kvůli provozu a podpoře.
- **Proč to bereme vážně.** Odkrytá mapa je hrubý obraz míst, kde jste
  se pohybovali, tedy údaj o poloze. Proto se ukládá jen pod účtem,
  v hrubém rozlišení stovek metrů, šifrovaně při přenosu i v úložišti
  Googlu, a smažete ho kdykoli.
- **Kdy se odesílá.** Po přihlášení, po skončení aktivity či při odchodu
  z aplikace a ručně („Více → Můj Okolník → Synchronizovat teď"). Při
  přihlášení na novém telefonu se stav ze serveru sloučí s tím v telefonu
  – nic se nepřepisuje ani nemaže. Účet je aktivní vždy jen na jednom
  telefonu: jiný telefon ho převezme po odhlášení na tom prvním, nebo
  když je první telefon den v klidu; čísla do žebříčku posílá jen
  aktivní telefon. Počet takových převzetí za měsíc se ukládá
  u hlavičky (ochrana žebříčku před sdílením účtu).
- **Smazání.** Smazáním účtu v aplikaci („Smazat účet a data ze serveru")
  nebo přes okolnik.cz/smazani-uctu se smaže i uložený postup. Data
  v telefonu tím nezmizí.
- **Právní základ.** Plnění smlouvy – poskytnutí funkce, kterou
  přihlášením využíváte (čl. 6 odst. 1 písm. b GDPR).

## Přátelé (dobrovolné)

Od verze 1.613.50 si přihlášení hráči mohou přidat **přátele**. Funkce je
zcela dobrovolná: kdo nikoho nepřidá, nesdílí nic.

- **Jak se přátelství uzavírá.** Každý přihlášený účet má šestimístný kód
  (odvozený z účtu, bez osobních údajů). Kdo kód zadá, pošle žádost; přátelé
  jste až po jejím přijetí druhou stranou. Kód i žádost nesou jen vaši
  přezdívku ze žebříčku (nebo slovo „Okolník", pokud přezdívku nemáte).
- **Co přátelé vidí automaticky.** Přezdívku, počet objevených obcí,
  nachozené kilometry, úroveň, počet fotovýprav a název poslední z nich
  názvy, data a délky posledních pěti z nich a **seznam objevených obcí** –
  na mapě přítele se ukazují jako barevně podbarvená území („společná
  mapa"). Neposílá se odkrytá mřížka buněk,
  trasy, zápisy deníku, fotografie ani doložené návštěvy.
- **Poloha.** Vaši aktuální polohu vidí přátelé **po dobu trvání
  přátelství** – tedy až po vzájemném potvrzení a jen dokud spojení sami
  nepřerušíte: jedním vypínačem pro všechny („Sdílet polohu s přáteli")
  nebo vypínačem u jednotlivého přítele. Poloha se odesílá, kdykoli
  aplikace zaznamenává polohu (v popředí i při zapnutém záznamu aktivity),
  nejvýš jednou za minutu a po posunu aspoň o 30 metrů, zaokrouhlená na
  metry, spolu s přesností a časem. Záznam na serveru platí nejvýš den
  a s každým odesláním se obnovuje; po přerušení sdílení se smaže. Přítel
  vidí polohu starou nejvýš 24 hodin (na mapě po 30 minutách zbledne).
- **Historie v telefonu.** Po odebrání přítele zůstane jen ve vašem
  telefonu záznam o tom, kdo a odkdy dokdy byl vaším přítelem, jeho
  poslední souhrn a názvy jeho posledních fotovýprav („vzpomínky") a
  poznámka v deníku. Na server se nic z toho neukládá; v aplikaci to jde
  smazat po jednom i celé.
- **Kde to je uloženo.** V databázi správce (Google Firebase / Firestore,
  servery v EU), ve třech malých záznamech svázaných s účtem: kód
  (`kody`), přátelství (`pratelstvi`), sdílený souhrn s obcemi
  (`sdileni`) a poloha (`poloha`). Pravidla databáze pouštějí ke čtení
  souhrnu jen potvrzené přátele a k poloze jen ty, komu jste ji zapnuli.
- **Odebrání a smazání.** Odebráním přítele (nebo odmítnutím žádosti)
  zmizí přátelství na obou stranách a s ním i přístup k souhrnu a poloze.
  Smazáním účtu se smažou všechny tyto záznamy.
- **Právní základ.** Souhlas – sdílení zapínáte vy sami, přátelství
  přijímáte výslovně a polohu zapínáte pro každého přítele zvlášť
  (čl. 6 odst. 1 písm. a GDPR); souhlas kdykoli odvoláte odebráním přítele
  nebo vypnutím polohy.

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

Stejně souhrnně aplikace počítá návštěvnost **stránek ověřených podniků**:
otevření stránky a klepnutí na Trasa, Volat, Web a Sdílet se připočtou k měsíčnímu počítadlu
podniku („září +1“, z jednoho telefonu nejvýš jednou denně). Neodesílá se žádný identifikátor
zařízení ani účtu a majitel podniku vidí jen měsíční součty. I tyto počty vypíná přepínač
„Anonymní statistiky používání“.

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
aplikace aktuální počasí z **našeho serveru** (Google Cloud Functions,
region EU), který je jednou za 15 minut přebírá ze služby **MET Norway**
(api.met.no, licence CC BY 4.0) pro **pevný seznam bodů** rozmístěných po
ČR, stejný pro všechny uživatele – vaše poloha ani výřez mapy se
neodesílají. Počasí pro vaše okolí se vybere z už stažených dat přímo
v telefonu.

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

Objednávka zvýraznění podniku se váže na **přihlášený účet**: k žádosti se uloží
identifikátor účtu a číslo objednávky Google Play, aby majitel mohl na okolnik.cz/firmy spravovat
stránku podniku. Co na stránku podniku zadá (otevírací doba, kontakty, texty, fotky), je veřejné
a vidí to všichni uživatelé; texty a fotky před zveřejněním schvaluje správce.

Máte-li přihlášený účet, aplikace k němu zapíše příznak, zda je Premium
aktivní (bez částek a údajů o platbě). Podle něj web okolnik.cz skryje
reklamy a povolí zakládání soutěží v Dobyvateli.


## Komu údaje předáváme

Údaje nikomu neprodáváme. Příjemci / poskytovateli služeb jsou:

- **Google** – AdMob (reklamy), Firebase/Firestore (návrhy, hlasy, zpětná
  vazba, souhrnné statistiky, žebříček, postup ve hře pod účtem), Firebase Auth (anonymní identita
  hráče a přihlášení účtem Google na webu), Google Play (nákupy
  a distribuce).
- **OpenStreetMap** – mapové dlaždice a komunitní poznámky (načítání
  i veřejné hlášení zaniklých míst).
- **OpenTopoMap** a **Esri** – mapové podklady (turistická mapa, letecké
  snímky).
- **Wikimedia / Wikipedia** – popisek zobrazovaného místa.
- **GitHub** (Microsoft) – stažení datového kanálu.
- **MET Norway** (přes náš server) – aktuální počasí pro pevné body v ČR
  (bez odeslání vaší polohy).
- **RainViewer** – snímky srážkového radaru (bez odeslání vaší polohy).
- **Navigační služby dle vaší volby** – Google Mapy, Mapy.com / Seznam.cz,
  Waze (jen když spustíte navigaci).
- **IDOS** (CHAPS) – odjezdové tabule zastávek a nádraží, jen když je sami
  otevřete (předá se název zastávky).
- **Organizátor akce** (hra na míru) – přezdívka a tým; poloha a trasa z akce jen tehdy, když mu je
  nastavení akce zpřístupňuje a vy jste s ním při připojení souhlasili, a jen po dobu uvedenou v souhlasu.

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
  Zmizí řádek v žebříčku za **všechna období**, profil pro web,
  uložený postup ve hře i identita hráče.
- **bez aplikace:** na stránce
  [okolnik.cz/smazani-uctu](https://okolnik.cz/smazani-uctu/), kde je
  i adresa pro žádost e-mailem. Žádost vyřídíme nejpozději do 30 dnů.

Data v telefonu — odkrytá mapa, ušlé kilometry, deník, výpravy a fotky —
smazáním účtu **nezmizí**; smaže se jen jejich kopie uložená pod účtem.
Z telefonu je odstraníte vymazáním dat aplikace nebo její odinstalací.

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
