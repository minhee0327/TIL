package level3;

import java.util.Scanner;

public class Main1244_최대상금 {
	public static String numbers[];
	public static int count;
	public static int ans;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int t = 1; t <= T; t++) {
			numbers = sc.next().split("");
			count = sc.nextInt();

			ans = 0;

			dfs(0, 0);

			System.out.printf("#%d %d%n", t, ans);
		}
	}

	// int p: pivot, int c: currentCount
	private static void dfs(int p, int c) {
		if (c == count) {
			String resultNum = "";
			for (String n : numbers) {
				resultNum += n;
			}
			if (Integer.parseInt(resultNum) > ans) {
				ans = Integer.parseInt(resultNum);
			}
			return;
		}else if(c == 0) {
			for (int i = p; i < numbers.length; i++) {
				for (int j = i + 1; j < numbers.length; j++) {
					swap(i, j);
					dfs(i, c + 1);
					swap(i, j);
				}
			}
		}else {
			for (int i = p; i < numbers.length; i++) {
				for (int j = i + 1; j < numbers.length; j++) {
					if (Integer.parseInt(numbers[i]) <= Integer.parseInt(numbers[j])) {
						swap(i, j);
						dfs(i, c + 1);
						swap(i, j);
					}
					
				}
			}
		}

		
	}

	private static void swap(int i, int j) {
		String temp = numbers[i];
		numbers[i] = numbers[j];
		numbers[j] = temp;
	}

}
