package level2;

import java.util.Scanner;

public class Main1989_초심자의회문검사 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int tc = sc.nextInt();
		
		for(int t = 1; t <= tc; t++) {
			String temp = sc.next();
			boolean flag = false;
			for(int i = 0; i < temp.length()/ 2; i++) {
				if(temp.charAt(i) != temp.charAt(temp.length()-i-1)) {
					System.out.printf("#%d %d%n", t, 0);
					flag = true;
					break;
				}
			}
			if(!flag) {
				System.out.printf("#%d %d%n", t, 1);
			}
		}
		
		sc.close();
	}

}
