# 이미지 파일 모듈로 다루어보기(**_file-loader_**)

-   Intro

    -   웹팩은 대부분의 리소스들을 모듈로 다룬다.
    -   css, js 파일 뿐만아니라 이미지파일과 같은 정적인 파일또한 모듈로 다룰 수 있다.
    -   다양한 모듈을 해석하기 위해 loader가 필요 (file-loader, url-loader)

-   **file-loader**

    -   모듈내에서 import나 require로 사용하고자 하는 file을 모듈로 읽어들일 수 있도록 하는 loader
    -   file-loader로 읽은 파일의 경우, build시 output dir경로로 파일을 카피해오는 역할
    -   실습

        -   file-loader 설치

            ```console
            npm i file-loader -D
            ```

        -   webpack.common.js rules 키에 추가.  
            (file-loader는 개발, 배포용 모두 사용되기 때문에 common에서 작성)

            ```js
            module.exports = {
                module: {
                    rules: [
                        {
                            //svg확장자는 url-loader에서 다룰 예정
                            //i의의미: 대소문자 구분 X
                            test: /\.(png|jpe?g|gif)$/i,
                            use: [
                                {
                                    loader: 'file-loader',
                                    options: {
                                        // ext: 확장자 약어
                                        name: '[contenthash].[ext]',
                                    },
                                },
                            ],
                        },
                    ],
                },
            };
            ```

        -   index.js 에서 file import 해오기

            ```js
            import cuteImg from './images/cute.png';

            const imgElement = document.createElement('img');
            imgElement.src = cuteImg;
            ```

    -   결과확인
        -   `npm start`: 이미지 tag내부에 contenthash가 붙여진 src가 들어가짐
        -   `npm run build`: dist 폴더 내부에 이미지 파일 생성됨.
        -   단, image와 같은 정적 리소스는 한 파일에서 관리하고 싶음.
        -   file-loader에 대한 설정을 더 추가.
        -   그전에 모듈들을 관리할 폴더(src) 생성후, index.js, index.css, assets폴더 src 폴더로 이동
        -   entry위치가 src 아래로 변경되었기 때문에, webpack.common.js에서 해당 엔트리 수정
            ```js
            module.exports = {
                entry: './src/index.js',
            };
            ```
    -   파일로더를 통해 빌드를 했을 때, 이미지 파일들이 assets 폴더 내부에 생성되도록 수정하기(2가지)
        -   파일을 참조하는 url정보에 assets 경로가 추가되어야함
        -   file-loader로 읽어들인 모듈들이 dist 폴더안에 맞바로 생성되는 것이 아니라, 그 내부에 assets 폴더안에 생성되게끔 수정.
            -   file-loader options에 추가
                ```js
                publicPath: 'assets/',
                outputPath: 'assets/'
                ```
    -   개발모드일때와 배포모드일때를 분기처리하기
        -   기존에 key에 해당하는 값을 문자열과 객체형태로 작성하여 프로퍼티를 전달 했었는데  
            이번에는 프로퍼티를 함수형태로 전달해볼 것.
        -   함수에 전달되는 매개변수의 경우, loader의 종류별로 상이하기 때문에 해당 공식문서를 확인하고 사용할 것.
        -   실습환경에서는 isProduction에 process.env.NODE_ENV === 'PRODUCTION' 에 대한 boolean값을 저장하고 있어서 해당 식별자로 작성
        -   나머지는 file-loader github문서 참조
        ```js
        module.exports = {
            module: {
                rules: [
                    {
                        test: /\.(png|jpe?g|gif)$/i,
                        loader: 'file-loader',
                        options: {
                            name() {
                                if (!isProduction) {
                                    return '[path][name].[ext]';
                                }
                                return '[contenthash].[ext]';
                            },
                        },
                    },
                ],
            },
        };
        ```

-   실습용 image 자료는 src/images/ 하위에 관리중
-   dist/assets/아래 build결과 나오는 이미지 파일 관리중.
    -   `npm run build`를 하면 dist/assets/내부에 contenthash값이 적용된 파일이 생성되어있음
