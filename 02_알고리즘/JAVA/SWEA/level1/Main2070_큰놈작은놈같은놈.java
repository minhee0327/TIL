package level1;

import java.util.Scanner;

public class Main2070_큰놈작은놈같은놈 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int tc = sc.nextInt();

		for (int t = 0; t < tc; t++) {
			int a = sc.nextInt();
			int b = sc.nextInt();

			if (a > b) {
				System.out.printf("#%d %c\n", t + 1, '>');
			} else if (a == b) {
				System.out.printf("#%d %c\n", t + 1, '=');
			} else {
				System.out.printf("#%d %c\n", t + 1, '<');
			}
		}
	}
}
