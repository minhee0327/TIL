package level1;

public class Q14_두정수사이의합 {

	public static void main(String[] args) {

	}
	//내가 푼 코드
	public long solution1(int a, int b) {
	      long answer = 0;
	      if(a > b){
	          for(int i = b; i <= a; i++){
	              answer += i;
	          }
	      }else{
	          for(int i = a; i <= b; i++){
	              answer += i;
	          }
	      }
	      return answer;
	  }
	
	//참조코드중 아이디어1: 등차수열의 합이용
	public long solution2(int a, int b) {
		long x = Math.min(a, b);
		long y = Math.max(a, b);
		return (x + y) * (y - x + 1 ) / 2;
	}
	
	//내 코드를 삼항연산자로 활용해볼 수 있음!
	public long solution3(int a, int b) {
		long answer = 0;
		for(int i = ((a <b) ? a : b); i <= ((a > b)?a:b); i++) {
			answer += i;
		}
		return answer;
	}
}
