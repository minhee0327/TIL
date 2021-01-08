package level2;

import java.util.Scanner;

public class Main1859_백만장자프로젝트 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int tc = sc.nextInt();
		for (int t = 1; t <= tc; t++) {
			int n = sc.nextInt();
			int arr[] = new int[n];

			for (int i = 0; i < n; i++) {
				arr[i] = sc.nextInt();
			}

			// total 이익
			long total = 0;
			// pivot 기준
			int pivot = arr[n - 1];

			for (int i = n - 1; i >= 0; i--) {
				if (pivot <= arr[i]) {
					pivot = arr[i];
				} else {
					total += (pivot - arr[i]);
				}
			}

			System.out.printf("#%d %d%n", t, total);
		}
	}
}
