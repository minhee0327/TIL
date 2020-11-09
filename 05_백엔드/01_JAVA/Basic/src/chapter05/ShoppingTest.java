package chapter05;

public class ShoppingTest {

	public static void main(String[] args) {
		ShoppingInfo hong = new ShoppingInfo();
		
		hong.orderedNum = 201907210001L;
		hong.orderedPersonID = "abc123";
		hong.orderedDate = "2019년 7월 21일";
		hong.orderedPersonName = "홍길순";
		hong.orderedProductNum = "PD0345-12";
		hong.address = "서울 영등포구 여의도동 20번지";
		
		hong.ShoppingInfoPrint();
	}

}
