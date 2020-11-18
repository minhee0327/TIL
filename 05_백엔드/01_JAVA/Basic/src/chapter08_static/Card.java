package chapter08_static;

public class Card {
	private int cardNumber;
	private static int serialNumber= 1000;
	
	Card(){
		serialNumber++;
		cardNumber = serialNumber;
	}
	
	public int getCardNumber() {
		return cardNumber;
	}
	public void setCardNumber(int cardNumber) {
		this.cardNumber = cardNumber;
	}
}
