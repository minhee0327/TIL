package chapter05;

public class Person {
//	과제: 나이가 40살, 이름이 James라는 남자, 결혼 했고, 자식 셋있음 class로 구현해보기.
	
	int age;
	String name;
	boolean isMarried;
	int childrenNum;
	
	public void personInfo() {
		System.out.println("나이: " + age + ", 이름: "+ name+", 결혼여부" + isMarried + ", 자녀수: "+ childrenNum);
	}

}
