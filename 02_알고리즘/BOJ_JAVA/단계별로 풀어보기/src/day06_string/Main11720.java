package day06_string;

import java.util.Scanner;

public class Main11720 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		//1. java, int 크기를 넘어간 값이 들어와서 error => 수정..(문자열로 해결해야할듯) 
		//2. 문자열 입력을 받은 후, => char타입으로 변환(charAt) => int타입으로 변환 '0' 붙여줌 
		//3. type casting에 익숙해질 필요가 있음.. (js, python써왔다보니 타입을 사용하는데 불편함이 있음;;)
		int n = sc.nextInt();
		String num = sc.next();
		int result = 0;
		
		while(n>0) {
			result += num.charAt(n-1) - '0';
			n--;
		}
		
		System.out.println(result);
	}

}
