package level3;

import java.util.Scanner;

public class Main1206_view {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for(int t = 0 ; t < 10; t ++) {
			int n = sc.nextInt();
			int[] building = new int[n];
			for(int i = 0 ; i < n ; i++) {
				building[i] = sc.nextInt();
			}
			
			int sum = 0;
			for(int i = 2; i < n-2; i++) {
				int max = max(building[i-2], building[i-1], building[i+1], building[i+2]);
				if(max < building[i]) sum += (building[i]- max);
			}
			
			System.out.printf("#%d %d%n", t+1,sum);
			
		}
	}

	private static int max(Integer ...integers) {
		int max = 0;
		for(int i : integers) {
			if(i > max) {
				max = i;
			}
		}
		return max;
	}

}
