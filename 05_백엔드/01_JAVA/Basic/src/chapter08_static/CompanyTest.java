package chapter08_static;

import java.util.Calendar;

public class CompanyTest {

	public static void main(String[] args) {
		Company company1 = Company.getInstance();
		
		Company company2 = Company.getInstance();
		
		//동일한 주소값을 반환한다. 단하나만 생성해서 계속 사용함
		System.out.println(company1);
		System.out.println(company2);
		
		
		Calendar calendar = Calendar.getInstance();
	}
}
