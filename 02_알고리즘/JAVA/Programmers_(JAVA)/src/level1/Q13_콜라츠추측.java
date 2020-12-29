package level1;

public class Q13_콜라츠추측 {

	public static void main(String[] args) {

	}
    public int solution(long num) {
        int answer = 0;
        
        while(num != 1){
            if (answer >= 500){
                return -1;
            }
            if (num % 2 != 0){
                num = num * 3 + 1;
            }else {
                num /= 2;
            }
            answer ++;
        }
        return answer;
    }
}
