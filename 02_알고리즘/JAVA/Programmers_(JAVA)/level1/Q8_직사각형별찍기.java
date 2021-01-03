package level1;

import java.util.Scanner;

public class Q8_직사각형별찍기 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		//java11이상에서 돌아갈 코드
		/*
		for(int i = 0; i<b; i++){
		    System.out.println("*".repeat(a));
		}
		*/
		
		//local환경에서는 8버전 사용하고 있기 때문에, 2중 for문 활용
		for (int i = 0; i < b; i++) {
			for (int j = 0; j < a; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
	
}
