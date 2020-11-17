package chapter07;

public class PersonTest01 {

	public static void main(String[] args) {
		Person personNoname = new Person();
		
		personNoname.showInfo();
		
		Person personLee = new Person("Lee", 20);
		personLee.showInfo();
//		personLee 인스턴스를 가리키는 주소값
		System.out.println(personLee);
		
//		personLee 인스턴스를 가리키는 주소값 (this로 가리킬수있다.)
		Person p= personLee.getSelf();
		System.out.println(p);
	}
}
