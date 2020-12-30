package level1;

import java.util.Scanner;

public class Main2068_최대수구하기 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int tc = sc.nextInt();

		for (int t = 0; t < tc; t++) {
			int max = -1;

			for (int j = 0; j < 10; j++) {
				int temp = sc.nextInt();
				if (temp > max) {
					max = temp;
				}
			}

			System.out.printf("#%d %d\n", t + 1, max);
		}

	}

}
