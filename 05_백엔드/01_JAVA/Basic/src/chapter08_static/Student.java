package chapter08_static;

public class Student {
	 private static int serialNum = 1000;
	 public int studentID;
	 public String studentName;
	 public String address;

	 public Student() {};
	 
	 public Student(String name) {
		 studentName = name;
		 serialNum++;
		 studentID = serialNum;
	 };
	 public Student(int id, String name) {
		 studentID = id;
		 studentName = name;
		 address = "주소 없음";
		 serialNum++;
		 studentID = serialNum;
	 }
	 
	 public void showStudentInfo() {
		 System.out.println(studentName + " , " + address);
	 }
	 
	 public String getStudentName() {
		 return studentName;
	 } 
	 public int getStudentID() {
		 return studentID;
	 }

	public static int getSerialNum() {
//		지역 변수: 함수 내에 선언된 변수 (stack)
		int i = 0;
//		인스턴스 변수는 static 메서드 내부에서 사용 불가능
//		static 변수, 메서드는 프로그램이 로드될때 할당이 되기 때문. (static은 큰 크기를 할당하지 않도록 노력할것 => 성능)
//		studentName = "Lee";
		
//		static변수
		return serialNum;
	}

	public static void setSerialNum(int serialNum) {
		Student.serialNum = serialNum;
	}
	 
}
