package level2;

import java.util.Scanner;

public class Main1288_새로운불면증치료법 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int t = 0; t < T; t++) {
			int n = sc.nextInt();
			int cnt = 1;
			boolean[] number = new boolean[10];
			
			while(isAllNumber(n * cnt, number)) {
				cnt++;
			}
			
			System.out.printf("#%d %d%n", t+1, cnt * n);
		}
	}

	private static boolean isAllNumber(int num, boolean[] arr) {
		while(num > 0) {
			arr[num%10] = true;
			num/=10;
		}
		for(int i = 0; i < arr.length; i++) {
			if(arr[i] == false) return true;
		}
		return false;
	}
}
