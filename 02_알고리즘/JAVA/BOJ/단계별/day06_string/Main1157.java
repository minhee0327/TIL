package day06_string;

import java.util.Scanner;

public class Main1157 {

	public static void main(String[] args) {
		/* 내가 풀고자하는 방향
		 * 1. 알파벳 단어는 총 26개로 제한된 값 => 배열로 접근하는게 조금 더 나을 것 같음.
		 * 2. string으로 입력을 받고 => 대문자/소문자 중 하나로 통일 => ascii로 각 자리에 cnt를 증가
		 * 3. cnt의 최대값과 일치하는게 2개 이상일 경우 ?출력 하고 아니면 그 위치의 문자 출력 
		 * */
		Scanner sc = new Scanner(System.in);
		
		int cnt[] = new int[26];
		String alphabet = sc.next().toUpperCase();
		int maxCnt = 0;
		char result = '?';
		
		for (int i = 0; i < alphabet.length(); i++) {
			cnt[alphabet.charAt(i)-65]++;
			if(maxCnt < cnt[alphabet.charAt(i)-65]) {
				maxCnt = cnt[alphabet.charAt(i)-65];
				result = alphabet.charAt(i);
			}else if(maxCnt == cnt[alphabet.charAt(i)-65]) {
				result = '?';
			}
		}
		System.out.println(result);
	}
}
