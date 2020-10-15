# Cvičení č. 3 – 16.10.2020

## Algoritmizace

### Úlohy na cykly

1) Kolikrát se provede vnitřní cyklus v závislosti na `n`? Jaká bude jeho asymptotická časová složitost vyjádřená pomocí `n`?
```python
l=0
for i in range(n):
    for j in range(i,n):
        l+=1
```
2) Kolikrát se provede vnitřní cyklus v závislosti na `m` a `n`? Jaká bude jeho asymptotická časová složitost vyjádřená pomocí `m` a `n`?
```python
for i in range(n):
    for j in range(n*n):
        k = 0
        while k*k < m:
            k += 1
```
3) Kolikrát se provede cyklus v závislosti na `n`? Jaká bude jeho asymptotická časová složitost v závislosti na hodnotách `n` (uvažujte *best-case* a *worst-case*)?
```python
while n > 0:
  if n % 3 == 0:
    n //= 3
  else:
    break
```
4) Kolikrát se provede vnitřní cyklus v závislosti na `n`? Jaká bude jeho asymptotická časová složitost vyjádřená pomocí `n`?
```python
for i in range(n,1,-1):
    j = i
    while j > 0:
        j //= 2
```

### Úlohy na asymptotickou složitost
*viz slide 9 v [prezentaci z přednášky](2Numericke.pdf)*

Dokažte nebo vyvraťte:
1. Pokud `f(n)=O(g(n))`, pak `g(n)=O(f(n))`
2. Pokud `f(n)=O(g(n))`, pak `2^f(n)=O(2^g(n))`
3. Pokud `f(n)=O(g(n))`, pak `g(n)=Ω(f(n))`
4. `f(n)=O(f(n)^2)`