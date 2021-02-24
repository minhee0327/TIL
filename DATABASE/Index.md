# Index

- # 인덱스

  > 개요

  - DBMS는 내가만든 table을 저장장치에 저장하고 필요에 따라 검색, 결과를 보여준다.
  - DBMS는 어떻게 DB를 저장하고 검색할까?
  - **B-tree**: DBMS에서 테이블이 저장되는 물리적인 구조와 함께, 대부분의 RDBMS가 사용하는 기본 자료구조.
  - MySQL에서 사용가능한 인덱스 종류 일부를 확인해보자.

  

  ### DB의 물리적인 저장

  - DBMS는 운영체제 위에서 실행되는 응용프로그램의 일종

  - SQL Tool (SQL Shell or WorkBench)을 통해서 SQL문을 작성하면

  - DBMS에 의해 처리방법이 결정이 되고, OS를 통해 각장치에 명령이 내려져서 작업을 처리한다.

  - **운영체제의 파일시스템에 종속적**인 데이터베이스파일로 저장된다. (OS file system 참조)

  - **실제 데이터가 저장되는 위치는 보조기억장치** (하드디스크(多), SSD, USB등등)
      - 하드디스크

          ![harddisk](https://github.com/minhee0327/TIL/blob/master/image/index-1.jfif)

          - 원형플레이트로 구성됨.
          - 플레이트는/ 논리적으로 트랙으로 나뉘며 / 트랙은 다시 몇개의 섹터로 나뉨
          - 회전하는 플레이트를 하드디스크의 Actuaor Arm과 헤더가 접근하여 원하는 섹터에서 데이터를 가져온다.
          - 하드디스크에 저장된 데이터를 읽어오는데 걸리는 시간에 영향받는 3가지.
              - 모터에의해 분당 회전하는 속도(RPM)
              - 데이터 읽을 때, 엑세스 암이 이동하는 시간 (latency time)
              - 주 기억장치로 읽어오는 시간(transfer time)
          - 위와 같은 디스크 입출력시간을  엑세스 시간이라고 한다. 엑세스 시간은 데이터의 저장, 읽기에 많은 영향을 끼친다.
              - access time = seek time + rotational latency time + data transfer time
                  - seek time : 탐색시간, 엑세스 헤드를 트랙에 이동시키는 시간
                  - rotational latency time: 회전지연시간, 섹터가 엑세스 헤드에 접근하는시간
                  - data transfer time: 데이터를 주 기억장치로 읽어오는 시간

        ![DBMS Structure](https://github.com/minhee0327/TIL/blob/master/image/index-2.png)

  - DBMS가 하드**디스크**에서 데이터를 저장하고 읽어올 때에는 근본적인 **속도 문제**가 발생할 수 밖에 없다. 이런 속도 문제를 줄이기 위해, 주기억장치에 DBMS가 사용하는 공간중 일부를 **buffer pool**로 만들어 사용하는 방법이 있다. 자주 사용하는 데이터를 저장하고, **LRU알고리즘**으로 사용빈도가 높은 데이터 위주로 **저장하고 관리**한다. 데이터 검색시, 버퍼풀에 저장된 데이터를 우선 읽어들여 작업을 진행한다.

  - DBMS는 DB 별로 1개 이상의 데이터 파일을 생성한다. 테이블은 생성시 정의된 내용에 따라 논리적으로 구분하여 각 데이터 파일에 저장한다. 이런 파일들은 DBMS 별로 고유한 파일주소를 가지고 동시에 수많은 사용자가 사용해야 하므로 특별한 처리방법을 통해 관리된다.

  - MySQL의 저장장치 엔진은 플러그인 방식으로 선택이 가능하고, InnoDB 엔진이 기본으로 설치되어있다. MySQL의 InnoDB는 주로 데이터파일, 폼파일등을 저장한다. 생성한 DB 별로 관리.

  

  

  

  ### 인덱스와 B-tree

  - **인덱스 (색인)**
      - 자료를 쉽고 빠르게 찾을수 있도록 만든 데이터 구조.
      - 일반적인 RDBMS의 인덱스는 대부분 B-tree 구조로 되어있다.

  - **B-tree**
      - 데이터 베이스와 파일 시스템에서 많이 사용하는 자료구조.
      - **데이터의 검색시간을 단축하기 위한 자료구조**
      - 이진 트리: 자식노드가 최대 2개, B-tree 는 자식 노드 갯수가 2개 이상인 트리.
      - 루트노드, 내부노드, 리프노드로 구성.
      - 노드의 데이터는 반드시 정렬된 상태여야 한다.
      - Leaf 노드로 가는 경로의 길이는 모두 같아야한다. 즉, 모두 같은 레벨에 존재해야한다.
      (균형 트리)
      - 각 노드는 키값과 포인터를 가지고 있고, 키값은 오름차 정렬 되어있음. 키의 좌우에 있는 포인터는 각각 키 값보다 작은 값과 큰 값을 가진 다음 노드를 가리킴.
      - 입력 자료는 중복될 수 없음.
      - 탐색:
          - 이진트리와 마찬가지로 작은 값은 왼쪽, 큰값은 오른쪽 서브트리에 이뤄져있음.
          - 루트 노드에서 값을 비교해서 중간단계인 내부노드에서 해당 노드를 찾고, 최종 마지막 레벨인 리프노드에 도달. 리프 노드에는 해당 데이터 저장 위치에 대응하는 rowid(RID, Row IDentify, 테이블 행에 대한 논리적 위치)를 가지고 있어 찾고자 하는 행을 바로 찾을 수 있다.
      - 삽입, 삭제 등 갱신시: 차수에 따라 다름. 동적으로 노드를 분할하거나 통합하면서 균형 유지

  - **인덱스 특징**
      - 인덱스는 테이블에서 한 개 이상의 속성(col)을 이용하여 생성함.
      - **빠른 검색**과 함께 효율적인 레코드 접근이 가능함.
      - 순서대로 **정렬**된 속성과 데이터의 **위치만 보유**하므로 테이블보다 **작은 공간**을 차지함.
      - 저장된 값들은 테이블의 부분집합이 됨.
      - 일반적으로 **B-tree** 형태의 구조를 가짐
      - 데이터의 수정, 삭제 등의 변경이 발생하면 인덱스의 재구성이 필요함.
      - 100만개의 튜플을 가진 데이터도 3-4번의 디스크 블록을 읽으면 찾을 수 있다.
      - 데이터 변경, 삽입이 많을 경우 모양 유지를 위해 분할 및 이동이 잦다.

  - **MySQL 인덱스**
      - 클러스터 인덱스(Clustered Index) & 보조 인덱스 (Secondary Index)
      - **클러스터 인덱스**
          - 연속되니 키값의 레코드를 묶어서 같은 블록에 저장하는 방법
          - **테이블당 하나만 생성 가능**
          - B-tree 인덱스 리프 노드에서 페이지의 주소 대신, 테이블의 열 자체가 저장되는 형태
          - 리프 노드들이 **정렬**된 상태로 저장된 테이블 자체가 된다.
          - 루트 노드의 키값을 비교해서, 해당 리프 노드로 이동하여 리프 노드의 행에서 해당 데이터를 찾는다.
          - 키 값에 의한 동등 및 범위(between) 검색에 모두 유리
          - 테이블 생성시 기본키 (PK)를 생성하면 자동 생성 된다.
          - 인덱스 페이지가 단순해져 인덱스 저장시 차지하는 공간이 작다.
          - 생성시 PK → UNIQUE → 자체 rowId 순서로 인덱스를 생성.

      - **보조 인덱스**
          - 속성의 값으로 B-tree 인덱스를 구성하며, 리프노드의 각 행은 해당 페이지의 주소 값 지정
          - 테이블의 데이터가 갱신 또는 삭제되면서 무작위로 데이터가 저장된다. 이 때, 저장된 데이터가 양이 많다면 원하는 자료를 찾기위한 시간이 오래 걸린다.
          - 생성된 인덱스의 리프노드는 실제 데이터 값이 아니라, 테이블상의 데이터 위치를 지정하는 rowid를 저장한다. (ex. Block번호 - Block 내의 Row가 위치한 순번)
          - 따라서 실제 테이블의 자료가 무작위로 (정렬되지 않은채로) 있더라도, 쉽게 찾을 수 있다.
          - 단일 컬럼 인덱스 뿐만 아나라 복합적으로 결합하여 사용하는 인덱스도 만들 수 있다.
          - 클러스터 인덱스가 아닌 모든 인덱스는 보조 인덱스.
          - 보조 인덱스를 검색하여 기본키 속성을 찾은다음, 클러스터 인덱스로 가서 해당 레코드(row)를 찾는다.
      - 인덱스를 사용하여 검색할 경우, 인덱스와 데이터 파일의 구조적인 특징으로 인해 **특정 키값을 찾는 검색의 경우는 성능 보장**이 가능.
      - 하지만 범위 검색은 데이터가 저장된 Blcok 값들의 저장 순서가 일정치 않을 수 있어서, 원하는 만큼의 빠른 검색 효과를 보장 할 수 없음.
      - 따라서 인덱스 구성시 자료 저장 및 질의 형태에 따라 신중히 생성해야한다.

  

  

  

  ### 인덱스 생성

  - 인덱스는 검색 속도 향상을 위해 사용
  - 하지만, 인덱스 사용한다고 (생성한다고) 데이터 검색이 무조건 빨라지는게 아님.
  - 데이터 양이 별로 없거나, 데이터 값이 몇 종류 안되면 인덱스 없는게 빠를 수도 있음
  (=선택도가 높다고 표현함. = 1/서로다른 값의 개수)
  - 의미 없이 인덱스를 생성하면 오히려 공간 낭비, 검색 속도가 떨어질 수 있음.
  - **인덱스 생성 고려사항.**
      - 인덱스는 WHERE절에 자주 사용되는 속성이어야 함.
      [where절에 자주 사용되는 속성일 수록 자주 접근한다는 의미니까.]
      - 인덱스는 Join(조인)에 자주 사용되는 속성이어야 함.
      - 단일 테이블에 인덱스가 많으면 속도가 느려질 수 있음
      - 속성이 가공되는 경우에 사용하지 않음
      - 속성의 선택도가 낮을 때 유리함
  - 단, 무분별하게 인덱스 많이 생성하면 오히려 효율이 느려질 수 있음. **테이블당 4~5개 정도 권장.**
  - 문법

  ```sql
  CREATE [UNIQUE] INDEX [인덱스이름]
  ON 테이블이름 (컬럼이름 [ASC|DESC] [{, 컬럼이름 [ASC|DESC]} ...]);
  ```

  - 인덱스 생성 예시

  ```sql
  CREATE INDEX ix_Book ON Book(bookname);
  CREATE INDEX ix_Book2 ON Book(publisher, price);
  ```

  - 생성된 index로 SQL문을 처리하는지 확인
  - workbench →[Query탭] → [Explain Current Statment]
  - 실행 결과

      ![index execute](https://github.com/minhee0327/TIL/blob/master/image/index-3.png)

  ---

  [하드디스크 구조 자료 ] [https://gsk121.tistory.com/260](https://gsk121.tistory.com/260)

  [MySQL DBMS구조] : [https://mysqldba.tistory.com/2](https://mysqldba.tistory.com/2)

  [B-tree] [https://hyungjoon6876.github.io/jlog/2018/07/20/btree.html](https://hyungjoon6876.github.io/jlog/2018/07/20/btree.html)

  [MySQL로 배우는 데이터 베이스 개론과 실습 책 내용 요약 및 정리]