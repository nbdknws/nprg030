#!/usr/bin/env python3

# spočítá nejvyššího společného dělitele čísel a,b
def euclid_gcd(a, b):
    while b > 0:
        a = a % b

        if a < b:
            a, b = b, a

    return a

# testy
assert(euclid_gcd(10,2) == 2)
assert(euclid_gcd(10,5) == 5)
assert(euclid_gcd(7,7) == 7)
assert(euclid_gcd(7,3) == 1)
assert(euclid_gcd(3,7) == 1)
assert(euclid_gcd(21,14) == 7)