package chapter04;

import java.util.Scanner;

public class ch05_star {

	public static void main(String[] args) {
		System.out.println("홀수값 입력");
		Scanner sc = new Scanner(System.in);
		
		int row = sc.nextInt();
		int spaceCnt = row / 2;
		int starCnt = 1;
		
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < spaceCnt; j++) {
				System.out.print(' ');
			}
			for (int j = 0; j < starCnt; j++) {
				System.out.print("*");
			}
			for (int j = 0; j < spaceCnt; j++) {
				System.out.print(" ");
			}
			if (i < row /2) {
				spaceCnt-=1;
				starCnt+=2;
			}else {
				spaceCnt+=1;
				starCnt-=2;
			}
			System.out.println();
		}
		
		
		
	}

}
