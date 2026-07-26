# Zásady ochrany soukromí – aplikace Okolník

*Platné od 26. 7. 2026*

Aplikace **Okolník – vyhledávač míst v okolí** (dále „aplikace") respektuje
vaše soukromí. Tento dokument popisuje, jaké údaje aplikace zpracovává, proč
a jaká máte práva. Zpracování probíhá v souladu s nařízením (EU) 2016/679
(GDPR). Provozovatelem je **Stanislav Mudra**, e-mail: stamu.apps@gmail.com.

## Shrnutí

Aplikace **nevytváří účty ani neshromažďuje osobní údaje spojené s vaší
osobou** a nemá vlastní servery pro vaše data. Poloha, trasa, deník, výpravy
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

## Souhrnné statistiky používání

Aby bylo možné aplikaci zlepšovat a odhalovat chyby, odesílá aplikace do služby
Google Firebase základní **souhrnné** statistiky používání – počet
spuštění, denní počet aktivních zařízení, verzi aplikace, orientační stáří
instalace, počty použití funkcí a počty pádů. Zapisují se pouze jako souhrnná
počítadla („dnes +1"); neodesílá se žádné jméno, identifikátor, poloha ani
obsah, takže je nelze přiřadit ke konkrétní osobě. Sběr lze kdykoli vypnout
v nastavení aplikace (přepínač „Anonymní statistiky používání").

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

## Nákupy v aplikaci

Prémiové funkce lze zakoupit přes **Google Play**. Platbu zpracovává výhradně
Google – správce nemá přístup k údajům o platební kartě a od Googlu obdrží
pouze informaci, zda je nákup aktivní.

## Komu údaje předáváme

Údaje nikomu neprodáváme. Příjemci / poskytovateli služeb jsou:

- **Google** – AdMob (reklamy), Firebase/Firestore (návrhy, hlasy, zpětná
  vazba, souhrnné statistiky), Google Play (nákupy a distribuce).
- **OpenStreetMap** – mapové dlaždice a komunitní poznámky (načítání
  i veřejné hlášení zaniklých míst).
- **OpenTopoMap** a **Esri** – mapové podklady (turistická mapa, letecké
  snímky).
- **Wikimedia / Wikipedia** – popisek zobrazovaného místa.
- **GitHub** (Microsoft) – stažení datového kanálu.
- **Open-Meteo** – aktuální počasí pro pevné body v ČR (bez odeslání vaší
  polohy).
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

## Data míst

Databáze míst pochází z projektu **OpenStreetMap**
(© přispěvatelé OpenStreetMap, licence ODbL 1.0). Průměrné ceny pohonných
hmot pocházejí z otevřených dat **Českého statistického úřadu** a jsou
celorepublikovým průměrem, nikoli cenou konkrétní čerpací stanice.

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
