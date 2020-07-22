#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

pthread_mutex_t mutex_lock = PTHREAD_MUTEX_INITIALIZER;
int g_count = 0;

void *t_function(void *data){
	char* thread_name = (char*)data;
	pthread_mutex_lock(&mutex_lock);
	printf("%s start \n", thread_name);
	for(int i =0; i<10000000;i++){
		g_count++;
	}
	printf("%s, g_count = %d\n", thread_name, g_count);
	pthread_mutex_unlock(&mutex_lock);
}
int main(){
	pthread_t p_thread1, p_thread2;
	int status;
	pthread_create(&p_thread1, NULL, t_function , (void*)"Thread1");
	pthread_create(&p_thread2, NULL, t_function, (void *)"Thread2");
	pthread_join(p_thread1, (void*) &status);
	pthread_join(p_thread2, (void*) &status);
}
