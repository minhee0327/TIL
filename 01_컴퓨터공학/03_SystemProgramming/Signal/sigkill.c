#include <sys/types.h>
#include <signal.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv){
	int pid, result;
	int sig_num;

	if(argc != 3){
		printf("Usage %s [pid] [signum] \n", argv[0]);
		exit(1);
	}

	pid = atoi(argv[1]);
	sig_num = atoi(argv[2]);
	result = kill(pid, sig_num);

	if(result <0){
		perror("To send Signal is failed\n");
		exit(1);
	}
	return 0;

}
