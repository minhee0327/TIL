package day06_string;

import java.util.Scanner;

public class Main5622 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next();
		int result = 0;
		
		for (int i = 0; i < s.length(); i++) {
			result+= (changeNum(s.charAt(i)) + 1);
		}
		
		System.out.println(result);
	}

	private static int changeNum(char c) {
		if (c-65>=0 && c-65<3) {
			return 2;
		}else if (c-65>=3 && c-65<6) {
			return 3;
		}else if (c-65>=6 && c-65<9) {
			return 4;
		}else if (c-65>=9 && c-65<12) {
			return 5;
		}else if (c-65>=12 && c-65<15) {
			return 6;
		}else if (c-65>=15 && c-65<19) {
			return 7;
		}else if (c-65>=19 && c-65<22) {
			return 8;
		}else if (c-65>=22 && c-65<=25) {
			return 9;
		}else {
			return 0;
		}
	}

}
