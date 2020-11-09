package chapter05;

public class ShoppingInfo {
	long orderedNum;
	String orderedPersonID;
	String orderedDate;
	String orderedPersonName;
	String orderedProductNum;
	String address;
	
	public void ShoppingInfoPrint() {
		System.out.println("주문번호: "+ orderedNum);
		System.out.println("주문자 아이디: " + orderedPersonID);
		System.out.println("주문날짜: " + orderedDate);
		System.out.println("주문자 이름: " + orderedPersonName);
		System.out.println("주문 상품 번호: " + orderedProductNum);
		System.out.println("배송 주소: " + address);
	}
}
