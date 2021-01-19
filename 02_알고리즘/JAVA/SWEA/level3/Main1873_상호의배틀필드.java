package level3;

import java.util.Arrays;
import java.util.Scanner;

public class Main1873_상호의배틀필드 {

	public static String doing[] = { "U", "D", "L", "R", "S" };
	public static String look[] = { "^", "v", "<", ">" };
	public static int dir[][] = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 }, { 0, 0 } };
	public static String field[] = { ".", "*", "#", "-" };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int t = 1; t <= T; t++) {
			int H = sc.nextInt();
			int W = sc.nextInt();
			char Map[][] = new char [H][W];
			int position[] = {0, 0, 0};
			
			//filed입력받으면서 시작점을 찾아서, 좌표와 방향을 가리키는 idx를 저장한다.
			for(int i = 0; i < H; i++) {
				String temp = sc.next();
				for(int j = 0; j < W; j++) {
					Map[i][j] = temp.charAt(j);
					int idx = Arrays.asList(look).indexOf(String.valueOf(Map[i][j]));
					System.out.println(i+" " + j + Map[i][j]+" "+ idx);
					if(idx >= 0) {
						position[0] = i;
						position[1] = j;
						position[2]	= idx;
						Map[i][j] = '.';
					}
				}
			}
			System.out.println(position[0]+" " + position[1]);
			int N = sc.nextInt();
			String instruction = sc.next();
			for(int i = 0; i < instruction.length(); i++) {
				int currentIdx = Arrays.asList(doing).indexOf(String.valueOf(instruction.charAt(i)));;
				System.out.println(currentIdx);
				//currentIdx <4의 경우 U~R, 아니면 S
				if (currentIdx < 4) {
					position[2] = currentIdx;
					int nx = position[0] + dir[position[2]][0];
					int ny = position[1] + dir[position[2]][1];
					if(0<=nx && nx<H && 0<=ny && ny<W && Map[nx][ny]=='.') {
						position[0] = nx;
						position[1] = ny;
					}
				}else {
					int nx = position[0];
					int ny = position[1];
					while(true) {
						nx = nx + dir[position[2]][0];
						ny = ny + dir[position[2]][1];
						if(0<=nx && nx<H && 0<=ny && ny<W) {
							if(Map[nx][ny] == '*') {
								Map[nx][ny] = '.';
								break;
							}else if(Map[nx][ny]=='#') {
								break;
							}
						}else {
							break;
						}
					}
				}
			
			}
			
			Map[position[0]][position[1]] = look[position[2]].charAt(0);
			System.out.printf("#%d ", t);
			for(int i = 0; i < H; i++) {
				for(int j = 0; j < W; j++) {
					System.out.print(Map[i][j]);
				}
				System.out.println();
			}
		}
	}
}

/*
 * 수정에 수정에 수정을 거쳐 통과한 문제 !! ㅠㅠ 전체적인 흐름은 잘 잡고 구현했으나, 중간중간 조금씩 생각을 놓친 부분이 있었다.
 * 
 * 1. 처음에 어디있는지 찾을때, idx값이 0보다 크거나 같은 경우로 찾았어야했는데, 0보다 큰으로 계산해서 몇몇 TC가 통과를 못했었다.
 * 2. type (char, string, 그리고 문자 주어진건 문제에서 복사해서 쓰자.. 내가 쓰다가 틀릴수있음.) 3. shoot할때
 * nx, ny구할때 잘못구했었음. 반목문 밖에서 현 위치를 정의하고, 반복문 내부에서 계속 변경해갔어야했음...ㅠㅠ 4. 평지였을 경우 한번
 * shoot한 후에는 break;걸었어야하는데 안걸어서 또 무한 반복문 걸림;;
 * 
 * 
 */
