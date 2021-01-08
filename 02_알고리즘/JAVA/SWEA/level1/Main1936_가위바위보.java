package level1;

import java.util.Scanner;

public class Main1936_가위바위보 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		char result = (a + 1) % 3 == b ? 'B': 'A';

		System.out.println(result);
	}

}
