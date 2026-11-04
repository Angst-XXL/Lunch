Úloha: každý pracovní den ráno (Europe/Prague, přehled má být hotový do 7:30) vytvoř přehled obědů ve Zlíně na dnešek a na další pracovní den a zveřejni ho na stálé adrese https://claude.ai/artifact/47hfrdXTR3C8J7uo4pLsTK (uživatel ji má v záložkách Safari). Odpověď piš česky.

1) Svátky: pokud je dnes státní svátek v ČR nebo víkend, napiš jen "Dnes je volno", pošli oznámení podle bodu 11 a skonči. Stránku nepřepisuj.

2) Šablona: zavolej nástroj Artifact s action "read" a url https://claude.ai/artifact/47hfrdXTR3C8J7uo4pLsTK. Vrátí aktuální HTML stránky a uloží ho do souboru. Tato stránka JE šablona: obsahuje záložky dnů, řazení podle polohy diváka, oblíbené restaurace, filtry, třídění, sloupec s číslem menu, přepínače „+ Polévka / + Salát“, barevné odstíny, přepínač tématu, tlačítko pro ruční aktualizaci a vykreslovací kód. Neměň v ní nic kromě bloku mezi řádky "// ===== DATA:START" a "// ===== DATA:END =====". Pokud read selže, nic nevymýšlej, napiš proč a skonči.

3) Stáhni menu z těchto stránek (každá restaurace má vlastní stránku, přehled města zlin.html je nespolehlivý, nepoužívej ho):
- Prostě Restaurace, Vavrečkova 7074: https://www.menicka.cz/8250-proste-restaurace.html
- Pilsner Urquell Original Restaurant, Vavrečkova 7074: https://www.menicka.cz/2992-pilsner-urquell-original-restaurant.html
- Restaurace Flip (Bernard Pub), Gahurova 5265: https://www.menicka.cz/24-restaurace-flip-bernard-pub.html
- Budvarka Zlín, náměstí Práce 2523: https://www.menicka.cz/5881-budvarka-zlin.html
- U Ševce, Kvítková 4323: https://www.menicka.cz/5492-u-sevce.html
- Radegastovna Rex, Okružní 4701: https://www.menicka.cz/3538-radegastovna-rex.html
- U Barcuchů (jídelna), Mokrá 5215: https://www.menicka.cz/3027-u-barcuchu.html
Každá stránka má bloky <div class='menicka'> s nadpisem <div class='nadpis'> (např. "Čtvrtek 5.11.2026"), jeden na den. Vezmi blok s dnešním datem a blok s datem dalšího pracovního dne (v pátek je to pondělí, přeskoč i státní svátky). Jídla si nevymýšlej. Když restaurace na daný den blok nemá, dej jí v tom dni prázdný seznam řádků (stránka napíše „Tento den menu nemá“). Když další pracovní den nemá menu žádná restaurace, druhý den do dat vůbec nedávej.
Názvy jídel ber ze stránek, čísla alergenů vynech, poznámky o nápojích a obalech nevypisuj. Pořadové číslo jídla ze zdrojové stránky (před názvem, např. „3.“) uveď jako 10. pole řádku (uživatel podle něj objednává); polévky, saláty, tip šéfa a jídla bez čísla mají 0. Do názvu číslo nepiš. U Barcuchů mají minutky vlastní čísla (např. 8–14), ty ponech; řádek „Obědové minutky od…“ je jen nadpis, ne jídlo. Polévky bez ceny označ "v menu"; "v menu" dej i polévce, o které restaurace píše, že je v ceně denního menu (např. „Celý měsíc polévka v ceně denního menu“), pokud ta poznámka platí pro aktuální měsíc. Saláty, které restaurace nabízí k menu, zapiš jako řádek typu "p" se slovem „salát“ v názvu, i když jsou na stránce jen jako poznámka (např. Budvarka „Miska salátu dle denní nabídky k menu 35 Kč“ → "Miska salátu dle denní nabídky (k menu)"). Sladká jídla (vdolečky, sladké knedlíky, žemlovka, palačinky…) zapiš jako hlavní jídlo (typ "") s druhem "d", i samostatný kus za pár korun.

4) Pro každé jídlo včetně polévek odhadni kcal a bílkoviny/sacharidy/tuky v gramech (restaurace je neuvádějí, jsou to odhady). Stejné jídlo ve stejné restauraci odhadni stejně jako v předchozích dnech (najdeš je v přečtené stránce).

5) V každé restauraci a každém dni označ jedno doporučené jídlo (typ "b"): málo kcal, sacharidů a tuků, hodně bílkovin. Polévka, salát, sladké jídlo ani ryba to být nemůže. Do pole tip dej krátkou neutrální radu, jak jídlo odlehčit (např. „přílohu sněz jen napůl“, „hranolky vyměň za salát“); když má restaurace víc polévek, doporuč lehčí. Stránku může vidět i někdo jiný, proto v tipech nezmiňuj osobní cíle ani zdraví konkrétního člověka.

6) Pořadí restaurací v datech nehraje roli: stránka je řadí sama podle polohy diváka. Dodržuj pořadí ze seznamu výše.

7) Data: blok DATA nahraď tímto obsahem (komentáře v bloku ponech). AKT vyplň vždy, i když se jídla nezměnila; podle něj uživatel pozná, že je přehled aktuální:
var AKT="<skutečný čas, kdy jsi menu stáhl a zkontroloval, ISO s pražským posunem, např. 2026-11-05T07:21:00+01:00 (v létě +02:00); zjisti ho příkazem TZ=Europe/Prague date -Iseconds>";
var DNY=[
{datum:"<RRRR-MM-DD dnes>", den:"<den a datum malými, např. čtvrtek 5. 11. 2026>", R:[ ...restaurace... ]},
{datum:"<RRRR-MM-DD další pracovní den>", den:"<např. pátek 6. 11. 2026>", R:[ ...restaurace... ]}
];
Restaurace: [název, adresa, url, tip, [řádky]].
Řádek: [název, cena, kcal, B, S, T, typ, druh, smažené, číslo menu]
- název: BEZ ikon a emoji (ikony doplní stránka sama)
- typ: "b" doporučené, "s" polévka, "p" salát nebo příloha samostatně, "" hlavní jídlo
- druh: "k" drůbež: kuřecí, krůtí, kachna, husa (i slepičí vývar), "v" vepřové (i uzenina, slanina, šunka, špek, karbanátek, směs, srdce, játra), "h" hovězí (i telecí), "z" bez masa (slané: sýr, vejce, zelenina, luštěniny), "d" sladké, "r" ryba. U jídla s více druhy masa dej hlavní maso.
- smažené: 1 když je HLAVNÍ složka obalovaná nebo smažená (řízek, smažený sýr, cordon bleu, stripsy, v bramboráku, Kentucky, panko, smažený květák), jinak 0. Smažené přílohy (hranolky, krokety, smažená cibulka) se nepočítají, ty jde vyměnit.
- číslo menu: pořadové číslo jídla na zdrojové stránce, 0 = bez čísla
Příklad: ["Pečené kuřecí stehno, rýže, okurek (240 g)","179 Kč",700,48,62,27,"b","k",0,4]

8) Ulož výsledek jako obedy-YYYY-MM-DD.html do pracovního adresáře. Před zveřejněním ověř, že stránka jde otevřít bez chyb ve skriptu (např. v Playwrightu, bez chyb v konzoli) a že ukazuje záložku „Dnes“.

9) Zveřejni: Artifact publish s file_path dnešního souboru, url https://claude.ai/artifact/47hfrdXTR3C8J7uo4pLsTK a label s dnešním datem (např. "5. 11. 2026"), bez icon a bez capabilities (stránka si oprávnění ponechá). NIKDY nevytvářej nový Artifact bez url. Pokud zveřejnění selže, pošli soubor nástrojem SendUserFile (display: render) a napiš proč.

10) Na konec napiš krátké shrnutí: odkaz na stránku, doporučené jídlo (s číslem menu) v každé restauraci pro dnešek a které restaurace dnes nebo další pracovní den menu nemají.

11) Oznámení: úplně nakonec zavolej nástroj PushNotification (načti ho přes ToolSearch "select:PushNotification") se zprávou do 200 znaků, např. "Obědy 5. 11. hotové. Doporučené: č. 1 kuřecí roláda se špenátem (U Ševce). claude.ai/artifact/47hfrdXTR3C8J7uo4pLsTK". Pošli ho i v den volna ("Dnes je volno"). Pokud nástroj hlásí, že oznámení nebylo odesláno, napiš to do shrnutí.

(Záložní kopie šablony s prázdnými daty je v repozitáři angst-xxl/lunch, soubor sablona-obedy.html na větvi claude/new-session-w07zdq.)
