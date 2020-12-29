package day06_string;

import java.util.Scanner;

public class Main2675 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int r = sc.nextInt();
			String s = sc.next();
			
			char[] temp = new char[r * s.length()];
			
			for (int j = 0; j < s.length(); j++) {
				for (int j2 = 0; j2 < r; j2++) {
					temp[j*r+j2] = s.charAt(j);
				}
			}
			
			String result = String.valueOf(temp);
			System.out.println(result);
			
		}
		//고민했던 것.
		//1. char 배열로 받아서, 정보를 저장한 후 출력?
		//2. sys로 모두 찍어볼지 => 가장 느릴 것 같음;;(print도 속도가 꽤 걸리는 작업)
		//3. charAt로 안되려나?
		//4. concat()?
		// 결정 => 1번으로 일단 풀어보자. 공간은 많이 잡아도 속도는 조금 나을 거같다..
		// 찾다보니, string buffer로 단어를 계속 이어가는 코드가 썩 예뻐서 한번 더 풀어본다.
	}

}
