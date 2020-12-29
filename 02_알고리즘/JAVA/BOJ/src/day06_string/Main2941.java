package day06_string;

import java.util.Scanner;

public class Main2941 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next();
		String croatia[] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
		
		for (int i = 0; i < croatia.length; i++) {
			s = s.replace(croatia[i], "a");
		}
		System.out.println(s.length());
	}
}
