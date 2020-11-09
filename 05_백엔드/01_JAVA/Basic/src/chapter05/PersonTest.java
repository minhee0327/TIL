package chapter05;

public class PersonTest {

	public static void main(String[] args) {
		Person James = new Person();
		
		James.age = 40;
		James.name = "James";
		James.isMarried = true;
		James.childrenNum = 3;
		
		James.personInfo();
	}
}
