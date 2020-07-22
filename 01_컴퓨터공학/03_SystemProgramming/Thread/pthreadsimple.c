#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *thread_function (void *ptr){
	char *msg;
	msg = (char*) ptr;
	printf("%s \n", msg);
	pthread_exit((void*)100);
}

int main(){
	pthread_t thread1, thread2;
	const char *msg1 = "Thread1";
	const char *msg2 = "Thread2";
	int ret, status;

	ret = pthread_create(&thread1, NULL, thread_function, (void*)msg1);
	printf("%d \n", ret);

	if(ret == 0){
		printf("pthread_create returns %d\n", ret);
	}else{
		printf("pthread_create returns error: %d\n", ret);
		exit(1);
	}
	ret = pthread_create(&thread2, NULL, thread_function ,(void*) msg2);
	if (ret ==0){
		printf("pthread_create returns %d\n", ret);
	}else{
		printf("pthread_create returns error: %d\n",ret);
		exit(1);
	}
	pthread_join(thread1, (void**) &status);
	printf("thread1 returns : %d\n", status);
	pthread_join(thread2, (void**) &status);
	printf("thread2 returns : %d\n", status);
	return 0;

}
