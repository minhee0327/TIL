/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//1~100���� ����ϱ�
int main(void) {
	int i;
	for (i = 1; i <= 100; i++)
	{
		printf("%d\n", i);
	}
	system("pause");
	return 0;
}
*/

/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//1~n������ �� ���ϱ�
int main(void) {
	int n, sum = 0;

	printf("n�� �Է��ϼ���..\n");
	scanf("%d", &n);
	for (int i = 1; i<= n;  i++)
	{
		sum += i;
	}
	printf("%d", sum);

	system("pause");
	return 0;
}
*/

/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// a ������ŭ, c(����) ����ϱ�
int main(void) {
	int a;
	char c;

	scanf("%d %c", &a, &c);
	while (a--) {
		printf("%c ", c);
	}
	system("pause");
	return 0;
}

*/


/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//������ �� Ư�� �� ���
int main(void) {
	int n;

	printf("�� ���� �ñ��ϽŰ���?\n");
	scanf("%d", &n);
	int i = 1;

	while (i<=9){
		printf("%d * %d = %d\n", n, i, n * i);
		i++;
	}

	system("pause");
	return 0;
}
*/


/*
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int i = 1;

	while (i<=9){
		int j = 1;
		while (j <= 9) {
			printf("%d * %d = %d\n", i, j, i * j);
			j++;
		}
		printf("----------\n");
		i++;
	}

	system("pause");
	return 0;
}
*/

/*
- �ݺ���
	- for�� �� while ���� ���� ġȯ�� �����ϴ�.
	- (���������� ����� �ܿ����� ���� �����ϱ� ����)
	- ���ѷ����� �׻� �����ϰ�
	- ���߹ݺ����� ���, �׷��� ���꿡�� ���� Ȱ���
	- ��, ��ø(����)�ݺ����� ����� ��, ���ɿ� ���ؼ� �� ����Ͽ� ������ ��.
*/