package day04_array;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main10818_1 {
// 	배열을 사용한 코드보다는 min, max를 계속 비교해서 변수에 저장해가는 방식이 
//	시간, 공간면에서 상당히 더 효율적이다.
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		int[] a = new int[n];
		int idx = 0;
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		while(st.hasMoreTokens()) {
			a[idx] = Integer.parseInt(st.nextToken());
			idx ++;
		}
		
//		Arrays.sort(): 자바 sort
		Arrays.sort(a);

		bw.write(a[0] + " " + a[a.length - 1]);
		
		bw.flush();
		bw.close();
		br.close();
	}
}
