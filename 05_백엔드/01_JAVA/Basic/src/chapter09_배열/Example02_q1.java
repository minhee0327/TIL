package chapter09_배열;

public class Example02_q1 {

	public static void main(String[] args) {
		//대문자 A~Z까지 배열에 저장하고 다시 출력하는 프로그램
		char [] alpha = new char[26];
		char ch = 'A';
		
		for (int i = 0; i < alpha.length; i++) {
//			alpha[i] = (char) (65 +i);
			alpha[i] = ch++;
		}
		for (int i = 0; i < alpha.length; i++) {
			System.out.println(alpha[i] + " | " + (int)alpha[i]);
		}
	}
}
