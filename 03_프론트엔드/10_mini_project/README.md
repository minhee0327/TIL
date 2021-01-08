# mini-project 개요

## clone coding & toy project

1. old-git: 예전 git사이트 구현
    - 반응형 웹에 초점 두고 구현
    - [예전 사이트 모습](https://heropcode.github.io/GitHub-Responsive/)
    - [강사님 git(완성모습)](https://github.com/HeropCode/GitHub-Responsive)
    - 연습 focus: 반응형 웹페이지
2. TodoList: React 로 구현한 TodoList

    - styled components 활용하기
    - Context API활용해서 상태 전역으로 관리하기

3. catch-the-lion: TypeScript로 구현한 사자잡기 게임
    - parcel bundler활용
        - 설치
            - 개발모드
                - `npm i parcel-bundler -D`
            - 시작 할 위치(entry point 설정)
                - package.json파일의 scripts내부에 설정(나는 요렇게)
                ```json
                "scripts":{
                        "dev": "parcel index.html"
                }
                ```
        - 실행
            - `npm run dev`
            - 컴파일 실시간으로 진행됨. 빠름. 자동적으로 되는점이 많아서 편리.
            - 단 더 많은 옵션과 범용적으로 사용하기위해서는 webpack에도 익숙해지자!
