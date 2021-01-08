package level3;

import java.util.ArrayList;
import java.util.Scanner;

public class Main1234_비밀번호 {

	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		
		for(int t = 0; t < 10; t++) {
			int n = sc.nextInt();
			char[] str = sc.next().toCharArray();
			ArrayList<Character> list = new ArrayList<Character> ();
			for(int i = 0; i<n;i++) {
				list.add(str[i]);
			}
			int start = 0, end = 1;
			
			while(end < list.size()) {
				if(list.get(start)==list.get(end)) {
					list.remove(end);
					list.remove(start);
					start--;
					end = start+1;
				}else {
					start++;
					end++;
				}
				if(start <0) {
					start++;
					end = start+1;
				}
			}
			String result = "";
			for(char c: list) {
				result+=c;
			}
			
			System.out.printf("#%d %s\n", t+1, result);
		}
	}

}
