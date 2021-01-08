package level3;

import java.util.ArrayList;
import java.util.Scanner;

public class Main1228_암호문2 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		for(int t = 0; t < 10; t++) {
			int n = sc.nextInt();
			ArrayList <Integer> arrlist = new ArrayList<Integer>();
			
			for(int i = 0; i < n; i++) {
				arrlist.add(sc.nextInt());
			}
			
			int m = sc.nextInt();
			for(int i = 0; i< m; i++) {
				char instuction = sc.next().charAt(0);
				if(instuction=='I') {
					int x = sc.nextInt();
					int y = sc.nextInt();
					for(int j = 0; j < y; j++) {
						arrlist.add(x+j, sc.nextInt());
					}
				}else if(instuction=='D') {
					int x = sc.nextInt();
					int y = sc.nextInt();
					for(int j = 0; j < y ;j ++) {
						arrlist.remove(x);
					}
				}
			}
			System.out.printf("#%d ", t+1);
			for(int i = 0 ; i < 10; i++) {
				System.out.print(arrlist.get(i)+" ");
			}
			System.out.println();
		}
	
	}
}
