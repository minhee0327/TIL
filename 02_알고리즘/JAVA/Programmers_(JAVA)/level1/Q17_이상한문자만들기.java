package level1;

public class Q17_이상한문자만들기 {

	public static void main(String[] args) {
		char[] arr = "asdf".toCharArray();
		
	}
	
	//split(" ", -1) : 공백이 맨 끝에 올 경우를 고려하기위해 -1
	public static String solution(String s) {
        String[] arr = s.split(" ", -1);
        String answer = "";

        for(int i = 0 ; i<arr.length; i++){
            char[] temp = arr[i].toCharArray();
            String word = "";
            for(int j = 0; j < temp.length; j++){
                if(j % 2 == 0){
                    word += Character.toUpperCase(temp[j]);
                }else{
                    word += Character.toLowerCase(temp[j]);
                }
            }
            answer += word;
            if(i != arr.length-1){
                answer += ' ';
            }
        }
        return answer;
    }
	
	
	//idx를 활용한 코드 
	//2중반복문도 피할 수 있고, String타입보다 작은 char타입을 활용할 수 있어 좋은거같다.
	public static String solution2(String s) {
		char [] arr = s.toCharArray();
		int idx = 0;
		
		for(int i = 0; i < arr.length; i ++) {
			if (arr[i] == ' ') {
				idx = 0;
			}else {
				arr[i] = idx++ % 2 == 0 ? Character.toUpperCase(arr[i]): Character.toLowerCase(arr[i]);
			}
		}
		
		return String.valueOf(arr);
	}
}
