package chapter06;

public class Student {
	 public int studentID;
	 public String studentName;
	 public String address;

//	 기본생성자
	 public Student() {};
	 
//	 생성자
	 public Student(String name) {
		 studentName = name;
	 };
// 	 overloading: 메서드 명은 같고, 매개변수의 개수나, 매개변수의 data type이 다를 경우
	 public Student(int id, String name) {
		 studentID = id;
		 studentName = name;
		 address = "주소 없음";
	 }
	 
	 public void showStudentInfo() {
		 System.out.println(studentName + " , " + address);
	 }
	 
	 public String getStudentName() {
		 return studentName;
	 }  
}
