package day06_string;

import java.util.Scanner;

public class Main2908 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String a = sc.next();
		String b = sc.next();
		
		for (int i = 2; i >= 0; i--) {
			if(a.charAt(i) == b.charAt(i)) {
				continue;
			}else if (a.charAt(i)> b.charAt(i)) {
				System.out.println(reverseWords(a));
				break;
			}else if (a.charAt(i)< b.charAt(i)) {
				System.out.println(reverseWords(b));
				break;
			}
		}
	}

	private static StringBuffer reverseWords(String a) {
		StringBuffer sb = new StringBuffer();
		for (int i = a.length()-1; i >=0; i--) {
			sb.append(a.charAt(i));
		}
		return sb;
	}
}
