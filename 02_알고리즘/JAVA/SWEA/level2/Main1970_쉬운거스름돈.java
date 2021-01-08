package level2;

import java.util.Scanner;

public class Main1970_쉬운거스름돈 {
	public static int[] money = {50000, 10000, 5000,1000,500,100,50,10};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int t= 0; t < T; t++) {
			int n = sc.nextInt();
			int count[] = new int[money.length];
			
			for(int i = 0; i < money.length; i++) {
				count[i] = n/money[i];
				n-= count[i] * money[i];
			}
			
			System.out.printf("#%d%n", t+1);
			for(int i = 0; i< count.length; i++) {
				System.out.printf("%d ", count[i]);
			}
			System.out.println();
		}
	}

}
