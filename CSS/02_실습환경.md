1. CSS Reset
    - Chrome 브라우저만 사용하는게 아니기 때문에
    - 브라우저 별로 출력되는 모양이 다를 수 있다. 그래서 기본적으로 제공되는 것을 초기화한다.
    - 방법
        - css에 설정을 하거나
        ```css
        body{
        margin: 0;
        padding: 0; 
        }
        ```
        - reset.css 라이브러리 활용하기
            - reset.css cdn 검색 
            - reset-css CDN by jsDelivr 들어가기
            - reset.min.css (.min: 압축) 파일 copy to clipboard
            - copy html로 해서 붙여넣기 하되, 우리가 작성한 css파일보다 위에서 호출

2. Codepen 이용할 것
    - [민희's codepen](https://codepen.io/dashboard/)
    - 제목을 단원으로 구분해두면 찾기 편할 것 같다.
    - pen 을 들어가서 작성할 수 있음
    - change View
        - editor 위치 조정
        - html 에 ```<body></body>```가 작성되있는 상태임.
        - 맞바로 내용 작성하면 됨.
    - css 왼쪽 톱니바퀴(설정)
        - CSS Base 를 Reset으로 설정하고 하면, reset.css라이브러리 사용한것과 같은 결과
        - 우측 상단 save & close

3. Emmet 문법
    - HTML, CSS 조금 더 편리하게 작성하는 문법
    - .box 하고 tab  => ```<div class="box">```
    - ul.list 하고 tab => ```<ul class="list>"```
    - .container>ul.list>li.list-item*5>a{list$} 하고 tab
    ```html
    <div class="container">
        <ul class="list">
            <li class="list-item"><a href="">list1</a></li>
            <li class="list-item"><a href="">list2</a></li>
            <li class="list-item"><a href="">list3</a></li>
            <li class="list-item"><a href="">list4</a></li>
            <li class="list-item"><a href="">list5</a></li>
        </ul>
    </div>
    ```
    - Emmet plugin 은 대부분 설치 되어있어서 자동완성
    - css에서 Emmet
        - w:100 하고 tab => width: 100px;
        - h:100 하고 tab => height: 100px;