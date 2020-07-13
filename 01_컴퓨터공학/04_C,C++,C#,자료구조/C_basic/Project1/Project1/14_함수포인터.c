/*
- C������ �Լ��� �̸��� �̿��� Ư���� �Լ��� ȣ��
- �Լ� �̸��� �޸� �ּ� ��ȯ

#include <stdio.h>

void function() {
	printf("It's my Fucntion");
}
int main(void) {
	printf("%d\n", function);

	system("pause");
	return 0;
}

---
- �Լ�������
	- �Լ� �����ʹ� Ư���� �Լ��� ��ȯ�ڷ����� �����ϴ� ������� ������ �� ����.
	- �Լ� �����͸� �̿��ϸ� ���°� ���� ���� �ٸ� ����� �Լ��� ���������� ����� �� ����.
	- ��ȯ�ڷ��� (*�Լ���)(�Ű�����) = �Լ���;
	- ��ȯ�ڷ��� (*�̸�)(�Ű�����) = �Լ���;
	
- �Ű����� �� ��ȯ�ڷ����� ���� �Լ� ������
#include <stdio.h>

void myfunction() {
	printf("It's my Fucntion\n");
}
void yourfunction() {
	printf("It's your Fucntion\n");
}


int main(void) {
	void (*fp)() = myfunction;
	fp();
	fp = yourfunction;
	fp();

	system("pause");
	return 0;
}


---
- �Ű������� ��ȯ �ڷ����� �ִ� �Լ�������
#include <stdio.h>

int add(int a, int b) {
	return a + b;
}
int sub(int a, int b) {
	return a - b;
}

int main(void) {
	int (*fp)(int, int) = add;
	printf("%d\n", fp(10, 3));
	fp = sub;
	printf("%d\n", fp(10, 3));

	system("pause");
	return 0;
}


---
- �Լ������� ��ȯ�Ͽ� ����ϱ�.

#include <stdio.h>

int add(int a, int b) {
	return a + b;
}
int (*process(char* a))(int , int ) {
	printf("%s\n", a);
	return add;
}

int main(void) {
	printf("%d\n", process("10�� 20�� ���غ��ڽ��ϴ�.")(10, 20));
	system("pause");
	return 0;
}



---
- typedef ����Ͽ� �� ª�� ���� ����
#include <stdio.h>

typedef struct Student
{
	char studentId[10];
	char name[10];
	int grade;
	char major[100];
} Student;

int main(void) {
	// ����ü ���� ����
	Student s = {"201012223","minheeKang",4, "��ǰ�������"};

	//����ü ���� ���
	printf("�й�: %s\n", s.studentId);
	printf("�̸�: %s\n", s.name);
	printf("����: %d\n", s.grade);
	printf("�а�: %s\n", s.major);

	system("pause");
	return 0;
}


---
- Ȥ�� �͸� ����ü ���� 

#include <stdio.h>

typedef struct
{
	char studentId[10];
	char name[10];
	int grade;
	char major[100];
} Student;

int main(void) {
	// ����ü ���� ����
	Student s = {"201012223","minheeKang",4, "��ǰ�������"};

	//����ü ���� ���
	printf("�й�: %s\n", s.studentId);
	printf("�̸�: %s\n", s.name);
	printf("����: %d\n", s.grade);
	printf("�а�: %s\n", s.major);

	system("pause");
	return 0;
}

*/