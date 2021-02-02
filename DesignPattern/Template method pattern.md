# Template method pattern(템플릿 메소드 패턴)

* 한줄 요약: 알고리즘의 일부 단계를 서브 클래스에서 정의한다.
* 의도
  * super class에 기본적인 로직의 흐름을 정의하고
    그 기능의 일부를 추상메소드나 오버라이딩이 가능한 protected method등으로 만든 뒤,
    sub class에서 이런 메소드를 필요에 맞게 구현해서 사용하는 방법
  * 알고리즘의 구조(뼈대)는 그대로 놔두고, 알고리즘의 각 단계처리를 서브 클래스에서 재정의 할 수 있게 함.



* 특징
  * 기본 알고리즘(구조, 뼈대)에 대한 정의는 super class(abstract, final) 에 정의해 두고,
  * 실질적인 behavior는 하위 클래스에서 implements하도록 한다.



* 용어
  * 템플릿 메소드
    * 필수 처리 절차를 정의한 메소드
    * 서브 클래스가 오버라이드 하는 추상메소드를 사용하여 알고리즘을 정의하는 메소드.
  * hook 메소드(hook operation)
    * super class에서 디폴트 기능을 정의해 두거나 비워뒀다가, 서브클래스에서 선택적으로 override 할 수 있도록 만들어둔 메소드.
  
  

* 장단점
  * 장점
    * 코드 중복 감소
    * 자식 클래스의 역할을 감소 시키면서 핵심 로직 관리 용이
    * 객체 추가 및 확장이 쉽게 가능
  * 단점
    * 추상 메소드가 많아지면, class 관리 복잡해짐
    * 추상 클래스와 구현클래스간의 복잡성 증대



* 예제 소스

  * Super class 예

    ```java
    public abstract class Super{
    	// 기본 알고리즘 코드 (기본 골격, 템플릿 메소드)
    	// 서브 클래스에서 구현하거나 오버라이드할 메소드 사용.
    	public void templateMthod(){
    		hookMethod();
    		abstractMethod();
    	}
    	// hook method: 선택적으로 오버라이드 가능 
    	protected void hookMethod(){};
    	// 서브 클래스에서 반드시 구현해야 하는 추상메소드
    	public abstract void abstractMethod(){};
    }
    ```

  * Sub class 예

    ```java
    // super class의 메소드를 오버라이딩 하거나 구현해서 기능 확장
    public class Sub extends Super{
    	protected void hookMethod(){
    		...
    	}
    	public void abstractMethod(){
    		...
    	}
    }
    ```





---

[참조 자료]

토비의 스프링 3.1

[좋은사람 blog](https://niceman.tistory.com/142)

[기계인간 github](https://johngrib.github.io/wiki/template-method-pattern/)

[crocus](https://www.crocus.co.kr/1531)