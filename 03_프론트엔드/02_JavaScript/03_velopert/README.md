# 강사님 강의 정리하면서 자꾸 잊는 부분만 기록
1. 정보의 은닉성
    - 데이터 (필드)를 외부에서 직접적으로 접근하는 것을 막음
    - 보통은 필드들을 private으로 막아, 객체의 무결성을 보장.
    - [javaScript에서는 프로토타입 내부에서 데이터 관리함으로써 무결성 보장]
    - 객체 내부
        - 데이터 프로퍼티(value를 가짐)
            - _변수: 관례적으로 객체 내부에서만 활용하고 외부에서 건드리지 않는것이 관습.
            - 데이터를 holding(보유)함
        - 접근자 프로퍼티(get/set메서드 지님)
            - setter, getter
                - getter: 객체의 특정 프로퍼티 값을 가져옴
                - setter: 객체의 특정 프로퍼티 값을 설정
            - 데이터를 보유(holding)하지 않음
    - [javaScript 에서 setter와 getter를 쓰는이유](https://www.hongkiat.com/blog/getters-setters-javascript/)
        - 덮어쓰기 방지
        - 정보의 은닉성
            - 데이터를 직접 변경하는 실수를 방지하고, 보호할 수 있음.
            - setter를 통해 데이터를 사용할 수 있는 범위를 제한하여 추가.
            - 코드의 다른 부분에 영향을 주지않고, 해당 데이터에 대해 작업할 수 있는 특정 독립성을 가지기 때문에 사용하는 편이 좋다. 


2. 콜백함수
    - 함수 형태의 파라미터를 전달하는 것.
    - 나중에 호출되는 함수
    - 명시적 호출 함수가 아니라, 어떤 이벤트가 발생했거나, 특정 시점에 도달했을때 시스템에서 호출하는 함수
    - call back 함수를 사용하는 이유는 비동기적 프로그래밍을 할 수 있음.
    - 호출방식에 의한 구분.
    - 예
        ```javaScript
        const superhero = ['ironman','captainAmerica','superman']
        superhero.forEach((hero)=> {
            console.log(hero)
        })
        ```
3. javaScript 비동기
    - javaScript는 Single Thread로 작동을 한다.
    - 그런데 어떻게 비동기 처리를 하는지 궁금해서 자료를 찾아보다가, 그림으로 잘 설명된 글이 있어서 퍼왔다.
    - [참고자료](https://bit.ly/2NzCQj7)
    
    - javaScript Engine 구조
        - MEMORY HEAP
        - CALL STACK
            - 단일 호출 스택
            - 하나의 호출 스택만 가지기 때문에, 한번데 단 하나의 함수만 처리 할 수 있다.
    - 자바스크립트는 자바스크립트 엔진만 돌아가는 것이 아니다.
    - Web API, TaskQueue, Loop Event가 런타임에 같이 돌아간다.
        - 먼저 callback함수를 포함한 여러 함수들이 Call Stack에 LIFO형태로 쌓인다.
        - 이때, callback함수를 만나면 이 callback함수를 webAPI로 요청을 한다.
        - Web API
            - 브라우저에서 제공하는 API
            - DOM, Ajax(XML Http Request), setTimeOut,...등의 비동기 작업 실행
            - Web API에서 요청받은 callback함수를 요청에 맞게 수행한 후, 
        - TaskQueue에 callback을 전달한다.
        - Loop Event는 계속해서 CALL STACK과 TaskQueue를 확인하면서
            - CALL STACK이 비어있고, TaskQueue에 callback이 있다면 이를 CALL STACK으로 전달한다.
            - 전달받은 call back을 수행하고 종료한다.

    - 이렇게 비동기 작업(병렬작업)이 내부적으로 동작할 수 있기 때문에, 싱글 스레드인 javaScript이지만
    - 사용자가 요청하는 반응에 느려지지 않도록 구현을 할 수 있다.
    - 이걸 조금더 효과적으로 관리하고 사용하기 위해 (Promise와 async, await가 나왔는데 이도 추후 학습후 업로드 하겠음)

4. Promise
    - 