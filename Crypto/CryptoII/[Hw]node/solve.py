from Crypto.Util.number import inverse, bytes_to_long, isPrime, long_to_bytes
from collections import namedtuple
from sage.all import *

from data import Gx, Gy, gx, gy, p

Point = namedtuple("Point", "x y")

alpha, beta = Mod(1, p), Mod(-2, p)
G, g = Point(Gx, Gy), Point(gx, gy)

def phi(P):
    return (P.y + (alpha - beta).sqrt() * (P.x - alpha)) / (P.y - (alpha - beta).sqrt() * (P.x - alpha))

flag = discrete_log(phi(G), phi(g)) 
print(long_to_bytes(flag))