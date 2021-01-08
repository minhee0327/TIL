package day07_math01;

import java.util.Scanner;

public class Main1712_손익분기점 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();

		if ((c-b)<=0) {
			System.out.println(-1);
		}else {
			System.out.println(a/(c-b)+1);
		}
	}
}
//접근
//cnt = a/(c-b);
//여기서 a는 고정. 
//손익분기가 안일어난다는건 c-b<=0일경우.
