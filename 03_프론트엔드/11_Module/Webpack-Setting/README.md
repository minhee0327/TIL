# 웹팩 설정하기

### [1. Handlebars & Webpack (템플릿엔진을 웹팩과 함께 활용하기)](https://bit.ly/2EocDmZ)

### [2. Caching & Webpack (hash, contenthash, chunkhash)](https://bit.ly/34C86aZ)

### [3. Minification & Mangling (간결&난독)](https://bit.ly/2YVE12L)

### [4. Mode(Development mode & Production Mode)](https://bit.ly/3jdugV4)

#### 5. 참고

- 1-4 번까지 한 페이지에 작성했는데 내용이 길어서 파일별로 분할했음.(docs폴더에 있음)

- 사용한 loader
  - css-loader: css파일들을 읽음
  - style-loader: 읽은 css파일들을 style태그로 만들어 head 태그 안에 넣어줌
  - handlebars-loader: template engin
  - mini-css-extract-plugin: style태그 대신 css파일로 만들고 싶을 때 사용
- OS 환경(windows)

  - 강사님이 mac을 사용하고 계셔서 종종 ERR 뿜뿜을 했다.
  - NODE_ENV의 경우, 추가 설치를 해야한다.(`npm install -g win-node-env`)
  - 그리고 모듈을 설치할 때에도 -D(--save-dev)를 맨 뒤에 붙이면 ERR난다. 인스톨 명령어 다음에 붙여서 모듈설치하자.

- git
  - dist 폴더내부에 있는 파일을 올리지 말까하다가, production 모드로 올려두었다.
  - 파일명, 내부 상태가 어떻게 달라졌는지 눈으로 보자.
