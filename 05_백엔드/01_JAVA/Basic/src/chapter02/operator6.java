package chapter02;

public class operator6 {

	public static void main(String[] args) {
//		bit 연산
		int num1 = 0B00001010; // 10
		int num2 = 0B00000101; // 5
		
		System.out.println(num1 & num2); //1
		System.out.println(num1 | num2); //0
		System.out.println(num1 ^ num2); //0
		System.out.println(num2 << 1);   //10 (*2)
		System.out.println(num2 >> 1);   //2  ( /20)
	}
}
