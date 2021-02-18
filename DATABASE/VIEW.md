# View

* 하나 이상의 테이블을 합하여 만든 가상의 테이블
* 질의의 결과 만들어지는 가상의 테이블로, 실제 테이블 처럼 사용할 수 있다.
* 실제 디스크에는 저장되지 않고, 뷰 생성시 사용한 select 문의 정의를 DBMS가 저장한다.
* 장점
  * **편리성 & 재사용성**: 
    * 미리 정의된 뷰를 일반 테이블처럼 사용할 수 있기 때문에 편리.
    * 사용자가 필요한 정보만 요구에 맞게 가공하여 뷰로 만들어 쓸 수 있다.
    * 자주 사용되는 질의를 뷰로 미리 정의해 재사용이 가능하다.
  * **보안성**
    * 각 사용자별로 보안이 필요한 데이터를 제외하여 선별하여 보여줄 수 있다.
  * **독립성**
    * 논리 데이터베이스의 원본 테이블의 구조가 변해도, 응용프로그램에 영향을 주지 않도록 하는 논리적 독립성을 제공.
* SELECT 문을 제외한 일부 물리적인 테이블의 갱신작업을 수행하는데 제약이 있다.
* 기본키를 포함하지 않는 수정 요청이나, 테이블 2개 이상에서 속성을 포함하는 수정요청은 제약을 위한 할 가능성이 있으므로 갱신작업 제약이 있다.



### 뷰의 생성

* ```sql
  CREATE VIEW 뷰이름 [(열이름 [, ... n])]
  AS SELECT 문
  
  -- 예시
  create view vw_book
  as select * 
  from book
  where bookname like '%축구%';
  ```

* 뷰이름: 생성할 뷰의 이름

* 열이름: 뷰에서 사용할 열의 이름

* 열 이름과 select문에서 추출하는 속성은 1:1 대응





### 뷰의 수정

* 물리적인 테이블의 수정작업과 마찬가지로, 뷰도 필요에 따라 정의된 SQL문의 수정이 필요.

* 뷰의 수정은 CREATE VIEW문에 OR REPLACE명령을 더하여 작성

  ```sql
  CREATE OR REPLACE VIEW 뷰이름 [(열이름 [, ... n])]
  AS SELECT문
  
  --예
  create or replace view vw_orders (custid, name, address)
  as select custid, name, address
  from customer
  where address like '%영국%';
  ```





### 뷰의 삭제

* ```sql
  DROP VIEW 뷰이름 [,...n];
  
  --예
  DROP VIEW vw_orders;
  ```





#### 시스템 뷰

* DBMS는 데이터베이스 개체(테이블, 함수, 뷰 등)나 시스템의 통계 정보 등을 사용자가 직접 확인할 수 있도록 시스템 뷰를 만들어 제공한다.

* 시스템 뷰(=데이터 딕셔너리 뷰, 시스템 카탈로그)

* DBMS 관련 정보를 테이블 형태로 만들어 실시간으로 제공.

* 사용자들은 시스템뷰를 참조해서 데이터 베이스 튜닝, 기타문제들을 해결할 수 있다.

* MySQL 시스템 뷰는 INFORMATION_SCHEMA 데이터베이스에 저장되어 있으며, SELECT 명령으로 조회할 수 있다. 메뉴얼을 참조하여 필요한 뷰를 찾아 사용하면 된다. 

  ```sql
  SELECT * FROM INFORMATION_SCHEMA.TABLES
  WHERE table_schema like '스키마이름';
  
  --위 질의문은 아래 명령과 같다.
  show tables;
  ```

* 



