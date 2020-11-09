package chapter05;

public class FunctionTest {

	public static int addNum(int num1, int num2) {
		int result;
		result = num1 + num2;
		return result;
	}
	
	public static void sayHello(String greeting) {
		System.out.println(greeting);
	}
	
	public static int calcSum() {
		int sum = 0;
		
		for (int i = 0; i < 100; i++) {
			sum += i;
		}
		
		return sum;
	}
	
	public static void main(String[] args) {
		int num1 = 10;
		int num2 = 20;
		
		int total = addNum(num1, num2);
			
		sayHello("안녕하세요");
		
		int num = calcSum();
		
		System.out.println(total);
		System.out.println(num);
	}

}
