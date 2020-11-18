package chapter09_배열;

import java.util.ArrayList;

public class Example07_ArrayList {

	public static void main(String[] args) {
		//collection에서 다루기는 하지만 가볍게 한번
		//ArrayList: 자바에서 제공되는 객체 배열이 구현된 클래스
		//객체 배열을 사용하는데 필요한 여러 메서드들이 구현되어 있음
		//주요메서드: add(E e), size(), get(int index), remove(int index), isEmpty()
		
		
		ArrayList<String> list = new ArrayList<String>();
		
		list.add("aaa");
		list.add("vvv");
		list.add("ccc");
		list.add("ddd");
		
		//size는 element가 들어간 크기만큼만
		for(int i = 0; i< list.size(); i++) {
			String str = list.get(i);
			System.out.println(str);
		}
		
		for(String str : list) {
			System.out.println(str);
		}
		
		
	}
}
