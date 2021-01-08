/*
- 구조체
	- 여러개의 변수를 묶어 하나의 객체를 표현하고자 할때 구조체를 사용할 수 있음
	- 학생, 좌표, 동물, 캐릭터 등 다양한 객체를 모두 프로그래밍 언어를 이용해 표현할 수 있음.

- 정의 및 선언
	struct 구조체명{
	자료형1 변수명1;
	자료형2 변수명2;
	}

- 예: 한명의 학생에 대한 정보를 담고 있는 구조체 (Student)
struct Student
{
	char studentId[10];
	char name[10];
	int grade;
	char major[100];
};

- 구조체의 변수 선언과 접근
	- 기본적으로 구조체의 변수에 접근할 때에는 '.'을 사용.
	struct Student s; // 구조체 변수 선언
	strcpy(s.studentId, "201012223");
	strcpy(s.name, "minhee kang");
	s.grade = 4;
	strcpy(s.major, "생명공학");

- 출력해보기
#include <stdio.h>

struct Student
{
	char studentId[10];
	char name[10];
	int grade;
	char major[100];
};

int main(void) {
	// 구조체 변수 선언
	struct Student s;
	strcpy(s.studentId, "201012223");
	strcpy(s.name, "minhee kang");
	s.grade = 4;
	strcpy(s.major, "생명공학");

	//구조체 내용 출력
	printf("학번: %s\n", s.studentId);
	printf("이름: %s\n", s.name);
	printf("학점: %d\n", s.grade);
	printf("학과: %s\n", s.major);

	system("pause");
	return 0;
}




--
- 구조체 정의와 선언
	- 하나의 구조체 변수만 사용하는 경우 정의와 동시에 선언을 할수도 있다.
	- 이 경우, 변수는 전역변수로 사용된다.

#include <stdio.h>

struct Student
{
	char studentId[10];
	char name[10];
	int grade;
	char major[100];
} s ;

int main(void) {
	// 구조체 변수 선언
	strcpy(s.studentId, "201012223");
	strcpy(s.name, "minhee kang");
	s.grade = 4;
	strcpy(s.major, "생명공학");

	//구조체 내용 출력
	printf("학번: %s\n", s.studentId);
	printf("이름: %s\n", s.name);
	printf("학점: %d\n", s.grade);
	printf("학과: %s\n", s.major);

	system("pause");
	return 0;
}



---  
- 구조체의 초기화
	- 구조체의 변수를 한번에 초기화 하기 위해서는 중괄호에 차례대로 변수의 값을 넣는다.

#include <stdio.h>

struct Student
{
	char studentId[10];
	char name[10];
	int grade;
	char major[100];
} ;

int main(void) {
	// 구조체 변수 선언
	struct Student s = {"201012223","minheeKang",4, "식품생명공학"};

	//구조체 내용 출력
	printf("학번: %s\n", s.studentId);
	printf("이름: %s\n", s.name);
	printf("학점: %d\n", s.grade);
	printf("학과: %s\n", s.major);

	system("pause");
	return 0;
}

- 더 짧게 구조체 정의하기
	- typedef 키워드를 이용하여 임의의 자료형을 만들수 있으므로, 선언이 더 짧아짐.
	#include <stdio.h>

typedef struct Student
{
	char studentId[10];
	char name[10];
	int grade;
	char major[100];
} Student;

int main(void) {
	// 구조체 변수 선언
	Student s = {"201012223","minheeKang",4, "식품생명공학"};

	//구조체 내용 출력
	printf("학번: %s\n", s.studentId);
	printf("이름: %s\n", s.name);
	printf("학점: %d\n", s.grade);
	printf("학과: %s\n", s.major);

	system("pause");
	return 0;
}


- 익명구조체
#include <stdio.h>

typedef struct
{
	char studentId[10];
	char name[10];
	int grade;
	char major[100];
} Student;

int main(void) {
	// 구조체 변수 선언
	Student s = {"201012223","minheeKang",4, "식품생명공학"};

	//구조체 내용 출력
	printf("학번: %s\n", s.studentId);
	printf("이름: %s\n", s.name);
	printf("학점: %d\n", s.grade);
	printf("학과: %s\n", s.major);

	system("pause");
	return 0;
}


---
- 구조체가 포인터 변수로 사용되는 경우, 내부 변수에 접근할 때 화살표(->)를 사용.
#include <stdio.h>

typedef struct Student
{
	char studentId[10];
	char name[10];
	int grade;
	char major[100];
} Student;

int main(void) {
	// 구조체 변수 선언
	Student* s = malloc(sizeof(Student));

	strcpy(s->studentId, "201012223");
	strcpy(s->name, "minheeKang");
	s->grade= 4;
	strcpy(s->major, "식품생명공학");

	//구조체 내용 출력
	printf("학번: %s\n", s->studentId);
	printf("이름: %s\n", s->name);
	printf("학점: %d\n", s->grade);
	printf("학과: %s\n", s->major);

	system("pause");
	return 0;
}
*/