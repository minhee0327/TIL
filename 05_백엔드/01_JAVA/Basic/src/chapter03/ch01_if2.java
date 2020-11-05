package chapter03;

import java.util.Scanner;

public class ch01_if2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int age = sc.nextInt();
		int charge = 0;
		
		if (age < 8) {
			charge = 1000;
		}else if (age < 14) {
			charge = 1500;
		}else if (age < 20) {
			charge = 2000;
		}else {
			charge = 3000;
		}
		
		System.out.println("나이: "+ age );
		System.out.println("요금 "+ charge );
	
		sc.close();
	}
}
