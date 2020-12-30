-- 집합 연산자와 서브쿼리
-- 01 union연산
-- 두개 이상의 select문들의 결과 집합을 단일 결과 집합으로 결합하며 결합 시 중복된 데이터는 제거된다.
-- 두개의 select문에서 중복되는 데이터 값이 있다면 중복은 제거된다.

-- 실습준비
CREATE TABLE SALES2007_1(NAME VARCHAR(50), AMOUNT NUMERIC(15, 2));
CREATE TABLE SALES2007_2(NAME VARCHAR(50), AMOUNT NUMERIC(15, 2));

INSERT INTO SALES2007_1 VALUES ('Mike', 150000.25), ('Jon', 132000.75), ('Mary', 100000);
INSERT INTO SALES2007_2 VALUES ('Mike', 120000.25), ('Jon', 142000.75), ('Mary', 100000);

COMMIT;
SELECT * FROM SALES2007_1;
SELECT * FROM SALES2007_2;

-- 각 테이블 전체 집합 합친 후, 중복제거
SELECT * FROM SALES2007_1 
UNION
SELECT * FROM SALES2007_2;
-- amount컬럼만 합친후, 중복제거
SELECT amount FROM SALES2007_1 
UNION
SELECT amount FROM SALES2007_2;
-- 합친 후 정렬할때
SELECT * FROM SALES2007_1 
UNION
SELECT * FROM SALES2007_2
ORDER BY amount desc;


-- union all연산
-- 두개 이상의 select문들의 결과 집합을 단일 결과 집합으로 결합하며 결합시 중복된 데이터도 모두 출력한다.
SELECT * FROM SALES2007_1 
UNION ALL 
SELECT * FROM SALES2007_2;

SELECT amount FROM SALES2007_1 
UNION ALL 
SELECT amount FROM SALES2007_2;

SELECT * FROM SALES2007_1 
UNION ALL 
SELECT * FROM SALES2007_2
ORDER BY amount desc;


-- intersect 연산
-- 두개이상의 select 문들의 결과 집합을 하나의 결과 집합으로 연결한다.
-- 집합 a와 집합 b의 교집합
-- 실습준비
DROP TABLE employees_1;
DROP TABLE hipos;
DROP TABLE keys;

CREATE TABLE employees_1(
	employee_id serial PRIMARY KEY
	, employee_name varchar(255) NOT null
);

CREATE TABLE keys(
	employee_id INT PRIMARY KEY, 
	effective_date date NOT NULL,
	FOREIGN KEY (employee_id) REFERENCES employees_1 (employee_id)
);

CREATE TABLE HIPOS 
(
	employee_id int PRIMARY KEY,
	effective_date date NOT NULL,
	FOREIGN KEY (employee_id) REFERENCES employees_1 (employee_id)
)

INSERT INTO employees_1 (employee_name) VALUES 
	('joyce Edwards'), 
	('Diane Collins'), 
	('Alice Stewart'), 
	('Julie Sanchez'), 
	('Heather Morris'), 
	('Teresa Rogers'), 
	('Doris Reed'), 
	('Gloria Cook'), 
	('Evelyn Morgan'), 
	('Jean Bell');
	
INSERT INTO keys VALUES 
	(1, '2000-02-01'),
	(2, '2001-06-01'),
	(5, '2002-01-01'),
	(7, '2005-06-01');
	
INSERT INTO hipos VALUES
	(9, '2000-01-01'),
	(2, '2002-06-01'),
	(5, '2006-06-01'),
	(10, '2005-06-01');
	
SELECT * FROM employees_1;
SELECT * FROM keys;
SELECT * FROM hipos;

-- INTERSECT: inner join과 결과가 동일하여 자주 사용되는 명령은.. X
SELECT
	employee_id
FROM 
	keys
INTERSECT
SELECT
	employee_id
FROM 
	hipos;
--
SELECT
	employee_id
FROM 
	keys
INTERSECT
SELECT
	employee_id
FROM 
	hipos
ORDER BY employee_id DESC ;
-- inner join
SELECT 
	A.employee_id 
FROM keys A, hipos B
WHERE A.employee_id = B.employee_id ;
--
SELECT A.employee_id
FROM keys A INNER JOIN hipos B
ON A.employee_id = B.employee_id ;



-- except연산자: 맨 위에 select문의 결과 집합에서 그 아래에 있는 select 문의 결과 집합을 제외한 결과 리턴
-- 아래 구문: 재고 O 집합
-- 필름과 인벤토리 1:m관계 => 두 테이블 조인 => 영화 하나당 여러개의 재고
SELECT 
	DISTINCT A.film_id
	,B.title 
	FROM inventory A
INNER JOIN 
	film B
ON A.film_id = B.film_id
ORDER BY B.title;
-- 재고 없는 집합: 전체 - 재고 있는 집합
SELECT 
	film_id
	, title
FROM film
EXCEPT 
SELECT 
	DISTINCT A.film_id
	, B.title
	FROM inventory A
INNER JOIN 
	film B
	ON A.film_id = B.film_id
ORDER BY title ;
--
--SELECT * FROM inventory WHERE film_id = 13;
