/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//1~100까지 출력하기
int main(void) {
	int i;
	for (i = 1; i <= 100; i++)
	{
		printf("%d\n", i);
	}
	system("pause");
	return 0;
}
*/

/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//1~n까지의 합 구하기
int main(void) {
	int n, sum = 0;

	printf("n을 입력하세요..\n");
	scanf("%d", &n);
	for (int i = 1; i<= n;  i++)
	{
		sum += i;
	}
	printf("%d", sum);

	system("pause");
	return 0;
}
*/

/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// a 갯수만큼, c(문자) 출력하기
int main(void) {
	int a;
	char c;

	scanf("%d %c", &a, &c);
	while (a--) {
		printf("%c ", c);
	}
	system("pause");
	return 0;
}

*/


/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//구구단 중 특정 단 출력
int main(void) {
	int n;

	printf("몇 단이 궁금하신가요?\n");
	scanf("%d", &n);
	int i = 1;

	while (i<=9){
		printf("%d * %d = %d\n", n, i, n * i);
		i++;
	}

	system("pause");
	return 0;
}
*/


/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int i = 1;

	while (i<=9){
		int j = 1;
		while (j <= 9) {
			printf("%d * %d = %d\n", i, j, i * j);
			j++;
		}
		printf("----------\n");
		i++;
	}

	system("pause");
	return 0;
}
*/

/*
- 반복문
	- for문 과 while 문은 서로 치환이 가능하다.
	- (내부적으로 어셈블리 단에서는 같게 동작하기 때문)
	- 무한루프를 항상 조심하고
	- 이중반복문은 행렬, 그래프 연산에서 많이 활용됨
	- 단, 중첩(이중)반복문을 사용할 때, 성능에 대해서 잘 고려하여 구현할 것.
*/