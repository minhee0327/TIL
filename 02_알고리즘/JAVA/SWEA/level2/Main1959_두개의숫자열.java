package level2;

import java.util.Scanner;

public class Main1959_두개의숫자열 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int t = 0; t < T; t++) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			
			int firstArr[] = new int [n];
			int secondArr[] = new int [m];
			
			for(int i = 0; i < n; i++) {
				firstArr[i] = sc.nextInt();
			}
			for(int i = 0; i < m; i++) {
				secondArr[i] = sc.nextInt();
			}
			
			int result = 0;
			
			if(firstArr.length > secondArr.length) {
				result = findMax(firstArr, secondArr);
			}else {
				result = findMax(secondArr, firstArr);
			}
			
			System.out.printf("#%d %d%n", t+1, result);
		}
	}

	private static int findMax(int[] a, int[] b) {
		int max = Integer.MIN_VALUE;
		for(int i = 0; i <= a.length -b.length; i++) {
			int sum = 0;
			for(int j = 0; j < b.length; j++) {
				sum += b[j] * a[i+j];
			}
			if(max < sum) max = sum;
		}
		return max;
	}
}
