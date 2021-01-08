# JavaScript(기본문법 + es6)

1. ES5와 ES6의 차이점 요약
    - ES6 에 템플릿 리터럴 사용
        ```javascript
        let name = 'Minhee';
        let age = 30;
        console.log(`저의 이름은 ${name}이고 나이는 ${age}입니다.`)
        ```

    - 함수선언 방식
        - ES5에서 함수선언(3가지)
            - 함수 선언식
                ```javaScript
                function a(arg1, arg2){
                    console.log(arg1, arg2)
                }
                ```
            - 생성자 함수(많이 사용 X)
                ```javaScript
                var a = new Function('arg1','arg2','console.log(arg1, arg2)');
                ```
            - 함수 리터럴
                ```javaScript
                var a = function(arg1, arg2){
                    console.log(arg1, arg2);
                }
                ```
        - ES6에 추가된방식
            - arrow function(화살표 함수)
                ```javaScript
                var a = (arg1, arg2) => {
                    console.log(arg1, arg2);
                }
                ``` 
                - arrow function에서 하나의 arg만 있다면, 괄호 생략 가능
                - arg 값이 없다면 빈 괄호 써야한다.
                - 한줄로 표현이 가능하다면 {} 생략가능
    - 변수 선언
        - ES6에서 let, const 를 추가로 사용할 수 있음
        - const는 상수, 재할당 불가
        - let 은 hoisting이 일어나지 않음
        - let, const의 scope는 {} (블럭) 내부이지만
        - var의 경우 function scope를 따름.

    - 클래스 선언
        - ES5에서 클래스선언, 상속등은 prototype을 실현됨
        - ES6에서 class 키워드 사용해서 명시적으로 사용가능해짐
            - extends, constructor, super 키워드 사용

    - this의 다른 동작
        - 객체 안에서 동작
        - 함수 내부에서 호출했을 때는, 전역을 가리킴
        - 생성자 함수의 경우, 인스턴스를 가리킴
        - call, apply메소드 활용하여 첫번째 arg에 this바인딩
        - arrow function의 경우, 함수가 선언된 스코프에서만 자동바인딩
        함수 선언된 스코프 내부에 있지 않다면, bind되지 않음
    - 모듈
        - ES6에서 공식적으로 제공하기 전까지는 CommonJS, AMD, RequireJS등 비공식 모듈 스펙을 사용해왔음.
        - ES6에서 `import`, `export`사용해서 commonJS와 유사하게쓰임
        - ES6 확정되었지만, 모든 브라우저에서 완전하게 지원되지 않음
        - 따라서 ES6 사용하려면 `Babel`과 같은 컴파일러 사용해야함.
        - Grunt, Gulp및 Webpack용 Babel 플러그인이 있음.
        - (Webpack파트에서 확인)

    - 반복문에 for in/ for of
    - 키워드 매개변수 사용가능해짐(default처리 방식 변화)
    - 멀티라인 문자열(`(백틱)이용해서 + 넣지 않고도 맞바로 사용가능)
    - 비구조화 할당(이는 react할때 한번 더 자세하게 학습)
    - Promises