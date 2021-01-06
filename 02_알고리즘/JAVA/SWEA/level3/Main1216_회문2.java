package level3;

import java.util.Scanner;

public class Main1216_회문2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for(int t = 0; t < 10; t ++) {
			int n = sc.nextInt();
			char arr[][] = new char[100][100];
			int maxlen = 1;
			for(int i = 0 ; i < arr.length; i++) {
				String temp = sc.next();
				for(int j = 0; j < arr[i].length; j++) {
					arr[i][j] = temp.charAt(j);
				}
			}
			//가로 중 가장 긴 길이 구하기
			for(char a[]: arr){
				maxlen = Math.max(maxlen , maxLength(a));
			}
			//90도 회전: 세로 구하기위해서
			arr = rotate(arr);
			
			//회전한 배열의 가로(=구하고자하는 배열의 세로) 중 가장 긴 길이를 구함
			for(char a[]: arr){
				maxlen = Math.max(maxlen , maxLength(a));
			}
			
			System.out.printf("#%d %d\n",t+1, maxlen);
		}
	}
	//1차원 배열 중, 가장 긴 길이의 회문 찾아서, 해당 길이 반환
	private static int maxLength(char[] a) {
		int ret = 1;
		for(int i = 0; i < a.length-1; i++) {
			for(int j = a.length-1; j>i; j--) {
				if(isPalindrom(i, j, a)) {
					if(ret < j - i + 1) {
						ret = j - i + 1;
					}
					break;
				};
			}
		}
		return ret;
	}
	//회문 유무 체크
	private static boolean isPalindrom(int s, int e, char[] a) {
		int j = 0;
		for(int i = s; i <= (s+e)/2; i++) {
			if(a[i]!= a[e-j]) return false;
			j++;
		}
		return true;
	}
	//90도 회전
	private static char[][] rotate(char[][] arr) {
		char ret[][] = new char[arr.length][arr.length];
		
		for(int i = 0; i < arr.length; i++) {
			for(int j = 0; j< arr.length; j++) {
				ret[j][arr.length-i-1] = arr[i][j];
			}
		}
		return ret;
	}
}
