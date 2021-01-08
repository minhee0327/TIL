package level1;

public class Q21_최대공약수와최소공배수 {

	public static void main(String[] args) {
		
	}
	public int[] solution(int n, int m) {
        int[] answer = new int[2];
        
        
        answer[0] = gcd(n, m);
        answer[1] = n * m / answer[0];
        
        return answer;
    }
    
    public int gcd(int a, int b){
        return a % b == 0? b: gcd(b, a % b);
    }
}
