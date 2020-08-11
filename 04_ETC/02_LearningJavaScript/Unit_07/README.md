# 스코프

- 정적 스코프와 동적 스코프

  - 함수 f는 자신이 정의될 때 접근할 수 있었던 식별자에는 여전히 접근 할 수 있지만,  
    호출할 때 스코프에 있는 식별자에 접근할 수 없다. (예: example01.js 참조)
  - 정적 스코프는 전역스코프, 블록스코프, 함수 스코프에 적용됨
    - 전역스코프: 전역 스코프에서 선언한 것은 무엇이든 프로그램의 모든 스코프에서 확인할 수 있음
      - 전역 스코프에서 선언된 변수를 전역변수라고 함
      - 되도록 남용하지 않도록 주의할 것.
      - 데이터는 객체형태로 저장하되, 함수의 매개변수로 전달받아 사용하여 객체가 마음대로 변하지 않게 주의.
    - 블록스코프(example02.js)
    - 함수, 클로저, 정적 스코프
      - 클로저
        - 최신 자바스크립트에서, 함수가 필요한 곳에서 즉석으로 정의할 때가 많음.
        - 함수를 변수나 객체의 프로퍼티에 할당하거나, 배열에 추가하거나, 다른함수에 전달하거나, 함수가 함수를 반환하거나, 이름이 없는 경우도 있음..
        - **함수가 특정 스코프에 접근할 수 있도록 의도적으로 그 스코프에서 정의하는 경우를 \***클로저**라고 한다.**
        - 스코프를 함수 주변으로 줄이는 것이라고 생각해도 좋음
        - 함수를 정의해 클로저를 만들면 접근할 수 없었던 것들에 접근할 방법이 생김
  - 변수 숨기기

    - 스코프 중첩이 되었을 경우 내부 블록의 변수는 외부블럭세어 정의한 변수와 이름이 같더라도 다른 변수.  
      따라서, 동일한 이름의 외부 변수는 내부에서 숨기는(가리는) 효과가 있음
    - 스코프는 계층적
    - 이전 스코프를 떠나지 않더라도, 새 스코프에 진입할 수 있음.
    - 스코프의 계층적 성격때문에 어떤 변수가 스코프에 있는지 확인하는 '스코프 체인'이라는 개념이 생김

  - **즉시 호출하는 함수 표현식(IIFE) - example03.js**

    - 함수선언과 동시에 실행
    - 내부에 있는것들이 모두 자신만의 스코프를 가짐.
    - IIFE자체는 함수이기 때문에 해당 스코프 밖으로 무언가를 내보낼 수 있음.

  - **함수 스코프와 호이스팅**
    - let으로 변수를 선언하면, 그 변수는 선언하기 전에는 존재하지 않음
    - var로 선언한 변수는 현재 스코프 안이라면, 어디서든지 사용이 가능함.(심지어 선언 전에도 사용가능!)
      - 즉, 선언만하면 선언 이전에도 쓸 수 있음.
      - var로 선언한 변수는 끌어올린다는 뜻의 **'호이스팅'** 이라는 메커니즘을 따름
      - 할당은 끌어올리지 않고, 선언만 끌어올림
      - 같은 변수를여러번 정의하더라도 무시함.
    - 함수 호이스팅
      - 변수로 할당한 함수표현식은 호이스팅 되지 않지만 (변수 할당시, 변수 스코프를 따름)
      - 함수선언도 호이스팅이 일어날 수 있음.
  - 스트릭트모드
    - 암시적 전역변수 (변수선언시 var 이용해서 선언하는 것을 잊으면, 전역변수를 참조하려함.)
    - 문제를 발생시키는 여지가 많아, 스트릭트 모드를 도입
    - 암시적 전역변수 허용하지 않음.(코드 맨 앞에 "use strict")