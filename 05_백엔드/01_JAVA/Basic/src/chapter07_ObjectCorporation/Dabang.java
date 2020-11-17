package chapter07_ObjectCorporation;

public class Dabang {
	private String dabangName;
	private int amePrice;
	private int lattePrice;
	
	public Dabang(String name, String type, int money){
		this.setDabangName(name);
		if(type == "americano" || type=="아메리카노") {
			this.amePrice = money;
		}else if (type == "latte" || type == "라떼") {
			this.setLattePrice(money);
		}
	}
	
	public int getAmePrice() {
		return this.amePrice;
	}

	public int getLattePrice() {
		return this.lattePrice;
	}

	public void setLattePrice(int lattePrice) {
		this.lattePrice = lattePrice;
	}
	
	public String getDabangName() {
		return dabangName;
	}

	public void setDabangName(String dabangName) {
		this.dabangName = dabangName;
	}
	
	public void coffeeInfo() {
		System.out.println(this.dabangName+" (음료 및 가격) => 아메리카노: "+ amePrice + " 카페라떼: " + lattePrice);
	}
}
