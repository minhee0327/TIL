package level3;

import java.util.Scanner;

public class Main2806_NQueen {
	public static int[] visitedCol;
	public static int cnt;
	
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int t = 1; t <= T; t++) {
			int N = sc.nextInt();
			visitedCol = new int[N];
			cnt = 0;
			
			dfs(N,0);
			
			System.out.printf("#%d %d \n", t, cnt);
			
		}
	}

	private static void dfs(int n, int currentRow) {
		if(currentRow == n) {
			cnt ++;
			return;
		}
		
		for(int col = 0; col < n; col++) {
			boolean isAvailable = true;
			
			for(int row = 0; row< currentRow; row++) {
				if(col == visitedCol[row] 
				    || col == visitedCol[row] - (currentRow - row) 
					|| col == visitedCol[row] + (currentRow - row)) {
					isAvailable = false;
				}
			}
			
			if(isAvailable) {
				visitedCol[currentRow] = col;
				dfs(n, currentRow +1);
			}
		}
		
	}
}
