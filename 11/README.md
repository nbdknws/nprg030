# Cvičení č. 11 – 11.12.2020

## Programování

### Running example
[Lodě](lode)

- minimalistický Python projekt
- ukázka rozdělení do tříd a souborů, způsob návrhu programu

### Struktura programu

- je vhodné dělit projekt do více souborů
  - výhody: modularizace, přehlednější kód
- architektura [Model-View-Controller](https://cs.wikipedia.org/wiki/Model-view-controller) (MVC)
  - *model* - datové struktury
  - *view* - uživatelské rozhraní
  - *controller* - logika programu
- soubor `main.py`
  - konvence, slouží jako vstupní bod do našeho programu
- soubor `README`, `README.txt` nebo `README.md`
  - obsahuje stručný popis našeho programu a instrukce k použití
  - koncovka `md` značí použití formátování pomocí [Markdownu](https://cs.wikipedia.org/wiki/Markdown) (viz READMEs v tomto repozitáři) 
- soubor `LICENSE`: obsahuje [licenci](https://choosealicense.com) projektu
- soubor `requirements.txt`: obsahuje na jednotlivých řádcích balíčky potřebné ke spuštění projektu
  - pokud používáme pip, můžeme jednoduše nainstalovat pomocí `pip install -r requirements.txt`

### Moduly a importy
- Python modul vs. Python skript
  - liší se především ve způsobu použití: modul (většinou) importujeme, skript (většinou) pouštíme z příkazové řádky
  - vždy je to ale pouze obyčejný textový soubor se zdrojovým kódem
- import modulu "module.py" ve stejné složce: `import module`
  - stejné, jako když importujeme moduly ze standardní knihovny
  - k funkcím, třídám a proměnným pak přistupujeme přes tečku: např. `module.X()`
- `from module import X`: importuje `X` z `module` přímo do našeho namespace
  - nyní můžeme volat přímo `X()`
- `from module import X as Y`: přejmenuje v našem namespace `X` na `Y`
  - používá se často pro zkrácení zápisu, např. `import numpy as np`
- `from module import *`: importuje vše z modulu do našeho namespacu → **nepoužívat**
  - můžeme si nevědomky importovat další proměnné a s tím i pár záhadných chyb
- `if __name__ == "__main__":`
  - používáme pro kód, který se má spustit je v případě, že je soubor spuštěný z příkazové řádky
  - v tom případě je proměnná `__name__` nastavena na `"__main__"`
  - pokud je soubor importovaný jako modul, proměnná `__name__` je nastavena na jméno modulu a kód se neprovede

Oficiální style guide pro Python: [PEP8](https://www.python.org/dev/peps/pep-0008/#imports).


## Algoritmizace

### Přelévání vody
Máte k dispozici nádoby o objemu 10l, 7l a 2l. Na začátku máte 10l nádobu plnou vody, ostatní nádoby jsou prázdné.

- Jaké objemy vody (0l-10l) můžete s těmito nádobami odměřit?
- Kolik kroků na to potřebujete?

### Bludiště
Doplňte do [šablony](maze_template.py) kód, který najde cestu v bludišti.