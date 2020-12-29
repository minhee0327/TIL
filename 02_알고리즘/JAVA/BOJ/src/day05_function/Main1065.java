package day05_function;

import java.util.Scanner;

public class Main1065 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		if (n < 100) {
			//예제 입력 1을 통해서 100 ~ 110 까지는 계속 99이고
			//100미만의 수까지는 자기자신만큼이 한수의 개수인 것을 알 수 있다..
			System.out.println(n);
		}else {
			int ret = 99;
			for (int i = 100; i <= n; i++) {
				ret += checkHansu(i);
			}
			System.out.println(ret);
		}
		sc.close();
	}

	private static int checkHansu(int i) {
		int first = i /100;
		int second = (i/10) % 10;
		int third = i %10;
		// 세개의 수 중 (첫번째값과 세번째값의 합) == (가운데값 * 2) 이면 등차수열이 성립함.
		if (second * 2 == first + third) {
			return 1;
		}
		return 0;
	}
}
