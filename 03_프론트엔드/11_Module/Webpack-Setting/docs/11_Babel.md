# Babel

-   Intro

    -   일부 css기능들은 하위 브라우저에서 사요할 수 없는 기능들이기 때문에, 하위브라우저를 호환하기위해 vendor prefixer설정했음.
    -   css처럼 js의 스펙도 마찬가지로 실습했던 ES6스펙이 하위브라우저에서 지원이 안되는 기능들을 내포하고 있음.
    -   Bable
        -   ES6+코드를 하위버전 코드로 transpiling 하기 위한 도구
        -   Babel은 **다양한 모듈을 담는 일종의 상자 역할**. 코드를 컴파일하기 위해 작은 모듈들(ex:presets)을 사용
        -   크로스 브라우징의 혼란을 해결 해 줄 수 있다.
            > 점점 발전해가는 언어의 기능들을 사용하면 *간결하고 명확*하게 표현할 수 있는 기능 혹은
            > *코드를 더 안전하게 작성*할 수 있는
            > 이런 기능들을 *하위 브라우저에서도 안전하게 사용*할 수 있도록 도와주는 도구가 Babel

-   실습
    -   모듈 설치
        ```console
        npm i @babel/cli @babel/core @babel/preset-env babel-loader -D
        npm i @babel/polyfill -D
        ```
        -   `@babel/core`: Bable의 핵심기능이 들어있는 모듈
        -   `@babel/cli` : 터미널에서 코드를 transpile할 수 있는 도구
            -   사용예
            ```console
            babel input.js --out-file output.js
            ```
            -   `babel`: 바벨 호출
            -   `input.js`: transpile하려는 js파일(ES6+)
            -   `--out-file`: babel에 전달할 옵션 (파일로 output하는 옵션)
            -   `output.js`: 출력파일 이름
        -   `@babel/preset-env`: 설치하고 싶은 plugin을 간편하게 사용하기
            -   단 구형 브라우저에서 코드의 길이가 길어질 수 있다.
            -   이때는 원하는 브라우저만 선택적으로 지원하도록 option을 정해주자.
            -   preset이 없을때에는, 플러그인들을 일일이 npm명령으로 설치를하고, 해당 플러그인을 사용하는 것을 .babelrc파일에 알려야 했었는데
            -   preset을 통해서 npm 설치와 babel 설정을 한번만 하면 plugin들이 자동적으로 설치된다
        -   `@babel/loader`:
            -   Webpack이 모듈을 번들링할 때 Babel을 사용하여 ES6+ 코드를 ES5 코드로 트랜스파일링한다.
            -   바벨이 웹팩으로 동작할 수 있도록 설정
        -   `@babel/polyfill`:
            -   preset을 이용하여 하위 버전으로 트렌스파일해도, 브라우저가 지원하지 않는 코드가 남아있을 수 있음
            -   대체할 기능이 없기때문.
            -   구형 브라우저에서도 ES6+에서 새롭게 추가된 객체나 메소드를 사용하기 위해서 설치
            -   현재환경에서 지원이 안되는 상황에서 대체기능을 제공
    -   설정파일(.babelrc 혹은 babel.config.js)
        -   권장: babel.config.js
            ```js
            module.exports = {
                presets: ['@babel/preset-env'],
            };
            ```
    -   webpack 파일 설정(webpack.config.js)
        -   loader 설정하기 (아래내용 rules에 추가)
        ```js
        {
        test: /.js/,
        exclude: /node_modules/,
        loader: 'babel-loader'
        }
        ```
    -   build결과, const가 var로 작성되어있는게 확인됨
        -   Network탭 - js 파일에서 확인
        -   검색키워드: imgElment
    -   `@babel/polyfill` 적용
        -   어플리케이션에서 최초로 한번만 로드 되어야한다.
        -   index.js파일 하나만 사용했으니까 여기서 import 해온다.
            ```
            import '@babel/polyfill';
            ```
        -   서버 띄우고 Network 탭에서 확인해보기!
            -   검색키워드: polyfill
