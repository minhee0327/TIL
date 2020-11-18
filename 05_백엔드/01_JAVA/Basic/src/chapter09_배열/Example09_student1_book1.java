package chapter09_배열;

public class Example09_student1_book1 {

	public static void main(String[] args) {
		//과제
		// student1, book1, 클래스 구현하고 문제 풀기
		Student1 studentLee = new Student1("Lee");
		Student1 studentKim = new Student1("Kim");
		Student1 studentCho = new Student1("Cho");
		
		studentLee.addBookList("태백산맥1");
		studentLee.addBookList("태백산맥2");
		
		studentKim.addBookList("토지1");
		studentKim.addBookList("토지2");
		studentKim.addBookList("토지3");
		
		studentCho.addBookList("해리포터1");
		studentCho.addBookList("해리포터2");
		studentCho.addBookList("해리포터3");
		studentCho.addBookList("해리포터4");
		studentCho.addBookList("해리포터5");
		studentCho.addBookList("해리포터6");
		
		studentLee.showInfo();
		studentKim.showInfo();
		studentCho.showInfo();
		
	}

}
