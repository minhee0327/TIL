package day04_array;

import java.util.Scanner;

public class Main2577 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int total = a* b* c;
		
		int[] arr = new int[10];
		
		while (total> 0) {
			arr[total%10]++;
			total/=10;
		}
		for (int i = 0; i < arr.length; i++) {
			System.out.println(arr[i]);
		}
	}
}
