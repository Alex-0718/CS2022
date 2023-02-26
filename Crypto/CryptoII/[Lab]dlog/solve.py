from Crypto.Util.number import isPrime, getPrime, long_to_bytes
from sage.all import *
from pwn import *

while True:
    a = getPrime(15) 
    pad = 1024 - (a ** 50).bit_length()
    prime = (a ** 51) * (2 ** pad)
    if isPrime(prime + 1): 
        print(prime.bit_length())
        break

r = remote('edu-ctf.zoolab.org', '10103')
print(r.sendlineafter(b'give me a prime', str(prime + 1).encode()))
print(r.sendlineafter(b'give me a number', b'2'))
r.recvuntil(b'The hint about my secret: ')
hint = r.recv()[:-1].decode()

b = Mod(2, prime + 1)
a = Mod(hint, prime + 1)

flag = discrete_log(a, b)

print(long_to_bytes(flag))
