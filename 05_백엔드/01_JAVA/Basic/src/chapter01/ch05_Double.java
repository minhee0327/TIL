package chapter01;

public class ch05_Double {
	public static void main(String[] args) {
		double dNum = 3.14;
		
		float fNum = 3.14F;
		
		System.out.println(dNum);
		System.out.println(fNum);
		
		
		System.out.println("==================");
		double dNum2 = 1;
		for(int i = 0; i<10000; i++) {
			dNum2 = dNum2 + 0.1;
		}
//		예상: 1001
//		실제: 1001.000000000159 (오차, 부동소수점)
		System.out.println(dNum2);
	
	}
}
