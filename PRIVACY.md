# ZĂˇsady ochrany soukromĂ­ â€“ aplikace Okolník

*PlatnĂ© od 18. 7. 2026*

Aplikace **Sarcher â€“ vyhledĂˇvaÄŤ mĂ­st v okolĂ­** (dĂˇle â€žaplikace") respektuje
vaĹˇe soukromĂ­. Tento dokument popisuje, jakĂ© Ăşdaje aplikace zpracovĂˇvĂˇ.

## ShrnutĂ­

Aplikace **nevytvĂˇĹ™Ă­ ĂşÄŤty, nesbĂ­rĂˇ ani neuklĂˇdĂˇ osobnĂ­ Ăşdaje a nemĂˇ ĹľĂˇdnĂ©
vlastnĂ­ servery**. DatabĂˇze mĂ­st je pĹ™ibalenĂˇ pĹ™Ă­mo v aplikaci a vyhledĂˇvĂˇnĂ­
probĂ­hĂˇ vĂ˝hradnÄ› ve vaĹˇem zaĹ™Ă­zenĂ­.

## Poloha

Aplikace pouĹľĂ­vĂˇ polohu zaĹ™Ă­zenĂ­ (GPS) **pouze k zobrazenĂ­ mĂ­st ve vaĹˇem
okolĂ­ na mapÄ› a v seznamu**. Poloha se zpracovĂˇvĂˇ jen v zaĹ™Ă­zenĂ­,
**nikam se neodesĂ­lĂˇ ani neuklĂˇdĂˇ**. OprĂˇvnÄ›nĂ­ k poloze mĹŻĹľete kdykoli
odebrat v nastavenĂ­ systĂ©mu; aplikace pak nabĂ­dne omezenĂ˝ reĹľim.

## SĂ­ĹĄovĂˇ komunikace

PĹ™i pouĹľĂ­vĂˇnĂ­ aplikace dochĂˇzĂ­ k tÄ›mto sĂ­ĹĄovĂ˝m poĹľadavkĹŻm (vaĹˇe IP adresa
je z technickĂ© podstaty viditelnĂˇ provozovatelĹŻm danĂ˝ch sluĹľeb):

- **MapovĂ© podklady** â€“ dlaĹľdice map od OpenStreetMap
  (https://www.openstreetmap.org/copyright) a leteckĂ© snĂ­mky Esri.
- **DatovĂ˝ kanĂˇl** â€“ aplikace stahuje soubor s prĹŻmÄ›rnĂ˝mi cenami paliv
  (zdroj: ÄŚeskĂ˝ statistickĂ˝ ĂşĹ™ad) a odkazy na akÄŤnĂ­ letĂˇky z veĹ™ejnĂ©ho
  repozitĂˇĹ™e na GitHub.com.
- **Odkazy** â€“ po ĹĄuknutĂ­ na navigaci, letĂˇk, hodnocenĂ­ ÄŤi web se otevĹ™e
  pĹ™Ă­sluĹˇnĂˇ externĂ­ aplikace nebo webovĂˇ strĂˇnka, kterĂˇ mĂˇ vlastnĂ­ zĂˇsady.

## Reklamy (Google AdMob)

Na podporovanĂ˝ch zaĹ™Ă­zenĂ­ch zobrazuje aplikace reklamnĂ­ banner sluĹľby
**Google AdMob**. SpoleÄŤnost Google mĹŻĹľe v souvislosti se zobrazovĂˇnĂ­m
reklam zpracovĂˇvat reklamnĂ­ identifikĂˇtory zaĹ™Ă­zenĂ­ a souvisejĂ­cĂ­ Ăşdaje
dle svĂ˝ch zĂˇsad: https://policies.google.com/privacy a
https://support.google.com/admob/answer/6128543.

V zemĂ­ch EU/EHP se pĹ™ed zobrazenĂ­m reklam zobrazĂ­ **formulĂˇĹ™ souhlasu
(GDPR)**, kde mĹŻĹľete personalizaci reklam odmĂ­tnout. Volbu lze pozdÄ›ji
zmÄ›nit smazĂˇnĂ­m dat aplikace.

## HlasovĂˇnĂ­ o aktuĂˇlnosti mĂ­st

Aplikace umoĹľĹuje anonymnÄ› hlasovat, zda je mĂ­sto stĂˇle v provozu.
OdesĂ­lĂˇ se pouze **souhrnnĂ˝ hlas** (+1 k poÄŤĂ­tadlu danĂ©ho mĂ­sta) do sluĹľby
**Google Firebase (Firestore)** provozovanĂ© sprĂˇvcem aplikace; nepĹ™enĂˇĹˇĂ­ se
ĹľĂˇdnĂ© osobnĂ­ Ăşdaje ani identifikĂˇtory uĹľivatele. VolitelnĂ© hlĂˇĹˇenĂ­
zaniklĂ©ho mĂ­sta vytvĂˇĹ™Ă­ veĹ™ejnou anonymnĂ­ poznĂˇmku v projektu
OpenStreetMap (viz openstreetmap.org).

## Data mĂ­st

DatabĂˇze mĂ­st pochĂˇzĂ­ z projektu **OpenStreetMap**
(Â© pĹ™ispÄ›vatelĂ© OpenStreetMap, licence ODbL 1.0). PrĹŻmÄ›rnĂ© ceny pohonnĂ˝ch
hmot pochĂˇzejĂ­ z otevĹ™enĂ˝ch dat **ÄŚeskĂ©ho statistickĂ©ho ĂşĹ™adu** a jsou
celorepublikovĂ˝m prĹŻmÄ›rem, nikoli cenou konkrĂ©tnĂ­ ÄŤerpacĂ­ stanice.

## VaĹˇe prĂˇva

JelikoĹľ aplikace neuklĂˇdĂˇ ĹľĂˇdnĂ© osobnĂ­ Ăşdaje, nenĂ­ co exportovat ani mazat.
Pro Ăşdaje zpracovĂˇvanĂ© spoleÄŤnostĂ­ Google (reklamy) vyuĹľijte nĂˇstroje
Google. S dotazy se obraĹĄte na sprĂˇvce aplikace:

**Stanislav Mudra**, e-mail: stanislavmudra@gmail.com

## ZmÄ›ny

AktuĂˇlnĂ­ verze tÄ›chto zĂˇsad je vĹľdy dostupnĂˇ na tĂ©to adrese. O podstatnĂ˝ch
zmÄ›nĂˇch budeme informovat v popisu aktualizace aplikace.

