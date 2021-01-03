package level2;

import java.util.Scanner;

public class Main1948_날짜계산기 {
	public static int[] month = {0,1,2,3,4,5,6,7,8,9,10,11,12};
	public static int[] day = {0,31,28,31,30,31,30,31,31,30,31,30,31};
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int t = 1; t <= T; t++) {
			int firstMonth = sc.nextInt();
			int firstDay = sc.nextInt();
			int secondMonth = sc.nextInt();
			int secondDay = sc.nextInt();
			
			if(firstMonth == secondMonth) {
				System.out.printf("#%d %d%n", t, secondDay - firstDay + 1);
			}else {
				int res = day[firstMonth] - firstDay;
				for(int i = firstMonth +1; i<secondMonth; i++) {
					res += day[i];
				}
				res += secondDay +1;
				System.out.printf("#%d %d%n", t, res);
			}
		
		}
		sc.close();
		
	}
}
