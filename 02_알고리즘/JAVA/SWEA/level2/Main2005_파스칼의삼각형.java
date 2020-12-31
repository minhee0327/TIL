package level2;

import java.util.Scanner;

public class Main2005_파스칼의삼각형 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int tc = sc.nextInt();
		
		for(int t = 0; t < tc; t ++) {
			int n = sc.nextInt();
			int arr[][] = new int[n][n];
			
			arr[0][0] = 1;
			for(int i = 1; i < n; i++) {
				arr[i][0] = 1;
				arr[i][i] = 1;
				for(int j = 1; j< i; j++) {
					arr[i][j] = arr[i-1][j-1] + arr[i-1][j]; 
				}
			}
			System.out.println("#" + (t+1) +" ");
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < i+1; j++) {
					System.out.print(arr[i][j]+" ");
				}
				System.out.println();
			}
		}
		
	}
}
