package level3;

import java.util.Scanner;

public class Main1220_Magnetic {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for(int t = 0; t < 10; t++) {
			int n = sc.nextInt();
			int[][] arr = new int[n][n];
			int total = 0;
			
			for(int i = 0; i < n; i ++) {
				for(int j = 0; j < n; j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			
			for(int i = 0; i < n ; i ++) {
				boolean flagN = false;
				for(int j = 0; j <n ; j++) {
					if(arr[j][i] == 1) {
						flagN = true;
					}
					if(flagN &&arr[j][i] == 2) {
						total++;
						flagN = false; 
						
					}
				}
			}
			
			System.out.printf("#%d %d\n", t+1, total);
		}
		
	}
}
