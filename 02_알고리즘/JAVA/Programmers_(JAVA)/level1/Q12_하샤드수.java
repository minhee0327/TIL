package level1;

public class Q12_하샤드수 {

	public static void main(String[] args) {

	}
    public boolean solution(int x) {
        boolean answer = true;
        int z = x;
        int y= 0;
        
        while(z > 0){
            y += z %10;
            z /= 10;
        }
        
        if (x % y != 0){
            answer = false;
        }
        
        return answer;
    }
}
