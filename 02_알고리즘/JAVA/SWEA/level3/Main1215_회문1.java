package level3;

import java.util.Scanner;

public class Main1215_회문1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for(int t = 0; t < 10; t ++) {
			int n = sc.nextInt();
			char arr[][] = new char [8][8];
			int cnt = 0;
			for(int i = 0 ; i < arr.length; i++) {
				String temp = sc.next();
				for(int j = 0; j < arr[i].length; j++) {
					arr[i][j] = temp.charAt(j);
				}
			}
			//가로 체크
			for(char a[]: arr) {
				cnt += palindrom(a, n);
			}
			//오른쪽 90도 회전
			arr = rotate(arr);
			
			//다시 가로 체크
			for(char[] a: arr) {
				cnt += palindrom(a, n);
			}
			
			System.out.printf("#%d %d\n", t+1, cnt);
		}
	}

	private static char[][] rotate(char[][] arr) {
		char ret[][] = new char[arr.length][arr.length];
		
		for(int i = 0; i < arr.length; i++) {
			for(int j = 0; j< arr.length; j++) {
				ret[j][arr.length-i-1] = arr[i][j];
			}
		}
		return ret;
	}

	private static int palindrom(char[] a, int n) {
		int ret = 0;
		for(int i = 0; i < a.length - n + 1; i++) {
			boolean flag = true;
			for(int j = 0; j < n/2; j++) {
				if(a[i+j] != a[(i+n-1)-j]) {
					flag = false;
					break;
				}
			}
			if(flag) ret++;
		}
		return ret;
	}

}
