#include <errno.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void quit(int sig) {
	printf("The current local time is:\n");
	system("date");
	printf("Goodbye...\n");
	exit(0);
}

void nope(int sig) {
	printf("Don't you wish you could just QUIT me?\n");
}

int main() {
	if (signal(SIGINT, nope) == SIG_ERR) {
		fprintf(stderr, "Unable to establish signal handler: %s\n",
				strerror(errno));
		exit(1);
	}
	if (signal(SIGTSTP, nope) == SIG_ERR) {
		fprintf(stderr, "Unable to establish signal handler: %s\n",
				strerror(errno));
		exit(1);
	}
	if (signal(SIGQUIT, quit) == SIG_ERR) {
		fprintf(stderr, "Unable to establish signal handler: %s\n",
				strerror(errno));
		exit(1);
	}
	for ( ; ; ) {
		pause();
	}
}
