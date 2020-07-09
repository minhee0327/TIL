/*
- 컴퓨터가 변수를 처리하는방법
	- 지역변수, 전역변수, 레지스터 변수 등을 학습
	- 특정 함수에 값을 전달하거나 주소를 전달하는 방법 학습

- 프로그램 메모리 주소
	- 컴퓨터에서 프로그램이 실행되기 위해서는 프로그램이 메모리에 적재(Load)되야함.
	- 당연히 프로그램의 크기를 충당할 수 있을만큼의 메모리공간이 있어야함.
	- 일반적인 OS에서는 메모리공간을 4가지로 구분 및 관리 (OS참조)
		- STACK : 지역변수, 매개변수
		- HEAP : 동적 할당 변수
		- DATA(BSS): 전역변수, 정적변수
		- CODE: 소스코드
---

- 전역변수
	- Global Varialbe, 프로그램의 어디서든 접근 가능한 변수
	- main함수가 실행되기 전, 프로그램 시작과 동시에 메모리에 할당(DATA영역에)
	- 프로그램크기가 커질 수록 전역변수로 인해 프로그램이 복잡해질수 있음.
	- 메모리의 데이터 영역에 적재됨.

#include <stdio.h>

int a = 5; //메인함수 밖에 선언

void changeValue() {
	a = 10;
}

int main(void) {
	printf("%d\n", a);
	changeValue();
	printf("%d\n", a);
	system("pause");
	return 0;
}


---
- 지역변수
	- Local Variable 프로그램에서 특정 블록에서만 접근할 수 있는 변수
	- 함수가 실행될때마다 메모리에 할당되어 함수가 종료되면 메모리에서 해제됨.
	- STACK영역에 적재

#include <stdio.h>

int main(void) {
	int a = 7;
	if (1) {
		int a = 5;
	}
	printf("%d\n", a);
	system("pause");
	return 0;
}
---

- 정적 변수
	- Static variable 특정 블록에서만 접근할 수 있는 변수
	- 프로그램이 실행될때 메모리에 할당되어 프로그램이 종료되면 메모리에서 해제.
	- DATA 영역에 적재

#include <stdio.h>

void process() {
	static int a = 5;
	a = a + 1;
	printf("%d\n", a);
}

int main(void) {
	process();
	process();
	process();
	system("pause");
	return 0;
}

---
- 레지스터 변수
	- 메인메모리대신 CPU에 붙어있는 레지스터를 사용하기 때문에, 훨씬 빠를 수 있다고 기대.
	- 메모리보다 레지스터가 CPU에 가까움
	- 레지스터는 매우 한정되어 있으므로, 실제로 레지스터에서 처리될지는 장담할 수 없음.

#include <stdio.h>

int main(void) {
	register int a = 10, i;
	for (i = 0; i < a; i++) {
		printf("%d ", i);
	}
	system("pause");
	return 0;
}

---
- 함수의 매개변수가 처리될때
	- 함수를 호출할 때 함수에 필요한 데이터를 매개변수로 전달.
	- 전달방식 2가지
		- 값에 의한 전달방식 (call by value)
			- 단지 값을 전달하기때문에, 함수 내에서 변수가 새롭게 생성
			- argument를 복사하여 호출된 함수의 매개 변수로 전달. (local value)
		- 참조에 의한 전달방식(call by reference)
			- 주소를 전달하기 때문에, 원래의 변수 자체에 접근할 수 있음.
			- &를 사용하여 선언하고, 별도 공간이 할당된 것이 아니라, 원본 변수 공간을 공유함.
- 참조: 

#include <stdio.h>

void add(int a, int b) { //STACK 
	a = a + b; // STACK 
	printf("%d\n", a); // STACK (17)

}

int main(void) {
	int a = 7; // DATA 
	add(a, 10);
	printf("%d\n", a); // DATA (7)
	system("pause");
	return 0;
}



#include <stdio.h>

void add(int *a) { //간접참조
	*a = *a + 10; //해당 주소의 공간에 있는 값을 변경.
}

int main(void) {
	int a = 7;
	add(&a); //주소 전달
	printf("%d\n", a); //17
	system("pause");
	return 0;
}

*/