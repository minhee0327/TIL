package chapter10_inheritance;

public class CustomerTest {

	public static void main(String[] args) {
		
		Customer customerLee = new Customer();
		customerLee.setCustomerName("이순신");
		customerLee.setCustomerID(100010);
		customerLee.bonusPoint = 1000;
		
		System.out.println(customerLee.showCustomerInfo());
		
		VIPCustomer customerKim = new VIPCustomer();
		customerKim.setCustomerName("김유신");
		customerKim.setCustomerID(10020);
		customerKim.bonusPoint = 10000;
		
		//하위클래스가 생성될때, 상위클래스가 먼저 생성됨
		//상위클래스에 대한 생성자가 없으면, super();라는 키워드가 free compile.
		//상위클래스가 먼저 메모리에 잡힌 다음, 하위 클래스가 메모리에 잡힌다.
		System.out.println(customerKim.showCustomerInfo());
		
		
		//상위클래스로 묵시적 형변환(upcasting)
		//상위클래스로 변수선언, 하위클래스로 인스턴스 생성
		//하위 클래스는 상위 클래스의 타입을 내포하고 있으므로, 상위클래스로 묵시적 형변환.
		//하위 => 상위(O), 상위 => 하위(X)
		//인스턴스는 vipcustomer까지 만들어졌지만, 변수 타입으로 customer로 사용되었기 때문에, customer거만 가리킬 수 있음
		Customer vc = new VIPCustomer();
		System.out.println(vc.getCustomerGrade());
		
		
		
	}
}
