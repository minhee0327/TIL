package chapter01;

public class ch04_CharTest {

	public static void main(String[] args) {
		char ch = 'A';
		System.out.println(ch);
		System.out.println((int)ch);
		
		int iCh = 66;
		System.out.println(iCh);
		System.out.println((char)iCh);
		
//		Error: 음수 사용 불가
//		char ch2 = -66;
		
		char hangul = '\uAC00';
		System.out.println(hangul);
		
		char ch3 = '한';
		System.out.println(ch3);
	}

}
