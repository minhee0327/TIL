package day04_array;

import java.util.Scanner;

public class Main3052_1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		boolean arr[] = new boolean[42];
		int cnt = 0;
		
		for (int i = 0; i < 10; i++) {
			int temp = sc.nextInt();
			if (!arr[temp % 42]) {
				cnt++;
				arr[temp % 42] = true;
			}
		}
		System.out.println(cnt);
	}
}
