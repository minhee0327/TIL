package level3;

import java.util.Scanner;

public class Main1289_원재의메모리복구 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int t = 1; t<=T; t++) {
			String memory = sc.next();
			char pivot = '0';
			int cnt = 0;
			
			for(int i = 0; i < memory.length(); i++) {
				if(pivot != memory.charAt(i)) {
					cnt ++;
					pivot = (pivot == '0')? '1': '0'; 
				}
			}
			System.out.printf("#%d %d\n", t, cnt);
		}
	}

}
