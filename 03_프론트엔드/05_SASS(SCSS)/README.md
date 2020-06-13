# Sass(SCSS)
### 1. Sass 와 SCSS의 차이점
- Sass의 3버전에 새롭게 등장한 SCSS
- SCSS는 CSS구문과 완전히 호환되도록 새로운 구문을 도입해 만든 Sass의 모든 기능을 지원하는 CSS의 상위집합.
- 즉, SCSS는 CSS와 거의 같은 문법으로 Sass기능을 지원

### 2. 개요 
- Sass(SCSS)는 웹에서 직접 동작 X
- 최종에는 표준 CSS로 동작해야하고, 전처리기로 작성 후, **CSS 컴파일해야한다.**
- js 개발환경에서 추천하는 방법
    - SassMeister(강의에서 자주 사용)
    - node-sass, webpack, ....중 Parcel 이용!
    - node js 사용자 기준, 웹 애플리케이션 번들러 **Parcel**을 사용할것
        - 패키지 관리(package.json) `npm init -y`
        - Parcel전역설치  
            `npm install -g parcel-bundler`
        - dev dependencies에 설치 
        `npm i -D parcel-bundler`
        - Sass 컴파일러설치(node-sass) `npm install --save-dev node-sass`
        - HTML에 `<link>`로 Sass 파일 연결하기  
        `<link rel="stylesheet" href="scss/main.scss">`
        - 필요한 모듈 자동으로 설치. parcel이 컴파일해서 scss를 읽을수있도록해줌.  
        `npx parcel index.html`

### 3. 문법
#### 3.1 주석
- // : 컴파일 되지 않는 주석
- /* */: 컴파일 되는 주석
    - Sass의 경우에는 줄을 맞춰 * 을 사용해야하지만, 
    - SCSS는 각 줄에 * 없어도 호환 쉽다.

#### 3.2 데이터 종류
|데이터|	설명|	예시|
|---|-----|---|
|Numbers	|숫자	|1, .82, 20px, 2em…
|Strings	|문자	|bold, relative, "/images/a.png", "dotum"
|Colors	|색상 표현	|red, blue, #FFFF00, rgba(255,0,0,.5)
|Booleans	|논리	|true, false
|Nulls	|아무것도 없음	|null
|Lists	|공백이나 ,로 구분된 값의 목록	|(apple, orange, banana), apple orange
|Maps	|Lists와 유사하나 값이 Key: Value 형태	|(apple: a, orange: o, banana: b)

---
#### (참고) 목차
- [중첩](#33-중첩)
- [변수](#34-변수)
- [가져오기(Import)](#35-가져오기)
- [연산](#36-연산)
- [재활용(Mixins)](#37-재활용)
- [확장](#38-확장)
- [함수](#39-함수)
- 조건과 반복
- 내장함수


#### 3.3 중첩
- 상위선택자 참조 (`&`) : 상위 선택자를 사용해서, 일치선택자를 만들 수 있음.
    ```SCSS
    /*SCSS*/
    .fs{
        &-small{
            font-size: 14px;
        }
        &-medium{
            font-size: 16px;
        }
        &-large{
            font-size: 18px;
        }
    }
    ```
    ```css
    /*CSS로 컴파일시*/
    .fs-small {
        font-size: 14px;
    }
    .fs-medium {
        font-size: 16px;
    }
    .fs-large {
        font-size: 18px;
    }
    ```
- 중첩 벗어나기 `@at-root`
    ```SCSS
    /*SCSS*/
    .section{
        $width: 100px;
        $height: 200px;
        width: $width;
        height: $height;
        .item{
            width: $width;
            height: $height;
        }
        @at-root .box{
            width: $width;
            height:$height;
        }
    }
    ```
    ```CSS
    /*CSS*/
    .section {
        width: 100px;
        height: 200px;
    }
    .section .item {
        width: 100px;
        height: 200px;
    }
    .box {
        width: 100px;
        height: 200px;
    }
    ```
- 중첩된 속성
    - 동일한 네임스페이스 (margin-, font-, padding-..)를 사용할 때
    ```SCSS
    .box{
        font:{
            size: 10px;
            weight: bold;
        };
        margin:{
            top: 100px;
            left: 20px;
            right: 30px;
        };
    }
    ```
    ```CSS
    .box {
        font-size: 10px;
        font-weight: bold;
        margin-top: 100px;
        margin-left: 20px;
        margin-right: 30px;
    }
    ```



[목차][TOC]

---
#### 3.4 변수
- 반복 사용되는 값을 변수로 지정(`$`)  
    `$변수이름: 속성값`
    ```SCSS
    $w: 100px;
    $color: red;
    $url: "/assets/images/";

    .box{
    width: $w;
    margin-left: $w;
    background: $color url($url + "pretty.jpg");
    }
    ```
    ```CSS
    .box {
        width: 100px;
        margin-left: 100px;
        background: red url("/assets/images/pretty.jpg");
    }
    ```

- 변수 유효범위(Variable Scope)
    - 선언된 블록 `{}` 내에서만 유효
- 변수 재 할당
    - 변수에 변수를 할당할 수 있음
- 변수 전역설정
    - `!global` 플래그를 사용하여, 유효범위를 전역(Global)로 설정
- 변수 초깃값 설정
    - `!default` 플래그는 할당되지 않은 변수의 초깃값을 설정합니다.
    - 즉, 할당되어 있는 변수가 있다면 변수가 기존 할당값을 사용합니다.
    - 기존 변수가 있을 경우, 현재 설정하는 변수의 값은 사용하지 않겠다는 뜻.
    - 기존 코드(원본)을 Overwrite하지 않고 사용하기 위해서 사용.
- 문자보간(`#{}`)
    - `#{}`를 사용하여, 코드의 어디든지 변수값을 넣을 수 있다.
    ```SCSS
    /*SCSS*/
    $family: unquote("Droid+Sans");
    @import url("http://fonts.googleapis.com/css?family=#{$family}");
    ```
    ```CSS
    /*CSS*/
    @import url("http://fonts.googleapis.com/css?family=Droid+Sans");
    ```
    - unquote()는 문자에서 따옴표 제거

[목차][TOC]

---
#### 3.5 가져오기
- @import로 외부에서 가져온 Sass 파일은 모두 단일 CSS출력 파일로 **병합**
    - Sass @import 는 기본적으로 Sass파일을 가져오는데, CSS @import 규칙으로 컴파일되는 몇가지 상황이 있다.
        - 파일확장자가 .css일때
        - 파일이름이 `http://`로 시작하는 경우
        - url()이 붙었을 경우
        - 미디어 쿼리가 있는경우
    - 위의 경우 CSS @import 규칙대로 컴파일됩니다.

- 여러가지 파일가져오기
    ```SCSS
    @import "header", "footer";
    ``` 
- 파일 분할
    - 파일이름 앞에 `_`를 붙이면 컴파일시 `~.css`파일로 컴파일하지 않는다.
    - Webpack 이나 Parcel, Gulp 같은 일반적인 빌드툴에서는 Partials 기능을 사용할 필요 없이, 설정된 값에 따라 빌드 된다. 하지만 `_`를 사용할 것을 권장.

[목차][TOC]

---

#### 3.6 연산
- 산술연산자
- 비교연산자
- 논리연산자(and, or, not)
- 숫자
    - 상대전 단위 연산(%, em, vm등)의 연산의 경우 CSS 의 calc()로 연산
        ```SCSS
        width: 50%- 20px; // 단위 모슨 에러
        width: calc(50%-20px); // 연산가능
        ```
    - 나누기 연산 주의사항
        - CSS는 속성 값의 숫자를 분리하는 방법으로 /를 허용하기 때문에, 연산이 안될 수도 있다.
        - 예를들어   
        `font:16px/22px serif;` 는  
         `font-size:16px; line-height:22px`을 뜻하기 때문.
        - 따라서 `/`를 나누기 연산으로 사용하려면 다음 조건을 충족해야한다.
            - 값 또는 그 일부가 변수에 저장되거나 함수에 의해 반환되는 경우
            - 값이 ()로 묶여있는 경우
            - 값이 다른 산술 표현식의 일부로 사용되는 경우
        - 나눗셈 연산을 하려면 `/`를 기준으로 오른쪽에는 숫자만 쓰자.
- 문자
    - 문자연산에는 `+` 사용
    - 문자연산으 결과는 첫번째 피연산자를 기준으로 함.
    - 첫번째 피연산자가 따옴표 있었다면, 결과도 따옴표로 묶인채로 반환
    - 첫번째 피연산자에 따옴표 없는문자였다면, 결과도 따옴표 없이 반환

- 색상
    - 색상도 연산할 수 있다.
    ```SCSS
    div{
        color: #123456 + #345678;
        //R: 12 + 34 = 46 //16진수로 표시
        //G: 34 + 56 = 8a
        //B: 56 + 78 = ce
        background: rgba(50,100,150,.5)+ rgba(10,20,30,.5);
        //R: 50+10 = 60
        //G: 100 +20 =120
        //B: 150+30 = 180
        //A: Alpha channels must be equal
    }
    ```
    ```CSS
    div{
        color: #468ace;
        background: rgba(60,120,180,.5)
    }
    ```
    - alpha channels 값을 연산하고 싶다면, opacify(), transparentize() 함수 사용.
        - oacify(컬러변수, .3) : 컬러변수를 30% 더 불투명하게(+)
        - transparentize(컬러변수, .3): 컬러변수를 30% 더 투명하게(-)

- 논리
    - `@if`조건문에서 사용되는 논리 연산
    ```SCSS
    /*SCSS*/
    $w:100px;
    .item{
        display: block;
        @if not ($w>50px and $w<90px){
            width: 400px;
        }
    }
    ```

[목차][TOC]

---

#### 3.7 재활용
- Sass Mixins는 스타일 시트전체에서 재사용할 CSS 선언 그룹을 정의하는 아주 훌륭한 기능.
- 약간의 Mixin(믹스인)으로 다양한 스타일을 만들어 낼 수 있다.
- 기억할것 2가지
    - 선언하기 `@Mixin`
    - 포함하기 `@include`
    ```SCSS
    //SCSS
    @mixin size($w:100px, $h:100px){
        width: $w;
        heigh: $h;
        &::after{
            content:"!!";
        }
    }

    .box1{
        @include size;
    }
    .box2{
        @include size(200px, 300px);
    }
    .box3{
        @include size($h:400px);
    }
    ```
    ```CSS
    .box1 {
        width: 100px;
        heigh: 100px;
    }
    .box1::after{
        content:"!!";
    }

    .box2 {
        width: 200px;
        heigh: 300px;
    }
    .box2::after{
            content:"!!";
        }
    .box3 {
        width: 100px;
        heigh: 400px;
    }
    .box3::after{
        content:"!!";
    }
    ```
    - 상위 참조 연산 사용가능
    - 키워드인자 사용가능
    - 가변인수(매개변수 뒤에 ...)를 사용하여 입력할 인수갯수가 불확실할때 사용. 
    - @content: 해당부분에 원하는 스타일 블록을 전달.
    ```SCSS
    //SCSS @content 사용예시
    @mixin icon($url){
        &::after{
            content: $url;
            @content;;
        }
    }

    .box1{
        @include icon("image/icon1.png")
    }
    .box2{
        @include icon("image/icon2.png"){
            display:block;
            position: absolute;
            width: 100px;
            height: 100px;
        }
    }
    ```
    ```CSS
    /*compile 된 css*/
    .box1::after {
        content: "image/icon1.png";
    }

    .box2::after {
        content: "image/icon2.png";
        display: block;
        position: absolute;
        width: 100px;
        height: 100px;
    }
    ```
[목차][TOC]

---

#### 3.8 확장
- `@extend 선택자`
- 다중선택자 형식으로 들어가진다.
- 권장되는 방법은 아님, 되도록 mixin을 대체기능으로 사용!
```SCSS
.btn{
  padding: 10px;
  margin: 10px;
  background: blue;
}
.btn-danger{
  @extend .btn;
  background:red; 
}
```
```CSS
.btn, .btn-danger {
  padding: 10px;
  margin: 10px;
  background: blue;
}

.btn-danger {
  background: red;
}
```
[목차][TOC]

---

#### 3.9 함수
- Mixin: 지정한 스타일을 반환함
- function: 보통 연산된(Computed) 특정값을 @return 지시어를 통해 반환
- 함수이름 명명시, 내장함수와 겹칠 수 있으므로 접두어를 붙여 지을것.
- 예: `extract-read()` 같은 이름
- 사용방법
    ```SCSS
    // 선언
    //Mixin
    @mixin 믹스인이름($매개변수){
        스타일;
    }
    //Function
    @function 함수이름($매개변수){
        @return 값
    }
    ```
    ```SCSS
    //사용
    //Mixin
    @include 믹스인이름(인수);
    //Fuction
    함수이름(인수)
    ```
- 실제 적용예시
    ```SCSS
    @function columns($number:1, $columns:12, $width:1200px){
        @return $width *($number/$columns);
    }

    .container{
        $width: 1200px;
        width: $width;
        .item:nth-child(1){
            width: columns();
        }
        .item:nth-child(2){
            width: columns(8, $width:$width);
        }
        .item:nth-child(3){
            width: columns(3);
        }
    }
    ```

[목차][TOC]





[Heropy님](https://heropy.blog/2018/01/31/sass/)

[TOC]:#참고-목차
