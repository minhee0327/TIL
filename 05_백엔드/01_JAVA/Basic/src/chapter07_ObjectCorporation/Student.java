package chapter07_ObjectCorporation;

public class Student {
	String studentName;
	int grade;
	int money;
	
	public Student(String studentName, int money) {
		this.studentName = studentName;
		this.money = money;
	}
	//버스를 탔을 경우
	public void takeBus(Bus bus) {
		bus.take(1000);
		this.money -= 1000;
	}
	//지하철을 탄 경우
	public void takeSubway(Subway subway) {
		subway.take(1200);
		this.money -=1200;
	}
	//taxi를 탄 경우
	public void takeTaxi(Taxi taxi) {
		taxi.take(10000);
		this.money -= 10000;
	}
	
	// 돈이 얼마가 남았는지 출력
	public void showInfo() {
		System.out.println(studentName +"님이 남은 돈은 " + money + "입니다.");
	}
}
