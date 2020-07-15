#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/msg.h>

typedef struct msgbuf{
	long type;
	char text[50];
}MsgBuf;

int main(void){
	int msgid, len;
	MsgBuf msg;

	key_t key = 1234;

	msgid = msgget(key, IPC_CREAT|0644);
	if(msgid == -1){
		perror("msgget");
		exit(1);
	}
	msg.type = 1;
	strcpy(msg.text, "Hello Message Queue\n");
	if (msgsnd(msgid, (void *)&msg, 50, IPC_NOWAIT) == -1){
		perror("msgsnd");
		exit(1);
	}

	len = msgrcv(msgid, &msg, 50, 0, 0);
	printf("Received Message is '%s' [%d]\n", msg.text,len);
	//msg controll
	//해방 메세지 큐를 삭제.
	msgctl(msgid, IPC_RMID, 0);
	
	return 0;
}


