#include <stdio.h>

int main(){
	int A[5] = {1,2,3,4,5};
	int b = 12;

	A[4] = b + A[0];
	printf("%d\n",A[4]);

	return 0;
}