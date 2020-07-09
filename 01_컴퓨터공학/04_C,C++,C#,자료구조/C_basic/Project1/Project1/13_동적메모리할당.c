/*
- 동적 메모리 할당의 원리 학습
- 동적 메모리 할당을 통해 프로그램 실행 도중에 메모리 할당 될 수 있도록 함.

- C언어에서 배열의 경우 사전에 적절한 크기만큼 할당.
- 그렇지 않고, 
- 우리가 원하는 만큼만 메모리 할당해서 사용하려한다면, 동적 메모리 할당 사용한다.
- 동적이라는 말 == 프로그램 실행 도중에 (유사한 의미)

- malloc()함수를 이용해 원하는 만큼의 메모리 공간을 확인할 수 있음.
- malloc()함수는 메모리 할당에 성공을 하면 주소반환을 하고, 아니면 NULL을 반환함.
- <stdlib.h> 라이브러리에 정의되어 있음.

- malloc(할당할 바이트 크기)

- 동적 메모리 할당을 수행할 때마다, 할당되는 포인터의 주소는 변칙적.
- 컴퓨터에 남아있는 공간을 변칙적으로 할당해줌.
- 따라서 아래 예제에서 print되는 두 값이 서로 다른 주소값을 출력하게 된다.

#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int* a = malloc(sizeof(int)); //sizeof(int)== 4
	printf("%d\n", a);
	a = malloc(sizeof(int));
	printf("%d\n", a);
	system("pause");
	return 0;
}


- 전통적인 C언어에서는 스택에 선언된 변수는 따로 메모리 해제 해주지 않아도 된다.
- 반면, 동적으로 할당된 변수는 반드시 free()함수로 메모리를 해제해 주어야한다.
- 메모리 해제를 하지 않으면, 메모리 내의 프로세스 무게가 더해져, 언젠가는 오류를 발생시키기 때문.
- 메모리 누수(Memory Leak)방지 중요!합니다!!!


- 할당한 메모리를 해제한 뒤에 다시 할당해서 사용하는 예제(아래)
- 이경우 동일한 메모리 주소를 할당 받을 확률이 높음.(해제후 바로 할당하니까)
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int* a = malloc(sizeof(int));
	printf("%d\n", a);
	free(a);
	a = malloc(sizeof(int));
	printf("%d\n", a);
	free(a);
	system("pause");
	return 0;
}


- 동적으로 문자열 처리하기
	- 일괄적인 범위의 메모리를 모두 특정한 값으로 설정하기 위해서는 memset)을 사용한다.
	- memset(포인터, 값, 크기);
	- 한 바이트씩 값을 저장하므로, 문자열 배열의 처리방식과 흡사.
	- 따라서, memset()함수는 <string.h>라이브러리에 선언되어있음.

#include <stdio.h>
#include <string.h>

int main(void) {
	char* a = malloc(100);
	memset(a, 'A', 100);
	for (int i = 0; i < 100; i++) {
		printf("%c ", a[i]);
	}

	system("pause");
	return 0;
}


#include <stdio.h>
#include <stdlib.h>


int main(void) {
	//**p: 2중포인터, 2차원배열
	//sizeof(int*) *3 : 3개의 행
	//(int**) : malloc 함수로 선언한 동적할당 변수를 좌항의 자료형과 동일하게, 형변환을함.
	int** p = (int**)malloc(sizeof(int*) * 3);
	//각 행에 3개의 열을 할당
	for (int i = 0; i < 3; i++) {
		*(p + i) = (int*)malloc(sizeof(int*) * 3);
	}
	//행렬값을 저장
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			*(*(p + i) + j) = i * 3 + j;
		}
	}
	// 출력
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			printf("%d ", *(*(p + i) + j));
		}
		printf("\n");
	}


	system("pause");
	return 0;
}


*/