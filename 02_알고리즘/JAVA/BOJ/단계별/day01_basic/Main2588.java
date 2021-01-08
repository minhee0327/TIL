package day01_basic;

import java.util.Scanner;

public class Main2588 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int c, d, e, f;
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		c = a * (b%10);
		b /= 10;

		d = a * (b%10);
		b /= 10;
		
		e = a * (b%10);
		
		System.out.println(c + "\n"+ d+ "\n" + e+ "\n" + (c+d* 10+e* 100));
	}

}
