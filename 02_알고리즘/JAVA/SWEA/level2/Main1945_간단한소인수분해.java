package level2;

import java.util.Scanner;

public class Main1945_간단한소인수분해 {
	public static int[] soinsu = {2, 3, 5, 7, 11};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int t = 0; t < T; t++) {
			int n = sc.nextInt();
			int[] count = new int[5];
			
			for(int i = soinsu.length -1; i > -1; i--) {
				while(n % soinsu[i] ==0) {
					count[i]++;
					n/= soinsu[i];
				}
			}
			System.out.printf("#%d ", t+1);
			for(int c: count) {
				System.out.print(c+" ");
			}
			System.out.println();
		}
	}
}
