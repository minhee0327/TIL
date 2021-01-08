package level2;

import java.util.ArrayList;
import java.util.Scanner;

public class Main1961_숫자배열회전 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int t = 0; t < T ; t++) {
			int n = sc.nextInt();
			int[][] arr = new int[n][n];
			
			for(int i = 0; i < n; i ++) {
				for(int j = 0; j < n; j ++) {
					arr[i][j] = sc.nextInt();
				}
			}
			
			int[][] arr90 = rotate(arr);
			int[][] arr180 = rotate(arr90);
			int[][] arr270 = rotate(arr180);
			
			for(int i = 0; i < n ; i ++) {
				for(int j = 0; j < n; j ++) {
					System.out.print(arr90[i][j]);
				}
				System.out.print(" ");
				for(int j = 0; j < n; j ++) {
					System.out.print(arr180[i][j]);
				}
				System.out.print(" ");
				for(int j = 0; j < n; j ++) {
					System.out.print(arr270[i][j]);
				}
				System.out.println();
			}
			
			
		}
	}



	private static int[][] rotate(int[][] arr) {
		int ret[][] = new int[arr.length][arr.length];
		for(int i = 0; i < arr.length; i++) {
			for(int j = 0; j < arr.length; j++) {
				ret[j][arr.length-i-1] =arr[i][j];
			}
		}
		return ret;
	}

}
