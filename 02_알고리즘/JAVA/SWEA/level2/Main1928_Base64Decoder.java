package level2;

import java.util.Base64;
import java.util.Base64.Decoder;
import java.util.Scanner;

public class Main1928_Base64Decoder {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int t = 0; t < T; t ++) {
			String text = sc.next();
			byte[] targetByte = text.getBytes();
			
			//디코딩
			Decoder decoder = Base64.getDecoder();
			byte[] decodeBytes = decoder.decode(targetByte);
			
			System.out.printf("#%d %s%n",t+1, new String(decodeBytes));
		}
	}

}
