package level2;

import java.util.Scanner;

public class Main1986_지그재그숫자 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int tc = sc.nextInt();
		
		for(int t = 1 ; t <= tc ; t++) {
			int total = 0;
			int n =  sc.nextInt();
			
			for(int i = 1; i <= n; i++) {
				if(i % 2 == 0) {
					total -= i;
				}else if(i %2 != 0) {
					total += i;
				}
			}
			
			System.out.printf("#%d %d%n", t, total);
		}
		
	}

}
