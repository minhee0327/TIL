/*
#include <stdio.h>

int main(void) {
	int a[10] = { 6,5,4,3,9,8,0,1,2,7 };
	int i;
	for (i = 0; i < 10;i++) {
		printf("%d ", a[i]);
	}
	system("pause");
	return 0;
}
*/

/*
#include <stdio.h>
#include <limits.h>

//�迭 �߿� �ִ밪 ã��
int main(void) {
	int a[10] = { 6,5,4,3,9,8,0,1,2,7 };
	int i, maxValue=INT_MIN;
	for (i = 0; i < 10;i++) {
		if (maxValue < a[i]) {
			maxValue = a[i];
		}
	}
	printf("%d\n", maxValue);
	system("pause");
	return 0;
}
*/

/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//���ڿ��� �迭
int main(void) {
	char a[20];
	scanf("%s", &a);
	printf("%s\n", a);
	system("pause");
	return 0;
}
*/

/*
#include <stdio.h>

//���ڿ��� �迭: Ư�� �ε��� ����
int main(void) {
	char a[20]= "Hello World";
	a[5] = ',';
	printf("%s\n", a);
	system("pause");
	return 0;
}
*/

/*
#include <stdio.h>

//���ڿ��� �迭: ���ڿ��� ���Ե� 'l'���� ����ϱ�
int main(void) {
	char a[]= "Hello World";
	int count = 0;
	for (int i = 0; i <  10; i++) {
		if (a[i] == 'l') {
			count++;
		}
	}
	printf("%d\n", count);
	system("pause");
	return 0;
}
*/