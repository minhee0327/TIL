# 3 Tier Architecture

### 용어

##### 계층(Tier): 컴포넌트들의 물리적인 분리

##### 층(Layer): 컴포넌트들의 논리적인 분리

### 1-Tier

![072714_1307_3TierArchit1](https://github.com/minhee0327/TIL/blob/master/image/072714_1307_3TierArchit1.png)

### 2-Tier

![072714_1307_3TierArchit2](https://github.com/minhee0327/TIL/blob/master/image/072714_1307_3TierArchit2.png)

* 클라이언트에서 DB 서버로 직접 데이터 입력하고 불러오는 방식 
* file server, DBMS server등 서버와 클라이언트로 구성된 단순 분산처리.
  * 클라이언트 : Business Logic
  * 서버: 데이터베이스
* 장점
  * 개발이 편리하고, 개발비용이 저렴하다. 
* 단점
  * 보안 취약, 재사용 어려움. 서버에 부하가 많이 일어남. 



### 3-Tier

![072714_1307_3TierArchit3](https://github.com/minhee0327/TIL/blob/master/image/072714_1307_3TierArchit3.png)

- 클라이언트가 미들웨어로 메세지를 주고받으면서, 데이터베이스에 저장하여 사용하는 형태.

- 결과 값을 클라이언트가 약속된 메세지 형태로 받을 수 있는 양방향 프로그래밍.

- 장점

  - 보안 용이
  - 재사용 용이
  - 일정한 퍼포먼스 가능

- 단점

  - 개발 환경 복잡, 구현 어려움. 기간 늘어남

  - 개발 비용 비쌈. (미들웨어 및 하드웨어 도입 등)

    



[참조](https://m.blog.naver.com/limoremo/220073573980)

[참조](https://mkil.tistory.com/53)
