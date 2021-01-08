package level1;

public class Q11_핸드폰번호가리기 {

	public static void main(String[] args) {

	}
	/*
	 //Java11이상
    public String solution(String phone_number) {
        String answer = "";
        
        answer += "*".repeat(phone_number.length() - 4);
        
        for(int i = 0; i< 4;i ++){
            answer += phone_number.charAt(answer.length());
        }
        
        return answer;
    }
    */
	
	public String solution(String phone_number) {
		char[] arr = phone_number.toCharArray();
		
		for (int i = 0; i < arr.length - 4; i++) {
			arr[i] = '*';
		}
		
		return String.valueOf(arr);
	}
}
