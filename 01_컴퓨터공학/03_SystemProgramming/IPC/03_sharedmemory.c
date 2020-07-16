#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int main(){
	int shmid, pid;
	char *shmaddr_parent, *shmaddr_child;
	shmid = shmget((key_t)1234,10, IPC_CREAT|0644);

	if (shmid ==-1){
		perror("shmget error\n");
		exit(1);
	}
	pid = fork();
	//부모 process
	if(pid>0){
		//child process 종료까지 wait
		wait(0);
		shmaddr_parent = (char*) shmat(shmid, (char*)NULL, 0);
		printf("%s\n", shmaddr_parent);
		shmdt((char*)shmaddr_parent);
	}
	else{
		shmaddr_child = (char*) shmat(shmid, (char*)NULL, 0);
		strcpy((char*) shmaddr_child, "Hello Parent!");
		shmdt((char*) shmaddr_child);
		exit(0);
	}
	shmctl(shmid, IPC_RMID, (struct shmid_ds *)NULL);
	return 0;
}
