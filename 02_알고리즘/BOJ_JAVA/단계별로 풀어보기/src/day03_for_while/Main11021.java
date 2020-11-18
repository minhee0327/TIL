package day03_for_while;

import java.util.Scanner;

public class Main11021 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for (int tc = 0; tc < T; tc++) {
			int A = sc.nextInt();
			int B = sc.nextInt();
			
			System.out.printf("Case #%d: %d\n",tc+1,A+B);
		}
	}
}
