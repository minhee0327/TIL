package chapter07_ObjectCorporation;

public class Person {
	private String name;
	private int money;
	private String coffee;
	
	public Person(String name, int money) {
		this.name = name;
		this.money = money;
	}
	
	public void buyCoffee(Dabang dabang, String coffee) {
		this.coffee=coffee;
		if (dabang.getDabangName() == "콩다방") {
			if (coffee=="아메리카노") {
				this.money -= dabang.getAmePrice();
			}else {
				this.money -= dabang.getLattePrice();
			}
		}else if (dabang.getDabangName() == "별다방") {
			if(coffee=="아메리카노") {
				this.money -= dabang.getAmePrice();
			}else {
				this.money -= dabang.getLattePrice();
			}
		}
	}
	
	public void personInfo() {
		System.out.println(this.name + "님이 구매하신 커피는" + this.coffee + "이고, 남은돈은: " + this.money + " 입니다.");
	}
}
