package day04_array;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main3052 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		boolean arr[] = new boolean[42];
		int cnt = 0;
		
		for (int i = 0; i < 10; i++) {
			int temp = Integer.parseInt(br.readLine());
			if (!arr[temp % 42]) {
				cnt++;
				arr[temp % 42] = true;
			}
		}
//		형변환(integer => string ; 위에서 부터 가장 빠르고 아래로 갈수록 느림)
		bw.write(String.valueOf(cnt));
//		bw.write(Integer.toString(cnt));
//		bw.write(cnt+"\n");
		bw.flush();
		bw.close();
		br.close();
	}
}
