package level1;

public class Q4_서울에서김서방찾기 {

	public static void main(String[] args) {
		String [] test = {"Jane", "Kim"};
		System.out.println(Solution4.solution(test));
	}
}

class Solution4 {
    public static String solution(String[] seoul) {
    String answer = "김서방은 ";
    
	for (int i = 0; i < seoul.length; i++) {
		if(seoul[i].equals("Kim")) {
			answer += i;
			answer += "에 있다";
			break;
		}
	}
	
    return answer;
    }
}