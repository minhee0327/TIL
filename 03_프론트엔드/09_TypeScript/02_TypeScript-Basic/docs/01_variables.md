# variable

-   선언(js와 동일한 방법)

    -   typeScript는 한번 변수를 선언하고 초기값을 할당하면, 타입이 고정이된다.

        ```ts
        function outer() {
            if (true) {
                let score = 0; //선언과 동시에 타입 number로 고정됨
                score = 30; //number type가능
                score = '30'; //error(type이 number가 아니기 때문!)
            }
        }
        ```

    -   변수를 선언하고 초기값을 할당하지 않으면, any타입.

        ```ts
        function outer() {
            if (true) {
                let score; //선언만 하고 할당하지 않을경우 어떤타입이든 가능한 'any'타입
                score = 30; // number type가능
                score = '30'; // string type 가능
            }
        }
        ```

    -   type annotaion으로 해당 변수의 type지정하기

        ```ts
        function outer() {
            if (true) {
                let score: number; //type annotaion(:number) 지정하는 방법
                score = 30; // ok
                score = '30'; //error (non number)
            }
        }
        ```

    -   var와 let의 큰차이점: scope

        -   var: **함수스코프**, 함수 내부에 선언된 변수를 함수 밖에서 접근 불가

            ```js
            function outer() {
                function inner() {
                    var score = 0;
                }
                console.log(score); //score에 접근불가능
            }
            ```

            ```js
            function outer() {
                if (true) {
                    var score = 0;
                }
                for (var i = 0; i < 3; i++) {
                    setTimeout(() => {
                        console.log(i); //0 1 2를 예상했겠지만 Nope! (3 3 3이 출력된다.)
                    }, 100);
                }
                console.log(score); //if문 에서 할당한 0이 출력된다. (같은 함수 scope에 있기 때문)
            }
            ```

        -   let: (es6) **block단위 스코프**

    -   const: (es6) - **block단위 스코프**
        -   상수: 한번 정해지면 변하지 않는값. 따라서 선언시 무조건 초깃값 할당해야함.
            -   따라서 type annotaion을 사용하지 않더라도 자동으로 type이 지정됨.(값을 무조건 할당하니까)
            ```ts
            const score1: number = 100; //ok
            const score2 = 100; //ok
            score2 = 30; //error (상수는 한번 할당하면 재할당 불가)
            ```

# variable

-   선언(js와 동일한 방법)

    -   typeScript는 한번 변수를 선언하고 초기값을 할당하면, 타입이 고정이된다.

        ```ts
        function outer() {
            if (true) {
                let score = 0; //선언과 동시에 타입 number로 고정됨
                score = 30; //number type가능
                score = '30'; //error(type이 number가 아니기 때문!)
            }
        }
        ```

    -   변수를 선언하고 초기값을 할당하지 않으면, any타입.

        ```ts
        function outer() {
            if (true) {
                let score; //선언만 하고 할당하지 않을경우 어떤타입이든 가능한 'any'타입
                score = 30; // number type가능
                score = '30'; // string type 가능
            }
        }
        ```

    -   type annotaion으로 해당 변수의 type지정하기

        ```ts
        function outer() {
            if (true) {
                let score: number; //type annotaion(:number) 지정하는 방법
                score = 30; // ok
                score = '30'; //error (non number)
            }
        }
        ```

    -   var와 let의 큰차이점: scope

        -   var: **함수스코프**, 함수 내부에 선언된 변수를 함수 밖에서 접근 불가

            ```js
            function outer() {
                function inner() {
                    var score = 0;
                }
                console.log(score); //score에 접근불가능
            }
            ```

            ```js
            function outer() {
                if (true) {
                    var score = 0;
                }
                for (var i = 0; i < 3; i++) {
                    setTimeout(() => {
                        console.log(i); //0 1 2를 예상했겠지만 Nope! (3 3 3이 출력된다.)
                    }, 100);
                }
                console.log(score); //if문 에서 할당한 0이 출력된다. (같은 함수 scope에 있기 때문)
            }
            ```

        -   let: (es6) **block단위 스코프**

    -   const: (es6) - **block단위 스코프**
        -   상수: 한번 정해지면 변하지 않는값. 따라서 선언시 무조건 초깃값 할당해야함.
            -   따라서 type annotaion을 사용하지 않더라도 자동으로 type이 지정됨.(값을 무조건 할당하니까)
            ```ts
            const score1: number = 100; //ok
            const score2 = 100; //ok
            score2 = 30; //error (상수는 한번 할당하면 재할당 불가)
            ```
