package chapter02;

public class operator4 {

	public static void main(String[] args) {
		int score = 100;
		
//		statement가 끝나기 전에 증가
		System.out.println(score);
		System.out.println(++score);
		System.out.println(score);
		score = 100;

		System.out.println("---------------");
//		statement가 끝난 후 증가
		System.out.println(score);
		System.out.println(score++);
		System.out.println(score);
	}
}
