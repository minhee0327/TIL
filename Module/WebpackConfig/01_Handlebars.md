# 1. Handlebars & Webpack [템플릿엔진을 웹팩과 함께 활용하기]

- #### Handlebars

  - JS의 [템플릿 엔진](#템플릿-엔진)중 하나.
  - 템플릿 엔진이라 하면, 프로그램 로직과 프레젠테이션 계층 분리 수단.
  - mustache 를 기반으로 구현한 템플릿 인자.
  - mustache(콧수염모양의 {{ }}) Bracket을 이용하여 data 표현하는 것.
  - html페이지에서 HTML + Bracket의 구성으로 디자이너와 개발자가 협업할 때, 디자이너에게 이해하기 쉬운 구조로 협업에 도움이 된다.
  - 확장자(.hbs)를 가지고 컴파일 과정을 거친다.
  - [참조문서](https://sailboat-d.tistory.com/40)

- #### 템플릿 엔진

  - 템플릿 양식과 특정 데이터 모델에 따른 입력자료를 결합하여 원하는 결과문서를 출력하는 소프트웨어
  - 그 중, **웹 탬플릿 엔진**이란 웹문서가 출력되는 엔진을 말한다.
    - Web Template / Database(Model) => Template Engine(Compile) => Web document (View)
    - view Code(html) 과 data logic code(db connection)을 분리해주는 기능
  - **텍스트 템플릿 엔진**
    - 템플릿 양식에 적절한 특정 데이터를 넣고 결과문서 출력
      - Thymeleaf, JSP,...
    - **서버 사이드 템플릿 엔진(Server Side Template Engine)**
      - 역할:서버에서 DB나 API에서 가져온 데이터를 미리 정의된 Template에 넣어 html을 그려, 클라이언트에 전달.
      - HTML에서 고정적으로 사용되는 부분을 template로 만들고 동적으로 생성되는 부분만 템플릿에 소스코드 넣는방식
      - 예(js): _Handlebars_, EJS, Jade,...
    - **클라이언트 사이드 템플릿 엔진(Client Side Template Engine)**
      - 역할: 동적으로 DOM을 그리게 하는 역할
      - 데이터를 받아서, DOM 객체에 동적으로 그려주는 프로세스 담당
      - 예를 들어, 공통적인 프레임을 미리 제작한 것을 template이라고 한다.
      - script타입을 미리 만들어서 사용
      - _필요성_
        - HTML DOM이 다 그려진 뒤, 서버 통신 없이 화면변경이 필요한 경우.
        - 단일 화면에서 특정 이벤트에 따라 화면이 계속 변경되어야하는 경우.
      - 예: _Handlebars_, Mustache, ...
    - 과정
      - 클라이언트에서 공통적인 프레임(template) 개발
      - 서버에서 필요한 데이터 요청
      - 데이터를 template의 적절한 위치에 대체한 후 DOM객체에 동적으로 전달
    - 필요성
      - HTML에 비해 간단한 문법을 사용하여 _코드량을 줄임_
      - 데이터만 바뀌는 경우가 많기 때문에 *재사용성*이 높아짐
      - _유지보수_ 용이
  - [참조문서](https://gmlwjd9405.github.io/2018/12/21/template-engine.html)

- #### 실습
  - handlebars 모듈설치
    ```console
    npm i handlebars -D
    ```
  - .hbs 확장자를 읽을 수 있도록 handlebars-loader설치 후, loader에 설정
    ```console
    npm i handlebars-loader -D
    ```
    - 옵션없이 사용시
    ```js
    {
        test: /\.hbs$/,
        use:['handlebars-loader']
    }
    ```
  - plugin
    - HtmlWebpackPlugin으로 Data를 전달하게 될 때 plugin설정
    ```js
    plugins:[
        new HtmlWebpackPlugin({
            title:'Webpack',
            template:'./template.hbs'
        })
    ],
    ```
    - 위와같이 설정시, 데이터가 hbs쪽에서 아래와 같이 작성해서 title값을 받아올 수 있다.
    - template.hbs에 아래 작성
    ```html
    {{htmlWebpackPlugin.optioins.title}}
    ```
  - build(bundle) 결과 확인하기
    ```
    npm run build
    ```
  - meta 태그도 위와 같은 방법으로 적용해보기.
    - webpack.config.js 내부 meta키 확인
    - template.hbs 에 작성된 meta태그를 지우고 build 해보기
    

