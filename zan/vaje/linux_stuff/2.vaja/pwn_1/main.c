#include <stdio.h>
#include <unistd.h>

void win() {
	printf("You win!\n");
}

int main() {
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);

	char buffer[64];
	
	printf("Enter your buffer: ");
	read(0, buffer, 0x64);

	printf("Hello, %s! What's your surname?\n", buffer);
	read(0, buffer, 0x64);

	printf("Got it, %s!\n", buffer);

	return 0;
}
