#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	// Get name
	char* name = malloc(128);
	printf("Enter your name: ");
	scanf("%s", name);
	printf("Hello, %s!\n", name);

	// Open file
	FILE *input = fopen(argv[1], "r");

	// Get file size
	fseek(input, 0, SEEK_END);
	int size = ftell(input);
	fseek(input, 0, SEEK_SET);

	if (size > 10*1024*1024*1024) // size > 10GB
	{
		printf("File too large!\n");
		return 1;
	}

	// Read file
	int len;
	fscanf(input, "%d", &len);

	// Read data and calculate statistics
	int sum = 0;
	int* entries = malloc(len * sizeof(int));
	for (int i = 0; i < len; i++)
	{
		fscanf(input, "%d", &entries[i]);
		sum += entries[i];
	}
	int avg = sum / len;
	printf("Average: %d\n", avg);

	// Do stuff!
	int entry = 0;
	for (int i = 0; i < 10; i++)
	{
		printf("Select entry: ");
		scanf(" %d", &entry);
		printf("Entry %d: %d\n", entry, entries[entry]);
		printf("Modify entry: ");
		scanf(" %d", &entries[entry]);
	}

	// Greet and exit
	printf("Goodbye, %s!\n", name);
	return 0;
}
