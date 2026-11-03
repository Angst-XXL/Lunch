Úloha: každý pracovní den ráno (Europe/Prague, přehled má být hotový do 7:30) vytvoř přehled denních obědů ve Zlíně. (Stejné zadání je v souboru prompt-obedy.md v repozitáři angst-xxl/lunch.)

1) Svátky: pokud je dnes státní svátek v ČR nebo víkend, napiš jen "Dnes je volno" a skonči.

2) Stáhni dnešní menu z těchto stránek (každá restaurace má vlastní stránku, přehled města zlin.html je nespolehlivý, nepoužívej ho):
- Prostě Restaurace (Vavrečkova 7074): https://www.menicka.cz/8250-proste-restaurace.html
- Pilsner Urquell Original Restaurant (Vavrečkova 7074): https://www.menicka.cz/2992-pilsner-urquell-original-restaurant.html
- Restaurace Flip (Bernard Pub), Gahurova 5265: https://www.menicka.cz/24-restaurace-flip-bernard-pub.html
- Budvarka Zlín: https://www.menicka.cz/5881-budvarka-zlin.html
- U Ševce, Kvítková 4323: https://www.menicka.cz/5492-u-sevce.html
- Radegastovna Rex, Okružní 4701: https://www.menicka.cz/3538-radegastovna-rex.html
- U Barcuchů (jídelna), Mokrá 5215: https://www.menicka.cz/3027-u-barcuchu.html
Ověř, že menu na stránce je opravdu pro dnešní datum. Jídla si nevymýšlej. Pokud restaurace dnes menu nemá, napiš to u ní.

3) Pro každé jídlo včetně polévek odhadni kcal a bílkoviny/sacharidy/tuky v gramech (restaurace je neuvádějí, jsou to odhady). Polévky označ 🥣, ryby 🐟, jídla s masem (včetně uzeniny, slaniny, šunky a polévek s masem) 🥩. Ikony piš na začátek názvu jídla v pořadí ✅ 🥣 🥩/🐟, např. "✅ 🥩 Kuřecí stehno, rýže".

4) V každé restauraci označ ✅ jedno nejvhodnější jídlo: málo kcal, sacharidů a tuků, hodně bílkovin (cíl: zhubnout kortizolové břicho). Ryba nikdy nesmí být označena jako nejlepší, uživatel ryby nejí. Do pole tip dej krátkou radu (např. zaměnit přílohu za salát).

5) Pořadí restaurací podle polohy: pondělí až středa od Vavrečkova 7074 (Prostě a Pilsner Urquell první, pak podle vzdálenosti), čtvrtek a pátek od Podlesí 5375 (domov). Souřadnice restaurací jsou ve stránkách v kódu mapy (maps.LatLng).

6) Výstup: vytvoř stránku přesně podle šablony níže. Neměň CSS, strukturu ani vykreslovací kód, jen vyplň pole R a nadpis. Formát řádku: [název, cena, kcal, B, S, T, typ], kde typ je "b" (nejlepší), "f" (ryba), "s" (polévka) nebo vynech. Restaurace: [název, adresa, url, tip, [řádky]]. Ulož ji jako HTML soubor obedy-YYYY-MM-DD.html do pracovního adresáře (je-li to git repozitář, commitni ho a pushni na svou pracovní větev) a zveřejni ho na STÁLÉ adrese Artifactu https://claude.ai/artifact/47hfrdXTR3C8J7uo4pLsTK: nejdřív zavolej nástroj Artifact s action "read" a tímto url, pak Artifact publish s file_path dnešního souboru, stejným url a label "D. M. RRRR" (bez icon, NIKDY nevytvářej nový Artifact bez url). Uživatel má tuto adresu v záložkách Safari. Pokud zveřejnění selže, pošli soubor nástrojem SendUserFile (display: render) a napiš proč. I v den volna („Dnes je volno“) stránku nepřepisuj. Názvy jídel ber ze stránek, čísla alergenů vynech, poznámky o nápojích a obalech nevypisuj. Na konec napiš česky krátké shrnutí: nejlepší jídlo v každé restauraci a které restaurace dnes menu nemají. Odpověď piš česky.

ŠABLONA:
```html
<title>Obědy Zlín</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Layout: restaurace pod sebou; dish = karta na telefonu, řádek tabulky od 760px */
:root{
  --bg:#f3f5f2; --surface:#ffffff; --fg:#1d2a24; --muted:#5b6b62; --line:#dde3dd;
  --best:#1f7a4d; --best-bg:#e3f3ea; --fish:#2b6cb0; --fish-bg:#e4eef9; --soup:#9a6b12; --soup-bg:#f6ecd6;
  --f-body:'Figtree',system-ui,sans-serif; --f-num:'IBM Plex Mono',ui-monospace,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --bg:#121a16; --surface:#1b2520; --fg:#e8eee9; --muted:#9bab9f; --line:#2c3a33;
  --best:#5fd197; --best-bg:#163626; --fish:#7db3ee; --fish-bg:#172a40; --soup:#e3b55a; --soup-bg:#3a2f14; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#121a16; --surface:#1b2520; --fg:#e8eee9; --muted:#9bab9f; --line:#2c3a33;
  --best:#5fd197; --best-bg:#163626; --fish:#7db3ee; --fish-bg:#172a40; --soup:#e3b55a; --soup-bg:#3a2f14; color-scheme:dark}
body{background:var(--bg);color:var(--fg);font-family:var(--f-body);font-size:15px;line-height:1.4;
  padding-block:20px 40px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
main{max-width:980px;margin:0 auto;display:flex;flex-direction:column;gap:20px}
h1{font-size:1.6rem;margin:0;text-wrap:balance}
.sub{color:var(--muted);margin:4px 0 0;font-size:.9rem}
.legend{display:flex;flex-wrap:wrap;gap:8px;font-size:.8rem}
.chip{padding:2px 8px;border-radius:99px;background:var(--surface);border:1px solid var(--line)}
.rest{background:var(--surface);border:1px solid var(--line);border-radius:12px;overflow:hidden;min-width:0}
.rest header{padding:12px 14px;border-bottom:1px solid var(--line)}
.rest h2{margin:0;font-size:1.05rem}
.addr{color:var(--muted);font-size:.8rem}
.tip{padding:8px 14px;font-size:.85rem;background:var(--best-bg);color:var(--best)}
.dish{display:grid;grid-template-columns:1fr auto;gap:2px 10px;padding:10px 14px;border-top:1px solid var(--line)}
.dish:first-of-type{border-top:0}
.name{font-weight:600;min-width:0}
.price{font-family:var(--f-num);font-size:.85rem;color:var(--muted);text-align:right}
.m{grid-column:1/-1;display:flex;flex-wrap:wrap;gap:4px 12px;font-family:var(--f-num);font-size:.8rem;color:var(--muted)}
.m b{color:var(--fg);font-weight:500}
.m span::before{content:attr(data-l)" ";font-family:var(--f-body);font-size:.72rem}
.best{background:var(--best-bg)} .best .name{color:var(--best)}
.fish .name{color:var(--fish)} .soup .name{color:var(--soup)}
.note{font-size:.8rem;color:var(--muted)}
.note a{color:inherit}
@media(min-width:760px){
  .cols,.dish{display:grid;grid-template-columns:minmax(0,1fr) 70px 70px 60px 60px 60px;gap:0 8px;align-items:baseline}
  .cols{padding:6px 14px;font-size:.72rem;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);border-bottom:1px solid var(--line)}
  .cols span:nth-child(n+2){text-align:right}
  .m{display:contents}
  .price{order:2}.m span{text-align:right;order:3}
  .m span::before{content:none}
  .name{order:1}
}
@media(max-width:759px){.cols{display:none}}
</style>
<main>
<div><h1>Obědy Zlín · {DEN A DATUM}</h1>
<p class="sub">Pořadí podle polohy: Po–St Vavrečkova 7074, Čt–Pá Podlesí 5375. {Dnes DEN, KANCELÁŘ nebo DOMA.}</p></div>
<div class="legend"><span class="chip">✅ nejlepší volba</span><span class="chip">🥣 polévka</span><span class="chip">🐟 ryba</span><span class="chip">🥩 maso</span><span class="chip">B bílkoviny · S sacharidy · T tuky (g)</span></div>
<div id="out" style="display:contents"></div>
<p class="note">Kalorie a makra jsou moje hrubé odhady, restaurace je neuvádějí. Jídla a ceny z jednotlivých stránek na <a href="https://www.menicka.cz/zlin.html">menicka.cz</a>.</p>
</main>
<script>
// [název, cena, kcal, B, S, T, typ] typ: b=best, f=ryba, s=polévka
var R=[ /* SEM VLOŽ DATA DNEŠNÍHO DNE */ ];
function e(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;")}
document.getElementById("out").innerHTML=R.map(function(r){
 return '<section class="rest"><header><h2><a style="color:inherit;text-decoration:none" href="'+r[2]+'">'+e(r[0])+'</a></h2><div class="addr">'+e(r[1])+(r[1]?'':'')+'</div></header>'+
 (r[3]?'<div class="tip">'+e(r[3])+'</div>':'')+
 '<div class="cols"><span>Jídlo</span><span>Cena</span><span>kcal</span><span>B</span><span>S</span><span>T</span></div>'+
 r[4].map(function(d){
  return '<div class="dish '+(d[6]=="b"?"best":d[6]=="f"?"fish":d[6]=="s"?"soup":"")+'"><div class="name">'+e(d[0])+'</div><div class="price">'+e(d[1])+'</div>'+
  '<div class="m"><span data-l="kcal"><b>'+d[2]+'</b></span><span data-l="B"><b>'+d[3]+'</b></span><span data-l="S"><b>'+d[4]+'</b></span><span data-l="T"><b>'+d[5]+'</b></span></div></div>';
 }).join('')+'</section>';
}).join('');
</script>

```
