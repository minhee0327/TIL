package chapter07_ObjectCorporation;

public class Bus {
	int busNumber;
	int passengerCount;
	int money;
	
	public Bus(int busNumber) {
		this.busNumber = busNumber;
	}
	// 승차 메서드
	public void take(int money) {
		this.money += money;
		passengerCount++;
	};
	public void showInfo() {
		System.out.println(busNumber + "번 버스의 승객은"+ passengerCount + "명 이고, 수입은 "+ money + "입니다.");
	}
}
