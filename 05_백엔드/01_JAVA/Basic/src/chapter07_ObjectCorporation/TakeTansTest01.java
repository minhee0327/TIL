package chapter07_ObjectCorporation;

public class TakeTansTest01 {

	public static void main(String[] args) {
		Student studentJ = new Student("James", 5000);
		Student studentT = new Student("Thomas", 10000);
		Student Edward = new Student("Edward", 50000);
		
		Bus bus100 = new Bus(100);
		Bus bus500 = new Bus(500);
		Subway subwayGreen = new Subway(2);
		Subway subwayBlue = new Subway(4);
		Taxi taxi1234 = new Taxi(1234);
		
		studentJ.takeBus(bus100);
		studentT.takeSubway(subwayGreen);
		Edward.takeTaxi(taxi1234);
		
		studentJ.showInfo();
		studentT.showInfo();
		Edward.showInfo();
		
		bus100.showInfo();
		bus500.showInfo();
		taxi1234.showTaxiInfo();
		
		subwayGreen.showSubwayInfo();
		
	}
}
