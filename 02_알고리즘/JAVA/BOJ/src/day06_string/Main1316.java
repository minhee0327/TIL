package day06_string;

import java.util.Scanner;

public class Main1316 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int cnt = 0;
		
		for (int i = 0; i < n; i++) {
			cnt += isGroupWords(sc.next());
		}
		
		System.out.println(cnt);
	}

	private static int isGroupWords(String s) {
		boolean visited[] = new boolean[26];
		char prev = ' ';
		
		for (int i = 0; i < s.length(); i++) {
			char nxt = s.charAt(i);
			if (prev == nxt) {
				continue;
			}else {
				if (visited[nxt- 97]) {
					return 0;
				}else {
					visited[nxt- 97] = true;
					prev = nxt;
				}
			}
		}
		return 1;
	}
}
