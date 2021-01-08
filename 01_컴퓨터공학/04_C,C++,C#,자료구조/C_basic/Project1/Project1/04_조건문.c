/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	printf("손님이 몇명 왔나요?");

	int a;
	scanf("%d", &a);

	if (a == 1 || a == 2) {
		printf("2인석으로 안내합니다\n");
	}
	else if (a==3 || a==4) {
		printf("4인석으로 안내합니다\n");
	}
	else {
		printf("단체석으로 안내합니다\n");
	}


	system("pause");
	return 0;
}
*/

/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//switch case 예제

int main(void) {
	printf("학점을 입력하세요.");

	char a;
	scanf("%c", &a);

	switch (a) {
	case 'A':
		printf("A 학점입니다. \n");
		break;
	case 'B':
		printf("B 학점입니다. \n");
		break;
	case 'C':
		printf("B 학점입니다. \n");
		break;
	default:
		printf("학점을 바르게 입력하세요 \n");
	}
	system("pause");
	return 0;
}
*/

/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// switch case 대표 예제

int main(void) {
	printf("월을 입력하세요...");

	int a;
	scanf("%d", &a);

	switch (a)
	{
	case 1: case 2: case 3:
		printf("봄\n");
		break;
	case 4: case 5: case 6:
		printf("여름\n");
		break;
	case 7: case 8: case 9:
		printf("가을\n");
		break;
	case 10: case 11: case 12:
		printf("겨울 \n");
		break;
	default:
		break;
	}

	system("pause");
	return 0;
}
*/