package level1;

import java.util.Scanner;

public class Main2043_서랍의비밀번호 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int p = sc.nextInt();
		int k = sc.nextInt();
		
		System.out.println(p - k + 1);
		
		sc.close();
	}
}
