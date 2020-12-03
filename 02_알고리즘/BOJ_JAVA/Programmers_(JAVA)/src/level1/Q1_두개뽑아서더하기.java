package level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Q1_두개뽑아서더하기 {

	public static void main(String[] args) {
		System.out.println(Arrays.toString(solution(new int [] {2,1,3,4,1})));
		System.out.println(Arrays.toString(solution(new int [] {5,0,2,7})));
	}
	
	public static int[] solution (int[] numbers) {
		List <Integer> list = new ArrayList <Integer>();
		
		for (int i = 0; i < numbers.length; i++) {
			for (int j = i+1; j < numbers.length; j++) {
				if(list.indexOf(numbers[i] + numbers[j]) <0) {
					list.add(numbers[i] + numbers[j]);
				}
			}
		}
		
		int[] answer = new int[list.size()];
		for (int i = 0; i < answer.length; i++) {
			answer[i] = list.get(i);
		}
		
		Arrays.sort(answer);
		
		return answer;
	}
}
