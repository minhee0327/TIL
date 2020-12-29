package day04_array;

import java.util.Scanner;

public class Main1546 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int max = Integer.MIN_VALUE;
		double arr[] = new double[n];
		double sum = 0;
		
		for (int i = 0; i < n; i++) {
			int temp = sc.nextInt();
			if (max < temp) {
				max = temp;
			}
			arr[i] = temp;
		}
		
		
		for (int i = 0; i < n; i++) {
			sum += (arr[i]/max * 100);
		}

		System.out.println(sum/n);
		
	}

}
