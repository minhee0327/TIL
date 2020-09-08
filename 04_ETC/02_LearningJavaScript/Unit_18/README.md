# 브라우저 JS

-   문서 객체 모델(DOM)

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
