package chapter05;

// public class는 java파일내에 1번 사용가능
// java파일명과 이름이 동일해야한다.
public class Student {
	 public int studentID;
	 public String studentName;
	 public String address;
	 
	 public void showStudentInfo() {
		 System.out.println(studentName + " , " + address);
	 }
	 
	 public String getStudentName() {
		 return studentName;
	 }  
}
