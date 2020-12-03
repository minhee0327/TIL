package level1;

import java.util.Arrays;

public class Q7_문자열내림차순배치 {

	public static void main(String[] args) {
		System.out.println(Solution7.solution("Zbcdefg"));
	}
}
class Solution7 {
    public static String solution(String s) {
        char[] sol = s.toCharArray();
        Arrays.sort(sol);
        
        return new StringBuilder(new String(sol)).reverse().toString();
    }
}


// 정리해야할 것.
// StringBuilder : StringBuffer대체 사용. 동시 처리 불허. 단일 스레드 환경. 
// StringBuilder 내부에 reverse()가 있다는 점을 몰랐었는데 알면 좋을 것 같음!

// toString: Object => String (null일 경우 null point exception, String이 아니어도 출력)
// String.valueOf(): Object => String (null을 "null"로)
// 따라서 valueOf를 사용할 경우, "null".equals(String) 형태로 다시 한번 체크 해야할 수 있다.

// Collections 사용법!