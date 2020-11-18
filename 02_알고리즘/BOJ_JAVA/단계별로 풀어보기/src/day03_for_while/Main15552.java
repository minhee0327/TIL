package day03_for_while;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main15552 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int t = Integer.parseInt(br.readLine().trim());
		
		for (int i = 0; i < t; i++) {
			String s = br.readLine();
			String [] word = s.split(" ");
			
			int a = Integer.parseInt(word[0]);
			int b = Integer.parseInt(word[1]);
			
			bw.write((a+b)+"\n");
		}
		bw.flush();
		bw.close();
	}
}
