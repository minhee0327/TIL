package chapter01;

public class ch08_ExplicitConversion {
	public static void main(String[] args) {
//		명시적 형변환(ExplicitConversion)
//		data의 유실이 있을 수 있음 (프로그래머가 알고 있다는 가정하에 진행)
//		변환되는 자료형 명시
		
		int i = 1000;
		byte bNum = (byte) i;
		
		System.out.println(bNum);
		
//		소수점 이하 부분이 잘린다.
		double dNum1 = 1.2;
		float fNum1 = 0.9F;
		
		int iNum1 = (int)dNum1 + (int)fNum1; // 형변환 후 계산 (1 + 0) => 1 
		int iNum2 = (int)(dNum1 + fNum1); 	 // 계산 후 형변환 (2.1) => 2
		
		System.out.println(iNum1);
		System.out.println(iNum2);
	}
}
