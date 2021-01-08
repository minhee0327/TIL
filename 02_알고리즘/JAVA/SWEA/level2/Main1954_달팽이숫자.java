package level2;

import java.util.Scanner;

public class Main1954_달팽이숫자 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int t = 0; t < T; t++) {
			int n = sc.nextInt();
			int arr[][] = new int[n][n];
			int cnt = n;
			int r = 0, c = -1;
			int num = 0;
			int dir = 1;
			
			while(cnt> 0) {
				for(int i = 0 ; i < cnt; i++) {
					num ++;
					c+=dir;
					arr[r][c] = num;
				}
				cnt -=1;
				for(int i = 0; i <cnt; i++) {
					num ++;
					r+=dir;
					arr[r][c] = num;
				}
				dir *= -1;
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
