package level3;

import java.util.Scanner;

public class Main2805_농작물수확하기 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int t = 1; t <= T; t++) {
			int N = sc.nextInt();
			int farm[][] = new int[N][N];
			int value = 0;
			for(int i = 0; i < N; i++) {
				String temp = sc.next();
				for(int j = 0; j < N; j++) {
					farm[i][j] = temp.charAt(j) - '0';
				}
			}
			
			/*
			for(int i = 0; i < N/2; i++) {
				for(int j = N/2 - i ; j <= N/2 +i ; j++) {
					value += farm[i][j];
				}
			}
			
			for(int i = 0; i< N; i++) {
				value += farm[N/2][i];
			}
			
			for(int i = N-1; i>N/2; i--) {
				for(int j = N/2 - (N-i -1); j <= N/2 + (N-i -1);j++) {
					System.out.println(i + " " + j);
					value += farm[i][j];
				}
			}
			*/
			
			for(int i =0; i<N; i++) {
				for(int j = Math.abs(N/2 -i); j< N - Math.abs(N/2 -i); j++) {
					value +=farm[i][j];
				}
			}
			
			System.out.printf("#%d %d\n", t, value);
		}
	}

}
