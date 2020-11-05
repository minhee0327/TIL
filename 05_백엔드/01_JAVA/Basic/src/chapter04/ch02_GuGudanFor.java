package chapter04;

public class ch02_GuGudanFor {

	public static void main(String[] args) {
//		구구단
		for (int i = 2; i < 10; i++) {
			System.out.println(i + "단");
			for (int j = 1; j < 10; j++) {
				System.out.printf("%d X %d = %d\n", i, j, i*j);
			}
		}
	}
}
