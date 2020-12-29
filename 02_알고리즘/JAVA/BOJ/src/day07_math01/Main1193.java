package day07_math01;

import java.util.Scanner;

public class Main1193 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int x = sc.nextInt();
		
		int cross_cnt = 1;
		int sum = 0;
		
		while(true) {
			if(x <= sum + cross_cnt) {
				// 홀수인경우, 우측위로 증가
				if (cross_cnt % 2 == 1) {
					System.out.println((cross_cnt - (x-sum -1)) + "/"+ (x - sum));
					break;
				}else {
					System.out.println((x - sum) + "/"+ (cross_cnt - (x-sum -1)));
					break;
				}
			}else {
				sum += cross_cnt;
				cross_cnt++;
			}
		}
	}
}
//1차
//우측위로, 좌측하단으로 나뉘는걸 고려 하지 않아서 틀렸었음.

//2차
//고려해서 다시 돌려보기