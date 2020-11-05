package chapter04;

public class ch02_GuGudanWhile {

	public static void main(String[] args) {
//		구구단
		int dan = 2;
		
		while (dan<10) {
			System.out.println(dan + "단");
			int count = 1;
			while(count < 10) {
				System.out.printf("%d X %d = %d\n", dan, count, dan* count);
				count++;
			}
			dan++;
		}
	}
}
