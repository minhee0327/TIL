package chapter04;

import java.util.Scanner;

public class ch01_while {

	public static void main(String[] args) {
//		int num = 1;
//		int sum = 0;
//			
//		while (num <= 10) {
//			sum += num;
//			num ++;
//		}
//		System.out.println(sum);
//		System.out.println(num);
		
		Scanner sc = new Scanner(System.in);
		
		int input;
		int sum = 0;
		input = sc.nextInt();
		
		while(input!=0) {
			sum+= input;
			input = sc.nextInt();
		}
		System.out.println(sum);
	}
}
