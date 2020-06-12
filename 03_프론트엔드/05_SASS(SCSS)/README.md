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
- 가져오기(Import)
- 연산
- 재활용(Mixins)
- 확장
- 함수
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

[Heropy님](https://heropy.blog/2018/01/31/sass/)

[TOC]:#참고-목차
