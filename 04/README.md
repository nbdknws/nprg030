# Cvičení č. 4 – 23.10.2020

## Algoritmizace

### Opravy kódu

**Příběh** 

Váš nadřízený vám dal za úkol opravit projekt po předchozím programátorovi, panu X. Pan X už ve firmě nepracuje a při prohlížení jeho kódů vám dochází proč. Jeho kódy totiž fungují pouze na první pohled – při spuštění na reálných datech se chovají nepředvídatelně, zamrzají nebo vracejí nesprávné výsledky :man_shrugging:

**Úkoly**

Najděte vstupy, pro které kód nefunguje, identifikujte chyby v implementaci a  funkce opravte.

1. V souboru [euclid_notfixed.py](euclid_notfixed.py) se nachází funkce `euclid_gcd(a, b)` pro výpočet nejvyššího společného dělitele čísel `a` a `b`. Funkce prochází unit testy, ale na určitých datech se zacyklí a nevrátí žádný výsledek. 
2. V souboru [eratosthenes_notfixed.py](eratosthenes_notfixed.py) se nachází funkce `eratosthenes(n)` pro výpočet všech prvočísel `<= n`. Funkce prochází unit testy, ale s většími vstupy je příliš pomalá a na určitých datech vrací špatný výsledek.

**Vysvětlivka**

*Funkce `assert` se používá pro kontrolu podmínky, která musí být vždy splněna. Pokud je výraz uvnitř funkce `assert` vyhodnocen na False, funkce vrátí `AssertionError`. Toho se využívá např. pro automatické testování.*

### Třídění

Doplňte do [šablony](quadratic_sorts_template.py) funkce `bubble_sort(l)`, `insertion_sort(l)` a `selection_sort(l)`. Vypisujte každou záměnu prvků v poli (např. "Vyměňuji 5 a 4"), částečně setříděné pole po každé iteraci, a vraťte kromě setříděného pole i celkový počet kroků vnitřního cyklu.

[Odkaz na animace](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)