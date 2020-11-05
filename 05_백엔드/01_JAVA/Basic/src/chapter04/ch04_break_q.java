package chapter04;

public class ch04_break_q {
	public static void main(String[] args) {
//		문제: 구구단 출력 짝수단만 출력 + 단보다 곱하는 수가 작거나 같을 때까지만 출력
		
		for (int i = 2; i < 10; i++) {
			if (i %2 != 0) continue; 
			for (int j = 1; j < 10; j++) {
				if (i < j) break;
				System.out.printf("%d X %d = %d\n", i, j, i*j);
			}
			System.out.println();
		}
	}
}
