# Cvičení č. 4 – 23.10.2020

## Algoritmizace

### Opravy kódu

**Příběh** 

Váš šéf vám dal za úkol opravit projekt po předchozím programátorovi, panu X. Pan X už ve firmě nepracuje a při prohlížení jeho kódů vám dochází proč. Jeho kódy totiž fungují jen na první pohled – při spuštění na reálných datech se chovají nepředvídatelně, zamrzají nebo vracejí nesprávné výsledky.

**Úkoly**
1. Opravte funkci `euclid_gcd(a, b)` v souboru [euclid_notfixed.py](euclid_notfixed.py) pro výpočet nejvyššího společného dělitele čísel `a` a `b`.
   - Funkce prochází unit testy, ale na určitých datech se zacyklí a nevrátí žádný výsledek.
2. Opravte funkci `eratosthenes(n)` v souboru [erastothenes_notfixed.py](erastothenes_notfixed.py) pro výpočet všech prvočísel <= `n`
   - Funkce prochází unit testy, ale s většími vstupy je příliš pomalá a na určitých datech vrací špatný výsledek.

**Vysvětlivka:** Funkce `assert` se používá pro kontrolu podmínky, která musí být vždy splněna. Pokud je výraz uvnitř funkce `assert` vyhodnocen na False, funkce vrátí `AssertionError`. Toho se využívá např. pro automatické testování.