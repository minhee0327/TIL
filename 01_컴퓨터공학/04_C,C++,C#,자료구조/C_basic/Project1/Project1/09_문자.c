/*
- ����
	- �ƽ�Ű�ڵ�
		- 0~127�� 1byte�� ����. �ֿ乮�� ���
		- 0-9: 48-57, A: 65, a: 97
	- ���� �ϳ� �Է�(getchar())
	- buffer
		- ���ڿ� ó��
		- �ӽ÷� Ư�� �����͸� �����ϱ� ���� ����
		- ó���� �� �ִ� �翡 �Ѱ谡 �ֱ� ������, buffer�� �ӽ������� ����ִٰ� ����.
		- C ���α׷��� �⺻������ ����ڰ� �ǵ�ġ �ʾƵ� �ڵ����� buffer�� �̿��� �����.
*/

/*
#include <stdio.h>

//����: �ƽ�Ű�ڵ�
int main(void) {
	char a = 65;
	printf("%c\n", a);
	system("pause");
	return 0;
}
*/

/*
#include <stdio.h>

//����: getchar(): ���ϳ��� ���ڸ� �Է¹޴´�.
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

// �Է¹��۷� ���� �߻��ϴ� ����1:
// �����ؼ�, �ι� �Է��� ���� ��, c�� �Է¹��� �ʴ� �� ó�� ���δ�.!
// ����: scanf("%c",c);���� �ٹٲ�(���׹���) Ȥ�� ������ ���� ��, ���ڷ� �ν��ϱ� ����.
// ���� �׻� �Է¹��۸� �������.(���� ������ �ۼ�)
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

	//��� ���ڴ� ASCII�� ǥ������
	int temp;

	// �Է¹��۸� ����ִ� ���1: getchar()�� �̿��Ѵ�. (�� �ۿ��� ������, ���ǿ����� getchar()���)
	while ((temp = getchar()) != EOF && temp != '\n') {}
	// EOF: End of file
	// temp = getchar()�� ���� ���ۿ� ���� �ް�, �� ���� \n�� �ƴ϶��,
	// while�� true�� �ݺ��Ѵ�.
	// �ٽ� temp= getchar()�� ���� ���۸� �Է¹ް�, ������ �ް� �̸� ��� �ݺ��ϸ鼭,
	// getchar()�� �������� ���๮�ڸ� ������, �ش� while���� False�� �������ü��ְ�,
	// �̶� temp�� ���๮�ڰ� ����ȴ�. (���� ���� ���ڿ� ���๮�� ���� �ʰ� ���� ���� ����)

	scanf("%c", &c);
	printf("%c\n", c);
	system("pause");
	return 0;
}
*/