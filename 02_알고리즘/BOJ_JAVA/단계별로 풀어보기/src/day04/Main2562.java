package day04;

import java.util.Scanner;

public class Main2562 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int max = Integer.MIN_VALUE;
		int idx = 0;
		
		for (int i = 1; i < 10; i++) {
			int n = sc.nextInt();
			if (max <n) {
				max = n;
				idx = i;
			}
		}
		System.out.println(max);
		System.out.println(idx);
	}
}
