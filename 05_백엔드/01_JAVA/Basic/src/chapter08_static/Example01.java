package chapter08_static;

public class Example01 {

	public static void main(String[] args) {
		Student studentLee = new Student("Lee");
//		static변수는 객체의 참조 변수를 access하는게 아니라, class로 access한다.
//		인스턴스의 생성을 하지 않더라도 static변수를 사용할 수 있다. 
		System.out.println(Student.getSerialNum());
		
		Student studentKim = new Student("Kim");
		System.out.println(Student.getSerialNum());
		

		System.out.println(studentLee.getStudentID());
		System.out.println(studentKim.getStudentID());
	
	}

}
