#! /usr/bin/python3
from Crypto.Util.number import bytes_to_long, getPrime
import random

from secret import FLAG

p = getPrime(1024)
assert bytes_to_long(FLAG) < p
print(p)

g = int(input().strip())
g %= p
if g == 1 or g == p - 1:
    print("Bad :(")
    exit(0)

a = random.randint(2, p - 2)
# print(f"a = {a}")
A = pow(g, a, p)
# print(f"g_a = {A}")
if A == 1 or A == p - 1:
    print("Bad :(")
    exit(0)

b = random.randint(2, p - 2)
# print(f"b = {b}")
# print(f"g_ab = {pow(A, b, p)}")
c = pow(A, b, p) * bytes_to_long(FLAG) % p
print(c)
