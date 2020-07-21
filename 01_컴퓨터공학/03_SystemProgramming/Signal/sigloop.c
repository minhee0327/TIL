#include <signal.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

static void signal_handler (int signo){
	printf("Catch SIGINT!, but no stop\n");
}

int main(void){
	if (signal(SIGINT, signal_handler) == SIG_ERR){
		printf("Can't catch SIGINT!\n");
		exit(1);
	}
	for (;;)
		pause();
	return 0;
}
