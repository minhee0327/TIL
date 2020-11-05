package chapter04;

public class ch03_break {

	public static void main(String[] args) {
		int sum = 0;
		int num;

//		sum 105, num 15
		for (num = 1; sum <= 100; num++) {
			sum += num;
		}
		
		
//		for(num = 1; ; num++) {
//			sum += num;
//			if(sum >= 100) break;
//		}
		
//		sum 105 , num 14
		System.out.println(sum + " "+ num);
	}
}
