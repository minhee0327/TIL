# Comparable vs Comparator

- ### Comparable interface

  - 정렬 기준을 정의하는 2가지 방법 중 하나.

  - 정렬 대상 클래스를 **자바에서 기본적으로 제공**하는 `Comparable` 인터페이스를 구현하도록 변경.

  - `Comparable` 인터페이스의 `compareTo()` 메서드를 통해서, 인자로 넘어온 같은 타입의 다른 객체와 대소 비교가 가능. 

  - return 값으로 `Integer.compare(a, b)`, `Double.compare(a,b)` 등이 사용 가능한데, `Integer.compare` 함수원형은 아래와 같다.

    ```java
    public static int compare(int x, int y){
    	return (x>y) ? -1 : ((x==y)? 0 : 1);
    }
    ```

  - `Integer.compare()`은 단순히 첫번째 매개변수와 두번째 매개변수가 오름차를 유지할 수 있도록 비교해주는 메서드이다.

  - 정렬이 진행 될 때, 자리바꿈 여부를 결정하고, return 값이 양수일 대 자리바꿈을 수행한다.

  - 내림차를 사용하고 싶을 때는 `compare(int y , int x)`로 매개변수의 순서만 바꿔주면된다. 

  - 예제

    ```java
    //오름차
    class A implements Comparable <A> {
        int x;
        A(int x){
            this.x = x;
        }
        public int compareTo(A other){
            return Integer.compare(this.x, other.x);
        }
    }
    ```

  - `Integer.compare()` 대신 직접 구현해도 된다.

  - 예제

    ```java
    //오름차
    class A implements Comparable<A>{
    	int x;
    	public int compareTo(A other){
    		//양수일 경우에만 자리 바꿈
    		return this.x - other.x;
    	}
    }
    //내림차
    class A implements Comparable<A>{
    	int x;
    	public int compareTo(A other){
    		return other.x - this.x;
    	}
    }
    ```

    

* Comparator
  * **정렬 대상 클래스의 코드를 직접 수정할 수 없는 경우에 사용**

  * 혹은 정렬하고자 하는 **객체에 이미 존재하고있는 정렬 기준과 다른 정렬 기준을 사용하고 싶을 때.**

  * `Arrays.sort()`, `Collections.sort()`와 같은 정렬 메서드의 추가 인자로 사용해서 정렬기준을 누락된 클래스의 객체나, 기존의 정렬 기준을 무시하고 새로운 정렬 기준으로 객체 정렬이 가능.

  * 예시(Programmers, [가장 큰 수 문제](https://programmers.co.kr/learn/courses/30/lessons/42746?language=java)에서 가져옴.)

    ```java
    Arrays.sort(numStr, new Comparator<String>() {
    			@Override
    			public int compare(String a, String b) {
    				//여기서 compareTo는 String이 가진 기본 메서드
    				return (a+b).compareTo(b+a);
    			}
    		});	
    ```

  * 기본 정렬 기준과 다른 새로운 정렬 기준을 세울 때 사용. 주로 익명 클래스.



* 추가

  * 람다식으로 정렬하기 (js에서 함수형에 익숙해져서, 읽기 편했다!!)

  * ```java
    Arrays.sort(numStr, (a, b) -> (b+a).compareTo(a + b));
    ```

    







---

참조 링크

https://m.blog.naver.com/occidere/220918234464

https://www.daleseo.com/java-comparable-comparator/