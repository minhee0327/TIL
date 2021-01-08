package level1;

import java.util.Scanner;

public class Main2050_알파벳을숫자로변환 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String temp = sc.next();
		
		for(int i = 0; i<temp.length(); i++) {
			System.out.print(temp.charAt(i)- 'A' + 1 + " ");
		}
		
		sc.close();
	}

}
