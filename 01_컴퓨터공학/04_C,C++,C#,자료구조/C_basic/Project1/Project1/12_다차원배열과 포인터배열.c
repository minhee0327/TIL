/*
- ������ �迭�� ������ �迭

- 2���� �迭�� �ʱ�ȭ
	- ������
		- �ڷ��� �迭�̸�[��][��] = {{��1, ��2, ��3,...},{��1, ��2, ��3,...} ,...}

---
- 2�� for���� ����� 2���� �迭

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
- 3���� �迭
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
- ������ �迭�� ���� �м�
	- �迭�� �����Ϳ� ������ ������� ����
	- �迭�� �̸��� �迭�� ������ ù��° �ּҰ� �ȴ�.
	- ������ �������� �����ʹ� �����̰�, �迭�� �̸��� ����̴�.

#include <stdio.h>

int main(void) {
	int a = 10;
	int b[10];
	b = &a; //error: �迭�� ����ϱ�, ����Ұ�.

	system("pause");
	return 0;
}


---
- �����͸� �迭ó�� ����� ���� �ְ�, �����ʹ� �����̹Ƿ�, ���� ����
- �迭�� �̸���, �迭�� ù��° ������ �ּ�
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
- �����ʹ� ������ ���� �ڷ����� ũ�⸸ŭ �̵�
- ����, ����(int)�� �����ʹ� 4byte�� �̵�

#include <stdio.h>

int main(void) {
	int a[5] = { 1,2,3,4,5 };
	int i;

	for (i = 0; i < 5; i++) {
		printf("��������:%d / �ּҰ�: %d\n", *(a + i), a+i);
	}

	system("pause");
	return 0;
}


---
q1: 
- ũ�Ⱑ 10�� double�� �迭�� �������� ��, �迭�� �����ּҰ� X��� �մϴ�.
- �̶� �迭�� ������ ������ �ּҴ� ���ϱ��? 

#include <stdio.h>

int main(void) {
	double d [10];

	printf("X�ּ�: %d / ���������� �ּ�: %d\n", d, d+ 9);

	system("pause");
	return 0;
}
a1:
- double ���� 8byte�̰�, 9ĭ �����������ϱ�, X+ 72��ŭ ����� ����� ���´�.



---
q2: �Ʒ� ���α׷� ���?
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