package level1;

public class Q16_약수의합 {

	public static void main(String[] args) {
		
	}
	public int solution(int n) {
        int answer = 0;
        for(int i = 1; i<=n ; i++){
            if(n % i == 0){
                answer+= i;
            }
        }
        return answer;
    }
}
