# Singleton Pattern

- 정의
  - 하나의 클래스가 오직 단일 인스턴스만 가지는 경우 
  - 어플리케이션 내에서 전역적으로 접근이 가능하다.
  - 어떤 클래스가 최초 한번만 메모리에 할당(static) 하고, 그 메모리에 객체를 만들어 사용하는 패턴.



- 구현 (아래 *예* 같이 보기!)
  - 생성된 singleton object를 저장할 수 있는 자신과 같은 타입의 static field정의
  - 모든 초기화 코드를 캡슐화 (private or protected constructor)
  - 인스턴스에 대한 엑세스를 제공하는 public static member function  (public getter, ex: getInstance() )
    - 이 메소드가 호출되는 시점에서 한번만 오브젝트가 만들어지게 한다.
    - 생성된 오브젝트는 static field에 저장 하거나, static field의 초기값으로 오브젝트를 미리 만들어 둘 수 도 있다.
    - instance에 대한 접근 제공.
  - 한번 singleton object를 만들고 난 후에는 접근자 함수(getter) 를 통해 이미 만들어져  static field에 저장해둔 오브젝트를 넘겨준다.



* 예

  ```java
  public class Singleton{
      //static field
      private static Singleton instance;
      
      //private(protected) constructor: class 밖에서는 object 생성 X.
      private Singleton(){...}
     
      //static member function (static factory method)
      //synchronized: thread에서 동시접근에 대한 문제 해결 (성능 저하 원인)
      public static synchronized Singleton getInstance(){
          //lazy init
          if(instance == null) instance = new SingleTon(?);
          return instance;
      }
      
  }
  ```

  



- 문제점(한계)
  - 전역 상태를 만든다. 
    - static method로 쉽게 접근 가능
    - 아무 객체나 자유롭게 접근하고 수정하고 공유 가능한 전역상태 
  - private 생성자를 가지고 있어서, 상속 불가
    - 객체지향의 장점인 상속, 다형성 적용 불가
  - 테스트 하기 어렵다.
  - 서버 환경에서 싱글톤이 하나만 만들어지는 것을 보장 할 수 없다.



* 3가지 필수 중촉 요건
  * 단일 인스턴스의 소유권을 합리적으로 할당 가능해야함.
  * lazy initialize
  * global access 달리 제공되지 않는 경우.



* 장점
  * 한 번의 객체 생성으로 재사용이 가능하므로, 메모리 낭비 방지.
  * 한 번 생성한 객체는 무조건 한 번 생성으로 전역성을 띄며, 다른 객체와 공유가 가능.





---

[참고]

https://elfinlas.github.io/2019/09/23/java-singleton/

https://blog.seotory.com/post/2016/03/java-singleton-pattern

https://jeong-pro.tistory.com/86

책 - 토비의 스프링