#include<stdio.h>
#include<string.h>

char buffer[64];

void win(long a, long b)
{
	char secret[64];

	if (a == 0xdeadbeef)
	{
		FILE *f = fopen("secret.txt", "r");
		fgets(secret, 64, f);
	}

	if (b == 0x1337c0de)
	{
		puts(secret);
	}
}

int main()
{
	char buffer[64];
	gets(buffer);
	return 0;
}
