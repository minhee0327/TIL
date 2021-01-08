package level2;

import java.util.Scanner;

public class Main1859_백만장자프로젝트2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int tc = sc.nextInt();
		for (int t = 1; t <= tc; t++) {
			int n = sc.nextInt();
			int arr[] = new int[n];
			// cnt: 구매한 물건 개수, total: 현재 보유한 총금액
			int cnt = 0;
            long total = 0;

			for (int i = 0; i < n; i++) {
				arr[i] = sc.nextInt();
			}

			for (int i = 0; i < n; i++) {
				if (checkBigger(i + 1, n, arr[i], arr)) {
					cnt++;
					total -= arr[i];
				} else {
					if (cnt > 0) {
						total += (arr[i] * cnt);
						cnt = 0;
					} else {
						continue;
					}
				}
			}

			System.out.printf("#%d %d%n", t, total);
		}
	}

	/*
	 * checkBigger method: just check future value. (find Bigger value => true) s:
	 * start, e: end, c: current_value
	 */
	public static boolean checkBigger(int s, int e, int c, int[] arr) {
		int max = c;
		for (int i = s; i < e; i++) {
			if (arr[i] > max) {
				return true;
			}
		}
		return false;
	}
}

/*
 * 1. 백만장자 프로젝트 2가 java로 먼저 떠오른 로직이었다.
 * 2. 처음부터 돌면서, 그 값을 기준으로 뒤에 큰값이 있으면 매입하고, 뒤에 큰값이 없으면 팔아서 최대수익을 구함
 * 3. 이렇게 하니까, 속도측면에서 훨씬 느리게 돌아갔었다.
 * 4. 느릴 때에 뒤에서부터 반복하는 것을 떠올리면 좋을 것 같다!!!!
 *  
 * 로직과 별개로, 큰 수를 더하게 되면서 type error가 났었다. 타입체크도 주의하자.
 */
		