package level1;

public class Q3_문자열을정수로바꾸기 {

	public static void main(String[] args) {
		System.out.println(Solution1.solution("+1234"));
		System.out.println(Solution1.solution("-1234"));
	}
	
}

class Solution1 {
    public static int solution(String s) {
    	String answer = "";    	
        String [] array = s.split("");    
        
        if (array[0].equals("-")) {
            for (int i = 1; i < array.length; i++) {
			answer+= array[i];
		    }
            return Integer.parseInt(answer) * -1;
        	
        }else {
            for (int i = 0; i < array.length; i++) {
			answer+= array[i];
		    }
        	return Integer.parseInt(answer);
        }
    }
}