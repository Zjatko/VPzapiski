#include <stdio.h>
#include <stdlib.h>

void win()
{
	system("/bin/sh");
}

int main(int argc, char *argv[])
{
	char buf[512];
	
	if (argc != 2) {
		fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
		return 1;
	}

	FILE *fp = fopen(argv[1], "r");
	if (fp == NULL) {
		perror("fopen");
		return 1;
	}

	while (fgets(buf, 1024, fp) != NULL) {
		printf("%s", buf);
	}

	return 0;
}
