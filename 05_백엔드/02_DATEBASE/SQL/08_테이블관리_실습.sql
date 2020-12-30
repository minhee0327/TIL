CREATE TABLE data_type_test_1
(
	A_BOOLEAN BOOLEAN
	, B_CHAR CHAR(10)
	, C_VARCHAR VARCHAR(10)
	, D_TEXT TEXT
	, E_INT INT
	, F_SMALLINT SMALLINT
	, G_FLOAT FLOAT
	, H_NUMERIC NUMERIC(15, 2)
);

INSERT INTO DATA_TYPE_TEST_1 VALUES (TRUE, 'ABCDE', 'ABCDE', 'TEXT', 1000, 10, 10.12345, 10.25);

SELECT * FROM DATA_TYPE_TEST_1;
SELECT * FROM DATA_TYPE_TEST_2;


CREATE TABLE data_type_test_2
(
	A_DATE DATE
	, B_TIME TIME
	, C_TIMESTAMP TIMESTAMP
	, D_ARRAY TEXT[]
	, E_JSON JSON
);

INSERT INTO DATA_TYPE_TEST_2 VALUES 
	(CURRENT_DATE, 
	LOCALTIME, 
	CURRENT_TIMESTAMP, 
	ARRAY['010-1234-1234', '010-9992-8888'], 
	'{"customer":"John Doe", "items":{"product":"Beer", "qty": 6}}'
	);
	
SELECT * FROM data_type_test_2;




-- 테이블 생성 실습
CREATE TABLE ACCOUNT (
	USER_ID SERIAL PRIMARY KEY
	, USERNAME VARCHAR(50) UNIQUE NOT NULL
	, PASSWORD VARCHAR(50) NOT NULL
	, EMAIL VARCHAR(355) UNIQUE NOT NULL
	, CREATED_ON TIMESTAMP NOT NULL
	, LAST_LOGIN TIMESTAMP
);

CREATE TABLE ROLE(
	ROLE_ID SERIAL PRIMARY KEY
	, ROLE_NAME VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE ACCOUNT_ROLE(
	USER_ID INTEGER NOT NULL
	, ROLE_ID INTEGER NOT NULL
	, GRANT_DATE TIMESTAMP WITHOUT TIME ZONE
	, PRIMARY KEY (USER_ID, ROLE_ID)
	, CONSTRAINT ACCOUNT_ROLE_ROLE_ID_FKEY FOREIGN KEY (ROLE_ID)   	-- ROLE_ID 컬럼은 ROLL 테이블의 ROLE_ID컬럼을 참조
	REFERENCES ROLE(ROLE_ID) MATCH SIMPLE							-- ROLE_ID컬럼은 ROLE테이블의 ROLE_ID컬럼에 대한 삭제 혹은 변경시 아무것도 하지 않는다.
	ON UPDATE NO ACTION ON DELETE NO ACTION
	, CONSTRAINT ACCOUNT_ROLE_USER_ID_FKEY FOREIGN KEY (USER_ID)
	REFERENCES ACCOUNT(USER_ID) MATCH SIMPLE
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

INSERT INTO account VALUES (1, '강민희', '1234', 'mini@naver.com', current_timestamp, null);
SELECT * FROM account;

INSERT INTO ROLE values(1, 'DBA');
SELECT * FROM ROLE;

INSERT INTO account_role values(1, 1, current_timestamp);
SELECT * FROM account_role;


-- error 예시1 (참조 무결성 제약조건 위배)
INSERT INTO account_role values(2, 1 , current_timestamp);	-- user_id에 2가 없는데 넣으려 해서 나는 error; 참조하는 테이블의 pk가 null이거나 유일하지 않을 때 나는에러

-- error 예시2 
INSERT INTO account_role VALUES (1, 2, current_timestamp); 	-- role_id에 2가 없는데 넣으려 해서 나는 error;

-- error 예시3
INSERT INTO account_role values(1, 1, current_timestamp); 	-- 중복된 키 값은 들어갈 수 없음. (primary key니까), 개체무결성 pk는 항상 유일하며 not null만족해야함.

-- error 예시 4
UPDATE account SET user_id = 2 WHERE user_id =1; 			-- account table의 user_id를 account_role에서 참조하는 상황인데, 수정해버리면 안된다.




-- 테이블 관리
-- 03. CTAS: Create table as select 

select * FROM category WHERE category_id = 1;

-- 내가 원하는 정보만 추출
SELECT a.film_id, a.title, a.release_year, a.length, a.rating
FROM film a, film_category b
WHERE a.film_id = b.film_id AND b.category_id = 1;

-- 해당 결과집합으로 테이블 action_film을 만듬
CREATE TABLE action_film AS
SELECT a.film_id, a.title, a.release_year, a.length, a.rating
FROM film a, film_category b
WHERE a.film_id = b.film_id AND b.category_id = 1;

SELECT * FROM action_film;

-- not exists (존재하지 않을경우에만 생성, 존재할 경우 별도 작업 없이 종료.(error없이))
CREATE TABLE IF NOT EXISTS action_film AS
SELECT a.film_id, a.title, a.release_year, a.length, a.rating
FROM film a, film_category b
WHERE a.film_id = b.film_id AND b.category_id = 1;
-- 










-- 테이블 구조 변경실습
-- 한번 만들어진 테이블이더라도, 테이블 구조를 변경할 수 있다. (업무 변화에 유연하게 대처)
DROP TABLE LINKS;
CREATE TABLE LINKS (
	LINK_ID SERIAL PRIMARY KEY
	, TITLE VARCHAR(512) NOT NULL
	, URL VARCHAR(1024) NOT NULL UNIQUE
);

ALTER TABLE LINKS ADD COLUMN ACTIVE BOOLEAN;				-- ACTIVE COLUMN 추가
ALTER TABLE LINKS DROP COLUMN ACTIVE;						-- ACTIVE COLUMN 제거
ALTER TABLE LINKS RENAME COLUMN TITLE TO LINK_TITLE; 		-- TITLE COLUMN명을 LINK_TITLE로 변경
ALTER TABLE LINKS ADD COLUMN TARGET VARCHAR(10);			-- TARGET COLUMN 추가
ALTER TABLE LINKS ALTER COLUMN TARGET SET DEFAULT '_BLANK';	-- TARGET 컬럼의 DEFAULT를 "_BLANK"로 변경 


SELECT * FROM LINKS;

INSERT INTO LINKS (LINK_TITLE, URL) VALUES ('PostgreSQL', 'http://www.postgresqltutorial.com/');

ALTER TABLE LINKS ADD CHECK (TARGET IN('_BLANK', '_SELF', '_PARENT', '_TOP'));	-- TARGET COLUMN에 대한 체크 제약조건 추가

-- ERROR: TARGET CHECK 제약조건으로 4가지 종류만 허용함.
INSERT INTO LINKS (LINK_TITLE, URL, TARGET) VALUES ('PostgreSQL', 'http://www.postgresqltutorial.net/', '_WHATEVER');

-- _self는 check제약조건 안에 있으므로 사용가능.
INSERT INTO LINKS (LINK_TITLE, URL, TARGET) VALUES ('PostgreSQL', 'http://www.postgresqltutorial.org/', '_SELF');







-- 테이블 이름 변경
CREATE TABLE VENDORS (
	ID SERIAL PRIMARY KEY
	, NAME VARCHAR NOT NULL
);
CREATE TABLE SUPPLIER_GROUPS(
	ID SERIAL PRIMARY KEY
	, NAME VARCHAR NOT NULL
);

ALTER TABLE VENDORS RENAME TO SUPPLIERS;
ALTER TABLE SUPPLIERS ADD COLUMN GROUP_ID INT NOT NULL;
ALTER TABLE SUPPLIERS ADD FOREIGN KEY (GROUP_ID) REFERENCES SUPPLIER_GROUPS(ID);

SELECT * FROM SUPPLIERS;
SELECT * FROM SUPPLIER_GROUPS;

-- 뷰 (실체하는 데이터가 아닌 보기 용도)
CREATE VIEW SUPPLIER_DATA AS
SELECT 
	S.ID
	, S.NAME
	, B.NAME "GROUP"
FROM SUPPLIERS S, SUPPLIER_GROUPS B
WHERE S.GROUP_ID = B.ID

SELECT * FROM SUPPLIER_DATA;

-- TABLE명을 바꾸게 되면 기존의 참조 무결성 제약조건이나 뷰 등이 자동으로 갱신된다.
ALTER TABLE supplier_groups RENAME TO GROUPS;






-- 참고
-- 기본적으로 ORACLE(현존하는 최고의 DBMS), 특성을 알아두는게 좋다.
-- CREATE, DROP, ALTER => 치는순간 COMMIT (DDL)
-- DELETTE, UPDATE, MERGE, INSERT => 직접 COMMIT해주어야한다.

-- 컬럼 추가
CREATE TABLE TB_CUST(
	CUST_ID SERIAL PRIMARY KEY
	, CUST_NAME VARCHAR(50) NOT NULL
)

ALTER TABLE TB_CUST ADD COLUMN PHONE_NUMBER VARCHAR(13);
ALTER TABLE TB_CUST 
	ADD COLUMN  FAX_NUMBER VARCHAR(13),
	ADD COLUMN EMAIL_ADDR VARCHAR(50);

SELECT * FROM TB_CUST;

INSERT INTO tb_cust VALUES ( 1, '미니', '010-2121-1212', '031-212-1231', 'test@naver.com');

-- 기존 레코드들이 있고, 새로운 컬럼을 추가하게 되면 기존에 있던 레코드들에 null이 생기기 때문에 error발생한다.
ALTER TABLE tb_cust ADD COLUMN contact_nm varchar NOT NULL;
-- 이 경우, 해결책은 null조건으로 컬럼을 추가한다.
ALTER TABLE tb_cust ADD COLUMN contact_nm varchar NULL;
-- contact_nm컬럼을 update해준다.
UPDATE tb_cust SET contact_nm = '홍길동' WHERE cust_id = 1;
-- alter column으로 not null 제약조건을 준다.
ALTER TABLE tb_cust ALTER COLUMN contact_nm SET NOT NULL;
--





-- 컬럼 제거
CREATE TABLE PUBLISHERS (
	PUBLISHER_ID SERIAL PRIMARY KEY
	, NAME VARCHAR NOT NULL
);
DROP TABLE PRODUCTS CASCADE;
DROP TABLE categories;

CREATE TABLE CATEGORIES(
	CATEGORY_ID SERIAL PRIMARY KEY
	, NAME VARCHAR NOT NULL
);

CREATE TABLE BOOKS(
	BOOK_ID SERIAL PRIMARY KEY
	, TITLE VARCHAR NOT NULL
	, ISBN VARCHAR NOT NULL
	, PUBLISHED_DATE DATE NOT NULL
	, DESCRIPTION VARCHAR
	, CATEGORY_ID INT NOT NULL
	, PUBLISHER_ID INT NOT NULL
	, FOREIGN KEY (PUBLISHER_ID) REFERENCES PUBLISHERS (PUBLISHER_ID)
	, FOREIGN KEY (CATEGORY_ID) REFERENCES CATEGORIES (CATEGORY_ID)
);
CREATE VIEW BOOK_INFO AS SELECT
	B.BOOK_ID,
	B.TITLE,
	B.ISBN,
	B.PUBLISHED_DATE,
	P.NAME
FROM 
	BOOKS B
	,PUBLISHERS P
WHERE P.PUBLISHER_ID = B.PUBLISHER_ID
ORDER BY B.TITLE;

SELECT * FROM BOOK_INFO;
SELECT * FROM BOOKS;

ALTER TABLE BOOKS DROP COLUMN CATEGORY_ID;

-- VIEW에서 PUBLISHER_ID를 참조하고있기 때문에 아래 구문은 ERROR발생
ALTER TABLE BOOKS DROP COLUMN PUBLISHER_ID;

-- 이런경우, CASCADE옵션을 주어 삭제
-- 대신 참조하던 대상들도 같이 삭제가 된다.(주의)
-- DBA가 아니면 CASCADE를 사용해가며 삭제하지 않도록..!
ALTER TABLE BOOKS DROP COLUMN PUBLISHER_ID CASCADE;


-- 동시에 두개 컬럼 삭제해보기
ALTER TABLE BOOKS 
	DROP COLUMN ISBN,
	DROP COLUMN DESCRIPTION;














-- 컬럼 데이터 타입 변경
CREATE TABLE ASSETS(
	ID SERIAL PRIMARY KEY
	, NAME TEXT NOT NULL
	, ASSET_NO VARCHAR(10) NOT NULL
	, DESCRIPTION TEXT
	, LOCATION TEXT
	, AQUIRED_DATE DATE NOT NULL
);


INSERT INTO ASSETS (NAME, ASSET_NO, LOCATION, AQUIRED_DATE) 
VALUES 
	('Server', '10001', 'Server room', '2017-01-01')
	,('UPS', '10002', 'Server room', '2017-01-02');
	
SELECT * FROM assets;

ALTER TABLE assets ALTER COLUMN name TYPE varchar(50);
ALTER TABLE assets 
	ALTER column LOCATION TYPE varchar(100),
	ALTER COLUMN description TYPE varchar(500);
	
ALTER TABLE assets ALTER COLUMN asset_no TYPE int USING asset_no::integer;












-- 컬럼 이름 변경
DROP TABLE customer_groups;
DROP TABLE customers;
DROP TABLE customer_data;

CREATE TABLE CUSTOMER_GROUPS(
	ID SERIAL PRIMARY KEY
	, NAME VARCHAR NOT NULL
);

CREATE TABLE CUSTOMERS(
	ID SERIAL PRIMARY KEY
	, NAME VARCHAR NOT NULL
	, PHONE VARCHAR NOT NULL
	, EMAIL VARCHAR
	, GROUP_ID INT
	, FOREIGN KEY (GROUP_ID) REFERENCES CUSTOMER_GROUPS(ID)
);

CREATE VIEW CUSTOMER_DATA
AS SELECT 
	C.ID, 
	C.NAME,
	C.NAME CUSTOMER_GROUP
FROM CUSTOMERS C, CUSTOMER_GROUPS G
WHERE G.ID = C.GROUP_ID;

SELECT * FROM CUSTOMER_DATA;

-- 컬럼명이 바뀌었을 때, 뷰의 내용도 자동으로 바뀐다. 
ALTER TABLE CUSTOMERS RENAME COLUMN EMAIL TO CONTACT_EMAIL;
ALTER TABLE CUSTOMERS RENAME COLUMN NAME TO GROUP_NAME;










-- 테이블 제거
-- 테이블 제거 시는 항상 주의하고, fk관계도 유의할것
DROP TABLE page;

CREATE TABLE AUTHOR(
	AUTHOR_ID INT NOT NULL PRIMARY KEY
	, FIRSTNAME VARCHAR(50)
	, LASTNAME VARCHAR(50)
);

CREATE TABLE PAGE(
	PAGE_ID SERIAL PRIMARY KEY
	, TITLE VARCHAR(255) NOT NULL
	, CONTENT TEXT
	, AUTHOR_ID INT NOT NULL
	, FOREIGN KEY (AUTHOR_ID) REFERENCES AUTHOR(AUTHOR_ID)
);

INSERT INTO AUTHOR VALUES (1, 'kyounhoh', 'Lee');
INSERT INTO page VALUES (1, 'SQL과 데이터 베이스', 'drop table', 1);


-- fk 제약조건으로 인해 테이블 제거 실패
DROP TABLE author;
-- cacade 옵션으로 삭제
DROP TABLE author CASCADE;
-- page 테이블을 먼저 삭제할 수 있음! 자식 테이블이기 때문에 삭제 가능
DROP TABLE page;














-- 임시테이블
-- DB 접속 세션의 활동 기간동안 존재하는 테이블 (세션이 종료되면, 임시 테이블은 자동 소멸)
CREATE TEMP TABLE TB_CUST_TEMP_TEST(CUST_ID INT);

INSERT INTO tb_cust_temp_test values(1);
SELECT * FROM tb_cust_temp_test;

-- 기존에 존재하는 테이블과 같은 이름으로 임시테이블 생성후 임시 제거 해보기
DROP TABLE tb_cust_temp_test;
--일반테이블 생성 
CREATE TABLE tb_cust_temp_test (
	cust_id serial PRIMARY KEY,
	cust_nm varchar NOT null
);
-- 임시 테이블 생성 (기존의 일반 테이블과 같게)
CREATE TEMP TABLE tb_cust_temp_test(
	cust_id int
);
-- 조회 시, 임시 테이블 조회됨
SELECT * FROM tb_cust_temp_test;
-- 테이블 삭제
DROP TABLE tb_cust_temp_test;
-- 임시 테이블은 날아가고 일반 테이블만 남음!
SELECT * FROM tb_cust_temp_test;

-- 세션을 종료했다가 접속하게 될 경우 임시테이블은 날아가고, 일반 테이블을 바라보게 된다.















-- truncate: 대용량의 테이블을 빠르게 지울 수 있다. 세그먼트 자체를 바로 지우기 때문에 빠르게 데이터 지워진다.
CREATE TABLE truncate_test as
SELECT * FROM account;

SELECT * FROM truncate_test;

TRUNCATE TABLE truncate_test;

SELECT * FROM truncate_test;


