package chapter01;

public class ch07_ImplicitConversion {

	public static void main(String[] args) {
//		묵시적 형변환: 작은수 => 큰수
		byte bNum = 10;
		int iNum = bNum;
		
		System.out.println(bNum);
		System.out.println(iNum);
		
//		덜 정밀한 수 => 더 정밀한 수
		int iNum2 = 20;
		float fNum = iNum2;
		System.out.println(fNum);
		
//		iNum이 int=> float
//		합의 결과가 float => double
		double dNum;
		dNum = fNum + iNum;
		
		System.out.println(dNum);
	}
}
