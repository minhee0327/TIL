package chapter09_배열;

public class Example08_Student_Subject {

	public static void main(String[] args) {
		Student studentLee = new Student(1001, "이순신");
		Student studentKim = new Student(1002, "Kim");
		
		studentLee.addSubject("국어", 100);
		studentLee.addSubject("수학", 90);

		studentKim.addSubject("국어",90);
		studentKim.addSubject("수학",100);
		studentKim.addSubject("영어",80);
		
		studentLee.showStudentInfo();
		System.out.println("===============");
		studentKim.showStudentInfo();
		
	}

}
