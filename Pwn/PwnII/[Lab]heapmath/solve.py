from pwn import *

r = remote('edu-ctf.zoolab.org', '10006')

r.recvuntil(b"\n")
malloc_size, free_order = [], []

# ----------- ** tcache chall ** -----------
for i in range(7):
    malloc_size.append(int(r.recvuntil(b"\n").decode()[-7:-3], 16))

for i in range(7):
    free_order.append(ord(r.recvuntil(b"\n").decode()[-4:-3]) - 65)

order = ["", ""]

for i in reversed(free_order):
    if malloc_size[i] < 41 and malloc_size[i] > 24:
        order[0] += chr(65 + i) + " --> "
order[0] += "NULL\n"

for i in reversed(free_order):
    if malloc_size[i] < 57 and malloc_size[i] > 40:
        order[1] += chr(65 + i) + " --> "
order[1] += "NULL\n"

r.sendafter(b'> ', order[0].encode())
r.sendafter(b'> ', order[1].encode())

# ----------- ** address chall ** -----------

r.recvuntil(b"----------- ** address chall ** -----------\n")
record = r.recvuntil(b"\n").decode()
chunk1, address = record[8], int(record[13:-4], 16)
chunk2 = r.recvuntil(b"\n").decode()[0]

for i in range(ord(chunk1) - 65, ord(chunk2) - 65):
    if malloc_size[i] < 25:
        address += 32
    elif 24 < malloc_size[i] < 41:
        address += 48
    else:
        address += 64

r.sendafter(b"> ", hex(address).encode() + b"\n")

# ----------- ** index chall ** -----------
r.recvuntil(b"----------- ** index chall ** -----------\n")
size = int(r.recvuntil(b"\n")[-7:-3].decode(), 16)
size = int(r.recvuntil(b"\n")[-7:-3].decode(), 16)
index = int(r.recvuntil(b"\n")[2:3].decode())

index += size // 8 + 2
r.sendafter(b"> ", str(index).encode() + b"\n")

# ----------- ** tcache fd chall ** -----------
r.recvuntil(b"----------- ** tcache fd chall ** -----------\n")
r.recvuntil(b"\n")
r.recvuntil(b"\n")
address = int(r.recvuntil(b"\n")[13:-4].decode(), 16) - size - 16 # prev_data = 16
r.sendafter(b"> ", hex(address).encode() + b"\n")

# ----------- ** fastbin fd chall (final) ** -----------
r.recvuntil(b"----------- ** fastbin fd chall (final) ** -----------\n")
r.recvuntil(b"\n")
size = int(r.recvuntil(b"\n")[-7:-3].decode(), 16)
address = int(r.recvuntil(b"> ")[-19:-5].decode(), 16) - size - 32 # prev_data = 32
r.send(hex(address).encode() + b"\n")

r.interactive()
# r.interactive()