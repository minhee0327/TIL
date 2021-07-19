# 04장: HTTP 커넥션

[학습목표]

- HTTP는 어떻게 TCP 커넥션을 사용하는가
- HTTP 커넥션이 무엇이고, 어떻게 사용되는지 이해한다.
- TCP커넥션의 지연, 병목, 막힘현상
- 병렬커넥션, keep-alive커넥션, 커넥션 파이프라인을 활용한 HTTP 최적화
- 커넥션관리를 위한 규칙

## 1) TCP 커넥션

HTTP 통신은 TCP/IP 를 통해 이루어진다.

TCP/IP : 지구상의 컴퓨터와 네트워크 장비에서 널리 쓰이는 패킷 교환 네트워크 프로토콜들의 계층화 집합.

세계 어디서든 TCP/IP 커넥션을 맺을 수 있다.

일단 커넥션이 맺어지면, 클라이언트와 서버 컴퓨터간에 주고받는 메시지들은 손실되거나, 순서가 바뀌지 않고 안전히 전달이 된다.

### ① 신뢰할 수 있는 데이터 전송 통로 TCP

- 순서에 맞게, 손실 없이, 손상 없이, 안정이고 정확하게 통신

### ②TCP 스트림은 세그먼트로 나뉘어 IP 패킷을 통해 전송

![1](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fe0f7838f-76f4-4aff-9ce7-6906e698137b%2F.png?table=block&id=2c2f16ac-7a10-4afe-b6b8-a0173d50b33a&spaceId=da06fe4c-dbc0-451e-a09d-8fe561a808ae&width=1600&userId=&cache=v2)

- Segment: Transport 계층 [예:TCP] - 해당 애플리케이션과 연결(port)
- Packet: Network 계층 [예: IP] - 해당컴퓨터와 연결(host or ip address)

### ③ TCP 커넥션 유지하기

컴퓨터는 항상 TCP 커넥션을 여러개 가지고 있다. 포트번호를 통해 커넥션을 유지한다.

TCP 커넥션 식별은 네가지 값으로 한다.

`<발신지 IP 주소, 발신지 port번호, 수신지 IP주소, 수신지 IP번호>`

위 네가지 값으로 **유일한** 커넥션을 생성한다. 
[네가지 값이 모두 일치하는 경우는 없고, 구성 요소중 일부는 같을 수 있다.]

### ④ TCP 소켓 프로그래밍

운영체제는 TCP 커넥션 생성과 관련된 여러 기능을 제공한다. [소켓 API]

처음에는 유닉스 운영체제용으로 개발되었고, 현재는 대부분의 운영체제, 프로그래밍 언어에서 사용가능.

(소켓이란? 참조): [https://medium.com/@yeon22/term-socket이란-7ca7963617ff](https://medium.com/@yeon22/term-socket%EC%9D%B4%EB%9E%80-7ca7963617ff)

![2](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1ffab399-5add-4988-8644-df7957beb51c/xtrsq007.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210608T042256Z&X-Amz-Expires=86400&X-Amz-Signature=b938cb94be04c0b41a2a98523e72d1f761ed16a99f0daf34c50599ccf6d077d0&X-Amz-SignedHeaders=host)

클라이언트-서버 TCP 소켓 프로그래밍 상호작용 프로세스

## 2) TCP 성능에 대한 고려

HTTP는 TCP 바로 위에 있는 계층이기 때문에 TCP 성능은 HTTP 트랜잭션의 성능에 영향을 미친다.

### ① HTTP 트랜잭션 지연

대부분의 HTTP지연은 TCP 네트워크 지연때문에 발생한다. 
HTTP 트랜잭션 지연 원인은 여러가지가 있다.

- 클라이언트는 URI에서 웹 서버의 IP주소와 포트번호를 알아야하고, 최근에 방문한적 없는 URI라면, DNS로 호스트명을 IP주소로 변환하는데 수십초의 시간이 걸린다. 
[현재는 밀리초 단위로 분석이 끝난다. `host google.com` 을 terminal 에 입력해서 확인해볼것]
- 클라이언트는 TCP 커넥션 요청을 서버에 보내고 서버가 허가 응답을 회신하기를 기다린다.
새로운 커넥션에 항상 발생하는 시간으로, 현재는 1초 미만으로 끝난다.
- 요청메세지가 인터넷을 통해 전달되고, 서버에 의해 처리되는데까지 소요되는 시간.
- 반대로 웹서버가 HTTP응답을 보내는데 소요되는 시간.

### ② 일반적인 TCP 관련 지연

- TCP 커넥션 핸드셰이크 설정
- 인터넷 혼잡을 제어하기위한 TCP의 느린시작(slow-start)
- 데이터를 한데 모아 한번에 전송하기 위한 네이글(nagle) 알고리즘
- TCP의 편승(piggyback) 확인응답(acknowledgement) 을 위한 확인응답 지연 알고리즘
- TIME_WAIT 지연과 포트 고갈

## 3) HTTP 커넥션 관리

### ① Connection Header

- 커넥션 헤더는 3가지 종류의 토큰을 전달 할 수 있다.
    - HTTP 헤더 필드명은 이 커넥션에만 해당되는 헤더들을 나열한다.
    - 임시적인 토큰값은 비표준 옵션을 의미한다.
    - close 값은 커넥션이 작업 완료되면 종료되야함을 의미한다.
- HTTP 헤더 필드명은 현재 커넥션만을 위한 정보이므로 다음 커넥션에 전달하면 안되고, 다른 곳으로 전달하는 시점에 삭제해야한다.
- HTTP 내 커넥션 관리는 end-to-end가 아닌 hop-by-hop인 두개의 연속된 노드 사이의 커넥션에 적용
(='헤더 보호하기')

### ② 순차트랜잭션 처리에 의한 지연

- 예를들어 3개의 이미지가 있는 웹페이지를 보려면, 해당 HTML 과 이미지파일 3개를 받아와야하는데, 순차적으로 처리한다면 이미지를 내려받는동안 빈 화면만을 봐야하는 경우가 발생한다. HTTP 커넥션의 성능을 향상시키는 여러 최신기술 4가지를 살펴본다.
    - **병렬(Parallel) 커넥션:** 여러개의 TCP 커넥션을 통한 HTTP 요청
        - 여러개의 커넥션을 맺어 여러개의 HTTP 트랜잭션을 병렬로 처리
        - 병렬커넥션은 페이지를 더 빠르게 내려받는다.
        - 항상 더 빠른 것은 아니다. 실제로 적은수의 병렬커넥션만 허용한다.(현재 대부분 6~8개 허용)
        [네트워크 대역폭이 좁은경우, 대부분의 시간을 데이터 전송에만 쓰게됨.]
        [다수의 커넥션은 메모리를 많이 소모해서 성능문제를 일으킬 수 있음.]
        - 더 빠르게 '느껴질 수' 있다. 여러개의 객체가 동시에 보이면서 내려받는걸 보기때문에 작업이 일어나는 중임을 사용자가 눈으로 확인이 가능해서 더 빠르다고 느낀다.
    - **지속(Persistent) 커넥션:** 커넥션을 맺고 끊는데 발생하는 지연 제거를 위한 TCP 커넥션 재활용
        - 처리가 완료된 후에도 TCP 커넥션을 유지하여 앞으로 있을 HTTP 요청에 재사용한다.
        - 병렬 커넥션과 함께 사용함으로써 상호보완할 수 있다. (4.5.1 참조)
        - 2가지 타입:
            - **HTTP/1.0+ 의 `keep-alive` connection**(4.5.2~4.5.7 참조)
            HTTP/1.1 명세에서는 사용하지 않지만, 널리 사용되었었기 때문에 처리할 수 있어야한다.
            커넥션 유지를 위해서 `Connection: Keep-Alive` 헤더를 포함한다.
            클라이언트, 서버 모두 언제든 keep-alive 요청을 끊거나 처리되는 트랜젝션 수 제한이 가능
            프락시에서 Connection 헤더를 이해하지 못하고 무조건 전달하면서 문제가 발생할 수 있다.
            이런 문제를 Proxy-Connection 을 통해 단일 무조건 전달 문제를 해결해준다.(차선책)
            하지만 프록시가 많은 구조에서는 여전히 문제가 발생할 수 있다.
            - **HTTP/1.1 `persistent` connection**
            keep-alive를 지원하지 않는 대신 설계가 더 개선된 지속 커넥션을 지원한다.
            기본적으로 활성화가 되어있고, 별도 설정이 없다면 지속커넥션으로 취급한다.
            응답에 `Connection:close` 헤더가 없다면, 응답후에도 커넥션을 유지하는것으로 추정한다.
            언제든지 서버,클라이언트는 커넥션을 끊을 수 있고, `Connection:close` 안 보냈다고 커넥션을 영원히 유지하겠다는 의미는 아니다.
    - **파이프라인(pipelined) 커넥션:** 공유 TCP 커넥션을 통한 병렬 HTTP 요청
        - keep-alive 커넥션의 성능을 높여준다.
        - 여러개의 요청에 대해 응답이 도착하기전까지 큐에 쌓여있다.
        - 지속커넥션인 경우에만 클라이언트는 파이프라인을 이을수있다.
        - 응답은 요청 순서와 같게 와야한다.
        - 커넥션이 끊어지더라도 언제든 다시 요청을 보낼 준비가 되어있어야한다.
        - post같은 요청은 요청 중 어떤것이 처리됬는지 알길이 없기 때문에 post보내면안된다.
    - **다중(Multiplexed) 커넥션** : 요청과 응답들에 대한 중재

## 4) 커넥션 끊기

### ① 마음대로 커넥션 끊기

클라이언트, 서버, 프록시 언제든지 TCP 전송 커넥션을 끊을 수 있다.

### ② Content-Length, Truncation

실제 전달된 엔터티 본문의 길이와, content-length값이 일치하지 않거나
Content-Length 자체가 존재하지 않으면 수신자는 데이터의 정확한길이를 서버에 물어봐야한다.

### ③ 커넥션 끊기 허용, 재시도, 멱등성

에러가 없더라도 커넥션은 언제든지 끊을 수 있다.

예상치 못하게 커넥션이 끊겼을때 적절히 대응할수 있어야 한다.
한번 혹은 여러번 실행 되었는지와 상관없이 같은 결과를 반환했을 때 트랜잭션을 멱등(idempotent)하다고 표현.

### ④우아한 커넥션 끊기

![04%E1%84%8C%E1%85%A1%E1%86%BC%20HTTP%20%E1%84%8F%E1%85%A5%E1%84%82%E1%85%A6%E1%86%A8%E1%84%89%E1%85%A7%E1%86%AB%202c2f16ac7a104afeb6b8a0173d50b33a/_2021-06-03__6.05.06.png](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F82a894cf-8e25-413f-b553-444f0d816a92%2F_2021-06-03__6.05.06.png?table=block&id=0493fa5f-4039-48f4-80c6-cdd7ad603d0f&spaceId=da06fe4c-dbc0-451e-a09d-8fe561a808ae&width=1410&userId=&cache=v2)

- 전체끊기(a)와 절반 끊기(b,c)

---

[참조링크]

1. OSI 7 layers (segment,pakets,..): [https://krylon.tistory.com/114](https://krylon.tistory.com/114)
2. 소켓통신 그림:  [http://jkkang.net/unix/netprg/chap2/net2_1.html](http://jkkang.net/unix/netprg/chap2/net2_1.html)
3. HTTP 커넥션: [https://developer.mozilla.org/ko/docs/Web/HTTP/Connection_management_in_HTTP_1.x](https://developer.mozilla.org/ko/docs/Web/HTTP/Connection_management_in_HTTP_1.x)