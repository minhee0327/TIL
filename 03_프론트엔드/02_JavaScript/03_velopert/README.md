# 강사님 강의 정리하면서 자꾸 잊는 부분만 기록
1. 정보의 은닉성
    - 데이터 (필드)를 외부에서 직접적으로 접근하는 것을 막음
    - 보통은 필드들을 private으로 막아, 객체의 무결성을 보장.
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
    - 함수를 둥록하면 이를 forEach가 실행해줌
    - 예
        ```javaScript
        const superhero = ['ironman','captainAmerica','superman']
        superhero.forEach((hero)=> {
            console.log(hero)
        })
        ```