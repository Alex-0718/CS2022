from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes
# from sage.all import *
from pwn import *

r = remote('edu-ctf.zoolab.org', '10104')

p = int(r.recvuntil(b'\n').decode()[:-1])
if (p - 1) % 3 != 0: exit(0)
g = pow(2, (p - 1) // 3, p)
r.sendline(str(g).encode())
enc = int(r.recvuntil(b'\n').decode()[:-1])
for i in range(3):
    print(long_to_bytes(enc * pow(g, -i, p) % p))