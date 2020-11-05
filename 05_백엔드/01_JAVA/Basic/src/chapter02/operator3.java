package chapter02;

public class operator3 {

	public static void main(String[] args) {
//		단락 회로 평가(short circuit evaluation)
//		&&(논리곱) => 앞의 항이 false면 뒤의 항 판단 하지 않아도, false
//		앞의 항이 false면 뒤의 항 판단 X. 변화 X
		
		int num1 = 10;
		int i = 2;
		boolean value = ((num1 = num1 + 10) < 10 && ((i = i+2) <10) );
		
		System.out.println(num1); 	//20
		System.out.println(i);		//2
		System.out.println(value);
		
		System.out.println("-----------------");
//		||(논리합) => 앞의 항이 true이면 뒤의 항 판단하지 않아도, true
		int num2 = 10;
		int i2 = 2;
		boolean value2 = ((num2 +=10) > 10 || ((i2+=2) <10));
		
		System.out.println(num2);		//20
		System.out.println(i2);			//2
		System.out.println(value2);		//true
		
		
	}
}
