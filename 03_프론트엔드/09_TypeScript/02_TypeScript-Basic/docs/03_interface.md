# 인터페이스

1. 개요

    - 객체가 가진 프로퍼티나 메소드를 선언
    - 인터페이스는 타입의 이름을 지정하는 역할.

2. 선택적 프로퍼티

    - 인터페이스의 모든 프로퍼티를 사용하는 것은 아님.
    - 어떤 조건에서만 존재하거나 아예 없을 수도 있다.
    - 객체 안의 몇개의 프로퍼티만 채워 합수에 전달하는 패턴 ('option bags') 에 유용
    - 인터페이스에 속하지 않는 프로퍼티의 사용을 방지하면서도 사용가능한 속성을 기술한다.

3. 읽기전용 프로퍼티(`readonly`)

    - 생성 후변경하지 않음을 보장
    - readonly 가 붙어있으면, 일반 값이나 배열에 재할당 불가능
    - 타입단언(`as`로는 가능)
    - 주로 property사용에 사용하면 좋다. (변수 선언에는 const)

    ```ts
    let a: number[] = [1, 2, 3, 4];
    let ro: ReadonlyArray<number> = a;

    ro[0] = 3; // error
    ro.push(5); // error
    ro.length = 100; //error
    a = ro; //error
    ```

-   추가 프로퍼티 검사
    ```ts
    interface SquareConfig {
        color?: string;
        width?: number;
    }
    function createSquare(config: SquareConfig): { color: string; area: number } {
        // ...
    }
    // coloir이라는 속성은 없음 따라서 에러
    let mySquare = createSquare({ coloir: 'black', width: 10 });
    ```
    -   정의한 인터페이스보다 더 많은 프로퍼티를 선언해서 넘겨주었을 경우 컴파일 에러
    -   해결방법(3)
        -   타입단언을 먼저 사용해서 추가 프로퍼티 검사를 피해가도록 한다.
        ```ts
        let mySquare = createSquare({ coloir: 'black', width: 10 } as SquareConfig);
        ```
        -   특별한 경우, 문자열 인덱스 서명을 추가.
        ```ts
        interface SquareConfig {
            color?: string;
            width?: number;
            [propName: string]: any;
        }
        ```
        -   객체를 다른 변수에 할당
            -   단, 변수가 공통 객체 프로퍼티가 없을경우 에러남(현재는 공통 프로퍼티로 width)
        ```ts
        let squareOptions = { coloir: 'black', width: 10 }; //이렇게 변수 할당하면 검사를 하지 추가프로퍼티 검사 X
        let mySquare = createSquare(squareOptions);
        ```
-   함수타입

    -   인터페이스는 함수타입을 설명할 수 있음.
    -   매개 변수 목록과 반환타입만 주어진 함수 선언과 비슷
    -   call signature를 전달

    ```ts
    interface SearchFunc {
        (source: string, substring: string): boolean;
    }

    let mySearch: SearchFunc;
    mySearch = function (src: string, sub: string): boolean {
        let ret = src.search(sub);
        return ret > -1;
    };
    ```
