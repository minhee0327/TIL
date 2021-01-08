/*
- ����ü
	- �������� ������ ���� �ϳ��� ��ü�� ǥ���ϰ��� �Ҷ� ����ü�� ����� �� ����
	- �л�, ��ǥ, ����, ĳ���� �� �پ��� ��ü�� ��� ���α׷��� �� �̿��� ǥ���� �� ����.

- ���� �� ����
	struct ����ü��{
	�ڷ���1 ������1;
	�ڷ���2 ������2;
	}

- ��: �Ѹ��� �л��� ���� ������ ��� �ִ� ����ü (Student)
struct Student
{
	char studentId[10];
	char name[10];
	int grade;
	char major[100];
};

- ����ü�� ���� ����� ����
	- �⺻������ ����ü�� ������ ������ ������ '.'�� ���.
	struct Student s; // ����ü ���� ����
	strcpy(s.studentId, "201012223");
	strcpy(s.name, "minhee kang");
	s.grade = 4;
	strcpy(s.major, "�������");

- ����غ���
#include <stdio.h>

struct Student
{
	char studentId[10];
	char name[10];
	int grade;
	char major[100];
};

int main(void) {
	// ����ü ���� ����
	struct Student s;
	strcpy(s.studentId, "201012223");
	strcpy(s.name, "minhee kang");
	s.grade = 4;
	strcpy(s.major, "�������");

	//����ü ���� ���
	printf("�й�: %s\n", s.studentId);
	printf("�̸�: %s\n", s.name);
	printf("����: %d\n", s.grade);
	printf("�а�: %s\n", s.major);

	system("pause");
	return 0;
}




--
- ����ü ���ǿ� ����
	- �ϳ��� ����ü ������ ����ϴ� ��� ���ǿ� ���ÿ� ������ �Ҽ��� �ִ�.
	- �� ���, ������ ���������� ���ȴ�.

#include <stdio.h>

struct Student
{
	char studentId[10];
	char name[10];
	int grade;
	char major[100];
} s ;

int main(void) {
	// ����ü ���� ����
	strcpy(s.studentId, "201012223");
	strcpy(s.name, "minhee kang");
	s.grade = 4;
	strcpy(s.major, "�������");

	//����ü ���� ���
	printf("�й�: %s\n", s.studentId);
	printf("�̸�: %s\n", s.name);
	printf("����: %d\n", s.grade);
	printf("�а�: %s\n", s.major);

	system("pause");
	return 0;
}



---  
- ����ü�� �ʱ�ȭ
	- ����ü�� ������ �ѹ��� �ʱ�ȭ �ϱ� ���ؼ��� �߰�ȣ�� ���ʴ�� ������ ���� �ִ´�.

#include <stdio.h>

struct Student
{
	char studentId[10];
	char name[10];
	int grade;
	char major[100];
} ;

int main(void) {
	// ����ü ���� ����
	struct Student s = {"201012223","minheeKang",4, "��ǰ�������"};

	//����ü ���� ���
	printf("�й�: %s\n", s.studentId);
	printf("�̸�: %s\n", s.name);
	printf("����: %d\n", s.grade);
	printf("�а�: %s\n", s.major);

	system("pause");
	return 0;
}

- �� ª�� ����ü �����ϱ�
	- typedef Ű���带 �̿��Ͽ� ������ �ڷ����� ����� �����Ƿ�, ������ �� ª����.
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


- �͸���ü
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


---
- ����ü�� ������ ������ ���Ǵ� ���, ���� ������ ������ �� ȭ��ǥ(->)�� ���.
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
	Student* s = malloc(sizeof(Student));

	strcpy(s->studentId, "201012223");
	strcpy(s->name, "minheeKang");
	s->grade= 4;
	strcpy(s->major, "��ǰ�������");

	//����ü ���� ���
	printf("�й�: %s\n", s->studentId);
	printf("�̸�: %s\n", s->name);
	printf("����: %d\n", s->grade);
	printf("�а�: %s\n", s->major);

	system("pause");
	return 0;
}
*/