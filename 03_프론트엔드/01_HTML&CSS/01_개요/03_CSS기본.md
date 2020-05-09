1. css 기본 골격
    ```
    선택자{
        속성: 값;
        속성: 값;
    }
    ```
    1. 선택자(selector)의 역할
        - HTML에 스타일(css)를 적용하기 위해 HTML 의 특정 요소를 선택하는 sign
        - 스타일을 적용시키려는 대상
        - 대표 종류 2가지  
            - 태그로 찾기
            - 클래스로 찾기 (.)
            - id로 찾기 (#) 
            - 그밖에 다양한 방법은 추후 학습

    2. 속성(properites) 과 값(value)
        - 스타일을 지정할 때 사용
        - 대표 속성
            - 크기: width, height, font-szie...
            - 여백: 
                - margin: 요소 바깥여백, 요소와 요소 사이의 여백(거리,공간)생성
                - padding: 요소 내부 여백, 자식요소를 감싸는 여백
            - 컬러: color(글자 색상), background(요소 색상)
            - 그밖에 다양한 속성및 값들은 추후 학습

2. 선언방식
    1. **인라인선언**
        - 태그에 직접 작성하기
        - 태그에 직접 작성하기 때문에 선택자 필요 없음
        - 예: ```<div style="color:red;">```
        - 일일이 다 작성해야하는 어려움과 수정의 어려움이 크므로  
         직접 작성 피하도록하자
    2. **내장(embeded)**: 
        - HTML에 포함하기
        ```
        <heade>
            <style>
                h1{
                    color: red;
                }
            </style>
        </heade>
        ```
    3. **HTML 외부** 에서 불러오기: 
        - css 코드를 완전히 분리
        - css 파일에 선언된 방식으로, 여러 html파일에 적용할수 있다.
        ```
        <head>
            <link rel="stylesheet" href="/css/main.css">
        </head>
        ```
