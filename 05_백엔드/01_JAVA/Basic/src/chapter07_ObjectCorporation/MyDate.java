package chapter07_ObjectCorporation;

import java.util.Calendar;

public class MyDate {
	private int day;
	private int month;
	private int year;
	private boolean isValid = true;
	
	public MyDate(int year, int month, int day) {
		setYear(year);
		setMonth(month);
		setDay(day);
	}
	
	public int getYear() {
		return this.year;
	}
	
	public void setYear(int year) {
		//현재 날짜보다 더 큰 수를 입력했거나, 음수를 입력하면 불가능!
		if (year< 0 || year > Calendar.getInstance().get(Calendar.YEAR)) {
			this.isValid = false;
			isValid();
		}else {
			this.isValid = true;
			this.year = year;
		}
	}
	
	public int getMonth() {
		return this.month;
	}
	
	public void setMonth(int month) {
		if(month<1 || month > 12) {
			this.isValid = false;
			isValid();
		}else {
			this.isValid = true;
			this.month = month;
		}
	}

	public int getDay() {
		return this.day;
	}
	
	public void setDay(int day) {
		switch (this.month) {
		case 1:case 3:case 5:case 7:case 8:case 10:case 12:
			if (day<0 || day> 31) {
				this.isValid = false;
			}else {
				this.isValid = true;
				this.day = day;
			}
			break;
		case 4: case 6: case 9: case 11:
			if (day <0 || day> 30) {
				this.isValid = false;
			}else {
				this.isValid = true;
				this.day = day;
			}
			break;
		case 2:
			//윤년: 4의 배수이면서 100의 배수가 아닐때 또는 400의 배수일때 => 29일
			//평년: 28일
			if ((year % 4 == 0 && year %100 != 0) || (year % 400 == 0)) {
				if(day<0 || day> 29) {
					this.isValid = false;
				}else {
					this.isValid = true;
					this.day = day;
				}
			}else {
				if (day< 0 || day > 28) {
					this.isValid = false;
				}else {
					this.isValid = true;
					this.day = day;
				}
			}
			break;
		default:
			this.isValid = false;
			break;
		}
		
	}
	
	public String isValid() {
		if (this.isValid == true) {
			return "유효한 날짜 입니다.";
		}else {
			return "유효하지 않은 날짜 입니다." ;
		}
	}
	
	
}
