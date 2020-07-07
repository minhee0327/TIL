/*
- 문자열 개념
	- 문자들의 배열
	- 컴퓨터 메모리 구조상 마지막에 null값(존재X, \0) 포함 
	- null이 들어가는이유: 문자열의 끝을 알려주는 목적
	- printf()함수가 내부적으로 null을 만날때까지 출력하는 원리.

- 문자열과 포인터
	- 문자열 형태로 포인터를 사용하면, 포인터에 특정한 문자열의 주소를 넣게 된다.
	- 문자열을 읽기 전용으로 메모리 공간에 넣은 뒤, 그 위치를 처리함.
	- 이러한 문자열을 문자열 리터럴 이라고 한다. 컴파일러가 알아서 메모리 주소 결정.

#include <stdio.h>

int main(void) {
	char* a = "Hello World";
	printf("%s\n", a);
	system("pause");
	return 0;
}

- 포인터로 문자열을 선언했다 하더라도, 기존 배열처럼 사용가능.

#include <stdio.h>

int main(void) {
	char* a = "Hello World";
	printf("%c\n", a[1]);
	printf("%c\n", a[2]);
	printf("%c\n", a[6]);
	system("pause");
	return 0;
}

- 문자열 입출력 함수
	- 문자열 입출력 수행
	- scanf(): 공백을 만날때까지만 입력받음
	- gets() : 공백까지 포함하여 한 줄 입력받음 (보안상 취약해서 gets_s()가 좀 더 안정적)
	- gets_s(문자열, 크기): 버퍼의 크기를 철저히 지키는 함수. 
	- sizeof(): C에서 배열의 크기 알려주는 기본 내장함수

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


- 문자열 처리를 위한 다양한 함수
	- <string.h> 라이브러리에 포함되어 있음.
	- strlen(): 문자열길이 반환
	- strcmp(str1, str2): str1이 str2보다 사전적으로 앞에 있으면 -1, 뒤에있으면 1 반환
	- strcpy(): 문자열복사
	- strcat(): 문자열1에 문자열2를 더함
	- strstr(): 문자열1에 문자열2가 어떻게 포함되어있는지 반환.


#include <stdio.h>

int main(void) {
	char a[20] = "MinHee Kang";
	char b[20] = "JongHuyn Lee";
	char c[20] = "Change name";
	char d[30] = "My name is.."; //연결되어지는 문자열의 크기는 조금 더 넉넉히
	char e[20] = "name";

	printf("문자열의 길이: %d\n", strlen(a)); 

	printf("두 문자의 사전순 비교: %d\n", strcmp(a, b)); // 1: a 가 사전순으로 b보다 뒤에있음

	strcpy(c, a); //a값을 c에 복사
	printf("문자열 copy a to c: %s\n", c); 

	strcat(d, a); //d에 a 연결
	printf("문자열 연결하기: %s\n", d);

	// 긴 문자열에서, 짧은 문자열을 찾아서 위치를 반환함.
	// 단순 출력하게 되면, 찾은 이후 문자열 모두 반환됨.
	printf("strstr() 결과: %s\n", strstr(d, e));

	system("pause");
	return 0;
}
*/
