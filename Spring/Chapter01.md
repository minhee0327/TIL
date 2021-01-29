## Day01

### Spring이란?

* Java Enterprise App 개발에 사용되는 Application Framework
  * **Application의 바탕이 되는 틀**
    * Spring Container(=Application Context)이라 불리는 Spring runtime Engine제공.
    * 설정정보를 참조해서, Application을 구성하는 오브젝트를 생성하고 관리.
    * 독립적으로도 사용이 가능하고, 웹 모듈에서 동작하는 서비스나, 서블릿으로 등록해서 사용.
  * **공통 프로그래밍 모델**
    * Application Code가 어떻게 작성되야 하는지에 대한 기준(틀) 제시.
    * 3가지 핵심 프로그래밍 모델 지원
      * **IoC/DI**: Object 생명주기와 의존관계에 대한 프로그래밍 모델.
      * **서비스 추상화**: 환경, 서버, 특정기술에 종속되지 않고 이식성이 뛰어나고 유연.
      * **AOP**: Application Code에 산재해서 나타나는 부가적인 기능을 독립적으로 모듈화하는 프로그래밍.
  * **기술 API 등**





## Object와 의존관계

* Spring이 Java에서 가장 중요하게 가치를 두는것은 OOP가 가능한 언어라는 점.
* Application에서 Obj가 생성이 되고 다른 Obj와 관계를 맺고, 사용되고, 소멸하기까지 전 과정.
* 나아가서 어떻게 Obj를 설계하고, 어떤 단위로 어떤 과정을 통해 자신을 드러내고 등장하는지 살펴 볼것.



### 관심사의 분리 (Separation of Concerns, SoC)

* 객체 지향의 관점에서
  * 관심이 같은 것 끼리는 하나의 객체 안으로, 또는 친한 객체로 모이게하고
  * 관심이 다른것은 가능한 따로 떨어져서 서로 영향을 주지 않도록 분리하는 것.
  * 변화가 한가지 관심에 집중되서 일어난다면, 우리가 준비할 일은 한가지 관심이 한군데 집중되게 하는것.
  * 정리) 관심사가 같은것들끼리 분리해두면 변화가 생겼을 때 그 부분만 집중해서 보수하면 되니까 자유도 ↑



### 템플릿 메소드 패턴(Template method Pattern)

* super 클래스에 기본적인 로직의 흐름을 만들고, 그 기능의 일부를 추상메소드나, 오버라이딩이 가능한 protected mthod등으로 만든뒤, 서브 클래스에서 이런 메소드를 필요에 맞게 구현해서 사용하도록하는 방법.



### 팩토리 메소드 패턴(Factory method Pattern)

* 서브 클래스에서 구체적인 오브젝트 생성방법을 결정하게 하는 것.

---

1. MVC패턴
   1. DAO
2. Java Bean: 
   1. default 생성자
   2. property (setter, getter)
3. reflection



