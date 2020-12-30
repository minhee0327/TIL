-- 데이터 조작 및 테이블관리
-- 데이터 수정, 삭제, 관리 등

-- 01. insert문
-- 테이블이 만들어지면 빈 공간이 만들어지는 것이며, 테이블 안에 데이터를 insert하는 것이 필요하다.
-- 2가지 방법, 테이블 컬럼 순서대로 입력 (모두입력) / 테이블 컬럼을 지정해서 삽입
INSERT INTO table_name VALUES (value1, value2, value3,...);
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
-- commit을 하는게 기본인데 dbeaver에 auto commit 설정이 되어있어서 생략
SELECT * FROM link;
-- 작은 따옴표 입력하고 싶을 때.
INSERT into link (url, name) values('''http://naver.com''', '''Naver''');
-- 여러개 입력하고 싶을 때.
INSERT into link (url, name) values('http://google.com', 'Google'), ('http://daum.net', 'Daum'), ('http://yahoo.com', 'Yahoo');

-- CTS: create table select? => 테이블의 스키마(껍데기)만 가져와서, 테이블을 생성한다. 가져온 테이블의 기존 구조와 같고, 데이터는 0건인 스키마가 만들어진다.
CREATE TABLE link_tmp AS SELECT * FROM link WHERE 0 = 1;
SELECT * FROM link_tmp;
--
INSERT INTO link_tmp SELECT * FROM link;
SELECT * FROM link_tmp;
-- (link_tmp) - (link)
SELECT * FROM link_tmp
EXCEPT
SELECT * FROM link;
-- (link) - (link_tmp)
SELECT * FROM link
EXCEPT
SELECT * FROM link_tmp;









-- 02. update
-- 갱신, 테이블의 존재하는 데이터를 수정하는 작업. 동시성에 유의
-- 대상 행에 대해 다른 사용자는 해당 행에 대해 작업을 하지 못하도록 락(lock)을 건다. 
-- 즉 update를 한 후, 재빨리 commit하지 않으면 rdbms의 동시성이 낮아진다. (빠르게 commit할 수 있도록 할 것)
-- rdbms를 사용하는 이유: 데이터를 저장소에 저장해두고, 여러명의 사용자가 동시에 들어올 수 있게끔하기 위해.
UPDATE					-- uptdate할 테이블 지정
	table_name 
SET 					-- 수정할 컬럼 및 값 입력
	column1 = value1, 
	column2 = value2
WHERE					-- 대상조건
	조건;
	
-- 실습 준비
-- column추가
ALTER TABLE link ADD COLUMN last_update DATE;
ALTER TABLE link ALTER COLUMN last_update SET DEFAULT CURRENT_date; -- last_update 컬럼의 기본값: 현재날짜.
SELECT * FROM link;  
COMMIT;
-- 수정(last_update컬럼이 null인것을 => default value로 수정)
UPDATE link SET last_update = DEFAULT WHERE last_update IS NULL;
SELECT * FROM link;
-- 테이블 rel컬럼을 모두 'NO DATA'로 변경
-- 경고창: where절 없이 update 수행하려하는데, data가 손실될 수 있다. => dangerous query (전체컬럼을 바꾸는 실수를 방지하려고 뜨는 알림창)
UPDATE link SET rel ='NO DATA';
UPDATE link SET description = name;









-- 03. update join문
-- update시 다른 테이블의 내용을 참조하고 싶을 때 사용. 
-- 기본 문법
UPDATE target_table A				-- update할 테이블 지정
SET A.column_1 = 표현식				-- 특정 컬럼 update
FROM ref_table B					-- 참조 테이블 지정
WHERE A.column_1 = B.column_1; 		-- 조인 조건
--조회
SELECT * FROM product_segment;
SELECT * FROM product;
-- 정가(price) * 할인률(discount) => net_price column을 업데이트 해보자.
UPDATE product A
SET net_price =A.price - A.price * B.discount
FROM product_segment B
WHERE A.segment_id = B.id;






-- 04. delete
-- 테이블에서 특정 데이터를 삭제하거나 테이블 내에 존재하는 모든 데이터를 삭제할 수 있다.
DELETE FROM 테이블이름 WHERE 조건식;

DELETE FROM link WHERE id = 5;
SELECT * FROM link;

-- delete join
-- 두 테이블이 matching되는 row들을 모두 지운다.  
DELETE FROM link_tmp USING link WHERE link_tmp.id = link.id;
SELECT * FROM link_tmp;

-- 전체 행 삭제
DELETE FROM link;
SELECT count(*) FROM link;

DELETE FROM link_tmp;
SELECT count(*) FROM link;











-- 05. upsert문
-- insert 시도시 조건(상황)에 따라 update할 수 있는 구문.
-- 구문 예시
 INSERT
	INTO
	TABLE name(column_1) 			-- insert 시도
VALUES(value_1) ON
CONFLICT target ACTION;				-- 충돌시 다른 액션

-- do nothing: 충돌시 아무것도 하지 않음.
-- name이 unique조건이므로, 중복된 값이 없음에 주의하자.
INSERT INTO customers (name, email)
VALUES ('Microsoft', 'hotline@microsoft.com')
ON CONFLICT (name) DO NOTHING;

SELECT * FROM customers;

-- 충돌이 발생한 경우 do update + exclude(포함하여 내용이어가는 방법)
INSERT INTO customers(name, email)
VALUES ('Microsoft', 'hotline@microsoft')
ON CONFLICT (name) 
DO UPDATE SET email = EXCLUDED.email || ';' || customers.email;

SELECT * FROM customers;












-- 06. export 
-- 테이블의 데이터를 다른형태의 데이터로 추출하는 작업 (대표: csv)
-- 예
SELECT * FROM category;
-- C:\tmp가 있어야함
COPY category(category_id, name,last_update)
TO 'C:\tmp\DB_CATEGORY.csv'
DELIMITER ','
CSV HEADER;
-- text파일형태로 출력
COPY category(category_id, name,last_update)	-- 추출하고자하는 테이블과 컬럼
TO 'C:\tmp\DB_CATEGORY.txt'						-- 추출한 데이터를 저장할 파일경로\파일이름
DELIMITER '|'									-- 구분자 '|'
CSV HEADER; 									-- 파일형식, 컬럼명 추가
-- 
COPY category(category_id ,name, last_update)
TO 'C:\tmp\DB_CATEGORY_2.csv'
DELIMITER ','
CSV;











-- 07. import 
-- file => table로 넣기
-- import 실습준비
CREATE TABLE CATEGORY_IMPORT
(
	CATEGORY_ID serial NOT NULL
	, "name" varchar(25) NOT NULL
	, last_update timestamp NOT NULL DEFAULT now()
	, CONSTRAINT category_import_key PRIMARY KEY (category_id)
);

SELECT * FROM CATEGORY_IMPORT;

COPY category_import(category_id, "name", last_update)	-- 적재할 테이블 및 컬럼을 지정한다.
FROM 'C:\tmp\DB_category.csv'							-- 적재할 파일 지정
DELIMITER ','											-- 적재할 파일의 구분자를 알려준다.
CSV HEADER;												-- 파일형식 지정, header 사용유무

SELECT * FROM category_import;
DELETE FROM category_import;

COPY category_import (category_id, "name", last_update)
FROM 'C:\tmp\DB_category.txt'
DELIMITER '|'
CSV HEADER;

SELECT * FROM category_import;
DELETE FROM category_import;

COPY category_import(category_id, "name", last_update) 
FROM 'C:\tmp\DB_category_2.csv'
DELIMITER ','	
CSV ;													-- header가 없던 파일이므로, header키워드 제거









