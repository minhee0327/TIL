package level2;

import java.util.Scanner;

public class Main1946_간단한압축풀기 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int t = 0 ; t < T; t++) {
			String list = "";
			int n = sc.nextInt();
			int totalCnt = 0;
			for(int i = 0; i < n; i++) {
				String str = sc.next();
				int num = sc.nextInt();
				
				totalCnt += num;
				while(num>0) {
					list += str;
					num--;
				}
			}
			System.out.printf("#%d%n", t+1);
			for(int i = 0; i < totalCnt/10; i++) {
				System.out.println(list.substring(i * 10, (i+1)* 10));
			}
			System.out.println(list.substring(list.length() - totalCnt%10));
		}
		sc.close();
	}
}
