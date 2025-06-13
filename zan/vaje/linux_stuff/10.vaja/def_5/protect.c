#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <linux/landlock.h>
#include <fcntl.h>
#include <sys/prctl.h>
#include <seccomp.h>

#ifndef O_PATH
#define O_PATH 010000000
#endif

int main(int argc, char *argv[])
{
	if (argc < 2) {
		fprintf(stderr, "Usage: %s <program> <args...>\n", argv[0]);
		return 1;
	}

	// TODO: Protect program from running external programs
	

	// TODO: Protect program from opening files outside of the current directory
	

	// TODO: Apply protections
	

	// Run the program
	execv(argv[1], &argv[1]);
	perror("execv");
	return 0;
}
