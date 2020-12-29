package day03_for_while;

import java.util.Scanner;

public class Main10871 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int X = sc.nextInt();
		
		for (int i = 0; i < N; i++) {
			int temp = sc.nextInt();
			
			if(temp < X) {
				System.out.print(temp+" ");
			}
		}
	}

}
