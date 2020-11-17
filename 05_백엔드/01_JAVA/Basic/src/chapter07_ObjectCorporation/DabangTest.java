package chapter07_ObjectCorporation;

public class DabangTest {

	public static void main(String[] args) {
		Dabang starDabang = new Dabang("별다방","아메리카노", 4000);
		starDabang.coffeeInfo();
		
		Dabang kongDabang = new Dabang("콩다방", "latte", 4500);
		kongDabang.coffeeInfo();
		
		
		Person kimjoluy = new Person("김졸려", 10000);
		kimjoluy.buyCoffee(starDabang, "아메리카노");
		
		Person LeePigon = new Person("이피곤", 20000);
		LeePigon.buyCoffee(kongDabang, "라떼");
		
		kimjoluy.personInfo();
		LeePigon.personInfo();
	}
}
