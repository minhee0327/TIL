# TypeScript

## Intro

-   JavaScript 대체 언어의 하나로써, JS의 상위확장(superset)
-   ES6의 새로운 기능들을 사용하기 위해, Babel과 같은 별도 트랜스파일러를 사용하지 않아도 ES6의 새로운 기능을 JS Engine(Node, browser...)에서 실행가능
-   ECMA의 표준을 따라갈 수 있는 좋은 수단.



### **장점**

-   **정적타입**
    -   JS는 type을 사전에 타입을 지정하지 않는다.  
        (런타임에서 에러 발생가능성 높음)
    -   TS는 정적타입을 지원하므로 **컴파일 단계에서 오류를 포착**할 수 있다.
    -   대규모 Application 개발 용이 (실수 방지를 하니까)
-   **개발 도구의 지원**
    -   IDE(통합 개발 환경) 포함 다양한 도구 지원
    -   타입정보를 제공함으로써, 타입체크, 자동완성기능, code assist...등을 지원받을 수 있다는 장점이 있다.
-   **객체지향 프로그래밍 지원**
    -   class, interface, module등 강력한 기능을 제공하며 순수 객체 지향 코드를 작성할 수 있다.
-   **크로스 플랫폼 지원**
    -   JS가 실생되는 모든 플랫폼에서 사용가능
-   **DOM제어**
-   **최신 ECMAScript 지원**
-   **JS라이브러리와의 편리한 사용**









-   ## 개발환경

    -   ### Node.js설치
        -   Node.js가 설치된 환경에서 TS를 구동시킬수있다.
    -   ### VSCode (혹은 Webstorm)

        -   타입스크립트 기능 기본 내장되어있음.
        -   TS파일(.ts, .tsconfig.json,..)인식함.
        -   코드 검사, 빠른 수정, 실행 및 디버깅 등 다양한 기능 바로 사용가능.
        -   **단 컴파일러는 별도 설치(전역설치 진행)**
            -   _typescript 컴파일러는 node.js 프로그램_
                ```
                npm install typescript -g
                ```
            -   설치후, 커맨드 창에 `tsc [파일명].ts` 라고 하면 컴파일된 결과물이 나옴
        -   파일경로 보이기 설정: [파일] - [기본설정] - 설정 - [Breadcrumbs: Enabled] 체크

    -   ### **컴파일러 옵션설정**
        -   옵션설정 없이 컴파일을 거치면 ES5 형태 코드로 컴파일이된다.
        -   특정버전으로 사용하고싶을때 사용하는 옵션: `---target`
            ```console
            tsc hello.ts --target es6
            ```
        -   기능적코드 (예: Promise, Promise는 es6 버전 이상) `--lib`
            -   컴파일하면 err: Promise를 찾을수 없다는 error
            -   Promise를 지원하기 위한 별도의 polyfill이 필요하다.
            ```console
            tsc hello.ts --lib es5,es2015.promise,es2015.iterable,dom
            tsc hello ts --lib es2015,dom <!--축약형-->
            ```
            -   dom: console 사용하기 위해 추가
        -   module관련 옵션 `--module`
            -   util.ts파일에서 모듈을 export 해주고, hello.ts파일에서 import로 모듈 가져온 다음 compile진행
            ```
            tsc hello.ts --lib es2015,dom
            ```
            -   컴파일 결과, import가 require로 변경된 것을 확인할 수 있음.
            -   즉 es5는 기본적으로 commonJS시스템을 따르고 있다는 점을 알 수 있다.
            -   따라서 node로 js파일을 실행시키면 실행이 된다.
            -   `target`옵션을 es6로 줘보기
            ```console
            tsc hello.ts --target es6 --lib es2015,dom
            ```
            -   컴파일 결과가 es6버전이기 때문에 arrow function도 보이고, import가 사용된 것이 확인된다.
            -   단, js를 node.js로 실행시키려하면 syntax error를 뿜어낸다.
                -   왜? target은 es6지만 모듈 시스템은 commonJS형태이기때문
                -   해결: `module`옵션으로 해결
                    ```
                    tsc hello.ts --target es6 --lib es2015,dom --module commonjs
                    ```
        -   타입스크립트를 실행할 때마다, 이 옵션을 매번 터미널에 입력해서 실행시켜야할까? Nope!!!!!!
            -   compile 설정할 수 있는 별도 파일이 있음(tsconfig.json)
            -   compile 옵션을 지정할 수 있고 command명령을 통해 어떤 옵션들이 적용되어있는지도 확인할 수 있다. `showConfig`
                ```
                tsc hello.ts --target es6 --lib es2015,dom --module commonjs --showConfig
                ```
            -   configuration 파일을 설정해서 매번 옵션을 CLI에 입력하지 않아도 되게끔 해보자.
    -   ### TypeScript 컴파일러 설정파일(**tsconfig.json**)
        -   tsconfig.json (설정) 파일은 프로젝트의 최상단 위치에 존재하게됨
        -   설정을 주게되면 설정에 의해 컴파일되며, json형태
        -   컴파일하는데 필요한 루트파일과 컴파일러 옵션 설정
            -   `include` :타입스크립트 컴파일러에 포함되어질 파일 목록들
            -   `exclude`: 제외 목록
                -   대체로 typescript는 nodejs기반으로 만들어진다.  
                    `npm init --y ` 로 node project(pakage.json)를 만들고 생성되는 node modules는 typescript 컴파일 대상에서 제외
            -   `compilerOptions` :컴파일러 옵션
                -   예
                    -   `module`
                    -   `target`
                    -   등등
        -   설정 후에는 tsc만 호출해도 현재 dir부터 상위 dir chain을 따라서 tsconfig.json파일을 검색
        -   설정및 컴파일 후, browser에서 확인해보면 원본파일은 보이지 않고 컴파일 된 js파일만 보인다. 만약 원본파일(ts)을 보고싶을 경우 설정을 추가하자. `"sourceMap": true`
