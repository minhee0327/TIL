package day04_array;

public class Main15596 {
	public static void main(String[] args) {
		
	}
};

class Test{
	public long sum(int[] a) {
		long sum = 0;
		for (int i = 0; i < a.length; i++) {
			sum+= a[i];
		}
		return sum;
	}
}