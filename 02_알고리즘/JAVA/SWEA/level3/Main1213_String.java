package level3;

import java.util.Scanner;

public class Main1213_String {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for(int t = 0; t < 10 ; t++) {
			int tc = sc.nextInt();
			String findWord = sc.next();
			String str = sc.next();
			
			int sum = 0;
			for(int i = 0 ; i < str.length()- findWord.length() +1; i++) {
				String temp = str.substring(i, i + findWord.length());
				sum += (temp.equals(findWord)? 1: 0) ;
			}
			
			System.out.printf("#%d %d%n", t+1, sum);
		}
	}
}
