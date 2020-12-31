package level2;

import java.util.Scanner;

public class Main1926_간단한369 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		for(int i = 1; i<= n; i++) {
			System.out.print(checkNum(Integer.toString(i)) + " ");
		}
	}
	
	public static String checkNum(String n) {
		int cnt = 0;
		
		for(int i = 0; i< n.length(); i++) {
			char ch = n.charAt(i);
			if(ch =='3' || ch =='6' || ch =='9') {
				cnt ++;
			}
		}
		
		if(cnt == 0) {
			return n;
		}else {
			String res = "";
			for(int i = 0; i< cnt ; i++) {
				res += "-";
			}
			return res;
		}
	}
}
