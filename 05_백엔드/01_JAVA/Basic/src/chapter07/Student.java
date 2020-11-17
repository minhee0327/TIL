package chapter07;

public class Student {
	int studentID;
	String studentName;
	
//	참조 자료형 타입으로 변수를 선언하고 생성자에서 초기화
	Subject korea;
	Subject math;
	
	public Student(int id, String name) {
		studentID = id;
		studentName = name;
		
		korea = new Subject();
		math = new Subject();
	};
	
	public void setKoreaSubject(String name, int score) {
		korea.subjectName = name;
		korea.score = score;
	}
	public void setMathSubject(String name, int score) {
		math.subjectName = name;
		math.score= score;
	}
	public void showStudentScore() {
		int total = math.score + korea.score;
		System.out.println(studentName + " 학생의 총점은 " + total + "점 입니다.");
	}
}
