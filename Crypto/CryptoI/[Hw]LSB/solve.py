from pwn import *
from Crypto.Util.number import long_to_bytes, inverse

r = remote('edu-ctf.zoolab.org', '10102')

n = int(r.recvuntil(b'\n'))
e = int(r.recvuntil(b'\n'))
enc = int(r.recvuntil(b'\n'))

index, plainText, a, count, message = 0, 0, 0, 0, 0

def LSB_oracle(cipher):
    r.sendline(cipher)
    return int(r.recvuntil('\n'))

while True:
    inv = inverse(3, n)
    cipher = (pow(inv, index * e, n) * enc) % n
    plainText = LSB_oracle(str(cipher))
    coefficient = (plainText - (a * inv) % n) % 3
    if coefficient == 0:
        count += 1
        if count == 15: break
    else:
        count = 0

    a = a * inv + coefficient
    message = message + coefficient * (3 ** index) 
    index = index + 1
print(long_to_bytes(message)[:50])