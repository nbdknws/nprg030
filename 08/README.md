# Cvičení č. 8 – 21.11.2020

## Programování
### Textový vs. binární soubor
- každý soubor je jen posloupnost bitů, v zásadě je tedy každý soubor binární
- textový soubor je při interpretaci v určitém kódování složený z čitelných znaků a pomocí newlinů může být rozdělený na řádky
- newline (konec řádku) 
  - ve Windows dva symboly: CR (carriage return, "\r", 0x0D) a LF (line feed, "\n", 0x0A) 
  - na Unixových systémech pouze LF, na Mac OS pouze CR 
  - ve stringu v Pythonu používáme pouze LF ("\n") - pro soubory otevřené v textovém modu automaticky konvertované podle používaného OS
- přípona souboru: jen kosmetická záležitost, o obsahu souboru nemusí nic vypovídat

### Kódování
- ASCII
  - původní standard pro kódování znaků
  - obsahuje pouze znaky anglické abecedy, interpunkci a řidicí symboly
  - 7 bitů, A=65 (100 0001), a=97 (110 0001)
- kódování pro češtinu v 8 bitech (1 byte = 1 znak)
  - ISO 8859-2 - nejrozšířenější standard používaný pro východoevropské jazyky
  - Windows-1250 - až do nedávna kódování používané na Windows, částečně nekompatibilní s ISO 8859-2
- Unicode
  - unikátní kód pro každý symbol (v současnosti přes 140 000)
  - [web](https://home.unicode.org)
  - znak podle kódu: Ctrl+Shift+U na Linuxu, Alt Gr na Windows
- různé standardy jak Unicode kódovat: UTF-8, UTF-16, UTF-32
  - přímý zápis kódu znaku by přinášel různé nevýhody - dlouhý kód i pro nejzákladnější znaky, nekompatibilita s ASCII
  - UTF-8 - zpětně kompatibilní s ASCII, variabilní počet bytů na znak
  - UTF-32 - 4 byty na každý znak
  - [video o UTF-8](https://www.youtube.com/watch?v=MijmeoH9LT4)
  - [vysvětlení jak funguje Unicode](https://www.youtube.com/watch?v=I-pQH_krD0M)

### Standardní proudy
- standardní vstup: *stdin*
  - implicitně vstup z příkazové řádky
  - obsah souboru můžeme přesměrovat na standardní vstup: `python program.py < vstup.txt`
- standardní výstup: *stdout*
  - implicitně výstup na příkazovou řádku
  - výstup programu můžeme přesměrovat do souboru: `python program.py > vstup.txt`
  - pokud chceme obsah pouze přidat na konec souboru: `python program.py >> vstup.txt`
- standardní chybový výstup: *stderr*
  - lze potlačit, případně přesměrovat na standardní výstup (OS-specific, více případně později)

Dále viz [kód](lab08.py).

## Algoritmizace

### Rekurze
- příklady rekurze
	- matrjoška
	- [odrážející se zrcadla](https://en.wikipedia.org/wiki/Infinity_mirror)
	- [rekurzivní zkratka](https://cs.wikipedia.org/wiki/Rekurzivn%C3%AD_zkratka)
	- [kapradí](https://recursivecurve.files.wordpress.com/2016/11/green-715535_1920.jpg)
	- [fraktály](https://fractalfoundation.org/resources/what-are-fractals/) ([Sierpińského trojúhelník](https://vimeo.com/274300559))
	- halda
- rekurzivní definice (úplného) binárního stromu:
  1. binární strom je samotný uzel
  2. binární strom je uzel, který má jako levého a pravého potomka binární strom  
- při rekurzi se volání funkcí ukládají na zásobník → hloubka rekurze omezená velikostí zásobníku

### Zaplacení sumy mincemi
Máte k dispozici mince o hodnotě 5, 2 a 1. Je zadána částka `N`. Najděte všechny způsoby, jak můžeme částku zaplatit pomocí mincí.

Příklad:
```
N = 6

5 1
2 2 2
2 2 1 1
2 1 1 1 1
1 1 1 1 1 1
```

**[Spoiler] Řešení**
```python
seznam_minci = [5, 2, 1]

def zaplat(kolik, pouzite_mince, nejvyssi_pouzitelna_mince):
    # poslední krok, již není co zaplatit
    if kolik == 0:
        print(pouzite_mince)

    # zkoušíme přidat každou z dostupných mincí
    for mince in seznam_minci:
        # nezkoušíme ovšem mince, co by již přesáhly částku, kterou chceme zaplatit 
        # a mince bereme od největší k nejmenší pro omezení duplicit
        if kolik >= mince and mince <= nejvyssi_pouzitelna_mince:
            zaplat(kolik=kolik - mince, pouzite_mince=pouzite_mince + [mince], nejvyssi_pouzitelna_mince=mince)

zaplat(kolik=N, pouzite_mince=[], nejvyssi_pouzitelna_mince=seznam_minci[0])
```

### Uzávorkování
Na vstupu dostanete počet párů závorek `N`. Najděte všechna platná uzávorkování s těmito páry závorek.

Příklad:
```
N = 2

(())
()()
```

**[Spoiler] Řešení**
```python
def najdi_uzavorkovani(uzavorkovani, potreba_uzavrit, zbyva_levych):
    # došly závorky, vypiš uzávorkování
    if potreba_uzavrit == 0 and zbyva_levych == 0:
        print(uzavorkovani)

    # přidej levou závorku
    if zbyva_levych > 0:
        najdi_uzavorkovani(uzavorkovani=uzavorkovani+"(", potreba_uzavrit=potreba_uzavrit+1, zbyva_levych=zbyva_levych-1)
    
    # přidej pravou závorku
    if potreba_uzavrit > 0:
        najdi_uzavorkovani(uzavorkovani=uzavorkovani+")", potreba_uzavrit=potreba_uzavrit-1, zbyva_levych=zbyva_levych)

najdi_uzavorkovani(uzavorkovani="", potreba_uzavrit=0, zbyva_levych=N)
```