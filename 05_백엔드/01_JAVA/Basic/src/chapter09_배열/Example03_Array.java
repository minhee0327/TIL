package chapter09_배열;

public class Example03_Array {

	public static void main(String[] args) {
		// 참조 자료형 배열
		// 초기값 null, 생성한 객체의 주소를 담게된다.
		Book[] library = new Book[5];
		
		library[0] = new Book("태백산맥1", "조정래");
		library[1] = new Book("태백산맥2", "조정래");
		library[2] = new Book("태백산맥3", "조정래");
		library[3] = new Book("태백산맥4", "조정래");
		library[4] = new Book("태백산맥5", "조정래");
		
		for (int i = 0; i < library.length; i++) {
			System.out.println(library[i]);
			library[i].showBookInfo();
		}
		
	}

}
