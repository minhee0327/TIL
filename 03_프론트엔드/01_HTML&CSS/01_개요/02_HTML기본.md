1. 태그
    1. 요소(element): 열리고 닫히는 태그 구조(한 쌍)
    2. 닫히는 태그 이름 앞에 슬래시
    3. 빈태그(empty tag): 닫히는 태그가 없음  
     예: ```<img />```
    4. 원하는 형태로 사용하되, 혼용하지 말고 사용.

2. 속성(Attribute)과 값(Value)
    1. 태그(요소) 의 기능을 확장하기 위해 '속성' 사용
        ```
        <TAG 속성 = '값'></TAG>
        ```
    2. 태그 A 가 태그 B의 콘텐츠로 사용되면 
        - 태그 B는 태그 A의 부모요소
        - 태그 A는 태그 B의 자식요소
        ```
        <B> 
            <A></A> 
        </B>
        ```
        - 부모와 자식 요소는 상대적인 개념
            - 조상요소: 부모의 상위 요소
            - 부모요소
            - 자식요소
            - 후손요소: 자식의 하위 요소

3. HTML 문서의 범위
    ```
    <!DOCTYPE html>
    <html>
        <head>
            문서의 정보
        </head>
        <body>
            문서의 구조
        </body>
    </html> 
    ```
    1. html: 전체 범위, 웹프라우저가 해석할 시작과 끝을 알려준다.
    2. head: 문서 정보 범위, 화면을 구성하기 위한 기본설정
        - title(문서제목)
        - meta(웹 페이지 정보)
            - carset: 문자 인코딩 방식(UTF-8)
            - name: 검색엔진 등에 제공하기 위한 정보 종류 (author, description 등)
            - content: name이나 http-equiv 속성의 값을 제공
        - link: 외부 css 파일 연결 시 사용, 빈태그
            - rel: 현재 문서와 외부문서간의 관계(stylesheet, icon..)
            - href: 외부문서의 위치
        - style: html 내부에 css 작성할 때 사용
        - script: JS 외부 파일을 불러오거나, 내부에 작성할 때 사용

    3. body: 브라우저가 해석해야할 html 문서 구조범위, (사용자가 보는 내용, 레이아웃등)
        - div(division): 문서의 부분이나 섹션 정의, 단순히 wrap 용도
        - img : html삽입 & css (background) 삽입 가능
    4. DOCTYPE(DTD): 마크업 언어 문서 형식

4. 웹 표준 검사하기
    - [W3C validator](https://validator.w3.org/#validate_by_upload)
    - 테스트 통과가 웹표준/접근성 준수 여부를 최정 결정하지 않는다.  
    기본 문법 검사에 가깝다.

