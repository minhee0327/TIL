package chapter07;

public class StudentTest {

	public static void main(String[] args) {
		Student studentKang = new Student(100, "Kang");
		studentKang.setKoreaSubject("국어", 100);
		studentKang.setMathSubject("수학", 95);
		
		Student studentKim = new Student(101, "Kim");
		studentKim.setKoreaSubject("국어", 88);
		studentKim.setMathSubject("수학", 90);
		
		studentKang.showStudentScore();
		studentKim.showStudentScore();
	}

}
