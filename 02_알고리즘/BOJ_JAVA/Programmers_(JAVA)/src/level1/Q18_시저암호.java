package level1;

public class Q18_시저암호{
	
	public static void main(String[] args) {
		//hidden test case: 질문하기에서 알려주신 코드
		System.out.println(solution("AB", 1));
        System.out.println(solution("z", 1));
        System.out.println(solution("Z", 10));
        System.out.println(solution("a B z", 4));
        System.out.println(solution("aBZ", 20));
        System.out.println(solution("y X Z", 4));
        System.out.println(solution(". h z", 20));
	
	}
	public static String solution(String s, int n) {
        String answer = "";
        char[] arr = s.toCharArray();
        
        for (int i = 0; i < arr.length; i++) {
            if ('a' <= arr[i] && arr[i]<= 'z') {
            	answer+= (char) ((arr[i] - 97 + n) % 26 + 97);
            }else if ('A'<= arr[i] && arr[i]<='Z') {
            	answer+= (char) ((arr[i] - 65 + n) % 26 + 65);
            }else if (arr[i] ==' ') {
            	answer+= ' ';
            }
        }
		return answer;
	}
}


