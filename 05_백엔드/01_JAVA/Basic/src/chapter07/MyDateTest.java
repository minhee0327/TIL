package chapter07;

public class MyDateTest {

	public static void main(String[] args) {
//		default 접근제한자: 같은 패키지 내에 있는 것에만 접근 가능.
//		package가 달라질 경우, public으로 해야 접근가능.

		MyDate date = new MyDate();
		date.setDay(7);
		date.setMonth(11);
		date.setYear(2020);
		
		date.showDate();
		
		MyDate date2 = new MyDate();
		date2.setYear(2021);
	}

}
