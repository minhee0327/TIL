# Webpack-Practice 
## Loader & Plugin 실습폴더

- **CSS RESET**
    - *user Agent Style*: 브라우저 자체에 포함된 기본 스타일링 정보
    - 각 브라우저는 각각 기본 스타일이 설정이 되어있고, 이로인해 브라우저간에 표시가  
    생각처럼 되지 않을때가 있다. 따라서 user agent style을 *표준*화할 필요성이 있는데 이를 CSS RESET이라고 한다.
    -  종류
        - Reset.CSS: 적용된 css 제거
        - *Normalize.css*: 브라우저간 차이점을 수정하고, 사용하기 좋은 기본값은 유지
        - HTML5 Doctor CSS Reset
        - Yahoo! (YUI 3) Reset CSS
        - Universal Selector ‘*’ Reset
    - 이번 실습에서는 Normalize.css를 적용해서 사용해볼것.
    - (기존 css 실습했을때엔 Reset.css를 적용해보았음)
    - 크로스브라우징의 기본이라고 할 수 있다.

- Normalize.css 설치
    - console
        ```console
        npm install --save normalize.css
        ```
    - index.js
        ```js
        import 'noramlize.css'
        ```
    -  빌드(번들링) 후 개발자도구 확인

- loader 설정은 ```moules```에 한다.
    - 로더의 규칙 (```rule```) 을 정할 수 있다.
        - ```test```에서 정규식으로 어떤 확장파일인지 알려준다.
        - ```use```: 어떤 loader를 적용히실지 배열형태로 다룬다.
            - 내부에서 객체형태로 loader의 종류와, options종류를 객체형태로 정할 수 있다.
            - css-loader
                - ```loader:'css-loader'```
                - ```options```공식문서 참조(여러종류있음)
                    - modules: css 모듈에 대한 사용여부 결정. css파일을 모듈로 불러오고 class이름을 js에 불러와서 사용할 수있게 됨. css파일별로 class이름이 같아도, 겹치지 않는다는 장접이 있음
            - style-loader
                -```options:{injectType:'singletonStyleTag'}```
                    - 기존에는 처리하는 css 파일별로 스타일 태그를 만듬
                    - 스타일 태그 하나에 한번에 css들을 가져올 수있도록 지정함

- plugin
    