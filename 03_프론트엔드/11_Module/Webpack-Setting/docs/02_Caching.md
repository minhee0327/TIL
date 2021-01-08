# 2. Caching & Webpack

- #### Web Application

  - [사용자] <=> [브라우저(클라이언트)] <=> [서버]
  - 사용자는 클라이언트를 통해 서비스를 이용하고
  - 클라이언트는 서버에, 사용자가 필요한 데이터를 요청
  - 데이터를 요청하고 받을 때, 비용 발생 (사용자가 데이터를 사용한 시간,기다리는 시간, 돈... )
  - 사용자가 서비스를 이용할때 비용을 최소화 시키는 것은 상당히 중요하다.
  - 이 시간을 최소화하기 위해 사용하는 기술 '캐싱'

- #### 캐싱(Caching))

  - 리소스의 복사본을 놓고 서버보다는 가까운 위치에 놓고, 클라이언트에서 사용할수 있게끔한다.
  - 사용자에게 훨씬 빨리 리소스를 전달하고, 서버로 요청하는 횟수가 줄어 부하가 줄어든다.
  - 데이터의 지역성
    - 공간지역성: 한번 접근한 데이터의 인근에 저장되어있는 데이터가 다시 접근될 가능성이 높다.
    - 시간지역성: 한번 접근된 데이터가 가까운 시간내 다시 접근될 가능성이 높다.

- #### Caching & Webpack

  - 웹팩이 번들파일을 만드는 과정에서 caching을 효과적으로 사용하는 방법
    - 모듈들을 번들파일로 만들면, 브라우저는 번들파일을 받고, 웹 어플리케이션으로 동작시킴
    - 이때, 지금까지 만든 설정파일을 기반으로 번들파일을 만들게 되면 브라우저에서는 같은 이름으로 번들파일을 호출하게 된다.
    - 그런데 브라우저가 캐싱하는 기준은 url
    - 로드를 하는 리소스의 내용이 같을경우, 캐싱을 이용하기 때문에 이전파일이 호출된 결과로 보여지게됨.
    - 파일을 수정했을 경우, 마치 수정이 안된 것으로 인식하게 됨. 이를 해결하는 것이 hash값을 붙여주는 것.
    - 파일이 번들링 될때에만 hash값을 변경.
    - 번들링 되기 전까진 해시값이 유지가 되기 때문에, 같은 번틀 파일로 캐싱이 가능함.
    - 수정사항이 있어서 수정한 뒤 다시 번들링하면 해시값이 수정이되고, 캐시를 이용하지 않고 새로운 번들파일을 로드하면됨
  - 해시값: _hash, contenthash, chunkhash_

    - output의 filname에 작성
    - **hash**: 파일이변경되었을때, 빌드될때마다 자동으로 부여되는 값.
      - 그런데 빌드 될때마다 hash가 새로 부여되면, 파일내부에 bundle파일이 쌓여감.  
        (불필요한 파일이 쌓이기 때문에, 이를 해결해주는 plugin을 등록)
      - clean webpack plugin: 빌드 될때마다, 새로 생성된 파일들만 남기고 나머지는 비워주게됨
        ```console
        npm install clean-webpack-plugin -D
        ```
      - 외부 모듈이기때문에, require로 모듈을 부르고, plugin에 설정해주어야한다.
        ```js
        const { CleanWebpackPlugin } = require('clean-webpack-plugin');
        plugin: [new CleanWebpackPlugin()];
        ```
    - **contenthash**

      - ExtractTextPlugin에서 생성된 특정유형의 해시
      - mini-css-extract-plugin 모듈 설치

        ```console
        npm i mini-css-extract-plugin
        ```

        - require로 mini-css-extract-plugin을 가져와서, loader, plugin설정을 해준다.
        - 일전에 style-loader 설정해두었던 것은 주석처리 (충돌 방지)
        - link 태그 추가된 것을 확인할 수 있고, build(bundle)된 결과, main.css 파일을 확인할 수 있다.
        - css 자원은 캐싱이 되어 활용할 수 있는 형태가되고, html은 크기가 줄어든다.(style tag대신, 별도 파일 css로 변경됨.)
        - 단, main.css로 이름이 고정되면, css파일이 변경이되어도 이전 파일을 불러오는 문제가 생기기 때문에, hash를 적용해야함
        - 이 때 hash를 사용해야함.
          ```js
          new MiniCssExtractPlugin({
            filename: '[hash].css', //hash, createhash, chunkhash
          });
          ```
        - 그런데, js와 css를 수정하는 시점은 다름.
        - js가 수정되고 다시 빌드를 하면, css의 변경내용이 없더라도 매번 css도 새로 빌드됨.
        - hash는 기본적으로 파일이 수정된 후에 빌드가 실행됨에 따라 변화하기 때문에 이렇게 되면 css를 사용할 수 없다.
          - 변경이 일어나지 않은 리소스는(css) 캐싱에 있는 리소스를 사용해야하는데, 해시가 일괄 변경됨에 따라, 불러오지 못하는 상황발생
          - 제대로 캐싱 안됨
          - 해시값이 바뀌었기 때문에, css를 새로운 리소스로 판단하고 같은 내용을 요청하게 되어 content 종류에 따라 hash를 부여하는 contenthash를 사용하는 것이 좋다.
          - js가 변경되더라도, css는 유지하도록 함.

    - **chunkhash**

      - 번들링을 할 때마다, 번들파일의 사이즈가 늘어난다.
      - 파일의 요청수는 줄지만, 파일 크기가 커져 상대적으로 파일이 도착하는 시간이 지연될 수 있다.
      - 그래서 몇가지 기준을 가지고 파일을 분리하는데, 이를 'chunk'라고 한다.
      - 특정 기준으로 나누는데 2가지를 기준으로 나눌 것
        - runtime 청크파일
          - 웹팩이 모듈들을 해석해 의존성그래프를 완성하고 하나의 번들파일에 모듈들을 모두 모아서 번들파일을 완성하게 되는데,  
            번들파일로 app을 실행시킬때 모듈들을 순서대로 읽을 수 있도록 마련된 초기화에 해당하는 코드가 있다.
          - runtime: application 이 메모리를 할당받고, 실행되는 환경
          - 이 런타임 환경에서 모듈들을 안전하게 사용할 수 있도록 마련된 초기화 코드는 모듈이 몇개가 관여되던 변함이 없음.
          - 런타임때만 사용되는 코드들을 청크로 분류하게 되면, 나머지는 모듈에 대한 내용만 남게 된다.
          - 실제로 변화만 담고 있는 코드는 양이 상대적으로 줄고, 런타임 코드는 변화가 없기 때문에 런타임코드의 경우 캐시가 적용되서 app이 좀 더 빨리 실행됨.
        - 밴더 청크 파일
          - 벤더: 외부 패키지에 해당하는 모듈들 (예:jQuery)
            - jQuery는 우리가 버전업을 하지 않는이상, jQuery는 버전의 변화가 없다.
            - 외부에서 관리되는 모듈들만 따로 분류하면, 실제 우리가 작업하는 코드만 응집이 되고, 외부패키지들을 모아둔 벤더 청크 파일은 해시값이 바뀌지 않기 때문에 캐시를 통해 효율을 높일 수 있다.
      - chunk hash 는 chunk로 나누어진 파일들마다 hash값을 부여하게 됨
      - 마치 content hash처럼 나누어진 청크 별로 해시값을 적용하기 때문에, 직접 작성하는 모듈을 제외한 나머지 청크파일에는 영향이 없다.

      - chunkhash 실습

        - _runtime chunk_

          - file name 설정

            ```js
            output:{
              //name이라는 키워드는 entry 파일 이름(예bundle) 혹은
              //웹팩 설정 파일 내에서 name 프로퍼티에 할당하는 값이 적용되는 공간
              filename: '[name].[chunkhash].js',
            }
            ```

          - optimization (key): 웹팩의 번들파일을 최적화 시킴
            - runtimeChunk 를 plugin에 추가 : 빌드 시, 런타임 코드는 따로 분리됨(runtime, )
            ```js
            optimization:{
              runtimeChunk:{
                  name:'runtime'
              }
            },
            ```

        - _벤더 chunk_
          - 벤더파일 예시(jQuery)
          - jQuery 설치
            ```
            npm i -S jquery
            ```
          - 설치 이후, 클래스이름을 사용하여 DOM 갯수 몇개인지 체크(index.js)
            ```js
            import $ from 'jquery';
            console.log($(`.${styles.helloWebpack}`).length);
            ```
          - 웹팩 설정 파일에서, 벤더파일들에 대한 청크파일을 생성하기 위해 key를 하나 더 추가.(webpack.config.js)
            - splitchunk 내용을 plugin에 추가
            ```js
            splitChunks:{
              cacheGroups:{
                    commons:{
                        test: /[\\/]node_modules[\\/]/,
                        name: 'venders',
                        chunks: 'all'
                  }
              }
            }
            ```
            - build시, dist 폴더 내부에 vender.~ 이라는 파일이 생김 확인해보면, jQuery와 관련된 내용이 담겨있음(분리 성공!)

 [이전페이지](https://bit.ly/2EoeAjj)
