package level1;

public class Q6_문자열다루기기본 {

	public static void main(String[] args) {
		System.out.println(Solution6.solution("a1234"));
		System.out.println(Solution6.solution("1234"));
	}
}

class Solution6 {
    public static boolean solution(String s) {
        if(s.length() == 4  || s.length() == 6) {
        	try {
        		int x = Integer.parseInt(s);
        		return true;
        	}catch(NumberFormatException e){
        		return false;
        	}
        }else {
        	return false;
        }
       
    }
}