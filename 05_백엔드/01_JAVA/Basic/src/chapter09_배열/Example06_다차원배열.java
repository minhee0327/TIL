package chapter09_배열;

public class Example06_다차원배열 {

	public static void main(String[] args) {
		int[][] arr = {{1,2,3},{4,5,6}};

		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				System.out.print(arr[i][j]+" ");
			}
			System.out.println();
		}
	
	}
}
