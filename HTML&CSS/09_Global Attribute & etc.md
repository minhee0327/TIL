1. 전역속성
    - 모든 HTML요소에서 공통적으로 사용가능한 속성
        - class
        - id
        - style
        - title: (마우스 오버 시) 요소의 정보 
        - lang: 요소의 언어 지정(html에 선언)
        - data-*
            - 사용자 정의 데이터 속성을 지정, JavaScript에 이용할 수 있는 데이터 저장 용도
            ```html
            <div id="me" data-my-name="minhee" data-my-age="20">
            ```
            ```javaScript
            const $me = document.getElementById('me');
            console.log($me.dataset.myName) //minhee
            console.log($me.dataset.myAge) //20
            ```
        - draggable: 요소가 drag&drop api 사용가능 여부 지정
        - hidden: 요소 숨김
        - tabindex: 탭 키를 이용해, 요소를 순차적으로 포커스 탐색할 순서 지정.
            - 대화형 컨텐츠는 기본적으로 tabindex="0"으로 설정이 되어있음
            - 비대화형 컨텐츠(예div) 는 필요에 따라 tabindex를 설정할 것.
            - 논리 흐름에 방해 되서, 양수는 되도록 지양.
            - -1의 경우 포커스 되지 않음.
        - 절대 경로 & 상대경로 
        - 주석(Pass)
        - [특수기호(Entities)](https://freeformatter.com/html-entities.html)