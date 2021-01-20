# 이미지 파일 모듈로 다루어보기(**_url-loader_**)

-   Intro

    -   file-loader와 url-loader 비교: 출력의 형태가 다름
        ```
        - file-loader: 모듈로 파일을 입력받고, 특정파일을 출력.
        - url-loader: 파일을 입력받고, Data URIs라는 특정한 형태로 변환된 문자열 반환.
        ```
    -   url loader는 작은 이미지와 같은 리소스들을 문자열 형태로 변환
    -   인라인 형태로 적용되는 리소스
    -   Data URIs는 4가지 파트로 나뉨
        -   _data:mediatype;base64,data_
    -   이와 같이 한줄의 문자열 형태로 반환해 주는 것을 url-loader라고 한다.

-   실습

    -   url-loader 설치
        ```
        npm i -D url-loader
        ```
    -   svg 파일만 url-loader 적용할 것
    -   loader 설정하기(webpack.common.js)
        -   options
            -   limit: byte크기 단위의 숫자(파일크기 제한 )
        ```js
        {
            test: /\.svg$/i,
            use: [{
            loader: 'url-loader',
            options: {
                limit: 8192 //약 8KB까지만 적용
                }
            }]
        },
        ```
    -   서버 실행 시켜서 개발자도구 창의 element 의 src attribute 확인하기
        ```html
        <img src="data:image/svg+xml;base64,P...tMzN6Ii8+CjwvZz4KPC9zdmc+Cg==" />
        ```
        -   위와 같이 나옴.(8KB크기로)
        -   network 탭에서 svg를 읽어들이는 모습을 보자

-   Data URIs사용하는 이점?

    -   리소스 요청수를 줄일 수 있음
    -   uri로 바뀐 데이터는 문자열 형태로 바뀌어서 바로 문서에서 적용되기때문에 작은 이미지의 경우, 문자열로 바뀐 값들이 부담이 되지 않는 정도의 크기 이기때문에 문서를 다운받는 시간에 영향을 주지 않음
    -   파일 크기가 크거나, 중요한 파일을 빠르게 불러올 수 있는 이점이 있다.

-   fall-back
    -   만약 url-loader가 사용이 잘 안되었다면, default는 file-loader로 진행이 된다.
    -   예를들어 limit설정을 넘어선 파일의 경우에는 url-loader가 아닌, file-loader를 사용한다.
