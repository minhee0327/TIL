# 9. BLOWSERS LIST

* Intro
  * 지원하고자하는 브라우저에 대한 설정
  * autoprefix말고도 다른 plugin이나 도구에도 영향을 준다.
  * target-browser: 지원대상
  * 설정방법\(3가지\)
    * package.json에 정의하는 방법\(권장\)
    * .browserslistrc 파일에 정의
    * js 모듈로 만들어서 browserslist값을 관리할 수도 있음 \(postcss.config.js처럼\)
  * Query composition: 특정 브라우저를 표현한다.
    * 조건들을 조합해서 만들수있다.
    * 집합에 비유해서 사용
      * Union\(or\)
      * Intersectioin\(and\)
      * relative complement\(not\)
  * Full List:
    * 브라우저의 범위를 지정할때 어떤 조건을 사용할 수 있는지에 대해 자세히 설명
    * 작업하고 있는 Application이 있다면, 어떤 user에게 제공될 것인지 정의한 후, 참조해서 프로젝트별로 적용하기.
* 실습\(3가지 조건 적용해보기\)
  * package.json에 정의하기
    * 아래 내용 package.json에 추가후 서버를 띄워서 확인

      ```javascript
      "browserslist": [
      "last 2 versions", // 각브라우저별로 최신버전과, 최신버전 직전버전까지
      "IE 10", //특정브라우저에 대한 특정 버전(IE10지원)
      "Firefox > 20"//FIrefox에 대한 버전을 20이상인 버전 지원
      ]
      ```
  * 확인해보기
    * css display: flex를 적용했던 부분을 확인
    * Network tab에 preview 맨 하단부분 확인할것!!

      ```css
      ._2mSEvnqKhGDtOjMutd8GyH {
      display: -webkit-box;
      display: -moz-box;
      display: -ms-flexbox;
      }
      ```

