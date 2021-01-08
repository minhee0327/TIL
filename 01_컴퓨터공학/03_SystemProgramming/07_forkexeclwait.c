#include <sys/types.h>
#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>

int main()
{
	int pid;
	int child_pid;
	int status;
	int ret;
	pid = fork();

	switch(pid){
		case -1:
			perror("fork is failed\n");
			break;
		case 0:
			execl("/bin/ls", "ls","-al",NULL);
			perror("execl is failed\n");
			break;
		default:
			child_pid= wait(&status);
			printf("Parent PID(%d), Child PID(%d) \n",getpid(), child_pid);
			ret = WIFEXITED(status);
			if(ret !=0){
				printf("Child process is normally teminated\n");
			}else{
				printf("Child process is abnormally terminated\n");
			}
			exit(0);
	}
}
