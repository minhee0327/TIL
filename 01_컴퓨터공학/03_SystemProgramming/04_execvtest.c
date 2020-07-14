#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(){
	//일부러 error 발생(PATH설정 X)
	char *envp[] = {"USER=ubuntu",NULL};
	char *arg[] = {"ls","-al",NULL};

	printf("excute ls \n");
	execve("ls", arg, envp);
	perror("execve is failed \n");
	exit(1);

}
