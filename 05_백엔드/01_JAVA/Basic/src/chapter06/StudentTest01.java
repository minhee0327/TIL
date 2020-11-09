package chapter06;

public class StudentTest01 {

	public static void main(String[] args) {
		Student studentLee = new Student();
		studentLee.studentName = "이순신";
		studentLee.address = "서울";
		
		studentLee.showStudentInfo();
		
		Student studentKim = new Student();
		studentKim.studentName = "김유신";
		studentKim.address = "경주";
		
		studentKim.showStudentInfo();
		
//		instance를 가리키는 주소값 (참조 변수 출력)
//		package명.class명@주소값 형태로 찍힌다.
//		주소값: JVM이 준 가상 주소(hash값) - 총 32bit
		System.out.println(studentLee);
		System.out.println(studentKim);
	}
}
