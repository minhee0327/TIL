package level1;

public class Q10_행렬의덧셈 {

	public static void main(String[] args) {
		// no test
		// 금방통과해서 그냥 programmers에서 풀고 제출
	}
	public static int[][] solution(int[][] arr1, int[][] arr2) {


        int row = arr1[0].length;
        int col = arr1.length ;

        int[][] answer = new int[col][row];

        for(int i =0; i< col;i++ ) {
            for(int j=0; j< row;j++) {
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }

        return answer;
    }
}
