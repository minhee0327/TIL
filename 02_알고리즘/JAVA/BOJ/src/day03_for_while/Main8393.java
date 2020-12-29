package day03_for_while;

import java.util.Scanner;

public class Main8393 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int sum = 0;
		for (int i = 1; i <= n ; i++) {
			sum += i;
		}
		System.out.println(sum);
		
	}
}
