package day03_for_while;

import java.util.Scanner;

public class Main1110 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		int cnt = 0;
		int a = n/10;
		int b = n%10;
		int newValue = a+b;
				
		
		while(true) {
			a = b;
			b = newValue %10;
			newValue = a + b;
			cnt++;
			
			if (a*10 + b  == n) break;
		}
		
		System.out.println(cnt);
	}

}
