package chapter01;

public class ch02_integer {
	public static void main(String[] args) {
		byte bs = -128;
		System.out.println(bs);
		
//		Error: byte only (-128 ~ 127)
//		bs = 128;
		System.out.println(bs);
		
//		Error: int 범위 넣어감
//		int iVal = 12345678900;
		
//		숫자를 Long타입으로 사용하고 싶을때 마지막에 'L' 붙여줄 수 있다.
		long lVal = 12345678900L;
		long lVal2 = 100;
	}
}
