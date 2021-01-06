package level3;

import java.util.Scanner;

public class Main1209_sum {
	public static int max;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for(int t = 0; t < 10; t ++) {
			int n = sc.nextInt();
			int arr[][] = new int[100][100];
			max = Integer.MIN_VALUE;
			//입력
			for(int i = 0; i < arr.length; i++) {
				for(int j = 0; j <arr[i].length; j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			
			diagonally(arr);
			findGaro(arr);
			findSero(arr);

			
			System.out.printf("#%d %d\n", t+1, max);
		}
	}
	private static void diagonally(int[][] arr) {
		int ul =0, dr= 0;
		for(int i = 0; i < arr.length; i++) {
			ul += arr[arr.length-i-1][i];
			dr += arr[i][i];
		}
		max = Math.max(max, Math.max(ul, dr));
	}
	
	private static void findGaro(int[][] arr) {
		for(int i = 0; i < arr.length; i++) {
			int sum = 0;
			for(int j = 0 ; j < arr[i].length; j++) {
				sum += arr[i][j];
			}
			max = Math.max(max, sum);
		}
	}
	
	private static void findSero(int[][] arr) {
		for(int i = 0; i < arr.length; i++) {
			int sum = 0;
			for(int j = 0 ; j < arr[i].length; j++) {
				sum += arr[j][i];
			}
			max = Math.max(max, sum);
		}
	}

}
