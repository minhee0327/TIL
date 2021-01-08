# 리엑트 & 타입스크립트 (리덕스) 리뷰

- typesafe-actions 사용시 버전 충돌 해결
  - node 13.1.0
  - typesafe-actions@4.2.2
  - "colorette": "^1.2.0" css import 과정에서 node13버전과충돌 (node 14버전일 경우 괜찮을듯)
  - "autoprefixer": @9.8.4 버전으로 다운그레이드(css import에 error)
  - eslint기능 끄고싶어서 : .eslintignore추가
  - typesafe-actions랑 eslint랑 문제가 계속 생기는 것 같아서 devDependencies에 아래추가
    - "@typescript-eslint/eslint-plugin": "^2.23.0",
    - "@typescript-eslint/parser": "^2.23.0"
  - yarn.lock 파일 remove 했기때문에 yarn 으로 설치 시 문제 발생여지 있음
  - npm으로 돌릴것
- 해당 실습폴더로 진행한 것
  1. Counter
  - 기본 TypeScript와 Context API활용
  1. TodoList
  - Redux사용하고, 모듈분리(모듈 분리하는 과정에서 typesafe-actions 라이브러리 활용)
  1. GIT HUB에 가입된 아이디 입력시, 아이디, 이름, 프로필사진 및 블로그주소를 볼수있음.
  - Redux Thunk, Reudx Saga 활용하고 유지보수를 위한 리팩토링 진행
