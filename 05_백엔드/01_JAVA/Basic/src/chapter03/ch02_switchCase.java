package chapter03;

import java.util.Scanner;

public class ch02_switchCase {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int rank = sc.nextInt();
		char medalColor;
		
		switch(rank) {
			case 1: medalColor = 'G';
				System.out.println("금");
				break;
			case 2: medalColor = 'S';
				System.out.println("은");
				break;
			case 3: medalColor = 'B';
				System.out.println("동");
				break;
			default: medalColor = 'A';
			
		}
		System.out.println(rank + "등은 "+ medalColor + "메달 입니다.");
	}
}
