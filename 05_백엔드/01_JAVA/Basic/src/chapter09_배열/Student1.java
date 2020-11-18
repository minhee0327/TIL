package chapter09_배열;

import java.util.ArrayList;

public class Student1 {
	private String studentName;
	private ArrayList <Book1> bookList;
	
	public Student1(String studentName) {
		this.studentName = studentName;
		bookList = new ArrayList<Book1>();
	}

	public void addBookList(String bookName) {
		Book1 book = new Book1(bookName);
		
		bookList.add(book);
	}
	
	public void showInfo() {
		System.out.print(studentName +" 학생이 읽은 책은 : ");
		for(Book1 book: bookList) {
			System.out.print(book.getBookName()+" ");
		}
		System.out.println("입니다.");
	}
}
