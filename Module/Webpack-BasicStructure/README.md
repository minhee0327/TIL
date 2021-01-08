# 웹팩의 기본 구조
1. 웹팩의 주요속성: entry, output, loader, plugin, mode
    - **entry**
        - 모듈의 의존 관계를 이해하기 위한 *시작점*
        - 웹팩에서 웹 자원을 변환하기 위한 *최초 진입점*이자, 자바스크립트 파일경로
        - entry속성에 지정된 파일에는 웹 App의 전반적인 구조와 내용이 담겨 있어야 함.
            - 이 파일을 가지고, Web App에서 사용되는 모듈들의 연관관계를 이해하고 분석하기 때문 
        - 엔트리 포인트를 분리하는 경우는 SPA가 아닌, 다른 특정 페이지로 진입했을 때, 서버에서 해당 정보를 내려주는 형태의 멀티페이지App에 적합
            ```js
            //SPA
            module.exports = {
                entry: './src/index.js'
            }
            //Multi Page Application
            module.exports ={
                entry:{
                    login: './src/Login.js';
                    main: './src/Main.js';
                }
            }
            
            ```
    - **output**
        - 웹팩을 돌리고 난 결과물의 파일경로
        - 웹팩이 생성하는 번들 파일에 대한 정보를 설정
        - 객체 형태로 옵션을 추가해야함.
            ```js
            let path = require('path');
            module.exports ={
                output: {
                    filename: 'bundle.js'
                    path: path.resolve(__dirname, './dist') //결과: ./dist/bundle.js
                }
            }
            ```
            - 옵션 
                - 최소한 ```filename```은 지정해야함. 웹팩으로 빌드한 파일 명
                - ```path```: 해당 파일의 경로 의미
                - ```path.resolve()```: 인자로 넘어온 경로들을 조합해서 유효한 파일 경로를 만들어주는 Node.js API 
        - 파일이름 옵션
            ```js
                filename: '[name].bundle.js' // 결과 파일 이름에 entry 속성을 포함
                filename: '[id].bundle.js' // 결과 파일 이름에 웹팩 내부적으로 사용하는 모듈 ID 포함하는 옵션
                filename: '[name].[hash].bundle.js' // 매 빌드마다 고유 해시값 붙이는 옵션
                filename: '[chunkhash].bundle.js' //웹팩의 각 모듈 내용을 기준으로 생성된 해시값 붙이는 옵션
            ```
                
    - **loader** (실습: Webpack-Practice에서 진행)
        - 웹팩이 웹 App을 해석할 때 JS 파일이 아닌 웹 자원(HTML, CSS,Images, font...)들을 변환할 수 있도록 도와주는 속성
        - 다양한 모듈들을 입력받아 처리하는 역할
        - 웹팩의 의존성 그래프를 완성시키는 과정에서 의존관계를 가진 다양한 타입의 모듈들을 입력받고 처리하는 역할을 한다.
        - 웹팩이 기본적으로 인식하는 모듈형태는 js, json파일이기 때문에 다른 타입의 모듈들은 개별적으로 loader를 준비해서, 웹팩에 연결해야한다.
        - ```module```이라는 이름을 사용
        - CSS Loader 예시
            ```js
            module.exports = {
                module: {
                    rules:[
                        {
                            test: /\.css$/,
                            use:['css-loader']
                        }
                    ]
                }
            }
            ```
            - ```rules```: 지원해야하는 모듈타입들을 위해 필요한 로더들을 설정하는 공간. (배열타입), 사용하고자 하는 로더 내용을 넣는다.
            - ```test```: 로더 적용할 파일 유형
            - ```use```:해당 파일에 적용할 로더의 이름 
        - 로더의 종류
            - css-loader: css를 모듈로 사용하기 위한 로더
            - style-loader: css로더를 통해 가져온 내용을 header태그 내부에 넣는 로더
            - babel-loader
            - sass-loader
            - ts-loader
            - file-loader
            - vue-loader
        - 로더설치(devDependencies):
            ```console
            npm install --save-dev style-loader css-loader
            ```

    - **plugin** (실습: Webpack-Practice에서 진행)
        - 웹팩의 기본 동작에 추가기능 제공하는 속성
        - 웹팩이 동작하는 과정에 개입할 수 있어서 웹팩이 동작하는 과정에 전반적으로 참여
        - 번들파일에 변화를 주기도하고, 개발모드의 편의성을 제공하거나, production모드에서 코드의 최적화를 하는 등의 역할
        - 해당 결과물의 형태를 바꾸는 역할
            ```js
            let webpack = require('webpack');
            let HtmlWebpackPlugin = require('html-webpack-plugin);

            module.exports = {
                plugins:[
                    new webpack.ProgressPlugin({옵션..}),
                    new HtmlWebpackPlugin({옵션...}) 
                ]
            }
            ```
        - 플러그인의 배열에는 생성자 함수로 생성한 객체 인스턴스만 추가가능
        - 플러그인설치
            ```console
            npm install --save-dev html-webpack-plugin 
            npm i -D html-webpack-plugin <!-- 축약형 -->
            ```
        - 예제에서 사용한 플러그인
            - HtmlWebpackPlugin: 번들러를 위한 HTML파일을 자동으로 만들고 설정해줌. (외부저장소에 있는 플러그인), 웹팩으로 빌드한 결과물로 HTML파일을 생성해주는 플러그인      
            - 옵션으로 template옵션 사용해봄
            - build시, template.html을 기준으로 모듈 번들링된 js 파일(번들결과파일 내용들)이 script태그(혹은 link테그 등등) 에 추가됨. 또한, index.html이 dist폴더에 자동생성됨      

    - **mode**
        - pakage.json
            - 모듈을 기록
                - 프로젝트에서 사용하는 외부모듈을 관리할 때 모듈을 어떻게 기록
                
            - 프로덕션 환경과 개발환경
                - dependencies: 어플리케이션 내부에 직접 포함되는 모듈
                    - 예:jQuery(화면단에 보여져야함)
                    - ```--save```
                - devDependencies: 개발과정에 필요한 모듈
                    - 개발 효율을 높이거나, 코드의 컨벤션 검사, 개발자 코드의 품질 높이는 등 개발 자체에 영향미치는 모듈
                    - ```--save-dev```

            - pakage.json에 모듈을 기록하게되면, 다른환경에서 다시 프로젝트를 세팅할때, 패키지를 일일이 설치하지 않아도 된다. npm으로 pakage.json에 작성된 모듈을 설치할 수 있기 때문이다. 
            - ```npm install```만 해주면 pakage.json에 따라 모듈을 설치해준다.
            - ```scripts```
                ```js
                "scripts":{
                    "build":"webpack"
                }
                ```
                ```console
                npm run build
                ```
                - 터미널환경에서 위와같이 작성하면 번들링(빌드)된다.
                - 결과는 dist 폴더에서 확인
        - mode:'none' or 'development' or 'production'
        - 모드 설정 하지 않으면 기본 production 모드로 작동

2. 환경설정 (windows)
    1. package.json 생성
        - 프로젝트 정보 및 의존성(dependencies) 관리하는 문서
        - 옵션
            -y(--yes)
            -f(--force)
        - 옵션 없이 명령해서, description 수정함
        ```console
        npm init -y
        ```
    2. webpack, webpack-cli 설치
        - webpack: 웹팩의 핵심 패키지.
        - webpack-cli: 터미널에서 webpack 커맨드를 실행할 수 있게 해주는 커맨드 라인 도구
        - 배포X, 개발할때만 필요한 도구이므로, -D 옵션(--save-dev) 추가로 설치함 
        ```console
         npm install --save-dev webpack webpack-cli 
        ```
    3. CLI로 webpack 사용해보기
        1. npx
            - 설치된 패키지(node_modules)안에서 실행파일을 찾아 실행하는 역할
            - .bin폴더 내부에 있는 모듈들은 package에 있는 명령을 실행하는데, 직접 접근해서 실행할 수도 있지만, npx를 사용하면 간편하다.
            ```console
            npx webpack
            ```
            - 웹팩이 설정되어 있지 않을 경우 Error
            - 웹팩 4버전이 되면서 zero configuration을 제공
                - 자주 사용되는 웹팩 설정을 기본적으로 제공해줌
                - entry와 output 설정을 직접하지 않더라도 사용이 가능
                - 단, 반드시 설정할 사항(webpack.configure.json없이 가능토록하는 방법)
                    - entry 경로를 src/index.js 로 준비해야 동작 가능
                    - bundle 파일 위치도 dist 폴더 내부에  나오도록 되어있음
                    - 번들 파일도 main.js로 이름이 결정되어있음

        2. Error: Can't resolve readline ~~~(readline은 Node에서 기본 제공되는 내장 모듈)
            - 웹팩이 실행되고 있는 환경이 Node라는 점을 인식시켜야한다. 
            - 노드환경이라고 인식할 수 있도록, target이라는 key를 설정
            - target: 웹팩이 실행되고 있는 환경을 알려줌
            - 만약 target을 설정하지 않으면 기본환경이 브라우저라고 판단한다.
            ```console
            npx webpack --target=node
            ```
            - dist 폴더 내부에 main.js가 생성이 됨
            - 소스코드가 자동적으로 최적화 된 상태로 들어가짐
            - 번들파일이 잘 작성되어있다면 아래 명령이 정상적으로 실행된다.
            ```console
            node ./dist/main.js
            ```

    4. 설정파일을 만들어서 webpack 사용해보기
        - webpack.config.js 파일 만들기
        - target값은 node(CLI와 동일한 환경)
        - filename: bundle.js로 설정(설정을 안하고 CLI로 만들었던 내용은 main.js로 output되었었음 )
        - 아래 명령으로 실행
        ```console
        npx webpack
        ```
        - bundle.js 에 output 결과가 담기게 됨


