from Crypto.Cipher import AES
from pwn import *
import binascii
import tqdm

BLOCKSIZE = 32
TRUE = b'Well received :)\n'

def bytes2str(b):
    return str(b)[2:-1]

r = remote('edu-ctf.zoolab.org', '10101')
inp = r.recv()[:-1]

cipherList = list(map(bytes2str, [inp[i * BLOCKSIZE:(i + 1) * BLOCKSIZE] for i in range(int(len(inp) / BLOCKSIZE))]))
flag = []

for i in range(len(cipherList) - 1):
    iv, cipher = cipherList[i], cipherList[i + 1]
    for j in tqdm.tqdm(range(15, -1, -1)):
        original = int('0x' + iv[2 * j:2 * (j + 1)], 16)
        for k in range(257):
            if k == original: continue
            if k == 256: k = original 
            replaceBytes = hex(k)[2:] if len(hex(k)[2:]) == 2 else '0' + hex(k)[2:]
            iv = iv[:2 * j] + replaceBytes + iv[2 * (j + 1):]
            r.sendline(iv + cipher)
            receive = r.recv()
            if receive == TRUE:
                number = k ^ 128 ^ 00
                replaceBytes = hex(number)[2:] if len(hex(number)[2:]) == 2 else '0' + hex(number)[2:]
                iv = iv[:2 * j] + replaceBytes + iv[2 * (j + 1):]
                break
    plainText = int('0x' + iv, 16) ^ int('0x' + cipherList[i], 16)
    flag.append(bytes.fromhex(hex(plainText)[2:]))
print(b"".join(flag))