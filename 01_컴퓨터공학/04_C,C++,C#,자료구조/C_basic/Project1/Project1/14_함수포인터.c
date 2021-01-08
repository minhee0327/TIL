/*
- C언어에서는 함수의 이름을 이용해 특정한 함수를 호출
- 함수 이름은 메모리 주소 반환

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
- 함수포인터
	- 함수 포인터는 특정한 함수의 반환자료형을 지정하는 방식으로 선언할 수 있음.
	- 함수 포인터를 이용하면 형태가 같은 서로 다른 기능의 함수를 선택적으로 사용할 수 있음.
	- 반환자료형 (*함수명)(매개변수) = 함수명;
	- 반환자료형 (*이름)(매개변수) = 함수명;
	
- 매개변수 및 반환자료형이 없는 함수 포인터
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
- 매개변수와 반환 자료형이 있는 함수포인터
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
- 함수포인터 반환하여 사용하기.

#include <stdio.h>

int add(int a, int b) {
	return a + b;
}
int (*process(char* a))(int , int ) {
	printf("%s\n", a);
	return add;
}

int main(void) {
	printf("%d\n", process("10과 20을 더해보겠습니다.")(10, 20));
	system("pause");
	return 0;
}



---
- typedef 사용하여 더 짧게 선언 정의
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


---
- 혹은 익명 구조체 개념 

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

*/