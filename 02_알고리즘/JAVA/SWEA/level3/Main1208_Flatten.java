package level3;

import java.util.Arrays;
import java.util.Scanner;

public class Main1208_Flatten {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
	
		for(int t = 0 ; t < 10; t ++) {
			int n = sc.nextInt();
			int heights[] = new int[100]; 
			for(int i = 0; i < 100; i++) {
				heights[i] = sc.nextInt();
			}
			for(int i = 0; i < n; i++) {
				Arrays.sort(heights);
				heights[0]++;
				heights[99]--;
			}
			Arrays.sort(heights);
			System.out.printf("#%d %d%n", t+1, heights[99] - heights[0]);
		}
	}

}
