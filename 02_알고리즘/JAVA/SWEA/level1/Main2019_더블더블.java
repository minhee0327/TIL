package level1;

import java.util.Scanner;

public class Main2019_더블더블 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int res = 1;
		
		while(n >= 0) {
			System.out.print(res + " ");
			res *= 2;
			n --;
		}
	}
}
