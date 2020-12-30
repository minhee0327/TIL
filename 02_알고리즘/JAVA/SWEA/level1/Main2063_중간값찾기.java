package level1;

import java.util.Arrays;
import java.util.Scanner;

public class Main2063_중간값찾기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int[] arr = new int[N];

		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}
		Arrays.sort(arr);
		System.out.println(arr[N / 2]);
		sc.close();
	}
}
