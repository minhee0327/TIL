/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//사칙연산
int main(void) {
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d + %d = %d\n", a, b, a + b);
	printf("%d - %d = %d\n", a, b, a - b);
	printf("%d * %d = %d\n", a, b, a * b);
	printf("%d / %d = %d\n", a, b, a / b);
	printf("%d %% %d = %d\n", a, b, a % b);

	system("pause");
}
*/


/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//escape sequence (\n, \t, \", \b..)
int main(void) {
	printf("\"A\tB\tC\tD\"\n");
	printf("\"A\tB\tC\tD\"\n");
	printf("\"A\tB\tC\tD\"\n");

	system("pause");
	return 0;
}
*/


/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//관계연산자 (true: 1, false: 0반환)
int main(void) {
	int a, b;

	scanf("%d %d", &a, &b);
	printf("%d", a > b);

	system("pause");
	return 0;
}
*/


/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//논리연산자
int main(void) {
	int a, b, c;

	scanf("%d %d %d", &a, &b, &c);
	printf("%d\n", !a);
	printf("%d\n", a &&b);
	printf("%d\n", (a>b) && (b>c));

	system("pause");
	return 0;
}
*/

/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//증감연산자
int main(void) {
	int a = 7;

	printf("%d\n",++a); //8
	printf("%d\n",a++); //8
	printf("%d\n", ++a); //10

	system("pause");
	return 0;
}*/

/*
- 연산자 우선순위
1. ++, --
2. !, ~
3. *, /, %
4. +, -
5. <<,>>
6. <, <= , >= , >
7. ==, !=
8. 비트, 논리, 삼항
9. 삼항연산자

*/