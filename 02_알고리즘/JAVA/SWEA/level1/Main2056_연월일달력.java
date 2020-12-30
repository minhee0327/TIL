package level1;

import java.util.Scanner;

public class Main2056_연월일달력 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		sc.nextLine();
		
		for(int i = 0; i< t; i++) {
			String temp = sc.nextLine();
			
			String year = temp.substring(0, 4);
			String month = temp.substring(4, 6);
			String day = temp.substring(6, 8);
			
			if(isValid(Integer.parseInt(month), Integer.parseInt(day))) {
				System.out.printf("#%d %s/%s/%s%n", i+1, year, month, day);
			}else {
				System.out.printf("#%d %d%n", i+1, -1);
			}
		}
		sc.close();
	}
	
	public static boolean isValid(int month, int day) {
		switch (month) {
		case 1: case 3: case 5: case 7: case 8: case 10: case 12: {
			if( 1<= day && day<=31) {
				return true;
			}
			return false;
		}
		case 9: case 11: case 4: case 6: {
			if( 1<= day && day<=30) {
				return true;
			}
			return false;
		}case 2: {
			if( 1<= day && day <= 28) {
				return true;
			}
			return false;
		}
		default:
			return false;
		}
	}
}
