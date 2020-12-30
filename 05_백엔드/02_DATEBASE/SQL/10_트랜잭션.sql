-- 조건 연산자
-- with문, 트랜젝션

-- 01. case
-- if/else문과 같은 로직을 구사할 수 있다. 

-- case 표현식 문법
SELECT 
	CASE WHEN 조건식1 THEN 결과1
	CASE WHEN 조건식2 THEN 결과2
		 ELSE 결과3
 	END
 	
 	
-- 예
SELECT * FROM film;
-- 행은 1개로 가져가면서 컬럼 3개로 출력
SELECT 
	sum(
		CASE WHEN rental_rate = 0.99 THEN 1
		ELSE 0 END 
	) AS "C",
	sum(
		CASE WHEN rental_rate = 2.99 THEN 1
		ELSE 0 END 
	) AS "B",
	sum(
		CASE WHEN rental_rate = 4.99 THEN 1
		ELSE 0 END 
	) AS "B"
	FROM film;

-- 위와 같은 결과지만 다른 표현방법 (행 => 열 로 변환)
SELECT * 
FROM (
	SELECT 
	sum(CASE WHEN rental_rate = 0.99 THEN cnt ELSE 0 end) AS C,
	sum(CASE WHEN rental_rate = 2.99 THEN cnt ELSE 0 end) AS B,
	sum(CASE WHEN rental_rate = 4.99 THEN cnt ELSE 0 end) AS A
		FROM (
			SELECT rental_rate, count(*)cnt
			FROM film
			GROUP BY rental_rate
	)A
)A




-- 행을 3개로 출력
SELECT rental_rate, count(*) cnt
FROM film
GROUP BY rental_rate;











-- coalesce: 입력한 인자값 중 null값이 아닌 첫번째 값 반환
CREATE TABLE tb_item_coalesce_test(
	id serial PRIMARY KEY
	, product varchar(100) NOT NULL
	, price NUMERIC NOT NULL
	, discount numeric
);


INSERT INTO tb_item_coalesce_test (product, price, discount) VALUES
	('A', 1000, 10), 
	('B', 1500, 20), 
	('C', 800, 5), 
	('D', 500, NULL);
	

SELECT * FROM tb_item_coalesce_test;
-- 연산에 null이 포함되면, null이 나오게됨. price- discount를 했을 때 할인가가 null일 경우에는 그냥 price를 출력하고싶음! 이런상황에서 사용
SELECT product , (price - discount) AS net_price FROM tb_item_coalesce_test;
-- coalesce를 활용하여 null일 경우 두번째 인자를 반환하고, null이 아닐 경우 첫번째 값을 리턴해준다.
SELECT product,price, discount, COALESCE(discount, 0), (price - COALESCE (discount, 0)) AS net_price
FROM tb_item_coalesce_test;


-- case를 활용하여 위와 같이 표현해보기
SELECT product,(price - 
	CASE WHEN discount IS NULL THEN 0
	ELSE discount
	END ) AS net_price 
FROM tb_item_coalesce_test;










-- null if 
-- 입력한 두개의 인자의 값이 동일하면 null리턴하고 그렇지 않으면 첫번째 인자 리턴한다.
CREATE TABLE tb_member_nullif_test(
	Id serial PRIMARY KEY
	, first_name varchar(50) NOT NULL
	, last_name varchar(50) NOT NULL
	, gender SMALLINT NOT NULL -- 1: male, 2:female
);

INSERT INTO tb_member_nullif_test(
	first_name,
	last_name,
	gender
)VALUES
('John', 'Doe', 1),
('David', 'Dave', 1),
('Bush', 'Lily', 2);

SELECT * FROM tb_member_nullif_test;


-- 여자 대비 남자 비율 구해보기 (남2/여1 * 100)
SELECT sum(CASE WHEN gender = 1 THEN 1 ELSE 0 end) / sum(CASE WHEN gender = 2 THEN 1 ELSE 0 end) * 100 AS "MALE/FEMALE RATIO"
FROM tb_member_nullif_test ;

-- 0으로 나누는 경우 error가 나온다.
-- test 위해 한명 있던 여자를 남자로 변경
UPDATE tb_member_nullif_test SET gender = 1 WHERE gender = 2;
SELECT * FROM tb_member_nullif_test;
-- error발생 (여자가 0명이므로) 0으로 나눌 수 없다는 error를 낸다.
SELECT sum(CASE WHEN gender = 1 THEN 1 ELSE 0 end) / sum(CASE WHEN gender = 2 THEN 1 ELSE 0 end) * 100 AS "MALE/FEMALE RATIO"
FROM tb_member_nullif_test ;
-- 여성의 합계가 0이면 null을 리턴하도록 한다. (남자3 /null => null)
SELECT sum(CASE WHEN gender = 1 THEN 1 ELSE 0 end) / NULLIF(sum(CASE WHEN gender = 2 THEN 1 ELSE 0 end),0) * 100 AS "MALE/FEMALE RATIO"
FROM tb_member_nullif_test ;







-- cast: 특정 데이터 타입으로 형변환하는 것.
-- 각종 데이터 값을 cast 표현식을 활용하여 적절히 형변환한다.
-- 문자 => integer(정수형)
SELECT cast('100' AS integer);
SELECT '100'::integer;
-- 문자 => date타입으로
SELECT cast('2020-11-26' AS date);
SELECT '2020-11-26'::date;
-- 문자열을 실수형으로
SELECT cast('10.2' AS double precision);
SELECT '10.2'::double PRECISION;








-- with문의 활용
-- length별로 short, medium, long으로 나눔
SELECT film_id, title,
	(CASE
		WHEN length < 30 THEN 'short'
		WHEN length >=30 AND length <90 THEN 'medium'
		WHEN length >=90 THEN 'long'
		END 
	)length 
FROM film;


-- with문을 활용하여 해당 집합을 tmp1에 저장하고 select문으로 tmp1을 조회해볼 수 있다.
WITH TMP1 AS
(SELECT
	film_id,
	title,
	(CASE
		WHEN length < 30 THEN 'short'
		WHEN length >= 30
		AND length <90 THEN 'medium'
		WHEN length >= 90 THEN 'long'
	END )length
FROM
	film) SELECT * FROM tmp1 WHERE length ='long';












-- 재귀쿼리
-- with무을 이용하여 재귀쿼리를 작성할 수 있다. 데이터 값 기준 부모자식간의 관계를 표현하는 sql이다.

CREATE TABLE tb_emp_recursive_test(
	employee_id serial PRIMARY KEY
	, full_name varchar NOT NULL
	, manager_id int
);

INSERT INTO tb_emp_recursive_test (employee_id, full_name, manager_id)
VALUES
	(1, '이경오', null),
	(2, '김한이', 1),
	(3, '김승범', 1),
	(4, '하선주', 1),
	(5, '송백선', 1),
	(6, '이슬이', 2),
	(7, '홍발순', 2),
	(8, '김미순', 2),
	(9, '김선태', 2),
	(10, '이선형', 3),
	(11, '김선미', 3),
	(12, '김선훈', 3),
	(13, '이왕준', 3),
	(14, '김사원', 4),
	(15, '이시원', 4),
	(16, '최선영', 7),
	(17, '박태후', 7),
	(18, '최민준', 8),
	(19, '정택헌', 8),
	(20, '노가람', 8);
	
SELECT * FROM tb_emp_recursive_test;


-- 최고 관리자부터 ~ 마지막까지 depth
WITH RECURSIVE tmp1 as(
	SELECT employee_id, manager_id, full_name, 0 lvl FROM tb_emp_recursive_test
	union
	SELECT e.employee_id, e.manager_id, e.full_name, s.lvl + 1 FROM tb_emp_recursive_test e, tmp1 S
)SELECT employee_id, manager_id, lpad(' ', 4 * lvl) || full_name AS full_name FROM tmp1



WITH RECURSIVE tmp1 as(
	SELECT employee_id, manager_id, full_name, 0 lvl FROM tb_emp_recursive_test WHERE employee_id = 2
	UNION 
	SELECT e.employee_id, e.manager_id, e.full_name, s.lvl + 1 FROM tb_emp_recursive_test e, tmp1 s WHERE s.employee_id = e.manager_id
)SELECT employee_id , manager_id , lpad(' ', 4 * lvl) || full_name AS full_name FROM tmp1;











-- 트랜젝션
-- begin, commit, rollback
CREATE TABLE tb_account_transaction_test(
	id int GENERATED BY DEFAULT AS IDENTITY
	, name varchar(100) NOT NULL
	, balance dec(15, 2) NOT NULL
	, PRIMARY key(id)
);

BEGIN;

INSERT INTO tb_account_transaction_test (name, balance) VALUES ('Alice', 10000);
INSERT INTO tb_account_transaction_test (name, balance) VALUES ('Danny', 20000);

COMMIT;

SELECT * FROM tb_account_transaction_test;