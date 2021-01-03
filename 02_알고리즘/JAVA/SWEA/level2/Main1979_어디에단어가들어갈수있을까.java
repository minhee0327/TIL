package level2;

import java.util.Scanner;

public class Main1979_어디에단어가들어갈수있을까 {
	public static int n;
	public static int k;
	public static int cnt;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int tc = sc.nextInt();

		for (int t = 0; t < tc; t++) {
			n = sc.nextInt();
			k = sc.nextInt();
			int[][] arr = new int[n][n];

			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			
			cnt = 0;
			//가로 방향 count
			counting(arr);
			
			//90도 회전
			int arr90[][] = new int[n][n];
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < n; j++) {
					arr90[j][n-i-1]= arr[i][j];
				}
			}
			
			counting(arr90);
			System.out.printf("#%d %d%n",t+1, cnt);
		}
	}
	
	public static void counting(int arr[][]) {
		for (int i = 0; i < n ; i++) {
			for (int j = 0; j < n ; j++) {
				//0이면 단어 들어갈 수 없음 지나감.
				if(arr[i][j] == 0) {
					continue;
				}
				//왼쪽이 벽이거나, 검은부분 중에
				if(j == 0 || arr[i][j-1] == 0) {
					// 오른끝이 배열 범위 내에 있으면
					if(j+k<=n) {
						//체크 해보기(i,j)시작점, arr배열
						if(checkRow(i,j, arr)) {
							cnt++;
						}
					}
				}
			}
		}
	}
	
	private static boolean checkRow(int i, int j, int [][]arr) {
		boolean flag = true;
		//가로를 확인할 것이기때문에 j~ j+k만큼
		for(int a = j; a<j+k;a++) {
			//0이 있다면 false(불가능) 체크
			if(arr[i][a] == 0) {
				flag = false;
				break;
			}
		}
		//배열 범위에서 오른쪽끝이 1이됬을경우도 불가능
		if(j+k<n) {
			if(arr[i][j+k] == 1) {
				flag = false;
			}
		}
		return flag;
	}
}
