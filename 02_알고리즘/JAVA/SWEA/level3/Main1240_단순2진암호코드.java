package level3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main1240_단순2진암호코드 {
	public static List<String> pw = new ArrayList<String>(Arrays.asList("0001101", "0011001", "0010011", "0111101",
			"0100011", "0110001", "0101111", "0111011", "0110111", "0001011"));

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int tc = sc.nextInt();
		for (int t = 0; t < tc; t++) {
			int n = sc.nextInt();
			int m = sc.nextInt();

			// 암호코드 정보
			List<String> code = new ArrayList<String>();
			// 정상암호 검증하기 위해 담는 배열
			List<Integer> correctCode = new ArrayList<Integer>();

			for (int i = 0; i < n; i++) {
				code.add(sc.next());
			}

			outer: for (int i = 0; i < n; i++) {
				if (code.get(i).contains("1")) {
					for (int j = 0; j < code.get(i).length() - 56; j++) {
						boolean flag = true;
						for (int k = j; k < j + 56; k += 7) {
							String temp = code.get(i).substring(k, k + 7);
							if (!pw.contains(temp)) {
								flag = false;
								break;
							}
						}
						if (flag) {
							for (int k = j; k < j + 56; k += 7) {
								correctCode.add(pw.indexOf(code.get(i).substring(k, k + 7)));
							}
							break outer;
						}
					}
				}
			}
			
			int sum = 0;
			for (int i = 0; i < correctCode.size(); i++) {
				if (i % 2 == 0) {
					sum += correctCode.get(i) * 3;
				} else {
					sum += correctCode.get(i);
				}
			}
			System.out.printf("#%d ", t + 1);
			if (sum % 10 == 0) {
				System.out.println(sum(correctCode));
			} else {
				System.out.println(0);
			}

		}

	}

	private static int sum(List<Integer> correctCode) {
		int ret = 0;
		for (int i : correctCode) {
			ret += i;
		}
		return ret;
	}

}
