# Stylelint

- Intro

  - 코드를 작성하다보면, 비즈니스에 몰두한 나머지 일관된 코드를 구현하지 못할 때가 있다.
  - 코딩을 함께 만드는 환경이라면, 팀문화에 맞게 코드를 구현해야하기 때문에 작지만 신경써야한다.
  - 표현의 일관성을 맞추고, 문법적인 문제가 발생하지 않도록 올바르게 작성하는 것도 중요하다.
  - 이를 도와주는 stylelint를 사용해보기!!
  - [참조문서 stylelint](https://github.com/stylelint/stylelint)
  - [참조문서 stylelint-config-standard](https://github.com/stylelint/stylelint-config-standard)

- 실습
  - 모듈설치
  ```
  npm i stylelint stylelint-scss stylelint-webpack-plugin stylelint-config-standard -D
  ```
  - 해야할 것
    - stylint가 webpack에서 동작될수있도록 플러그인 추가
      - webpack.dev.js파일(개발과정에 쓰기 때문)
        - style-webpack-plugin 모듈 가져오고, plugins 설정
      - .stylelintrc파일 생성
        - stylelint-config-standard 설정 적용하기 위한 파일
        - 마지막이 rc로 끝나는 파일은 CLI가 동작될 때 설정들이 반영될 수있도록 하는 공통 파일이름.
        - 나의 경우 prettier 설정때문에 에러가 나는 부분을 해결해가면서 추가함
          ```
          {
          "extends": "stylelint-config-standard",
          "rules": {
                  "indentation": 4,
                  "number-leading-zero": null,
                  "no-missing-end-of-source-newline": null,
              }
          }
          ```
          - iindentation: prettier는 4인데, default가 2였는지 error나서 4로 수정
          - no-missing-end-of-source-newline:null => 문서 맨 마지막단에 \n안들어가야 하는 설정
    - stylint-config-standard라고 하는 설정내용이 lint가 작동했을때 반영되게끔 연결
