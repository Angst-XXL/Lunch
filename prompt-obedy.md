Úloha: každý pracovní den ráno (Europe/Prague, přehled má být hotový do 7:30) vytvoř přehled denních obědů ve Zlíně a zveřejni ho na stálé adrese https://claude.ai/artifact/47hfrdXTR3C8J7uo4pLsTK (uživatel ji má v záložkách Safari). Odpověď piš česky.

1) Svátky: pokud je dnes státní svátek v ČR nebo víkend, napiš jen "Dnes je volno", pošli oznámení podle bodu 11 a skonči. Stránku nepřepisuj.

2) Šablona: zavolej nástroj Artifact s action "read" a url https://claude.ai/artifact/47hfrdXTR3C8J7uo4pLsTK. Vrátí aktuální HTML stránky a uloží ho do souboru. Tato stránka JE šablona: obsahuje filtry, třídění, sloupec s číslem menu, tlačítko pro ruční aktualizaci a vykreslovací kód. Neměň v ní nic kromě bloku mezi řádky "// ===== DATA:START" a "// ===== DATA:END =====". Pokud read selže, nic nevymýšlej, napiš proč a skonči.

3) Stáhni dnešní menu z těchto stránek (každá restaurace má vlastní stránku, přehled města zlin.html je nespolehlivý, nepoužívej ho):
- Prostě Restaurace, Vavrečkova 7074: https://www.menicka.cz/8250-proste-restaurace.html
- Pilsner Urquell Original Restaurant, Vavrečkova 7074: https://www.menicka.cz/2992-pilsner-urquell-original-restaurant.html
- Restaurace Flip (Bernard Pub), Gahurova 5265: https://www.menicka.cz/24-restaurace-flip-bernard-pub.html
- Budvarka Zlín, náměstí Práce 2523: https://www.menicka.cz/5881-budvarka-zlin.html
- U Ševce, Kvítková 4323: https://www.menicka.cz/5492-u-sevce.html
- Radegastovna Rex, Okružní 4701: https://www.menicka.cz/3538-radegastovna-rex.html
- U Barcuchů (jídelna), Mokrá 5215: https://www.menicka.cz/3027-u-barcuchu.html
Ověř, že menu je pro dnešní datum (první blok <div class='menicka'> s nadpisem <div class='nadpis'>, např. "Úterý 3.11.2026"). Jídla si nevymýšlej. Pokud restaurace dnes menu nemá, dej jí prázdný seznam řádků (stránka sama napíše „Dnes menu nemá“). Názvy jídel ber ze stránek, čísla alergenů vynech, poznámky o nápojích a obalech nevypisuj. Pořadové číslo jídla ze zdrojové stránky (před názvem, např. „3.“) uveď jako 10. pole řádku (uživatel podle něj objednává); polévky, saláty, tip šéfa a jídla bez čísla mají 0. Do názvu číslo nepiš. U Barcuchů mají minutky vlastní čísla (např. 8–14), ty ponech; řádek „Obědové minutky od…“ je jen nadpis, ne jídlo. Polévky bez ceny označ "v menu".

4) Pro každé jídlo včetně polévek odhadni kcal a bílkoviny/sacharidy/tuky v gramech (restaurace je neuvádějí, jsou to odhady).

5) V každé restauraci označ jedno nejvhodnější jídlo (typ "b"): málo kcal, sacharidů a tuků, hodně bílkovin (cíl: zhubnout kortizolové břicho). Polévka ani salát/příloha to být nemůže. Ryba nikdy nesmí být nejlepší, uživatel ryby nejí. Do pole tip dej krátkou radu (např. zaměnit přílohu za salát).

6) Pořadí restaurací podle polohy: pondělí až středa od Vavrečkova 7074 (Prostě a Pilsner Urquell první, pak podle vzdálenosti), čtvrtek a pátek od Podlesí 5375 (domov). Souřadnice restaurací jsou ve stránkách v kódu mapy (maps.LatLng).

7) Data: blok DATA nahraď tímto obsahem (komentáře v bloku ponech). AKT vyplň vždy, i když se jídla od včerejška nezměnila; podle něj uživatel pozná, že je přehled aktuální:
var DEN="<den a datum malými, např. středa 4. 11. 2026>", SUB="<Dnes <den>, kancelář.> nebo <Dnes <den>, doma.>";
var AKT="<skutečný čas, kdy jsi menu stáhl a zkontroloval, ISO s pražským posunem, např. 2026-11-05T07:21:00+01:00 (v létě +02:00); zjisti ho příkazem TZ=Europe/Prague date -Iseconds>";
var R=[ ...restaurace... ];
Restaurace: [název, adresa, url, tip, [řádky]].
Řádek: [název, cena, kcal, B, S, T, typ, druh, smažené, číslo menu]
- název: BEZ ikon a emoji (ikony ✅ 🥣 🌱 🐟 doplní stránka sama)
- typ: "b" nejlepší, "s" polévka, "p" salát nebo příloha samostatně, "" hlavní jídlo
- druh: "k" drůbež: kuřecí, krůtí, kachna, husa (i slepičí vývar), "v" vepřové (i uzenina, slanina, šunka, špek, karbanátek, směs), "h" hovězí, "z" bez masa, "r" ryba. U jídla s více druhy masa dej hlavní maso.
- smažené: 1 když je HLAVNÍ složka obalovaná nebo smažená (řízek, smažený sýr, cordon bleu, stripsy, v bramboráku, Kentucky, panko), jinak 0. Smažené přílohy (hranolky, krokety, smažená cibulka) se nepočítají, ty jde vyměnit.
- číslo menu: pořadové číslo jídla na zdrojové stránce, 0 = bez čísla
Příklad: ["Pečené kuřecí stehno, rýže, okurek (240 g)","179 Kč",700,48,62,27,"b","k",0,4]

8) Ulož výsledek jako obedy-YYYY-MM-DD.html do pracovního adresáře. Před zveřejněním ověř, že stránka jde otevřít bez chyb ve skriptu (např. v Playwrightu, bez chyb v konzoli).

9) Zveřejni: Artifact publish s file_path dnešního souboru, url https://claude.ai/artifact/47hfrdXTR3C8J7uo4pLsTK a label s dnešním datem (např. "4. 11. 2026"), bez icon a bez capabilities (stránka si oprávnění tlačítka ponechá). NIKDY nevytvářej nový Artifact bez url. Pokud zveřejnění selže, pošli soubor nástrojem SendUserFile (display: render) a napiš proč.

10) Na konec napiš krátké shrnutí: odkaz na stránku, nejlepší jídlo (s číslem menu) v každé restauraci a které restaurace dnes menu nemají.

11) Oznámení: úplně nakonec zavolej nástroj PushNotification (načti ho přes ToolSearch "select:PushNotification") se zprávou do 200 znaků, např. "Obědy 4. 11. hotové. Nejlepší dnes: č. 4 kuřecí steak s fazolkami (U Ševce). claude.ai/artifact/47hfrdXTR3C8J7uo4pLsTK". Pošli ho i v den volna ("Dnes je volno"). Pokud nástroj hlásí, že oznámení nebylo odesláno, napiš to do shrnutí.

(Záložní kopie šablony s prázdnými daty je v repozitáři angst-xxl/lunch, soubor sablona-obedy.html na větvi claude/new-session-w07zdq.)
