#include <stdio.h>

void win() {
	printf("You win!\n");
}

int main() {
	char buffer[20];
	gets(buffer);

	printf("%s\n", buffer);
	return 0;
}
