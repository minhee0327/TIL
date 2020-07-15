#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#define MSGSIZE 255

char* msg = "Hello Child Process!";
int main(){
	char buf[255];
	int fd[2], pid, nbytes;
	//pipe(fd)로 pipe 생성, 0보다 작을 경우 비정상종료
	if(pipe(fd)<0) exit(1);
	
	//fork()로 부모, 자식 프로세스나뉨
	pid = fork();
	//pid값이 0이 아니면, 부모프로세스
	if (pid>0){
		printf("parent PID:%d, child PID: %d\n", getpid(), pid);
		//fd[1] 에 write
		write(fd[1], msg, MSGSIZE);
		exit(0);
	}
	else{
		printf("child PID: %d\n", getpid());
		//fd[0]으로 읽음
		nbytes = read(fd[0], buf, MSGSIZE);
		printf("%d %s\n", nbytes, buf);
		exit(0);
	}
	return 0;
}
