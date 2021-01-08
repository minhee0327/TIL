package level2;

import java.util.Scanner;

public class Main2001_파리퇴치 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int tc = sc.nextInt();
		for(int t = 1; t<= tc; t++) {
			
			int n = sc.nextInt();
			int m = sc.nextInt();
			
			int[][] arr = new int[n][n];
			
			for(int i = 0 ; i < n; i ++ ) {
				for(int j = 0; j < n ; j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			
			int max = Integer.MIN_VALUE;
			
			for(int i = 0 ; i<= n - m  ; i ++) {
				for(int j = 0; j<= n- m ; j ++) {
					int tempArea = fari(i, j, m, arr);
					if(tempArea> max) {
						max = tempArea;
					}
				}
			}
			System.out.printf("#%d %d%n", t, max);
		}
		
	}
	public static int fari(int r, int c, int m, int[][] arr) {
		int sum = 0;
		for(int i = r; i< r + m; i++) {
			for(int j = c ; j <c + m ; j++) {
				sum += arr[i][j];
			}
		}
		
		return sum;
	}
}
