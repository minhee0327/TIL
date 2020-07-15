#include <sys/resource.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(){
	int which = PRIO_PROCESS;
	id_t pid;
	int ret;

	pid = getpid();
	ret = getpriority(which, 0);
	printf("PID=%d, PRIORITY=%d\n", pid, ret);
	
	ret = nice(10);
	ret = getpriority(which, 0);
	printf("PID=%d, PRIORITY=%d\n", pid, ret);

	ret = setpriority(which, 0, 5);
	ret = getpriority(which, 0);
	//우선순위를 높이는 작업은 root가 소유한 프로세스만 가능
	//따라서 아래 결과는 5로 update되지 않음(ubuntu계정에서)
	//root 계정에서 확인해보니 5로 잘 업뎃 되었음.
	printf("PID=%d, PRIORITY=%d\n", pid, ret);

	return 0;

}

