package chapter09_배열;

public class Example05_ObjectCopy {

	public static void main(String[] args) {
		Book[] library = new Book[5];
		Book[] copyLibrary = new Book[5];
		
		library[0] = new Book("태백산맥1", "조정래");
		library[1] = new Book("태백산맥2", "조정래");
		library[2] = new Book("태백산맥3", "조정래");
		library[3] = new Book("태백산맥4", "조정래");
		library[4] = new Book("태백산맥5", "조정래");
		
		//얕은 복사: 실제 인스턴스가 생긴게 아니고, 주소를 가져오는 것. 따라서 복사한 것을 변화하면 같이 변화.
		System.arraycopy(library, 0, copyLibrary, 0, 5);

		/*
		for(Book book: copyLibrary) {
			book.showBookInfo();
		}
		*/
		library[0].setTitle("나목");
		library[0].setAuthor("박완서");
		
		for(Book book: library) {
			book.showBookInfo();
		}
		System.out.println("==============");
		for(Book book: copyLibrary) {
			book.showBookInfo();
		}
		
		
	}
}
