package day04_array;

import java.util.Scanner;

public class Main8958 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
//		toCharArray로 배열을 받아서도 풀었었고
//		string배열로 받아서, equals함수로 string비교로 풀기도 해보고
//		string배열로 받은것을 char로 받았는데 이 3가지 경우 중에서는 toCharArray가 가장 효율적이었다.
		int n = sc.nextInt();
		
		for (int i = 0; i < n; i++) {
			char OX[] = sc.next().toCharArray();
			int score = 0;
			int sum = 0;
			
			for (int j = 0; j < OX.length; j++) {
				if (OX[j] == 'O') {
					score+=1;
				}else {
					score = 0;
				}
				sum += score;
			}
			System.out.println(sum);
		}
	}
}
