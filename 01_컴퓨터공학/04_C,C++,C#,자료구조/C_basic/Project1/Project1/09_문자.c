/*
- 문자
	- 아스키코드
		- 0~127중 1byte로 구성. 주요문자 출력
		- 0-9: 48-57, A: 65, a: 97
	- 문자 하나 입력(getchar())
	- buffer
		- 문자열 처리
		- 임시로 특정 데이터를 저장하기 위한 목적
		- 처리할 수 있는 양에 한계가 있기 때문에, buffer에 임시적으로 담겨있다가 사용됨.
		- C 프로그램은 기본적으로 사용자가 의도치 않아도 자동으로 buffer를 이용해 입출력.
*/

/*
#include <stdio.h>

//문자: 아스키코드
int main(void) {
	char a = 65;
	printf("%c\n", a);
	system("pause");
	return 0;
}
*/

/*
#include <stdio.h>

//문자: getchar(): 단하나의 문자를 입력받는다.
int main(void) {
	char a = getchar();
	printf("%c\n", a);
	system("pause");
	return 0;
}
*/

/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// 입력버퍼로 인해 발생하는 오류1:
// 연속해서, 두번 입력을 받을 때, c를 입력받지 않는 것 처럼 보인다.!
// 이유: scanf("%c",c);에서 줄바꿈(개항문자) 혹은 파일의 끝일 때, 문자로 인식하기 때문.
// 따라서 항상 입력버퍼를 비워야함.(다음 예제에 작성)
int main(void) {
	int a;
	char c;
	scanf("%d", &a);
	printf("%d\n", a);
	scanf("%c", &c);
	printf("%c\n", c);
	system("pause");
	return 0;
}
*/

/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main(void) {
	int a;
	char c;
	scanf("%d", &a);
	printf("%d\n", a);

	//모든 문자는 ASCII로 표현가능
	int temp;

	// 입력버퍼를 비워주는 방법1: getchar()를 이용한다. (그 밖에도 있지만, 강의에서는 getchar()사용)
	while ((temp = getchar()) != EOF && temp != '\n') {}
	// EOF: End of file
	// temp = getchar()를 통해 버퍼에 값을 받고, 그 값이 \n이 아니라면,
	// while이 true로 반복한다.
	// 다시 temp= getchar()로 다음 버퍼를 입력받고, 조건을 받고 이를 계속 반복하면서,
	// getchar()가 마지막에 개행문자를 받으면, 해당 while문을 False로 빠져나올수있고,
	// 이때 temp에 개행문자가 저장된다. (따라서 다음 문자에 개행문자 받지 않고 정상 문자 받음)

	scanf("%c", &c);
	printf("%c\n", c);
	system("pause");
	return 0;
}
*/