# 3. Minification & Mangling

- 네트워크를 통해 전송되는 resource양이 커지면 사용자들에게 전달되는 컨텐츠 도착시간이 길어짐.  
  그래서, 최종적으로 사용자에게 전달되는 리소스들의 형태는 불필요한 요소를 제거한 **최적화된 상태**가 되어야하는데, 소스코드와 리소스들을 최적화할 때 어떻게 하는지 살펴보기.
- 모드값이 production인 경우, 소스코드가 압축된 상태를 확인했었는데 mode를 사용하지 않고 직접 최적화함으로써 js뿐만아니라 다른 자원들도 어떻게 최적화 시키는지 알아보자.
- 코드의 형태를 압축
- 압축과정에서 일어나는 일
  - **Minification**
    - 어플리케이션이 동작하는 과정에 관여하지 않는 요소 제거(주석, console.log,..) - 용량이 줄어듬
    - 표현을 간결화 (들여쓰기 또는 띄어쓰기 공백을 최대한 짧게, 분기문을 블럭형식 대신 삼항연산자로 표현 등)
  - **Minification: 표현의 난독화(uglify)**
    - 변수, 함수 클래스 이름같은 코드를 구성하는 표현을 알파벳 한두글자로 치환.
    - 외부에서 코드를 봤을때 코드를 분석하기 어렵게 만듬, 용량줄임
- 위와같은 과정을 거치면, 소스코드가 압축된 형태로 나오게 되는데 네트워크에 이 최적화된 리소스가 전달이 되고 최적화된 리소스들이 캐싱으로 저장되면
  사용자들이 App을 사용할 때 더 빠르게 동작시킬 수가 있다.

- #### 실습

  - **HTML Markup 최적화**

    - html-webpack-plugin설정에서 제공되는 key중 minify이라는 key가 제공됨.
    - mark up 이 생성될때 mark up 컨텐츠가 최적화되는 과정을 함께 진행함
    - 객체형태로 지정해서 선택적으로 (일부만) 최적화를 진행할 수 있다.
    - html-webpack-plugin [readme.md](https://github.com/jantimon/html-webpack-plugin) 문서 확인. (minify검색 상세 링크 클릭)
    - 실습에서는 공백을 줄이는것, doctype을 짧게 사용하는 것, type attribute 제거 사용
    - plugin 에 minify key와 옵션 추가
      ```js
      minify:{
                collapseWhitespace: true,
                useShortDoctype: true,
                removeScriptTypeAttributes: true, //script에 type attribute 제거
            },
      ```
    - 빌드 후, 결과확인

  - **CSS 최적화**

    - css파일크기 압축([css-nano compressor](https://cssnano.co/))
    - 스타일을 보다 빠르게 제공
    - css-nano를 사용하면 css를 최소화 한 결과물을 얻을 수 있고, 압축률 정보도 확인이 가능
    - css-nano module설치하기
      ```
      npm i -D cssnano
      ```
    - [optimize-css-assets-webpack-plugin 설치](https://github.com/NMFR/optimize-css-assets-webpack-plugin)
      ```
      npm i -D optimize-css-assets-webpack-plugin
      ```
    - webpack plugins 설정
      ```js
      plugins: [
        new OptimizeCssAssetsPlugin({
          assetNameRegExp: /\.css$/g,
          cssProcessor: require('cssnano'),
          cssProcessorPluginOptions: {
            preset: ['default', { discardComments: { removeAll: true } }],
          },
          canPrint: true,
        }),
      ];
      ```
    - plugin은 외부 모듈이므로 불러와야함
      ```js
      const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin');
      ```
    - build결과 (dist/~~.css확인해보기) => 압축 잘 되었다!

  - **JS최적화**
    - css처럼 js compressor 사용
    - 대표
      - uglify.js
      - babel-minify
      - terser
    - 웹팩이 기본적으로 채택하는 terser 사용해볼 것
    - 웹팩의 의존성에 포함된 모듈이기 때문에 별도로 terser를 설치할 필요는 없고, optimization키에 작성 해주면된다.
      - optimization 내부에 minimize라는 키를 true를 하면, 웹팩 내부에서 terser를 실행시켜 압축 진행.
      - minimizer 키에서 어떤 compressor를 사용할지 별도로 설정할 수 있음.(uglify, babel-mini)
      - terser를 작성한 이유?: terser customize하기 위해서
      - minimize만 true로 해두면 기본동작만 하기 때문.
        - 빠르게 cache되도록 설정함(빌드 되는 시간 줄임)
    - 혹시 terser확인하고 싶으면, node_modules확인! (webpack설치할때 같이 설치되었음)
    - terser-webpack-plugin 설치(외부 플러그인)
      ```console
       npm i terser-webpack-plugin -D
      ```
    - webpack.config.js 수정
      ```js
      modules.exports = {
        optimizations: {
          minimize: true,
          minimizer: [
            new TesrserWebpackPlugin({
              cache: true,
            }),
          ],
        },
      };
      ```
 [이전페이지](https://bit.ly/2EoeAjj)
