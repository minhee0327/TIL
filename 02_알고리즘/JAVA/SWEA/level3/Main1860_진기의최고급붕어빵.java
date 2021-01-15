package level3;

import java.util.Scanner;

public class Main1860_진기의최고급붕어빵 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int t = 1; t <= T; t++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			int K = sc.nextInt();
			int cnt = 0;
			boolean flag = true;
			int[] time = new int[101];
			
			for(int i = 0; i < N; i++) {
				time[sc.nextInt()] ++;
			}

			for(int i = 0; i< 100 ; i++) {
				if(i % M == 0 && i>0) cnt ++;
				if(cnt > 0 && time[i]> 0) {
					if(cnt >= time[i]) {
						cnt -= time[i];
					}else {
						flag = false;
						break;
					}
				}else if (cnt <= 0 && time[i]> 0) {
					flag = false;
					break;
				}
			}
			
			if(flag) {
				System.out.printf("#%d %s\n", t, "Possible");
			}else {
				System.out.printf("#%d %s\n", t, "Impossible");
			}
		}
	}
}
