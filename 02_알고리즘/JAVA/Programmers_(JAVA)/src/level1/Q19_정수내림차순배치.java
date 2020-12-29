package level1;

import java.util.Arrays;

public class Q19_정수내림차순배치 {

	public static void main(String[] args) {
		System.out.println(solution(118372));
	}
	public static long solution(long n) {
        
        String temp = n + "";
        char[] arr = temp.toCharArray();
        Arrays.sort(arr);
        
        temp = "";
        for(int i = arr.length-1; i>=0; i--){
            temp += arr[i];
        }
        
        return Long.parseLong(temp);
    }
	
}
