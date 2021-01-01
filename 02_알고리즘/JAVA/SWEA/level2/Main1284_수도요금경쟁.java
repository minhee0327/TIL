package level2;

import java.util.Scanner;

public class Main1284_수도요금경쟁 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int t= 0; t < T; t++) {
			int P = sc.nextInt();
			int Q = sc.nextInt();
			int R = sc.nextInt();
			int S = sc.nextInt();
			int W = sc.nextInt();
			
			int A = P * W; 
			int B = 0;
			if(W <= R) {
				B = Q;
			}else {
				B = (W-R) * S + Q;
			}
			
			System.out.printf("#%d %d", t+1, A>B? B: A);
		}
		
	}
}
