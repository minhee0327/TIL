/*
- 다차원 배열과 포인터 배열

- 2차원 배열의 초기화
	- 선언방법
		- 자료형 배열이름[행][열] = {{값1, 값2, 값3,...},{값1, 값2, 값3,...} ,...}

---
- 2중 for문과 사용한 2차원 배열

#include <stdio.h>

int main(void) {
	int a[3][3] = { {1,2,3},{4,5,6},{7,8,9} };
	int i, j;

	for (i = 0; i < 3; i++) {
		for (j = 0; j < 3; j++) {
			printf("%d ", a[i][j]);
		}
		printf("\n");
	}
	system("pause");
	return 0;
}


---
- 3차원 배열
#include <stdio.h>

int main(void) {
	int a[2][3][3] = { {{1,2,3},{4,5,6},{7,8,9}},{{1,2,3},{4,5,6},{7,8,9} }};
	int i, j,k;

	for (i = 0; i < 2; i++) {
		for (j = 0; j < 3; j++) {
			for (k = 0; k < 3;k++) {
			printf("%d ", a[i][j][k]);
			}
			printf("\n");
		}
		printf("\n");
	}
	system("pause");
	return 0;
}

---
- 포인터 배열의 구조 분석
	- 배열은 포인터와 동일한 방식으로 동작
	- 배열의 이름은 배열의 원소의 첫번째 주소가 된다.
	- 유일한 차이점은 포인터는 변수이고, 배열의 이름은 상수이다.

#include <stdio.h>

int main(void) {
	int a = 10;
	int b[10];
	b = &a; //error: 배열은 상수니까, 변경불가.

	system("pause");
	return 0;
}


---
- 포인터를 배열처럼 사용할 수도 있고, 포인터는 변수이므로, 변경 가능
- 배열의 이름은, 배열의 첫번째 원소의 주소
#include <stdio.h>

int main(void) {
	int a[5] = { 1,2,3,4,5 };
	int *b = &a;
	int *b = &a[0];

	printf("%d\n", b[2]);

	system("pause");
	return 0;
}


---
- 포인터는 연산을 통해 자료형의 크기만큼 이동
- 따라서, 정수(int)형 포인터는 4byte씩 이동

#include <stdio.h>

int main(void) {
	int a[5] = { 1,2,3,4,5 };
	int i;

	for (i = 0; i < 5; i++) {
		printf("간접참조:%d / 주소값: %d\n", *(a + i), a+i);
	}

	system("pause");
	return 0;
}


---
q1: 
- 크기가 10인 double형 배열을 선언했을 때, 배열의 시작주소가 X라고 합니다.
- 이때 배열의 마지막 원소의 주소는 몇일까요? 

#include <stdio.h>

int main(void) {
	double d [10];

	printf("X주소: %d / 마지막원소 주소: %d\n", d, d+ 9);

	system("pause");
	return 0;
}
a1:
- double 형은 8byte이고, 9칸 떨어져있으니까, X+ 72만큼 연산된 결과가 나온다.



---
q2: 아래 프로그램 결과?
#include <stdio.h>

int main(void) {
	int a[5] = { 1,2,3,4,5 };
	int* b = a;

	printf("%d\n", *(b++));
	printf("%d\n", *(++b));
	printf("%d\n", *(b+2));
	system("pause");
	return 0;
}


#include <stdio.h>

int main(void) {
	int a[2][5] = {{ 1,2,3,4,5 }, { 6,7,8,9,10 }};

	int (*p)[5] = a[1];

	int i;
	for (i = 0; i < 5;i++) {
		printf("%d ", p[0][i]);
	}

	system("pause");
	return 0;
}

//6 7  8 9 10

*/