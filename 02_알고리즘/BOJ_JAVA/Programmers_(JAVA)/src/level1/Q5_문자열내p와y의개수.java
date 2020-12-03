package level1;

public class Q5_문자열내p와y의개수 {

	public static void main(String[] args) {
		System.out.println(solution("pPoooyY"));
		System.out.println(solution("Pyy"));
	}
	
	//method 작성
	public static boolean solution(String s) {
		char[] arr = s.toLowerCase().toCharArray();
		int p_cnt = 0, y_cnt = 0;
		
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] == 'p') p_cnt ++;
			else if (arr[i] =='y') y_cnt++;
		}
		if (p_cnt == y_cnt) return true;
		else return false;
	}
}

// 나는 toCharArray()로 배열에 char로 쪼개어 담았는데, 
// string의 문자 하나하나를 비교하고 싶을 때, charAt(i) 를 사용하는 방법이 있다는 걸 자꾸 잊는다ㅠㅠ
// 요 방법을 기억하도록!

// 좋은 풀이중, 변수를 하나로 두고 p, y의 차이값으로 반환한 코드도 꽤 깔끔해서 좋은 듯!