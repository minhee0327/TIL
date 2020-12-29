package day07_math01;

import java.util.Scanner;

public class Main2839_설탕배달 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int cnt = 0;
		int min = Integer.MAX_VALUE;
		
		while(true) {
			if(n % 5 == 0) {
				System.out.println(n/5 + cnt);
				break;
			}else if (n<0) {
				System.out.println(-1);
				break;
			}
			cnt ++;
			n -=3;
		}
		
	}
}
