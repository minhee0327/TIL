# 브라우저 JS

-   문서 객체 모델(DOM) - sample01.html에서 test됨

    -   브라우저가 HTML문서를 조작하는 핵심
    -   트리구조
    -   DOM tree는 Node로 구성
    -   루트노드: document, 자식노드 html 요소 하나뿐.
    -   html자식으로 head, body태그
    -   DOM트리의 모든 노드는 Node클래스의 인스턴스
    -   Node객체에는 트리구조를 나타내는
        -   parentNode 프로퍼티
        -   childNodes 프로퍼티
        -   자기자신에 대한 프로퍼티
            -   nodeName
            -   nodeType

-   DOM전체를 순회하면서 콘솔에 출력해보기(DFS, 전위순회)

    -   browser 개발자도구에 복붙해보면 어떻게 된건지 바로 알수이따~~

    ```js
    function printDOM(node, prefix) {
        console.log(prefix + node.nodeName);
        for (let i = 0; i < node.childNodes.length; i++) {
            printDOM(node.childNodes[i], prefix + '\t');
        }
    }
    printDOM(document, '');
    ```

-   get메서드
    -   원하는 HTML요소를 빨리 찾을 수 있는 메서드
        -   `document.getElementById`
        -   `document.getElementByClassName`
        -   `document.getElementByTagName`
-   DOM요소 쿼리

    -   다른 요소와의 관계를 사용해서 원하는 요소를 찾을 때 좀 더 범용적인 메서드
        -   `document.querySelector`
        -   `document.querySelectorAll`

-   DOM요소 조작
    -   요소를 찾은 걸로 무엇을 할 수 있을까?
    -   컨텐츠 수정
        -   `textContent`: HTML 태그를 모두 제거하고 순수 텍스트 데이터만 제공
        -   `innerHTML`: HTML태그를 수정하면 DOM이 그에 맞게 변경
-   새 DOM요소 만들기

    -   `document.createElement`: 새 요소는 만들지만, DOM에 추가되지는 않음
        -   새 요소를 추가하기 위해서는
            -   `insertBefore(삽입요소, 삽입위치)`
            -   `appendChild(삽입요소)`: 항상 마지막 요소로 추가됨.

-   요소 스타일링

    -   DOM API만으로도 요소 스타일을 지정할 수 있지만, 직접 요소 프로퍼티를 수정하는것보다 calss를 사용하는게 좋다.
    -   요소의 스타일을 바꾸고 싶을 때, css클래스를 새로 만들고 그 클래스를 원하느 ㄴ요소에 지정.
    -   모든 요소에는 클래스를 나열하는 `classList` property가 있다.
        -   `add`메서드로 클래스를 추가할 수 있음
        -   `remove`메서드로 클래스 제거

-   데이터 속성
    -   HTML5의 데이터 속성(data-)
    -   데이터속성의 이름은 마음대로 정해도 괜찮음 (예: `data-contain`, `data-action`, ...)
    -   해당 요소의 dataset프로퍼티를 입력해보면 data-에 붙은 이름과 해당 값(문자열)이 객체형태로 제공된다.
    ```js
    const hightLightActions = document.querySelectorAll('[data-action="highlight"]');
    hightLightActions[0].dataset;
    // DOMStringMap {action: "highlight", containing: "unique"}
    ```
    -   데이터 속성 수정/추가
        ```js
        hightLightActions[0].dataset.containing = 'girraffe'; //수정(기존에 있는 dataset과 같은 이름이면 수정)
        hightLightActions[0].dataset.caseSensitive = 'true'; //삭제(없으면 추가)
        ```
-   DOM이벤트

    -   엄청 많기때문에 필요에 따라 공식문서 참조
    -   simple.html 의 `<script>` 내부 내용참조
    -   `addEventListener` 메서드로 이벤트가 일어났을 경우, 호출할 함수 지정

-   이벤트 버블링과 캡쳐링(sample02.html)

    -   버튼을 클릭했을 때, 버튼의 부모에서 이벤트 처리를 해도 되고, 그 부모의 부모에서 처리해도 된다.
    -   즉, HTML은 계층적임.
    -   여러 요소에서 이벤트 처리를 할 수 있다면, 이벤트에 응답해야할 기회는 어떤 순서일까?
        -   캡쳐링
            -   가장 먼 조상부터 시작하는 방법
        -   버블링
            -   이벤트가 일어난 요소에서 시작해 거슬러 올라가는 방법
        -   캡처링 => 버블링 순
    -   이벤트 핸들러에는 다른 핸들러가 어떻게 호출될지 영향을 주는 3가지 방법이 있다.
        -   `preventDefault` :
            -   defaultPrevented 프로퍼티가 true로 바뀐채로 이벤트를 계속 전달.
            -   true 인 경우 해당 이벤트를 무시하고 동작할 수 있음.
            -   눈에 보이기엔 새로고침 방지같은 느낌.(다른 요소에서 해당 위치의 이벤트가 발생했을 때 핸들러 동작 X)
        -   `stopPropagation`:
            -   이벤트를 현재 요소에서 끝내고 더는 전달하지 않음
            -   해당 요소에 연결된 이벤트 핸들러만 동작하고 다른 요소에 연결된 이벤트는 동작하지 않음
        -   `stopImmediatePropagation`:
            -   다른 이벤트 핸들러, 심지어 현재 요소에 연결된 이벤트 헨들러도 동작X

-   event category

    -   drag, dragstart, dragend, drop, ...
    -   focus, blur, change,..
    -   form(submit),..
    -   click, mousedown, mouseup, move, mouseenter, mouseleave, mousewheel...
    -   keydown, keypress, keyup
    -   pause, play
    -   progress(load, error, ...)
    -   touches,...

-   Ajax: 비동기적 자바스크립트와 XML
    -   서버와 비동기적으로 통신하면 페이지 전체를 새로고칠 필요 없이 서버에서 데이터 받아올 수 있다.
    -   XMLHttpRequest의 도입으로 가능해짐
    -   핵심개념
        -   브라우저 자바스크립트에서 HTTP요청을 만들어 서버에 보내고, 데이터를 받음
        -   데이터는 보통JSON형식(XML도 가능)
        -   브라우저에서 해당 데이터를 사용함.
    -   HTTP위에서 동작하긴하는데, 페이지를 불러오고 렌더링하는 부담이 줄어든다.
        -   (웹 앱이 빨라짐) - 최소 사용자가 느끼기에.
    -   단순한 서버 (Node.js) 만들어서 Ajax 서비스 제공(Server.js)
    -   Server.js파일과 sample03.html에서 실행함
        -   서버 실행하기위한 몇가지 모듈설치(`npm install`)
        -   실행시 모듈 설치 후 `npx babel-node Server.js`로 서버 실행해주세요.
        -   서버 구동후, 브라우저(sample03.html) open해보면 사용하는 os, node버전, 서버 실행시간을 확인할 수 있습니다.
