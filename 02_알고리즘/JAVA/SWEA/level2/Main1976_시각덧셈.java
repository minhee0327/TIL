package level2;

import java.util.Scanner;

public class Main1976_시각덧셈 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int t = 0; t < T ; t++) {
			int h = sc.nextInt();
			int m = sc.nextInt();
			int hh = sc.nextInt();
			int mm = sc.nextInt();
			
			int totalMinute = (h+hh) * 60 + (m + mm);
			
			System.out.printf("#%d %d %d%n", t+1, (totalMinute / 60)%12==0?12:(totalMinute / 60)%12 , totalMinute %60);
		}
	}

}
