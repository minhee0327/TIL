/*
- ���ڿ� ����
	- ���ڵ��� �迭
	- ��ǻ�� �޸� ������ �������� null��(����X, \0) ���� 
	- null�� ��������: ���ڿ��� ���� �˷��ִ� ����
	- printf()�Լ��� ���������� null�� ���������� ����ϴ� ����.

- ���ڿ��� ������
	- ���ڿ� ���·� �����͸� ����ϸ�, �����Ϳ� Ư���� ���ڿ��� �ּҸ� �ְ� �ȴ�.
	- ���ڿ��� �б� �������� �޸� ������ ���� ��, �� ��ġ�� ó����.
	- �̷��� ���ڿ��� ���ڿ� ���ͷ� �̶�� �Ѵ�. �����Ϸ��� �˾Ƽ� �޸� �ּ� ����.

#include <stdio.h>

int main(void) {
	char* a = "Hello World";
	printf("%s\n", a);
	system("pause");
	return 0;
}

- �����ͷ� ���ڿ��� �����ߴ� �ϴ���, ���� �迭ó�� ��밡��.

#include <stdio.h>

int main(void) {
	char* a = "Hello World";
	printf("%c\n", a[1]);
	printf("%c\n", a[2]);
	printf("%c\n", a[6]);
	system("pause");
	return 0;
}

- ���ڿ� ����� �Լ�
	- ���ڿ� ����� ����
	- scanf(): ������ ������������ �Է¹���
	- gets() : ������� �����Ͽ� �� �� �Է¹��� (���Ȼ� ����ؼ� gets_s()�� �� �� ������)
	- gets_s(���ڿ�, ũ��): ������ ũ�⸦ ö���� ��Ű�� �Լ�. 
	- sizeof(): C���� �迭�� ũ�� �˷��ִ� �⺻ �����Լ�

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	char a[100];
	gets(a);

	printf("%s\n", a);
	system("pause");
	return 0;
}

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	char a[100];
	gets_s(a, sizeof(a));

	printf("%s\n", a);
	system("pause");
	return 0;
}


- ���ڿ� ó���� ���� �پ��� �Լ�
	- <string.h> ���̺귯���� ���ԵǾ� ����.
	- strlen(): ���ڿ����� ��ȯ
	- strcmp(str1, str2): str1�� str2���� ���������� �տ� ������ -1, �ڿ������� 1 ��ȯ
	- strcpy(): ���ڿ�����
	- strcat(): ���ڿ�1�� ���ڿ�2�� ����
	- strstr(): ���ڿ�1�� ���ڿ�2�� ��� ���ԵǾ��ִ��� ��ȯ.


#include <stdio.h>

int main(void) {
	char a[20] = "MinHee Kang";
	char b[20] = "JongHuyn Lee";
	char c[20] = "Change name";
	char d[30] = "My name is.."; //����Ǿ����� ���ڿ��� ũ��� ���� �� �˳���
	char e[20] = "name";

	printf("���ڿ��� ����: %d\n", strlen(a)); 

	printf("�� ������ ������ ��: %d\n", strcmp(a, b)); // 1: a �� ���������� b���� �ڿ�����

	strcpy(c, a); //a���� c�� ����
	printf("���ڿ� copy a to c: %s\n", c); 

	strcat(d, a); //d�� a ����
	printf("���ڿ� �����ϱ�: %s\n", d);

	// �� ���ڿ�����, ª�� ���ڿ��� ã�Ƽ� ��ġ�� ��ȯ��.
	// �ܼ� ����ϰ� �Ǹ�, ã�� ���� ���ڿ� ��� ��ȯ��.
	printf("strstr() ���: %s\n", strstr(d, e));

	system("pause");
	return 0;
}
*/
