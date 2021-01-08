# Post CSS

-   Intro

    -   css를 위해 사용되는 도구
    -   js 플러그인을 추가해서, css를 목적에 맞게 변화시켜준다.
    -   원하는 목적에 맞는 플러그인을 찾고, Post css를 적용시킨다.
    -   [공식사이트](https://postcss.org/)
        -   기능 예
            -   *auto-prefixer*제공
            -   _cssdb_: css확장 사용
            -   *css 모듈사용*하는 것(이름이 겹치지 않도록 hash붙여주는 기능과 유사)
            -   *css로 error 피하*기: *styleint*를 통해 작성한 css코드에 문제가 있거나 형식에 맞지 않는 표현이 있을경우 알려줌.
            -   *grid시스템을 calc함수*를 통해 사용할 수 있도록 함.
        -   위 기능들 중, auto-prefixer, stylelint를 적용해보자!

-   **auto prefixer**

    -   prefixer: 접두사
    -   vendor-prefixer:
        -   각 웹브라우저사 별로 스펙에 대한 개발을 진행함.
        -   표준이 되기 이전에 각 브라우저 공급자별로 새로운 실험적인 기능을 제공할 때 이전 버전의 웹 브라우저에 그 사실을 알리기위한 접두사
        -   vendor-prefixer를 사용함으로써, 최신에 제공되는 기능들도, 하위브라우저에서 안전하게 사용할 수 있다.
        -   코딩을 하면서 계속 prefixer를 붙여준다면 굉장히 번거로운 일이다.
        -   Post CSS의 auto-prefixer를 설정해서 해결해보자!

-   실습 순서

    -   postcss, autoprefixer, postcss-loader 설치
        ```console
        npm i postcss autoprefixer postcss-loader -D
        ```
    -   postcss.config.js 파일 생성후 설정
        -   어떤 플러그인을 적용시킬지 파일(모듈)로 별도로 빼서 정의.
        ```js
        module.exports = {
            plugins: [require('autoprefixer')],
        };
        ```
    -   webpack.common.js파일 수정
        -   개발모드, 배포모드 모두 쓰기 위해 여기에 설정
        -   postcss loader 식별자에 할당
            ```js
            const postcssLoader = {
                loader: 'postcss-loader',
                options: {
                    config: {
                        path: 'postcss.config.js',
                    },
                },
            };
            ```
    -   css가 적용되는 순서(먼저 적용시켜야하는게 맨 아래로 가야한다!!!)
        -   'sass-loader': SASS => CSS로 변환
        -   'postcssLoader': 다른 js 플러그인을 css의 목적에 맞게 변화(autoprefix)
        -   'css-loader: css파일을 모듈로써 다룰 수 있도록 변환.(import, require이 가능하도록 함)
        -   MiniCssExtractPlugin.loader: style tag 대신 css 파일로 만들기

-   결과확인
    -   css에 접두사가 붙어있는지 확인할 것
    -   개발자 도구 - Network 탭 - css - 파일 클릭 후 - Preview탭에서 확인
        -   webkit이 붙어있는걸 확인할 수 있다~
    -   단, 브라우저 적용범위를 설정을 해야 벤더사별 접두사가 붙을 수 있음. => Blowsers List(다음챕터)
