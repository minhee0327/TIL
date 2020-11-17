package chapter07;

public class Person {
	String name;
	int age;
	
	public Person() {
//		this로 생성자를 부를 때에는 반드시 맨 첫줄에 문장이 나와야한다.
//		그 전에 다른 statement가 있으면 error발생.
		this("이름없음", 1);
	}
	
	public Person(String name, int age) {
		this.name = name;
		this.age = age;
	}
	public void showInfo() {
		System.out.println(name + ", "+ age);
	}
	public Person getSelf() {
		return this;
	}
}
