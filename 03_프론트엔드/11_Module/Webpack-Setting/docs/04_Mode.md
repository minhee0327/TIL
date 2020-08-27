# 4. Mode(Development mode & Production Mode)

- #### intro

  - 프로젝트의 환경설정을 하다보면, 개발자가 개발을 효율적으로 하기 위해 개발과정에서 도움이 되는 여러 설정을 세팅하게 되고
  - 사용자를 위해서는 정확하게 기능이 되면서도 빠르게 리소스가 전달이 되기 위해 최적화를 진행
  - mode설정을 할때 2가지 종류가 있었음(development, production mode)
    - 난독화: 사용자를 위한 설정 => production mode
    - build 명령을 수행했을 때, 조건이 늘어날때마다 build시간이 길어졌었음
    - 개발하는 과정에서 기능을 추가하거나 코드를 수정했을 때, App기능이 잘 되는지 화면을 매번 확인했어햐 했는데  
      이 때, build시간이 길어지면 개발 효율이 떨어지게 됨.
    - 최적화 관련 설정을 production모드에서만 가능하도록 분리를 해야함.
      - 개발 과정이 끝나고 진행해도 늦지는 않음.
      - 개발 하는 과정중에 진행하면 빠르게 수정사항에 대한 변화를 확인할 수 있음
    - production환경을 구분짓고, 개발 과정에 도움되는 여러 환경설정에 대해 다뤄보자.
  - 각 환경에 따라 빌드과정을 다르게 구분 짓기 위해 웹팩 머지를 통해 각 환경에 따른 파일을 따로 만들고, 스크립트 실행
    - 3개의 설정 파일
      - 공통적인 환경설정 파일
      - 개발담당 파일
      - 프로덕션 담당 파일
    - 각 설정 파일을 모드값이 적용된 상태로 진행

- #### 실습: dev, product, common파일 분리하기

  - webpack-merge 설치

    ```console
    npm i -D webpack-merge
    ```

    - merge function 을 사용하기 위해서는, merge함수를 그냥 import 해오면 안되고, {}로 감싸야한다.

  - webpack.common.js 파일에 공통적으로 사용하는 내용 분리

    - optimization과 최적화 관련 내용 제거
    - mode도 dev파일, production파일에서 설정하기 위해 삭제

  - webpack.dev.js (개발자 모드 파일)

    - 일단 공통적으로 설정하는 내용을 가져와야하기 때문에 webpack.common.js파일을 불러옴
    - merge를 통해 dev의 환경설정파일을 병합
    - dev쪽은 바로 이어서 개발환경을 위한 설정 진행.

  - webpack.prod.js (사용자 모드 파일)

    - optimization,최적화 관련된 내용이 들은 config 를 만들었고
    - 이를 common이라는 기본설정 파일과 병합해서 module.exports 로 내보냄.

  - 빌드 모드마다 다른 파일을 불러올 수 있도록, pakage.json파일 수정하기
    ```json
    "scripts": {
      "dev": "webpack --config webpack.dev.js",
      "build": "webpack --config webpack.prod.js"
    },
    ```
  - 각 모드별로 빌드명령 다름
    - dev: 개발자모드 (빌드시 `npm run dev`)
    - build: 사용자모드 (빌드시 `npm run build`)
  - define-plugin 설치

    - 웹팩이 빌드를 진행할때 특정 상수값을 만들어서 모듈들이 어디서든 쓸 수 있게 함
    - 현재 빌드되고 있는 모드가 production인지 유무를 알고 싶다면, 이 플러그인을 통해 모든 모듈에서 사용될 수 있도록 설정이 가능
    - webpack모듈 내부에 있는 plugin이라서 npm으로 별도로 설치할 필요는없고, 모듈을 불러와서 사용하면됨.
      - 모듈 전역으로 제공되는 상수값 지정해주어야하는데, plugin객체의 인자로 전달이 가능하다.
      - 이름은 IS_PRODUCTION이라고 지었음.  
        (true일경우 production build라는 의미로 진행)
        ```js
        const webpack = require('webpack');
        module.exports = {
          plugins: [
            new webpack.DefinePlugin({
              IS_PRODUCTION: true,
            }),
          ],
        };
        ```
      - 빌드 모드에 따라 IS_PRODUCTION값이 달라질 수 있도록, package.json 의 script설정 수정
        ```json
        "scripts": {
          "dev": "NODE_ENV=DEVELOPMENT webpack --config webpack.dev.js",
          "build": "NODE_ENV=PRODUCTION webpack --config webpack.prod.js"
        },
        ```
      - 위와같이 NODE_ENV값을 할당하면, node환경에서 process.env객체에 담긴 node_env에 접근할 수 있게됨.
      - windows에서는 추가 설치를 해야한다.(`npm install -g win-node-env`)
      - package.json에서 할당한 값을 IS_PRODUCTION변수에 담아서 webpack.common.js에 사용할 것
      - HTMLWebpackPlugin에 minify설정 중, IS_PRODUCTION 결과가 dev일 때는 압축이 안되도록, production일때는 압축되도록 설정  
        삼항연산자 활용
        ```js
        minify: isProduction ? {
          collapseWhitespace: true,
          useShortDoctype: true,
          removeScriptTypeAttributes: true,
        } : false,
        ```
      - `npm run dev`: 압축 안된상태(index.html확인)
      - `npm run build`: 압축 된 상태(index.html)

- #### 개발모드 세팅(webpack.dev.js)

  - 개발모드는 개발하는 과정을 위해 지원된 환경
  - 개발하는 과정에서 요구사항 분석하고, 필요한 기능을 구현하는 과정을 반복
  - 개발모드는 개발과정을 위한 편의성을 제공함.
  - 개발 생산성을 향상시키는 여러 option으로 이루어져있다.
  - 웹팩에서 특별한 local server를 지원함. 이걸 사용하기 위해 설치해야하는 모듈

    - webpack.common.js 파일에 DefinePlugin내용 수정(true => isProduction)
      - isProduction를 사용해서 true로 고정된 값이 아닌 동적인 값을 할당.(true/false)
      ```js
      new webpack.DefinePlugin({
        IS_PRODUCTION: isProduction,
      }),
      ```
    - webpack-dev-server모듈 설치
      ```
      npm i -D webpack-dev-server
      ```
      - 서버를 띄우기 위해서, 이 모듈에서 지원하는 명령어를 실행해야한다.
      ```console
      <!--나는 아래 명령만으로도 실행이 되었음..-->
      ./node_modules/.bin/webpack-dev-server
      <!-- 아래명령으로 실행, json파일에 설정한 내용-->
      ./node_modules/.bin/webpack-dev-server --config webpack.dev.js
      <!-- 명령어 길어서, package.json의 scripts에 start키로 등록하기-->
      ```
    - package.json

      ```json
      "scripts": {
        "start": "NODE_ENV=DEVELOPMENT webpack-dev-server --config webpack.dev.js",
      }
      <!-- npm start하면 이제 server띄워짐! -->
      ```

      - 연결된 포트번호로 접속하면 구현한 웹문서들을 브라우저에서 바로 확인가능
      - dist 폴더 내부 파일들이 사라져있음. 또한 dist 폴더를 삭제하고 새로고침하더라도 사용가능
      - build 결과물이 파일로 쓰이지 않는다는 의미
      - **webpack-build-server를 통해 빌드된 결과물은 메모리상에 있기 때문에 직접 파일을 쓰고 지우는 방식보다 빠름**
      - 수정된 결과물도 메모리상에 있는 결과값과 비교해서 바로 수정되는 것을 확인할 수 있음
      - 파일을 지우고 쓰고 하는 반복과정 없이, 개발을 하기 때문에 수정사항에 대한 피드백을 훨씬 빠르게 받을수있다.
      - file protocol이 아닌 환경으로 contents가 제공되고 있음
      - 기존에는 index.html을 open with live server로 확인을 해야했는데,  
        dev server를 쓰면 서버가 띄워진 상태이기 때문에 접근이 풜씬 쉽고,  
        cross-origin 설정내용도 나중에 API서버를 만들 때 확인할 수 있고,  
        HTTP url로 접근하기 때문에 실제 웹서비스에서 어떤식으로 이용될지에 대해 여러 생각을 해볼 수 있는 환경이 제공된다.
      - webpack-dev-server는 파일변화를 감지했을때,
        - 다시 빌드를 실행하는 실행하는 watch라는 옵션이 적용되어있음
        - live-reloading환경 지원 (수정사항이 생겼을때 다시 refresh할 필요 없음)
      - **_history-api-fullback_**

        - dev-server에서 제공하는 라우팅과 관련된 key.
        - 정 라우팅을 지정했을 때 우리가 제공하지 않는 라우팅으로 가게되면 예외처리를 하거나 특정 라우팅은 특정한 html문서로 이동할수 있게끔 지원하는 기능
        - false는 이 기능을 사용하지 않는다는 의미
          `historyApiFallback: false`
        - false로 해두고 개발자도구의 Network탭을 확인해보면, 내가 구현하지 않은 경로의 웹문서를 호출하면 status에서 404 를 볼 수 있다. (없는 문서 의미)
        - 예: localhost:[port]/hello => 구현 안된 페이지
          - status : 404
          - historyApiFallback으로 특정 위치 이동 가능
        - 만약 `historyApiFallback: true`이면
          - root dir의 index.html으로 이동
          - 경로가 없음에도 불구하고 status가 404가 아닌 200이 뜬다.
        - 혹은 객체로 값을 할당해서, 특정 경로로 이동할 수 있게도 가능하다.

          - rewrites key에 배열값으로 특정경로를 지정한다.

            ```js
            const config = {
              mode: 'development',
              devServer: {
                historyApiFallback: {
                  rewrites: [{ from: /^\/subpage$/, to: 'subpage.html' }],
                },
              },
            };
            ```

            - subpage 입력시, subpage.html로드
            - 없는 페이지 입력시, root dir의 index.html 로드

        - 특정 경로를 제외한 나머지 모든 페이지는 404 페이지로 보내보자.
          ```js
          ...
          rewrites: [
            { from: /^\/subpage$/, to: 'subpage.html' },
            { from: /./, to: '404.html' },
          ],
          ```

      - **_open_**

        - 최초로 웹팩과 관련된 실행을 했을 때, 새로운 탭으로 기본브라우저가 자동으로 실행
          ```js
          devServer: {
            open:true,
          }
          ```
        - 최초 작업시 브라우저를 별도로 열어도 될 필요가 없어서 편리함.

      - **_overlay_**

        - error msg가 떴을때 console.log로 확인하는게 아니라, 에러메세지 자체가 화면에 나오도록 만든다.

      - **_port_**
        - port 번호 지정
        
 [이전페이지](https://bit.ly/2EoeAjj)
