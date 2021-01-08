#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

void *thread_function (void *ptr){
	char *msg;
	msg = (char*) ptr;
	printf("%s start \n", msg);
	sleep(5); 
	printf("%s end \n", msg);
	return 0;
}

int main(){
	pthread_t thread1, thread2;
	const char *msg1 = "Thread1";
	const char *msg2 = "Thread2";
	int ret, status;

	ret = pthread_create(&thread1, NULL, thread_function, (void*)msg1);

	if(ret < 0){
		printf("thread create error");
	
	}
	pthread_detach(thread1);
	
	ret = pthread_create(&thread2, NULL, thread_function, (void*)msg2);
	if (ret<0){
		printf("thread create error");
	}
	pthread_join(thread2,(void**) &status);
	printf("thread2 returns : %d\n",status);
	sleep(10);
	
	return 0;

}
