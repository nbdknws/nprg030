# Cvičení č. 7 – 13.11.2020

## Algoritmizace

### Zásobník a fronta
- **abstraktní datové struktury**: definujeme operace, popisujeme chování  - neřešíme konkrétní implementaci
- zásobník
  - operace `push()` a `pop()`
  - princip LIFO: last in - first out
- fronta
  - operace `enqueue()` a `dequeue()`
  - princip FIFO: first in - first out
  
![stack-queue](stack-queue.png)


### Aritmetické výrazy
- infixová notace
  - operátor mezi operandy
  - záleží na prioritě operátorů / uzávorkování
- prefixová (polská) notace
  - operátor před operandy
  - jednoznačná
- postfixová notace
  - operátor po operandech
  - jednoznačná

---
#### Příklady
  - infix:  `A * B + C`
  - prefix:  `+ * A B C`  (odpovídá výrazu `sum(mul(A, B), C)`)
  - postfix:  `A B * C +` (vyhodnotím A B -> multi)
---
  - infix:  `A * (B + C)`
  - prefix:  `* A + B C`  (odpovídá výrazu `mul(A, sum(B,C)`)
  - postfix:  `A B C + *` 
---
#### Úkoly
Výrazy mohou obsahovat operátory `+`, `-`, `*`, `/` a číselné operandy. Jednotlivé literály můžete identifikovat pomocí funkcí `is_operator()` a `is_operand()`. Operátor se dvěma operandy můžete vyhodnotit jako `OPERATOR(OPERAND1, OPERAND2)`.

Máte k dispozici zásobník `stack` s funkcemi `push()` a `pop()`.

**Postfix**
1. Zapište (pseudo)kódem algoritmus pro vyhodnocení výrazu v postfixové notaci.
2. Převeďte ručně výraz `(7 + 3) * (5 - 2)` do postfixové notace.
3.Ukažte jednotlivé kroky Vašeho algoritmu z bodu 1 při vyhodnocení výrazu `(7 + 3) * (5 - 2)` v **postfixové notaci** z bodu 2.

**Prefix**
1. Zapište (pseudo)kódem algoritmus pro vyhodnocení výrazu v prefixové notaci.
2. Převeďte ručně výraz `(7 + 3) * (5 - 2)` do prefixové notace.
3. Ukažte jednotlivé kroky Vašeho algoritmu z bodu 1 při vyhodnocení výrazu `(7 + 3) * (5 - 2)` v **prefixové notaci** z bodu 2.

Která notace je výhodnější pro průběžné vyhodnocování výrazu během jeho zadávání?

### Průchod stromem po hladinách

![tree](tree.png)

#### Úkol

Strom obsahuje prvky typu `Node`, každý prvek obsahuje hodnotu `value`. Ke stromu můžete přistupovat přes jeho kořen `root` (v příkladu prvek s hodnotou `1`), k potomkům každého prvku pak přes atribut `node.children`.

Máte k dispozici frontu `queue` s funkcemi `enqueue()` a `dequeue()`.

1. Zapište (pseudo)kód, který vypíše prvky ve stromu po hladinách (tedy v příkladu v pořadí `1 2 3 4 5 6 7 8 9`).
2. Ukažte jednotlivé kroky Vašeho algoritmu z bodu 1 na stromu z příkladu.

## Programování
- viz [kód](lab07.py)