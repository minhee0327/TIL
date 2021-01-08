package level2;

import java.util.Scanner;

public class Main1204_최빈수구하기 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int tc = sc.nextInt();

		for (int t = 0; t < tc; t++) {
			int T = sc.nextInt();
			int[] score = new int[101];

			for (int i = 0; i < 1000; i++) {
				int temp = sc.nextInt();
				score[temp]++;
			}

			int maxCount = 0;
			for (int i = 0; i <= 100; i++) {
				if (maxCount < score[i]) {
					maxCount = score[i];
				}
			}

			for (int i = 100; i >= 0; i--) {
				if (maxCount == score[i]) {
					System.out.printf("#%d %d%n", T, i);
					break;
				}
			}
		}
	}
}
