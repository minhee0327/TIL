package level1;

public class Q22_정수제곱근판별 {

	public static void main(String[] args) {

	}
	public long solution1(long n) {
        //double => long type casting
        long sqt = (long) Math.sqrt(n);
        return sqt * sqt == n? (sqt+1) * (sqt+1): -1;
    }
	
	public long solution2(long n) {
		long sqt = (int) Math.sqrt(n);
		return Math.pow(sqt, 2) == n? (long) Math.pow(sqt+1, 2) : -1;
	}
}
