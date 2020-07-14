#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/wait.h>
#include <sys/types.h>
#define MAXLINE 64

int main(int argc, char **argv){
	char buf[MAXLINE];
	int proc_status;
	pid_t pid;
	printf("MinShell ver 1.0\n");
	while (1){
		memset(buf, 0X00, MAXLINE);
		fgets(buf, MAXLINE-1, stdin);
		//char *fgets(char *string, int n, FILE*stream)
		if (strncmp(buf, "exit\n",5)==0){
			break;
		}
		buf[strlen(buf)-1] = 0X00;
		
		pid=fork();
		if(pid==0){
			if (execl(buf, buf, NULL)== -1){
				printf("command execution is failed \n");
				exit(0);
			}
		}
		if (pid>0){
			wait(NULL);
		}
	}
	return 0;
}
