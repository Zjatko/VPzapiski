#include <stdio.h>

void win() {
	printf("You win!\n");
}

int main() {
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);

	char buffer[20];
	char choice = 'n';
	
	do
	{
		printf("Enter your name: ");
		gets(buffer);

		printf(buffer);
		printf("\n\nIs that correct? [y/n]\n");
		choice = getchar();
		getchar();
	} while (choice != 'y');

	printf("Hello, %s!\n", buffer);

	return 0;
}
