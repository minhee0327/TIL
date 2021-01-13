package level3;

import java.util.Scanner;

public class Main1491_원재의벽꾸미기 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int t = 1; t <= T; t++) {
			int N = sc.nextInt();
			int A = sc.nextInt();
			int B = sc.nextInt();
			
			long ans = Integer.MAX_VALUE;
			
			for(long r = 1; r <= Math.sqrt(N); r++) {
				long maxC = N/r;
				for(long c = 1; c <= maxC; c++) {
					long val = A * Math.abs(r-c) + B * (N - r*c);
					if(val < ans ) ans = val;
				}
			}
			System.out.printf("#%d %d\n", t, ans);
		}
	}
}

