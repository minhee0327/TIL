/*
- ���� ����� �ʿ伺
	- ���α׷� ���� ���Ŀ��� ������ ���尡��
	- ������ ���������� ����Ǵ� ���� : SSD 

- ������ ���� �ݱ�
	- ���� ����� ������ FILE������ ������ ������ �����մϴ�.
	- ������ ������ fopen()�Լ� �̿�
	- ������ �������� fclose()�Լ� �̿�
		- FILE *fp;
		- fp = fopen(���� ���, ���ٹ��);
		- fclose(fp);

- ���� ���� �ݱ�
	- ���� �����Լ��� fopen()�Լ����� ���ϰ�ο� ���ٹ���� ������ �� �ִ�.
	- �⺻ ��δ� ���� ���α׷��� ���
	- ���� ���� ���Ǵ� ���� ����� ������ ����.
		- r: ���Ͽ� �����Ͽ� �����͸� ����
		- w: ���Ͽ� �����Ͽ� �����͸� ��� (���� �̹� ������ ���, �����)
		- a: ���Ͽ� �����Ͽ� �����͸� �ڿ������� ���.

- ���� ����� �Լ�
	- �⺻���� ������� ����, printf()�� scanf()�Լ��� ����ߴµ�,
	- ��������¿����� fprintf()�� fscanf()�� �����.
		- fprintf(����������, ����, ����������);
		- fscanf(����������, ����, ����������);

- ���� ����°���
	- ����������� ����, �а�/����, �ݱ� ������ ö���� ������.
	- ������ ������ ���� �����Ͱ� ���Ǹ�, �̴� �������� �Ҵ�
	- ����, ���� ó�� ���Ŀ� ������ �ݾ����� ������, �޸� �����߻������� �� �ݱ�!

- ����1: ������ ���� ���ڿ� ����
	- ���� ���α׷��� ��ο��� Ư���� ������ ������� �����Ͽ� ���ڿ� ����� �� ����.

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	char s[20] = "Hello World";
	FILE* fp;
	fp = fopen("temp.txt", "w");
	fprintf(fp, "%s\n", s);
	fclose(fp);
	return 0;
}

- ����2: �л����� �ý��� �����
	- �л����� �̸���, ���� ���� ����� �ش� ������ ���� ����ϱ�

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	char name[20];
	int score;
} Student;

int main(void) {
	int n, sum = 0;
	FILE* fp;

	fp = fopen("input.txt", "r");
	fscanf(fp, "%d", &n);
	Student* students = (Student*)malloc(sizeof(Student) * n);
	for (int i = 0; i < n; i++) {
		fscanf(fp, "%s %d", &((students + i)->name), &((students + i)->score));
		printf("�̸�: %s, ����: %d\n", (students + i)->name, (students + i)->score);
	}
	system("pause");
	return 0;
}

- ���� ����� ���ϰ� �޸� �Ҵ� �����ϱ�.


*/