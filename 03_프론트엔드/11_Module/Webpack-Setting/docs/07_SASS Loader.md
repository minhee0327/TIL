# SASS Loader

-   Intro

    -   SASS: css작성시 가독성 높은 표현법 사용, 다양한 문법 제공(css 확장된 형태)
    -   SASS를 사용하는 경우, SASS파일을 css파일로 변환하는 과정을 거쳐야한다.
    -   SASS를 사용하면, 중복되는 코드를 제거하고 조금더 분명하게 css설계가 가능하기 때문에 사용
    -   SASS파일을 모듈로 해석하는 방법에 대한 실습

-   실습
    -   sass-loader, node-sass(node환경에서 sass파일을 읽어들이는 역할) 설치
        ```console
        npm i -D sass-loader node-sass
        ```
    -   **loader chaining**
        -   css를 SASS로 작성할 경우, build된 결과물은 SASS파일이 아닌, css결과물이어야 한다.
        -   과정: SASS모듈을 읽고 해석 => css 파일로 컴파일 => 컴파일된 css파일이 css-loader에 의해 build 결과물을 합쳐서 완성
        -   따라서 SASS-loader를 먼저 작동 => 결과물을 받아서 css-loader 작동
        -   즉, loader를 읽어들이는 순서가 필요한데 이를 chaining이라고 한다.
        -   그동안 loader설정은 use key에 배열로 설정을 했었는데, 이에대한 우선순위는 index크기가 클수록 먼저 적용이 되었었다.
        -   loader의 chaining방식은 index크기로 적용하는 방식 이외에 문자열로 설정 할 수 있다.
    -   **용도에 따라 css 파일들을 loader들이 다르게 적용되도록**
        -   css파일들을 만들때 2가지 목적을 가짐
            -   global 범위 css
            -   local 범위 css: 예: 특정 component 범위 내부에서만 작동
        -   이름을 인식해서 분기처리를 할 예정
            ```
            filename.module.scss => css modules
            filename.scss => global
            ```
        -   적용예
            ```js
            module.exports ={
                module:{
                    rules: [{
                        test: /\.s?css$/i,
                        oneOf: [{
                            test: /\.module\.s?css$/,
                            use: [
                                {
                                    loader: MiniCssExtractPlugin.loader,
                                },
                                {
                                    loader: 'css-loader',
                                    options: {
                                        modules: true,
                                    },
                                },
                                <!-- 축약형으로 작성 -->
                                'sass-loader'
                            ]}, {
                            use: [
                                MiniCssExtractPlugin.loader,
                                'css-loader',
                                'sass-loader'
                                ]
                            }]
                    },
                }
            }
            ```
            -   Oneof 프로퍼티에서 module이라는 keyword에 의해서 global로 적용할지, local로 적용할지 결정
            -   loader적용되는 순서(index 큰 순): sass-loader => css-loader => MiniCssExtractPlugin.loader
            -   css 파일이름에 module이 적용되었을 경우에만 option이 적용이되서 css의 module을 읽을 수 있다.
            -   scss-structure : [7-1 Sass Architecture](https://www.learnhowtoprogram.com/user-interfaces/building-layouts-preprocessors/7-1-sass-architecture)
                -   scss도 import 로 파일을 가져올수있기 때문에 가능한 구조
