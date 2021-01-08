package level3;

import java.util.ArrayList;
import java.util.Scanner;

public class Main1225_암호생성기 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		for(int t = 0; t < 10 ; t++) {
			int tc = sc.nextInt();
			ArrayList <Integer> list = new ArrayList<Integer>();
			for(int i = 0; i < 8 ; i++) {
				
				list.add(sc.nextInt());
			}
			outer: while(true) {
				for(int i = 1; i <= 5; i++) {
					int nxtNum = list.get(0) - i;
					if(nxtNum <=0) {
						list.add(0);
						list.remove(0);
						break outer;
					}else {
						list.add(nxtNum);
						list.remove(0);
					}
				}
			}
			
			System.out.printf("#%d ", tc);
			for(int i : list) {
				System.out.print(i +" ");
			}
			System.out.println();
		}
	
	}

}
