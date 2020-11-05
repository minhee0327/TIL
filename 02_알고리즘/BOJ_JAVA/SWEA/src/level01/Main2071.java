package level01;

import java.util.Scanner;

public class Main2071 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		
		for (int i = 0; i < t; i++) {
			float sum = 0;
			for (int j = 0; j < 10; j++) {
				sum += sc.nextInt();
			}
			System.out.printf("#%d %d\n", i+1, Math.round(sum/10));
		}
	}
}
