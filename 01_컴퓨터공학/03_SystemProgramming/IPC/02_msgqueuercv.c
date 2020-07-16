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

	if((msgid = msgget(key, IPC_CREAT|0644)) < 0 ){
		perror("msgget");
		exit(1);
	}
	
	len = msgrcv(msgid, &msg, 50, 0,0);
	printf("Received Message is [%d] %s\n", len , msg.text);
	return 0;
}


