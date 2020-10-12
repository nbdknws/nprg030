# #!/usr/bin/env python3

"""
Kód ke cvičení #1 z NPRG030.
Kód nemá fungovat jako celek, jednotlivé části byly postupně vysvětleny na cvičení.
"""

# funkce print() vytiskne svoje argumenty na standardní výstup
print("Hello world")

# bez argumentů vytiskne pouze nový řádek
print()

# ...ve skutečnosti vytiskne nový řádek na konci vždy, dokud neřekneme jinak
print("Hello world", end="")

# vstup získáme pomocí funkce input()
input()

# můžeme ho uložit do proměnné a přidat vstupní prompt
s = input("Zadejte text: ")

# vstup je vždy string, ale můžeme ho přetypovat na integer - celé číslo
i = int(input("Zadejte číslo: "))

# ...nebo na float - číslo s desetinnou částí
f = float(input("Zadejte číslo: "))

# čísla můžeme sčítat, odčítat...
j = 2 + 5
k = 1 - j

# ...násobit, umocňovat a dělit
l = 2 * 3
print(l)
m = 2 ** 3
print(m)
n = 2 / 3
print(n)

# zápis můžeme někdy zkrátit
o = 0
o += 1      # stejný výsledek, jako o = o + 1

# čísla také můžeme porovnávat...
print(l < m)
print(l >= m)
print(l == m) # musíme použít ==, protože = je přiřazení do proměnné
print(l != m) # nerovná se

# ...a to i zřetězeně
print(n < l <= m)

# pozor, float má omezenou přesnost
f = 1/6
print(f)

# a může se stát, že na to doplatíme
sum = 0
while sum != 1:
    sum += 1/6
    # toto nikdy nedoběhne

# while je tzv. cyklus (loop)
# while cyklus opakuje vnitřní blok kódu, dokud je PODMÍNKA vyhodnocena jako pravdivá (True)
# zapisujeme: `while PODMÍNKA:`
# vnitřní blok kódu je odsazený tabem / čtyřmi mezerami - pozor, používat konzistentně
i = 0

while i < 10:
    i += 1
    print(i)

# hodnotu proměnných můžeme kontrolovat pomocí podmínky if (/ elif / else)
age = int(input("Zadejte věk: "))

if 0 <= age < 18:
    print("Dítě")
elif 18 < age < 60:     # elif - klíčové slovo, zkratka pro "else if"
    print("Dospělý")
elif age > 60:
    print("Důchodce")
else:                   # pokud nebyla splněna žádná předchozí podmínka
    print("Neplatný věk")