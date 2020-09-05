# 정규표현식

-   Intro
    -   정교한 문자열매칭기능
    -   문자열교체
-   부분문자열 검색과 대체

    -   문자열 속에서 부분문자열을 찾고, 찾은 부분을 교체할 때 사용
    -   정규식이 제공하는 기능이 유연하고 강력하지만 양이 방대함
    -   따라서, 정규식을 쓰지않고 사용하는 방법도 같이 알아보자.
    -   `String.prototype` 메서드로 충분히 대체 가능
    -   예
        ```js
        const a = 'As I was going to Tans River';
        a.startsWith('As'); // true
        a.endsWith('River'); // true
        a.startsWith('going', 9); //true (index 9 시작)
        a.endsWith('going', 14); // true (index 14 부터 반대로 going 있음)
        a.includes('going'); // true
        a.includes('going', 10); // false
        a.indexOf('going'); // 9
        a.indexOf('going', 10); // -1 (찾을 수 없을 때)
        a.indexOf('nope'); //-1
        a.toLowerCase().startsWith('as'); //startsWith만쓰면 대소문자 구분하기 때문에 toLowerCase사용
        ```
        -   `String.prototype.toLowerCase`는 원래 문자열 그대로 두고 새로운 문자열 반환.
        -   즉, **JS의 문자열은 항상 불변!**
        -   `String.prototype.replace` 는 부분문자열을 찾아 교체

-   JS의 정규식(RegExp 클래스)

    -   RegExp 생성자로도 정규식을 만들 수 있지만, `리터럴 문법` 사용가능(`/`로 감싼형태)
        ```js
        const re1 = /going/; //리터럴 문법
        const re2 = new RegExp('going'); //생성자
        ```

-   정규식 검색

    -   예: `/\w{3,}/ig` : 3글자 이상인 단어이면서 대소문자 가리지 않음

    ```js
    const a = 'As I was going to Tans River';
    const re = /\w{3,}/gi;
    a.match(re); // ["was", "goin", "Tans", "River"]
    a.search(re); // 5 3글자 이상으로 이루어진 첫 단어의 index는 5
    ```

-   문자열 교체

    -   `String.prototype.replace`

-   입력소비

    -   큰문자열에서 부분문자열을 찾는 방법 뿐만이 아니라
    -   `정규식이 입력 문자열을 소비하는 패턴`이 정규식의 더 나은개념
    -   정규식이 문자열을 `소비`할때 사용하는 알고리즘
        -   문자열 왼쪽에서 오른쪽 진행
        -   일단 소비한 글자에 다시 돌아오지 않음
        -   한번에 한글자씩 움직이고 일치하는것이 있는지 확인
        -   일치하는 것을 찾으면 해당 글자를 한번에 소비하고 다음글자로 진행(/g 플래그로 전역검사할때 해당)

-   메타문자

    -   대체 : `|`
    -   대소문자 가리지 않고: `i`
    -   전체검색: `g` (이게 없으면 일치하는 맨 첫번째 값만 반환)
    -   문자셋 제외: `^`
    -   앞의 요소가 하나이상: `+` (문자셋 다음에 붙임)
    -   정확히 n개: `{n}`
    -   최소 n개 : `{n,}`
    -   n개 이상 m개 이하 : `{n,m}`
    -   0개 또는 1개와 동등: `?` = `{0,1}`
    -   숫자 상관없음: `*`

-   문자셋

    -   `\d`= `[0-9]`
    -   `\D`= `[^0-9]`
    -   `\s`= `[ \t\v\n\r]` (탭, 스페이스, 세로탭, 줄바꿈 포함)
    -   `\S`= `[^ \t\v\n\r]`
    -   `\w`= `[a-zA-Z_]`
    -   `\W`= `[^a-zA-Z_]`

-   마침표(`.`) 및 이스케이프(`\`)

    -   마침표: 줄바꿈을 제외한 모든 문자에 일치

-   와일드카드
    -   정규표현식에서는 `*`가 아님!!
    -   가능한 예: [\s\S]
