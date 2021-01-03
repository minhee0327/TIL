package day06_string;

import java.util.Scanner;

public class Main2675_re1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int r = sc.nextInt();
			String s = sc.next();
			
			StringBuffer sb = new StringBuffer();
			
			for (int j = 0; j < s.length(); j++) {
				for (int j2 = 0; j2 < r; j2++) {
					sb.append(s.charAt(j));
				}
			}
			
			System.out.println(sb);
			
		}
		//앞서 풀었던 코드보다 간결하고, 성능(공간, 속도 모두) 측면에서 효율적.
		//극적인 차이는 아니지만 .. 앞으로 stringbuffer를 떠올리면 좋겠다.
	}

}
