# CommonJS

* 가져오기

  ```javascript
    require('모듈의경로')
  ```

* 내보내기 \[크게 모듈 객체 사용하거나, exports키워드 사용하는 방법\]

  ```javascript
    module.exports = {...}
    module.exports = 값
    module.exports.key_name = value
    exports.key_name = value
  ```

* CommonJS는 기본적으로 전역에서 module이라는 키워드를 제공하고 있다.
* NodeJS에서 채택한 CommonJS, 따라서 경로지정시, .js 를 제외하고 작성해도 작동된다.

