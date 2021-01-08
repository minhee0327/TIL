# HTTP 프로토콜

-   HTTP는 클라이언트와 서버간 통신을 한다.
    -   클라이언트 request 송신 예
        ```
        GET /index.html HTTP / 1.1
        Host: www.blabla.com
        ...
        ```
        -   request msg 구성
            -   **메소드**(GET): 서버에 요구하는 종류
            -   **URI**(/index.html): 요구대상인 리소스(=리퀘스트 url)
            -   **Protocol version**(HTTP/1.1): 클라이언트 기능 식별위한, HTTP 버전 정보
            -   **리퀘스트 헤더필드**
            -   **엔티티**
    -   서버측 response 송신예
        ```
        HTTP/1.1 200 OK
        Date: Tue, 10 Jul 2012 06:50:15 GMT
        Content-Length: 362
        Content-Type: text/html

        <html>
        ...
        ```
        -   response msg 구성
            -   **Protocol Version**(HTTP / 1.1): 서버의 HTTP버전
            -   **리퀘스트 처리결과 상태코드와 설명**(200 OK)
            -   **response 발생 일시**(Date~~GMT) - 헤더필드중 일부
            -   **바디**: 빈줄 아래
