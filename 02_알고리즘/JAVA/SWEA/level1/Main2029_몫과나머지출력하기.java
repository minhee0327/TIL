package level1;

import java.util.Scanner;

public class Main2029_몫과나머지출력하기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		
		for(int i = 0; i< t; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			System.out.printf("#%d %d %d%n", i+1, a/b, a%b);
		}
	}
}
