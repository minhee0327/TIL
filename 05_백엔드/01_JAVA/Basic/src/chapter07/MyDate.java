package chapter07;

public class MyDate {
	private int day;
	private int month;
	private int year;
	private boolean isValid;
	
//	setter 사용 X, getter만 사용 O => read only
//	this: 
//	- 객체지향 언어에서 자기자신을 지칭(자신의 메모리 가리킴)하는 의미를 가지고있다.
//	- 생성자에서 다른 생성자를 호출
//	- 인스턴스 자신의 주소반환
	
//	super: 상속에서 상위 클래스를 가리킨다.
	
	public int getMonth() {
		return month;
	}

	public void setMonth(int month) {
		if(month < 1 || month > 12) {
			isValid = false;
		}else {
			this.month = month;
		}
	}

	public int getYear() {
		return year;
	}

	public void setYear(int year) {
		this.year = year;
	}

	public int getDay() {
		return day;
	}
	public void setDay(int day) {
		this.day = day;
	}
	public void showDate() {
		if(isValid) {
			System.out.println(year + "년 " + month + "월 " + day + "일");
		}else {
			System.out.println("유효하지 않은 날짜입니다.");
		}
	}
}
