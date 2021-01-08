package level3;

import java.util.Arrays;
import java.util.Scanner;

public class Main1221_GNS {
	public static String strArr[] = {"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int tc = sc.nextInt();
		
		for(int t = 0; t < tc; t++) {
			String T = sc.next();
			int n = sc.nextInt();
			int count[] = new int[strArr.length];
			
			for(int i = 0 ; i <n; i++) {
				String num = sc.next();
				int idx = Arrays.asList(strArr).indexOf(num);
				count[idx]++;
			}
			
			System.out.println(T);
			for(int i = 0; i < strArr.length; i++) {
				for(int j = 0; j < count[i]; j++) {
					System.out.print(strArr[i] +" ");
				}
			}
		}
	}

}
