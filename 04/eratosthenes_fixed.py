#!/usr/bin/env python3

# vrátí seznam prvočísel menších nebo rovných n
def eratosthenes(n):
    is_prime = [True for _ in range(2, n+1)]
    primes = []

    for p in range(2,n+1):
        if is_prime[p-2]:
            primes.append(p)

            for i in range(p*p, n+1, p):
                is_prime[i-2] = False

    return primes

# testy
assert(eratosthenes(1) == [])
assert(eratosthenes(4) == [2, 3])
assert(eratosthenes(15) == [2, 3, 5, 7, 11, 13])
assert(eratosthenes(100000)[-1] == 99991)