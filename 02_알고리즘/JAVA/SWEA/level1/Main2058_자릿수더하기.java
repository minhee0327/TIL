package level1;

import java.util.Scanner;

public class Main2058_자릿수더하기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int sum = 0;

		while (n > 0) {
			sum += n % 10;
			n /= 10;
		}

		System.out.println(sum);
	}
}
