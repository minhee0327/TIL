# 데이터베이스 프로그래밍

## 01. 데이터 베이스 프로그래밍 개념

- **프로그래밍**:
    - 프로그램을 설계하고 소스코드를 작성해서 디버깅하는 과정.
- **데이터베이스 프로그래밍**:
    - DBMS에 데이터를 정의하고, 저장된 데이터를 읽어와 데이터를 변경하는 프로그램을 작성하는 과정.
    - Database 언어인 SQL을 포함한다.
    - 호스트 언어, DBMS의 종류, 운영체제, 컴퓨터 기종에 따라 다양하다.
    - 데이터 베이스 프로그래밍 대표 방법 4가지
        - **SQL 전용 언어를 사용하는 방법**
            - SQL 자체 기능을 확장하여 변수, 제어, 입출력 등의 기능을 추가한 새로운 언어를 사용
                - MySQL: 저장 프로그램(stroed program)
                - Oracle: PL/SQL
                - SQL Server: T-SQL
            - SQL 전용언어는 DB를 다루는 능력이 뛰어나고, 다루는 방법이 쉽지만, GUI를 구축하는 기능이 없어서, 독립적으로 사용하기 보다는 프로시저나 함수등으로 구현하여 다른 프로그램에서 호출해서 사용한다.
        - **일반 프로그래밍 언어에 SQL을 삽입(embeded)하는 방법**
            - 자바, C, C++등 일반 프로그래밍언어에 SQL을 삽입하여 사용하는 방법.
            - 삽입된 SQL문은 DBMS의 컴파일러가 처리한다.
            - 일반 프로그래밍언어로 작성된 응용프로그램에서 데이터 관리, 검색 가능.
            - SQL 단독으로 사용할 때보다 복잡한 로직 구현이 가능해짐.
        - **웹 프로그래밍 언어에 SQL을 삽입하여 사용하는 방법**
            - JSP, PHP, ASP 등 웹 스크립트 언어에 SQL을 삽입하여 사용하는 방법
            - 웹 프로그래밍 언어로 작성된 프로그램에서 데이터 관리, 검색 가능.
            - SQL문의 결과는 웹 브라우저에서 확인.
            - 아파치와 같은 웹 서버가 데이터 베이스 연동을 지원한다.
        - **4GL (4th Generation Language)**
            - 4세대 언어의 일종으로 DB 관리 기능과 비주얼 프로그래밍 기능을 가진 GUI 기반 SW 개발 도구를 사용하여 프로그래밍한다.
            - 개발 도구로는 Delphi, PwoerBuilder, Visual Basic 등이 있다.

## 02. 저장 프로그램

- 저장프로그램(stored Program): 데이터베이스 응용 프로그램을 작성하는데 사용하는 MySQL의 SQL 전용 언어.
- SQL문에 **변수, 제어, 입출력** 등의 **프로그래밍 기능을 추가**하여 SQL만으로 처리하기 어려운 문제들을 해결한다.

### 01) 저장 프로그램

- 프로그램 로직을 프로시저(procedure) 로 구현하여 객체 형태로 사용한다.
- 일반 프로그래밍 언어에서 함수와 비슷한 개념.
- 작업 순서가 정해진 독립된 프로그램의 수행 단위.
- 정의 된 후에 MySQL(DBMS)에 저장되므로 저장 프로그램래이라고 한다.
- **저장 프로그램 구성**
    - **저장 루틴(routine)**
        - **프로시저**
        - **함수**
    - **트리거(trigger)**: 데이터 변경문이 실행될 때 자동으로 같이 실행되는 프로시저.
    - **이벤트(event)**
- 저장 프로그램 정의 과정
    - SQL 편집기에서 프로그램 정의
    - 스크립트 실행
    - 실행 결과가 화면 창에 뜬 후, 개체 탐색기의 Stored Procedures/Functions 폴더에 객체가 만들어진다.
- 프로시저 정의
    - 정의 : CREATE PROICEDURE 문을 사용.
    - 선언부-실행부(BEGIN-END)로 구성
        - 선언부에서는 변수, 매개변수를 선언하고, 실행부에는 프로그램 로직을 구현
        - 매개변수: 저장 프로시저가 호출될 때 전달되는 값.
        - 변수: 저장 프로시저나 트리거 내에서 사용되는 값.
        - 주석: /**/, --
    - 프로시저의 끝을 ';' 로 처리하면 프로시저 안의 명령어 끝을 나타내는 ';' 와 혼돈이 생기므로 구문 구분자 delimiter를 설정하는 '//'를 정의한 후, 마지막에 다시 ';'를 재정의 한다.
- 예시1

    ```sql
    delimiter //
    CREATE procedure dorepeat (p1 INT)
    BEGIN
    	SET @x=0;
      REPEAT SET @x= @x+1; UNTIL @x>p1 END REPEAT;
    END
    //

    call dorepeat(1000);

    select @x;

    -- procedure 삭제
    DROP procedure dorepeat;
    ```

- 예시2: 삽입

    ```sql
    delimiter //
    CREATE procedure INSERTBOOK(
    	IN myBOOKID INTEGER,
        IN myBookName varchar(40),
        IN myPublisher VARCHAR(40),
        IN myPrice INTEGER)
    BEGIN
    	INSERT INTO Book (bookid, bookname, publisher, price) values(myBookID, myBookName, myPublisher, myPrice);
    END;
    //

    delimiter ;
        
    CALL INSERTBOOK(13,'스포츠과학', '과학서적', 35000);
    select * from book;

    DROP procedure dorepeat;
    ```

- 예시3: 결과 반환 프로시저

    ```sql
    delimiter //
    Create procedure AveragePrice(
    	OUT AverageVal Integer
        )
        BEGIN
    		select avg(price) into AverageVal from book where price is not null;
    	END;
    //
    delimiter ;

    CALL AveragePrice(@myValue);

    select @myValue;
    ```

- 예시4: 커서를 사용한 프로시저

    ```sql
    delimiter //
    create procedure interest()
    begin
    	declare myInterest INTEGER default 0.0;
        declare Price integer;
        declare endOfRow boolean default false;
        declare InterestCursor CURSOR FOR
    		select saleprice FROM orders;
    	declare continue handler for not found set endOfRow = TRUE;
        OPEN InterestCursor;
        cursor_loop:LOOP
        fetch InterestCursor INTO PRICE;
        IF endOfRow THEN LEAVE cursor_loop;
        END IF;
        IF Price >= 30000 THEN
    		SET myInterest = myInterest + Price *0.1;
    	else
    		SET myInterest = myInterest + Price *0.05;
    	END IF;
    END LOOP cursor_loop;
    CLOSE InterestCursor;
    select concat('전체 이익 금액 = ', myInterest);
    END;
    //

    delimiter ;

    drop procedure interest;
    CALL interest();
    ```

    ### 02) 트리거

    - 데이터의 변경(INSERT, UPDATE, DELETE) 문이 실행될 때, 자동으로 같이 실행되는 프로시저.
    - 데이터의 변경문이 처리되는 세 가지 시점 (BEFORE, AFTER, INSTEAD OF)
    - 데이터의 변경이 일어날 때, 부수적으로 필요한 작업인 데이터의 기본값 제공, 데이터 제약 준수, SQL 뷰의 수정, 참조 무결성 작업 등을 수행한다.
    - 예시
        - 새로운 정보를 삽입할 때, 삽입된 내용을 백업하기 위해 Log에 삽입된 내용을 기록한다고 하자. 이 때, 삽입을 하면서 같이 log에 기록을 남길 수도 있지만 사용자 입장에서 번거롭기도 하고, 보안상 백업을 감추어야 할 경우도 있다. 이 기능을 수행하는 트리거를 작성해두면 편리하다.

    ```sql
    -- 실습 전 root 계정에서 트리거 작동을 위해 아래 구문 실행 (안하면 ERROR 1418)
    -- log_bin_trust_function_creators의 default value는 OFF 상태인데, 
    -- 이 상태에서는 권한이 있더라도, trigger나 function 생성이 불가능하다.
    -- OFF 상태에서는 root 권한이 없는 user 가 생성한 function을 일반 user가 사용 불가능하다.
    SET global log_bin_trust_function_creators=ON;

    -- (madang사용자, madang database에서)
    -- log를 남길 table생성
    create table log(
    	bookid_l integer,
    	bookname_l varchar(40),
    	publisher_l varchar(40),
    	rice_l integer
    );

    delimiter //
    CREATE TRIGGER InsertBook
    	AFTER INSERT ON Book for each row -- book 테이블에 행을 추가할 때마다
        BEGIN 
    		declare average INTEGER;
            -- new: 삽입될 튜플의 값
            insert into log values (new.bookid, new.bookname, new.publisher, new.price);
    	END;
    //

    delimiter ;

    insert into book values (14, "HTTP완벽가이드", "한빛미디어", 35000);

    select * from book;
    select * from log;
    ```

    - trigger 는 Book 테이블의 triggers 탭에 있다!

        ![image](https://github.com/minhee0327/TIL/blob/master/image/db-stored1.png)

### 03) 사용자 정의 함수

- 수학에서의 함수처럼, 입력된 값을 가공하여 결과값을 반환한다.
- 사용자가 직접 필요한 기능을 함수로 만들어 사용.
- **프로시저와 비슷해 보이지만, 프로시저는 CALL 명령에 의해 실행되는 독립적인 프로그램이고,**
- **사용자 정의 함수는select 문이나프로시저 내에서 호출되어 SQL문이나 프로시저에 값을 제공하는 용도로 사용된다.**
- 일반적으로 단일 값을 돌려주는 스칼라 함수가 일반적이다.
- 예시

```sql
delimiter //
CREATE FUNCTION func(
	PRICE INTEGER) RETURNS INT
BEGIN
	DECLARE myInterest INTEGER;
    -- 가격이 30,000원 이상이면 10%, 30000원 미만이면 5%
    IF PRICE >= 30000
		THEN SET MyInterest = PRICE * 0.1;
	ELSE 
		SET myInterest = PRICE * 0.05;
	END IF;
    RETURN MyInterest;
END;
//
delimiter ;

select custid, orderid, saleprice, func(saleprice) interest
from orders;

```

## 정리

- 저장 프로그램의 종류중 아래 3가지를 테스트 해봄
    - 프로시저
    - 트리거
    - 사용자 정의 함수
    
- 3가지 저장 프로그램의 차이점

    | 구분     | 프로시저                              | 트리거                                                       | 사용자함수                                   |
    | -------- | ------------------------------------- | ------------------------------------------------------------ | -------------------------------------------- |
    | 정의방법 | CREATE PROCEDURE 문                   | CREATE TRIGGER 문                                            | CREATE FUNCTION 문                           |
    | 호출방법 | CALL문으로 직접 호출                  | INSERT, DELTE, UPDATE문이 실행될 때, 자동으로 실행           | SELECT문에 포함                              |
    | 기능차이 | SQL문으로 할 수 없는 복잡한 로직 수행 | 기본값 제공, 데이터 제약 준수, SLQ 뷰의 수정, 참조 무결성 작업 등을 수행 | 속성 값을 가공하여 반환, SQL문에서 직접 사용 |

    

- 공통점: 저장 프로그램

---

[참조 목록]

[도서] MySQL로 배우는 데이터베이스 개론과 실습 chapter 5 참조

[[트리거나 함수 생성전 세팅]](https://www.leafcats.com/271) 

[[관련 mysql 공식 홈페이지 자료]](https://dev.mysql.com/doc/refman/8.0/en/stored-objects.html)