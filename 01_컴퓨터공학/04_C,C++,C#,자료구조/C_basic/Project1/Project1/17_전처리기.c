/*
- 전처리기
	- 다른 프로그램 영역과 독립적으로 처리
	- 소스 파일 단위로 효력이 있음

---
- 파일 포함 전처리기
	- #include는 전처리기에서 가장 많이 사용되는 문법
	- 특정 파일을 라이브러리로서 포함시키기 위해 사용.
	- #include 구문으로 가져올수있는 파일에는 제약이 없음.
	- 사용 방법 (2가지)
		- #include "파일이름"
			- 이와같이 선언하면, 현재 폴더에서 파일을 검색
			- 만약 해당 파일이 없으면, 시스템 디렉토리에서 파일을 검색.
		- #include <파일이름>
			- 이와같이 선언하면, 시스템 디렉토리에서 파일을 검색
			- 운영체제마다 시스템 디렉토리가 존재하는 경로가 다를 수 있음.
			- 대표적으로 <stdio.h>와 같은 헤더파일 등이 시스템 디렉토리에 존재함.

- 실습1(17_example01.h)
	- 나만의 헤더파일 작성하기
		- #include를 이용해 가져오는 파일은 말 그대로 파일의 소스코드 자체를 다 가져오는 것.
		- 따라서, 의도치 않게 한번 참조한 헤더파일을 여러번 참조하지 않도록 유의할 것.
		- 반드시 한번만 호출할것!

- 17_example01.h 파일 내용
int add(int a, int b){
	 return a + b;
	}

- main함수에서 실행

#include <stdio.h>
#include "17_example01.h"

int main(void) {
	printf("%d\n", add(3, 7));
	system("pause");
	return 0;
}



---
- 매크로 전처리기
	- 프로그램 내부에 사용되는 상수나 함수를 매크로 형태로 저장하기 위해 사용한다.
	- #define문법을 사용해 정의

- 실습1
#include <stdio.h>
#define PI 3.141592535

int main(void) {
	int r = 10;
	printf("원의 둘레: %.2f\n", 2 * PI * r);
	system("pause");
	return 0;
}

- 인자를 가지는 매크로 전처리기
	- #define 문법에는 인자가 포함 될 수 있다.
	- 소스코드의 양을 획기적으로 줄일 수 있다.

예1)
#include <stdio.h>
#define POW(x) (x * x)

int main(void) {
	int x = 10;
	printf("x의 제곱: %d\n",POW(x));
	system("pause");
	return 0;
}

예2)
#include <stdio.h>
#define ll long long
#define ld long double

int main(void) {
	ll a = 987654321000;
	ld b = 100.5054;

	printf("%.1f\n",a*b);
	system("pause");
	return 0;
}


---
- 조건부 컴파일
	- 조건부 컴파일은 컴파일이 이루어지는 영역을 지정하는 기법
	- 일반적으로 디버깅과 소스코드 이식을 목적으로 하여 작성
	- C언어로 시스템 프로그램을 작성할 때에는 운영체제에 따라 소스코드가 달라질 수 있음.
	- 이 때, 운영체제에 따라 컴파일이 수행되는 소스코드를 다르게 할 수 있음.

	- 대표적인 조건부 컴파일: #ifndef ~ #endif 문법
	- 흔히 헤더 파일이 중복되어 사용되지 않도록 하기 위해 적용
	- 특정 매크로가 이미 선언이 되어있지 않을 경우에만 구문을 컴파일함.

- 헤더파일 내용
#ifndef _TEMP_H_

#define _TEMP_H_
int add(int a, int b) {
	return a + b;
}

#endif

- main.c내용
- 두번 호출해도 error없이 실행됨
	
#include <stdio.h>
#include "17_example01.h"
#include "17_example01.h"

int main(void) {

	printf("%d\n",add(3,7));
	system("pause");
	return 0;
}


- 파일 분할 컴파일
	- 헤더파일에 있는 함수 내용을 c언어 코드로 구현하여 나누어 관리할 수 있다.
	
*/