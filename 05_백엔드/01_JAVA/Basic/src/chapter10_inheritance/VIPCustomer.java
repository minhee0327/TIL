package chapter10_inheritance;

public class VIPCustomer extends Customer {
	
	private int agentID;
	double salesRatio;
	
	public VIPCustomer() {
		//private으로 쓰인것은 상속되더라도 access할수가 없다.
		//상속관계에서는 접근이 가능하고, 외부에서 접근불가능하도록 => protected
		
		//상위 클래스의 기본 생성자 
		//기본 생성자가 없고, 다른 생성자가 있을 경우엔 error. (호출할 기본생성자가 없으니깐!)
		//super();
		customerGrade = "VIP";
		bonusRatio = 0.05;
		salesRatio = 0.1;
		
		System.out.println("VIPCustomer() 생성자 호출");
	}
	
	public VIPCustomer(int customerID, String customerName) {
		//상위클래스에 기본생성자가 없을 경우엔, 명시적으로 아래와같이 호출해야한다.
		super(customerID, customerName);
		
		customerGrade = "VIP";
		bonusRatio = 0.05;
		salesRatio = 0.1;
		
		System.out.println("VIPCustomer(int customerID, String customerName) 생성자 호출");
		
	}
}
