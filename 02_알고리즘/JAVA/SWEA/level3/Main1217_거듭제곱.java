package level3;

import java.util.Scanner;

public class Main1217_거듭제곱 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for(int t= 0 ; t < 10; t ++) {
			int tc = sc.nextInt();
			int n = sc.nextInt();
			int m = sc.nextInt();
		
			int result = recursive(n, m);
		
			System.out.printf("#%d %d\n", tc, result);
		}
	}

	private static int recursive(int n, int m) {
		if (m==1) {
			return n;
		}else {
			return n * recursive(n, m-1);
		}
	}
}
