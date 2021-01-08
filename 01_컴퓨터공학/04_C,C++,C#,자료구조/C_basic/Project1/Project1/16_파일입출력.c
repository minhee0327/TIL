/*
- 파일 입출력 필요성
	- 프로그램 꺼진 이후에도 데이터 저장가능
	- 파일이 실질적으로 저장되는 공간 : SSD 

- 파일을 열고 닫기
	- 파일 입출력 변수는 FILE형식의 포인터 변수로 선언합니다.
	- 파일을 열때는 fopen()함수 이용
	- 파일을 닫을때는 fclose()함수 이용
		- FILE *fp;
		- fp = fopen(파일 경로, 접근방식);
		- fclose(fp);

- 파일 열고 닫기
	- 파일 열기함수인 fopen()함수에는 파일경로와 접근방식을 설정할 수 있다.
	- 기본 경로는 현재 프로그램의 경로
	- 가장 많이 사용되는 접근 방식은 다음과 같다.
		- r: 파일에 접근하여 데이터를 읽음
		- w: 파일에 접근하여 데이터를 기록 (파일 이미 존재할 경우, 덮어쓰기)
		- a: 파일에 접근하여 데이터를 뒤에서부터 기록.

- 파일 입출력 함수
	- 기본적인 입출력을 위해, printf()와 scanf()함수를 사용했는데,
	- 파일입출력에서는 fprintf()와 fscanf()를 사용함.
		- fprintf(파일포인터, 서식, 형식지정자);
		- fscanf(파일포인터, 서식, 형식지정자);

- 파일 입출력과정
	- 파일입출력은 열고, 읽고/쓰고, 닫기 과정을 철저히 따른다.
	- 파일을 열때는 파일 포인터가 사용되며, 이는 동적으로 할당
	- 따라서, 파일 처리 이후에 파일을 닫아주지 않으면, 메모리 누수발생하으로 꼭 닫기!

- 예제1: 파일을 열어 문자열 쓰기
	- 현재 프로그램의 경로에서 특정한 파일을 쓰기모드로 생성하여 문자열 기록할 수 있음.

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

- 예제2: 학생정보 시스템 만들기
	- 학생들의 이름과, 성적 파일 만들고 해당 파일의 내용 출력하기

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
		printf("이름: %s, 성적: %d\n", (students + i)->name, (students + i)->score);
	}
	system("pause");
	return 0;
}

- 성적 평균을 구하고 메모리 할당 해제하기.


*/