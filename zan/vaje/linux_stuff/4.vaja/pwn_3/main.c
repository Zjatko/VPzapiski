#include <stdio.h>

void win(long a, long b)
{
	if (a == 0xdeadbeef && b == 0xbadc0ffee)
		printf("You win!\n");
	else
		printf("You lose!\n");
}

int main()
{
	char buffer[32];
	gets(buffer);
}

