package level2;

import java.util.Scanner;

public class Main1954_달팽이숫자2 {
	public static int[] dx = {0, 1, 0, -1};
	public static int[] dy = {1, 0, -1, 0};
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int t = 0; t < T ; t++) {
			int n = sc.nextInt();
			int arr[][] = new int[n][n];
			
			int cnt = 1;
			int x = 0, y = 0;
			
			for(int i = n-1; i >= 0 ; i-=2) {
				for(int d = 0 ; d < 4; d++) {
					for(int j = 0 ; j < i; j++) {
						arr[x][y] = cnt;
						cnt ++;
						x = x + dx[d];
						y = y + dy[d];
					}
					if(x == y && d == 3) {
						x++;
						y++;
					}
				}
			}
			
			if(n % 2 != 0) {
				arr[x-1][y-1] = cnt;
			}
			
			System.out.printf("#%d%n", t+1);
			for(int i = 0; i < n ; i++) {
				for(int j = 0; j < n; j ++) {
					System.out.print(arr[i][j]+" ");
				}
				System.out.println();
			}
		}
	}
}
