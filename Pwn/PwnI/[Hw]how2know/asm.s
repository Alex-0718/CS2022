	.file	"asm.c"
	.intel_syntax noprefix
	.text
	.data
	.align 32
	.type	flag, @object
	.size	flag, 48
flag:
	.string	"FLAG{NEVER_LOSES_87}"
	.zero	27
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	endbr64
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	push	r13
	push	r12
	push	rbx
	.cfi_offset 13, -24
	.cfi_offset 12, -32
	.cfi_offset 3, -40
	lea	rbx, flag[rip]
	movsx	rax, r13d
	add	rax, rbx
	movzx	ebx, BYTE PTR [rax]
	movsx	eax, bl
	cmp	r12d, eax
	setg	al
	movzx	ebx, al
.L2:
	test	ebx, ebx
	jne	.L2
	mov	eax, 0
	pop	rbx
	pop	r12
	pop	r13
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
