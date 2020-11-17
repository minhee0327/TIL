package chapter07_ObjectCorporation;

public class MyDateTest {

	public static void main(String[] args) {
		MyDate date1 = new MyDate(2020, 10, 11);
		System.out.println(date1.isValid());
		
		date1.setDay(40);
		System.out.println(date1.isValid());
		System.out.println(date1.getDay());
		
		date1.setYear(3033);
		System.out.println(date1.isValid());
		System.out.println(date1.getYear());
		
		date1.setMonth(10);
		System.out.println(date1.isValid());
		System.out.println(date1.getMonth());
		
		System.out.println("=======================");
		MyDate date2 = new MyDate(2001, 2, 31);
		System.out.println(date2.isValid());
	}
}
