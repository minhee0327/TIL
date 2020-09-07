# Basic Type

-   js의 기본 타입 지원(6 개의 원시형타입 + 참조형타입)

    ```ts
    //js에서
    //6개의 원시형타입
    let numValue: number;
    let stringValue: string;
    let boolValue: boolean;
    let nullValue: null;
    let undefinedValue: undefined;
    let SymbolValue: symbol; //(es6+)

    //1개의 참조형타입(reference type)
    let objValue: object;
    ```

-   any타입이 가장 상위타입. 하위타입들 모두 할당가능
    -   any> 나머지type >undefined, null
    ```ts
    //ts에서 type을 알지 못할 때.
    // 컴파일 중, 점진적으로 타입 검사를 하거나 하지 않을 수 있다.
    let anyValue: any;
    ```
-   배열
    ```ts
    let stringArray: string[];
    let numArray: number[];
    let anyArray: any[];
    ```
-   인라인 타입

    -   객체가 어떤 속성으로 구성되어있는지를 별도로 선언하지 않고, 인라인으로 설정할 수 있다.
    -   객체에 대한 리터럴 형태로 값이 아니라 type지정

    ```ts
    let user1: { name: string; score: number };
    ```

    -   재사용이 잦은 타입은 인라인타입보다는 타입얼라이언스, 클래스, 인터페이스로 정의하는 것이 유용하다.(다음 챕터)

-   js가 제공하는 type 이외에

    -   tuple, enum, never, void등
    -   그 중 tuple: 안에 들어가야하는 항목들의 갯수와 타입을 정함

    ```ts
    let tuple2: [number, string];
    tuple2 = [1, 'hello'];
    let tuple3: [number, boolean, string];
    tuple3 = [1, true, 'asdf'];
    ```

    -   타입 단언
        -   컴파일러에 값에 대해 나는 잘 알고 있음을 알려줄 때 사용.
        -   온전히 컴파일러만 사용하고, 개발자가 특성 검사를 수행했다고 생각해서 별다른 검사를 하거나 데이터 재구성하지 X.
        -   방법 2가지
            -   angle-bracket
                ```ts
                let some: any = 'this is a String';
                let someLen: number = (<string>some).length;
                ```
            -   `as-`문법(JSX에서 함께사용)
                ```ts
                let some: any = 'this is a string';
                let someLen: number = (some as string).length;
                ```
