# SQL

### SQL 기본

* **문법 순서**

  ```sql
  SELECT
  FROM
  WHERE
  GROUP BY
  HAVING
  ORDER BY
  ```

* **실행순서**

  ```
  FROM		-- 해당 데이터가 있는 곳을 찾아서
  WHERE		-- 조건에 맞는 데이터만 가져와서
  GROUP BY	-- 선택한 column으로 그룹화
  HAVING		-- group by 결과를 나타내는 그룹을 제한
  SELECT		-- 속성(열) 출력 선택
  ORDER BY	-- 정렬	
  ```

* **주의사항 - 별칭(Alias)**

  * 실행 순서에 맞게 사용할 것!
    * 예: select 절에 alias를 정의했다면 order by절에서는 사용이 가능하지만, where절에서는 사용 불가능하다.
    * 이유: select 절보다 where절이 먼저 실행이 되기 때문!
  * 만약 실행 순서에 맞지 않게 사용하게 되면 Invalid Identifier라는 Error발생



---

### 하나의 테이블을 이용한 SQL 질의

* **where 절에 조건으로 사용가능한 술어**	

  | 술어     | 연산자                                                  | 사용 예                                        |
  | -------- | ------------------------------------------------------- | ---------------------------------------------- |
  | 비교     | <, >,  <=, >=,=, <>,                                    | price < 2000                                   |
  | 범위     | between                                                 | price between 1000 and 2000                    |
  | 집합     | in, not in                                              | price in (1000, 2000, 3000)                    |
  | 패턴     | LIKE(더 복잡한 패턴은 REGEXP 연산자로 정규 표현식 활용) | bookname like '축구의 역사'                    |
  | NULL     | IS NULL, IS NOT NULL                                    | price IS NULL                                  |
  | 복합조건 | and, or , not                                           | (price<2000) and (bookname like '축구의 역사') |

* **LIKE와 같이 사용하는 와일드 문자**

  | 와일드 문자 | 의미                          | 사용 예                                          |
  | ----------- | ----------------------------- | ------------------------------------------------ |
  | %           | 0 개 이상의 문자열과 일치     | '%축구%': 축구를 포함하는 문자열                 |
  | +           | 문자열 연결                   | '골프' + '바이블': '골프 바이블'                 |
  | []          | 1개의 문자와 일치             | '[0-5]%': 0-5 사이의 숫자로 시작하는 문자열      |
  | [^]         | 1개의 문자와 불일치           | '[^0-5]' : 0-5사이의 숫자로 시작하지 않는 문자열 |
  | _           | 특정 위치의 1개의 문자와 일치 | '_구%': 두번째 위치에 '구'가 들어가는 문자열     |

* **GROUP BY**

  * 속성 값이 같은 값 끼리 (튜플들의)그룹을 만들 수 있다.
  * select 절에는 group by 절에 사용한 속성 혹은 집계함수만 사용 가능.

* **Having**

  * 반드시 group by절과 같이 작성해야함.
  * where 절 보다 뒤에 와야함
  * 검색조건(select)에는 집계함수가 와야함.

---

### 2개 이상의 테이블 SQL 질의 

- **join (예시)**

  - 여러개의 테이블을 연결하여 하나의 테이블을 만드는 과정

  - 두 릴레이션(테이블)의 공통 속성을 기준으로, 속성(열)이 같은 튜플(행)을 수평으로 결합

  - 두 테이블에 조건이 없는 경우 카디전 프로덕트 연산(customer 행 * orders 행)

    ```sql
    select * 
    from customer, orders;
    ```

  - 동등 조인(equal join) : 동등 조건에 의해 join, 일반적

    ```sql
    select * 
    from customer c, orders o
    where c.custid = o.custid;
    
    select *
    from customerc inner join orders o on c.custid = o.custid;
    ```

  - 세타 조인: 비교조건(>, >=, <. <=, =,!=)에 의해 join 이중 = 로 join 한걸 동등 조인이라고 할 수 있음.

  - 자연 조인: 중복 속성 제거

  - 셀프 조인(self join) : 하나의 테이블 (자신) 을 대상으로 조인

    ```
    select e.ename, e.job
    from emp m, emp e
    where m.empno = e.mgr and m.ename = "BLAKE";
    ```

  - 외부 조인(outer join) : 자연 조인 후, 모든 값 추출 (left, right, full)하되, 조인실패(대응 되지 않는 속성)시 NULL로 표시

    - MySQL에서 full outer join 은 left, right join을 union all해서 표현

      ```sql
      select c.name, o.saleprice
      from customer c left outer join orders o
      	on c.custid = o.custid
      union all
      select c.name, o.saleprice
      from customer c right outer join orders o
      	on c.custid = o.custid;
      ```

      

- **sub query (부속 질의)**
  - 부속질의 먼저 처리하고, 전체 질의를 처리

    ```sql
    select bookname
    from book
    where book.price = (
    	select MAX(price)
    	from book
    );
    ```

  - 부속질의 결과 4가지

    - 1*1  (단일행 * 단일열)
    - N*1 (다중행 * 단일열) - IN 키워드 활용
    - 1*N (단일행 * 다중열)
    - N*N (다중행 * 다중열)

  - 부속질의 간에는 상하관계가 있고, 실행 순서는 하위 부속질의를 먼저 실행하고, 그 결과를 이용해서 상위 부속질의를 실행한다.

  - 상관 질의 : 상위 부속질의와 하위 부속질의가 독립적이지 않고, 서로 관련을 맺고 있다.

    - ```sql
      select b1.bookname
      from book b1
      where b1.price > (
      	select avg(b2.price)
      	from book b2
      	where b1.publisher = b2.publisher
      )
      ```



---

### 집합연산자

* MySQL은 다른 DBMS와 달리, MINUS, INTERSECT연산이 별도로 없다. 대신 NOT IN, INNER JOIN을 사용.
* 합집합
  * UNION : 중복 제거 모든 결과
  * UNION ALL :중복을 포함하여 모든 결과

* 차집합(MINUS) -NOT IN 연산자
* 교집합(INTERSECT) - innter join



### EXISTS

* 조건에 맞는 튜플이 존재하면 결과에 포함

* 상관 부속 질의문 형식. 

  ```
  select name, address
  from customer cs
  where exists(
  	select * 
  	from orders od
  	wherer cs.custid = od.custid
  )
  ```

  * cs 테이블의 custid가 od테이블의 custid와 일치하면 존재하는 것 (true) => name, address 출


