package level2;

import java.util.Arrays;
import java.util.Scanner;

public class Main1983_조교의성적매기기 {
	public static String score[] = {"A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"};
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int tc = 0 ; tc < T; tc ++) {
			int n = sc.nextInt();
			int k = sc.nextInt();
			double[] arr = new double[n];
			int idx = -1;
			
			//1. 총점 구하기
			for(int i = 0; i < n ; i++) {
				int mid = sc.nextInt();
				int fin = sc.nextInt();
				int sub = sc.nextInt();
				
				double total = mid * 0.35 + fin * 0.45 + sub * 0.2;
				
				arr[i] = total;
			}
			//2. 찾고자 하는 점수
			double findNum = arr[k-1];
			
			//3. 정렬(등급메기기)
			Arrays.sort(arr);

			//4. 찾고자 하는 점수 학생의 index값 저장.(현재 오름차이기 때문에, n-i로 순위 정함)
			for(int i = 0; i < n ; i++) {
				if(findNum == arr[i]) {
					idx = n - i;
				}
			}
			//5. idx % (n/10) 결과가 0이면 해당 idx의 score를, 아니라면 다음 score를 반환해주면됨.
			if(idx % (n / 10) == 0) {
				System.out.printf("#%d %s%n",tc+1, score[(idx / (n/10))-1 ]);
			}else {
				System.out.printf("#%d %s%n",tc+1 ,score[idx / (n/10)]);
			}
		}
	}
}

/*[풀면서 든 생각]
 * 
 * 1. 로직을 생각해내는 것은 금방했는데, sort를 내림차로 변경하려다보니 ArrayList로 변환해야했는데, 
 * 그거보다는 전체길이가 고정되있으니까, idx를 구하는 방향으로 진행했다.
 * 
 * 2. idx %(n/10)을 생각해내는데 조금 오래 걸렸다... 자주 안풀면 머리도 굳는다....
 * 
 * 3. python에 익숙해져서 type casting에 시간이 소요된다... 연습연습!!
 */
