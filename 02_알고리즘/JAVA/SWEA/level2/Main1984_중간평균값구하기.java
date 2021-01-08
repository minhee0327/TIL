package level2;

import java.util.Arrays;
import java.util.Scanner;

public class Main1984_중간평균값구하기 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int tc = sc.nextInt();
		
		
		for(int t = 1; t <= tc; t++) {
			int arr[]  = new int[10];
			for(int i = 0; i < 10 ; i ++) {
				arr[i] = sc.nextInt();
			}
			Arrays.sort(arr);
			int sum = 0;
			for(int i = 1; i < 9; i ++) {
				sum += arr[i];
			}
			System.out.printf("#%d %d%n", t, Math.round(sum/8.0));
		}
	}
}
