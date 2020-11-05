package chapter04;

import java.util.Scanner;

public class ch01_while2 {

	public static void main(String[] args) {
//		do while : 먼저 수행문을 수행하고 조건 체크. (한 번 이상 수행문이 수행되어야 하는 경우 사용)
		
//		int num = 1;
//		int sum = 0;
//		
//		do {
//			sum += num;
//			num ++ ;
//		}while (num <= 10);
//		
//		System.out.println(sum);
//		System.out.println(num);
		
		
		Scanner sc = new Scanner(System.in);
		int input;
		int sum = 0;
		
		do {
			input = sc.nextInt();
			sum += input;
		}while(input != 0);
		
		System.out.println(sum);
	}
}
