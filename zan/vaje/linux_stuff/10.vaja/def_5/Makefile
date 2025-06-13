CC=clang

all: protect

cat: cat.c
	$(CC) -g -o $@ $< -static -no-pie -fno-stack-protector

protect: protect.c
	$(CC) -g -o $@ $< -lseccomp
