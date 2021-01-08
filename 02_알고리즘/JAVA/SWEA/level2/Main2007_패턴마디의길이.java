package level2;

import java.util.Scanner;

public class Main2007_패턴마디의길이 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		
		for(int i = 0; i< t ; i ++ ) {
			String temp = sc.next();
			for(int j = 1; j< 10; j++) {
				String a = temp.substring(0, j);
				String b = temp.substring(j, j *2);
				if(a.equals(b)) {
					System.out.printf("#%d %d%n", i + 1 , j);
					break;
				}
			}
		}
	}
}
