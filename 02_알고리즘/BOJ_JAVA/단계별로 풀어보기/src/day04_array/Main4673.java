package day04_array;

public class Main4673 {

	public static void main(String[] args) {
		boolean [] selfNum = new boolean [10001];

		for (int i = 0; i <= 10000; i++) {
			int dnum = d(i);
			if(dnum < 10000) {
				selfNum[dnum] = true;
			}else {
				continue;
			}
		}
		for (int i = 0; i < 10000; i++) {
			if(!selfNum[i]) {
				System.out.println(i);
			}
		}
	}
	
	
	//각 자리수들의 합
	public static int d(int num) {
		int n = num;
		while(num> 0) {
			n += num %10;
			num /= 10;
		}
		return n;
	}
}
