# jQuery

-   ## 개요
    -   DOM을 조작하거나, Ajax를 요청할때 쓰이는 라이브러리
    -   사용시 장점
        -   브라우저 호환성 걱정하지 않아도됨.
        -   jQuery가 제공하는 Ajax API는 무척 단순함
        -   내장 DOM API를 더 유용하고 단순하게 바꾼 메서드 제공
-   ### 사용기호
    -   식별자: `$` or `jQuery`
-   ### 불러오기
    -   CDN활용
        ```js
        <script src="https://code.jquery.com/jquery-2.2.4.min.js"></script>
        ```
    -   2.x 버전부터 IE 8 이하 지원 중단.(구 버전을 지원해야한다면 1.x버전 사용)
-   ### DOM기다리기

    -   브라우저가 페이지를 완전히 읽고 DOM을 구축한 다음에만 호출되는 콜백안에 코드작성

    ```js
    $(document).ready(function () {
        //html을 모두 불러오고, DOM이 구성된 다음 실행됨
    });

    $(function () {
        //단축표기
        //html을 모두 불러오고, DOM이 구성된 다음 실행됨
    });
    ```

-   ### jQuery로 감싼 DOM요소

    -   jQuery로 DOM조작할때 => `jQuery` or `$`로 DOM 요소를 감싸는 방법 자주쓰임
    -   jQuery객체: jQuery함수로 DOM요소(셋)을 감싼 것
    -   jQuery함수 호출은 주로 css 선택자나 html사용
    -   css 선택자로 jQuery 호출시, 해당 선택자와 일치하는 jQuery객체 반환
        -   `document.querySelectorAll`과 유사
    -   예

        ```js
        const $paras = $('p');
        $paras.length; // 문단수
        typeof $paras; // object
        $paras instanceof $; // true
        $paras instanceof jQuery; // true

        // html로 jQuery 호출하면 그에 맞는 DOM요소 새로 만들어진다. (innerHTMl과 유사)
        const $newPara = $('<p> blablabla... </p>');
        ```

    -   변수명도 \$기호를 붙여서, 제이쿼리 객체를 가리키는 변수라는 것을 명시해주는 습관을 기르는게 좋다.

-   ### 요소 조작
    -   jQuery를 써서 콘텐츠를 추가하거나 제거해보자.
    -   `text` 메서드 : 요소의 `textContent` property와 유사
    -   `html` 메서드 : 요소의 `innerHTML` property와 유사
    -   여러개의 요소들을 동시에 수정할때
        ```js
        $('p').text('ALL PARAGRAPHS REPLACED');
        $('p').html('<i>ALL</i> PARAGRAPHS REPLACED');
        ```
    -   원하는 요소만 작업할때 `eq()` (시작 인덱스는 0)
        ```js
        $('p').eq(2).text('ALL PARAGRAPHS REPLACED'); //3번째요소 변경
        $('p').html('<i>ALL</i> PARAGRAPHS REPLACED');
        ```
    -   요소 제거할때 jQuery객체에서 `remove` 호출
        ```js
        $('p').remove(); // 모든 문단제거
        ```
    -   jQuery 메서드는 모두 jQuery 객체 반환. 따라서 반환된 객체에서 다시 메서드 호출하는식으로 `체인` 연결가능
    -   새 콘텐츠를 추가하는 메서드
        -   `append`:
            -   jQuery 객체에 들어있는 모든 요소에 매개변수로 넘긴 contents를 이어붙인다.
            -   일치하는 요소에 *자식*을 추가한다.
            ```js
            $('p').append('<span>*</span>');
            ```
        -   `before`, `after`:
            -   형제 *삽입*시 사용
            ```js
            $('p').after('<hr>').before('<hr>');
            ```
        -   위 세가지 메서드와는 반대로, 삽입할 요소에서 호출하는 메서드도 있다.
            -   `appendTo`, `insertBefore`, `insertAfter`
            ```js
            $('<span>*</span>').appendTo('p');
            $('<hr>').insertBefore('p');
            $('<hr>').insertAfter('p');
            ```
    -   요소의 스타일변경 시 method
        -   클래스 추가: `addClass`
        -   클래스 제거: `removeClass`
        -   클래스 토글: `toggleClass` (특정 클래스의 유무에 따라서 추가제거)
        -   직접 css 수정: `css(attribute, value)`
            -   `:odd`, `:even`
            ```js
            $('p').css('color', 'red');
            $('p:odd').css('color', 'red'); //홀수 번째 문단의 color를 red로
            ```
        -   jQuery chain을 사용하다보면, 선택한 요소의 부분집합만 남겨야할 때가 있음.
            -   `filter`, `not`, `find`사용해서 선택범위를 줄일 수 있다.
                ```js
                //문단의 형제요소로 뒤에 hr태그를 삽입하고, 자식요소중 마지막에 span~~을 붙일건데 홀수요소에만 적용하고, css는 글자에 blue색.
                $('p').after('<hr>').append('<span>*</span>').filter(':even').css('color', 'blue');
                //class가 highlight인 요소를 제외하고 나머지요소에만 margin 왼쪽 20px
                $('p').after('<hr>').not('.highlight').css('margin-left', '20px');
                //모든 문단앞에 <hr>붙인다음, code클래스를 가진 요소의 자식요소들에 폰트사이즈를 30px로
                $('p').before('<hr>').find('.code').css('font-size', '30px');
                ```
-   ### jQuery 취소

    -   jQuery로 감싼 것을 취소하고, DOM요소에 접근하려면, `get`메서드 사용

-   ### Ajax
    -   Ajax 호출을 간편하게 바꾼 get과 post 메서드
    -   callbakc지원 및 서버 응답처리시 Promise반환
    -   구현 예시
        ```js
        function refreshServerInfo() {
            const $serverInfo = $('.serverInfo');
            $.get('http://localhost:7070').then(
                function (data) {
                    Object.keys(data).forEach((p) => {
                        $(`[data-replace="${p}"]`).text(data[p]);
                    });
                },
                function (jqXHR, textStatus, err) {
                    console.log(err);
                    $serverInfo.addClass('error').html(`Error connecting to server.`);
                },
            );
        }
        ```
    -   저번 실습과 마찬가지로, 패키지 설치 후에 서버 실행후, 브라우저 확인하면 서버로부터 받아온 data들을 볼 수 있다.
