package day04_array;

import java.util.Scanner;

public class Main4344 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int c = sc.nextInt();
		
		for (int i = 0; i < c; i++) {
			int n = sc.nextInt();
			int sum = 0;
			int score[] = new int[n];
			
			for (int j = 0; j < n; j++) {
				int temp = sc.nextInt();
				sum += temp;
				score[j] = temp;
			}
			
			float avg = (float) sum/n;
			int cnt = 0;
			
			for (int j = 0; j < n; j++) {
				if (avg<score[j]) cnt++;
			}
			System.out.printf("%.3f%s\n",(float) cnt/n * 100, "%");
		}
		sc.close();
	}
}
