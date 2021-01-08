package level1;

import java.util.Scanner;

public class Main2072_홀수만더하기 {

	public static void main(String[] args) {
		 Scanner sc = new Scanner(System.in);
			
			int t = sc.nextInt();
			
			for (int i = 0; i < t; i++) {
				int sum = 0;
				
				for (int j = 0; j < 10; j++) {
					int tmp = sc.nextInt();
					if(tmp %2 != 0) {
						sum += tmp ;
					}
				}
				
				System.out.printf("#%d %d\n", i+1, sum);
			}
		}
	}
