package level2;

import java.util.Scanner;

public class Main1974_스도쿠검증 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int t = 0 ; t < T; t++) {
			int arr[][] = new int[9][9];
			for(int i = 0; i < 9 ; i++) {
				for(int j = 0 ; j < 9; j++) {
					arr[i][j] = sc.nextInt();
				}
			}
		
			if (!checkRow(arr)) {
				System.out.printf("#%d %d%n", t+1, 0);
			}else if (!checkCol(arr)) {
				System.out.printf("#%d %d%n", t+1, 0);
			}else if(!checkRound(arr)) {
				System.out.printf("#%d %d%n", t+1, 0);
			}else {
				System.out.printf("#%d %d%n", t+1, 1);
			}
		}
		
	}
	
	private static boolean checkRound(int[][] arr) {
		for(int i = 0; i <= 6; i+=3) {
			for(int j = 0; j <= 6; j+=3) {
				boolean[] check = new boolean[9];
				for(int k = i; k <i+3; k++) {
					for(int l =j ; l <j+3; l++) {
						if(check[arr[k][l]-1]) {
							return false;
						}else {
							check[arr[k][l]-1] = true;
						}
					}
				}
			}
		}
		return true;
	}

	private static boolean checkRow(int[][] arr) {
		for(int i = 0; i < arr.length; i++) {
			boolean[] check = new boolean[9];
			for(int j = 0; j < arr[i].length ; j++) {
				if(check[arr[i][j]-1]) {
					return false;
				}else {
					check[arr[i][j]-1] = true;
				}
			}
		}
		return true;
	}
	private static boolean checkCol(int[][] arr) {
		for(int i = 0; i < arr.length; i++) {
			boolean[] check = new boolean[9];
			for(int j = 0; j < arr[i].length ; j++) {
				if(check[arr[j][i]-1]) {
					return false;
				}else {
					check[arr[j][i]-1] = true;
				}
			}
		}
		return true;
	}
}
