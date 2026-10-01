# Licence dat míst Okolníku

Databáze míst Okolníku (`sarcher.db` v aplikaci, datový balíček `data-v1`,
export `mapa/data` na okolnik.cz) je **odvozená databáze** z OpenStreetMap
(© přispěvatelé OpenStreetMap) a je dostupná pod licencí
**Open Database License (ODbL) 1.0** – https://opendatacommons.org/licenses/odbl/1-0/.
Jednotlivé prvky (tagy) podléhají Database Contents License (DbCL) 1.0.

Vedle ní stojí jako **souborná databáze** oddělené kolekce jiných licencí:
- prodejny z registru (ROS © Digitální a informační agentura, RES © ČSÚ,
  RÚIAN © ČÚZK) – CC BY 4.0;
- řetězce prodejen z All the Places – CC0;
- krajina, stavby a výškopis: ZABAGED® a DMR 5G © ČÚZK – CC BY 4.0;
- znaky obcí: Wikimedia Commons / REKOS PSP ČR (viz atribuce v aplikaci).

**Drobnosti na mapě** (archiv `drobnostiN.pmtiles` na úložišti map Okolníku, aktuálně
https://pub-503fa062ecca4774b24370946e2b2a70.r2.dev/drobnosti10.pmtiles, vektorové dlaždice PMTiles z14) jsou
rovněž **odvozená databáze z OpenStreetMap pod ODbL 1.0**: lampy, lavičky, studny, posedy, krmelce, schránky,
stromy, přechody, přejezdy, semafory, závory, nástupiště, železniční návěstidla a polohy zvířat (koně u jízdáren
a stájí, pastviny, obory, úly, chovné rybníky – spočítané z ploch a bodů OSM). Druh zabezpečení přejezdů
(jen kříž / světla / závory / mechanické závory) je ze **Seznamu železničních přejezdů © Správa železnic**
(stav k 31. 12. 2025, spravazeleznic.cz).

Samostatné archivy jiných licencí (nesloučené s OSM): lampy z otevřených dat měst (`lampy_mestaN.pmtiles`:
Brno CC BY 4.0, Plzeň, Děčín) a Digitální technická mapa krajů ČR (`dtmN.pmtiles`, IS DMVS – ČÚZK, otevřená data).

Sestavení databáze popisují skripty v `tools/` repozitáře aplikace
(Overpass/PBF → SQLite); kopii aktuální databáze lze získat z datového
balíčku `data-v1` (GitHub Releases) nebo z exportu na webu.
