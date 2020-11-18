package chapter09_배열;

public class Example01 {

	public static void main(String[] args) {
		//생성 및 초기화
		int [] arr = new int [] {1,2,3};
		int [] arr2 = {1,2,3};
		
		//배열 선언만
		int [] arr3 = new int[10];
		int total = 0;
		
		for (int i = 0 , num = 1; i < arr3.length; i++ , num ++) {
			arr3[i] = num;
		}
		
		for (int i = 0 , num = 1; i < arr3.length; i++ , num ++) {
			total += arr3[i];
		}
		System.out.println(total);
		
		
		
		//주의
		double [] dArr = new double[5];
		int count = 0; 
		dArr[0] = 1.1;count++;
		dArr[1] = 2.1;count++;
		dArr[2] = 3.1;count++;
		double mTotal = 1;
		
		for (int i = 0; i < count; i++) {
			mTotal *= dArr[i];
		}
		
		//배열에 초기화는 0이기 때문에, 길이 잘 고려하여 계산.
		System.out.println(mTotal);
		
		
	}
}
