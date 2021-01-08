# ESM
- ECMA에서 채택
- 가져오기  
    ```js
    import module_name from module_position
    ```    
- 내보내기
    ```js
    export
    export default
    ```
    - default 없이 내보냈을 경우, import 해올때 {func1, func2}
    - default 붙여서 내보냈을 경우, import 해올때 객체이름 지어주고
        - 기능 사용시, 객체이름.func1 이런식으로 사용가능

- nodeJS에서는 CommonJS를 기본적으로 따르기 때문에, ESM으로 모듈을 사용하려 외부 모듈이 필요하다.
    ```console
    npm install esm
    ```
- 실행시 명령문(기존에 ```node 파일명```)
    ```console
    node -r esm index.js
    ```
    - index.js파일을 esm 모듈을 사용해서 실행
    - r: 모듈을 commonJS외에도 적용가능토록하는 명령
