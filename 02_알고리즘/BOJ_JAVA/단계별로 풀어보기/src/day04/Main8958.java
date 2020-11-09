package day04;

import java.util.Scanner;

public class Main8958 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		for (int i = 0; i < n; i++) {
			char OX[] = sc.next().toCharArray();
			int score = 0;
			int sum = 0;
			
			for (int j = 0; j < OX.length; j++) {
				if (OX[j] == 'O') {
					score+=1;
				}else {
					score = 0;
				}
				sum += score;
			}
			System.out.println(sum);
		}
	}
}
