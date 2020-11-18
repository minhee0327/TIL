package day06_string;

import java.util.Scanner;

public class Main1152 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String sentance = sc.nextLine().trim();
		String arr[] = sentance.split(" ");
		
		if(sentance.isEmpty()) {
			System.out.println(0);
		}else {
			System.out.println(arr.length);
		}
	}
}

//구현방향
		//내가.. 어렵게 이해한듯;
		//여러번 같은단어가 나와도, 등장 횟수만큼 cnt..ㅎ
		//주의: 문자열 비어있는 경우 0
