-- 기본 data base 조회
select * from customer;
SELECT  FIRST_NAME, LAST_NAME, EMAIL FROM customer;
select A.FIRST_NAME, A.LAST_NAME, A.EMAIL from customer a;


-- order by: 가져온 데이터를 정렬, 업무 처리상 매우 중요 (ASC(오름차, default), DESC(내림차))
 SELECT
	FIRST_NAME,
	LAST_NAME
FROM
	customer
ORDER BY
	first_name ASC;


SELECT
	FIRST_NAME,
	LAST_NAME
FROM
	customer
ORDER BY
	first_name DESC;


SELECT
	first_name,
	last_name
FROM
	customer
ORDER BY
	first_name ASC,
	last_name DESC;


SELECT
	first_name,
	last_name
FROM
	customer
ORDER BY
	1 ASC,
	2 DESC;

-- select distict문 : 중복값을 제외한 결과값 출력 (DISTINCT 파일 참조)
 

-- 필터링1: where절
 SELECT
	LAST_NAME,
	FIRST_NAME
FROM
	customer
WHERE
	first_name = 'Jamie';


-- 조건이 2개일때 (and)
 SELECT
	LAST_NAME,
	FIRST_NAME
FROM
	CUSTOMER
WHERE
	first_name = 'Jamie'
	AND last_name = 'Rice';


-- 조건이 2개일때 (or)
 SELECT
	CUSTOMER_Id,
	AMOUNT,
	PAYMENT_DATE
FROM
	payment
WHERE
	AMOUNT <= 1
	OR AMOUNT >= 8;
	
-- LIMIT절: 특정 집합 출력시 출력하는 행의 수를 한정하는 역할. 부분 범위 처리. (MySQL, PostgreSQL)
-- OFFSET: 시작 위치 M+1 부터 (예 M:3 이면 0, 1, 2, 3, => 4번째 즉 3+1번째)
SELECT 
	* 
FROM
	TABLE_NMAE
LIMIT N OFFSET M;
-- 
SELECT * FROM film ORDER BY film_id ;

SELECT
	FILM_ID,
	TITLE,
	RELEASE_YEAR
FROM
	FILM
ORDER BY
	film_id
LIMIT 5;

SELECT
	FILM_ID,
	TITLE,
	RELEASE_YEAR
FROM
	FILM
ORDER BY
	film_id
LIMIT 4 OFFSET 3;

SELECT
	FILM_ID,
	TITLE,
	RENTAL_RATE
FROM
	FILM
ORDER BY
	RENTAL_RATE DESC
LIMIT 10;


-- FETCH절: 행의 수 한정, 부분 범위 처리시 사용
-- N을 입력하지 않고, ROW ONLY만 입력할 경우, 단 한건만 출력. (출력하는 행의 수 지정)
SELECT
	*
FROM
	TABLE_NAME FETCH FIRST [N] ROW ONLY;
	

-- 출력하는 행의 수를 지정하면서 시작위치 지정
 SELECT
	*
FROM
	TABLE_NAME OFFSET N ROWS FETCH FIRST [N] ROW ONLY;


-- 예시 (선입선출로, 최초 1건만 가져오는 경우에 쓰이는 경우가 많다.)
SELECT
	film_id,
	title
FROM
	film
ORDER BY
	title FETCH FIRST ROW ONLY;
	
-- 예시: 첫행부터 ~ n번째 행까지
SELECT
	film_id,
	title
FROM
	film
ORDER BY
	title FETCH FIRST 3 ROW ONLY;



-- 예시: 시작점 6부터 ~ 3개의 행을 가져오겠다.
 SELECT
	film_id,
	title
FROM
	film
ORDER BY
	title OFFSET 5 ROWS FETCH FIRST 3 ROW ONLY;


-- in 예시: customer_id가 1혹은 2 를 return_date기준으로 정렬
-- 가독성, 옵티마이저의 특성상, IN조건이 where or 조건보다 성능상 최적화에 좋다.
 SELECT
	customer_id,
	rental_id,
	return_date
FROM
	rental
WHERE
	customer_id IN (1,2)
ORDER BY
	return_date DESC;


-- or로 위 구문 같은 결과 만들어보기
 SELECT
	customer_id,
	rental_id,
	return_date
FROM
	rental
WHERE
	customer_id = 1
	OR customer_id = 2
ORDER BY
	return_date DESC; 
	

-- not in 
-- 1혹은 2를 제외한 나머지 ( 1혹은 2가 아닌 것)
SELECT 
	customer_id,
	rental_id,
	return_date
FROM 
	rental
WHERE 
	customer_id NOT IN (1, 2)
ORDER BY 
	return_date DESC;

-- and로 작성해보기
SELECT 
	customer_id,
	rental_id,
	return_date
FROM 
	rental
WHERE 
	customer_id <> 1 
	AND customer_id != 2
ORDER BY 
	return_date DESC;

--

SELECT 
	customer_id
FROM 
	rental
WHERE
	cast(return_date AS date) = '2005-05-27';



--
SELECT
	first_name,
	last_name
FROM
	customer
WHERE
	customer_id IN(
	SELECT
		customer_id
	FROM
		rental
	WHERE
		CAST(return_date AS date) = '2005-05-27');
		
	
--between (sql이 길어질수록 가독성을 위해 사용하는 것이 좋음)
SELECT customer_id, payment_id, amount
FROM payment
WHERE amount BETWEEN 8 AND 9;
-- and로 사용하는 방법
SELECT customer_id, payment_id, amount
FROM payment
WHERE amount >= 8 AND amount <= 9;
-- not between
SELECT customer_id, payment_id, amount
FROM payment
WHERE amount NOT BETWEEN 8 AND 9;
-- 위와 같은 결과
SELECT customer_id, payment_id, amount
FROM payment  
WHERE amount <8 OR amount  > 9;
-- between date 를 가지고 handling해보기
-- timestamp 에서 date 로 바꾼후 char타입으로 cast(형변환)
SELECT customer_id, payment_id, amount, payment_date
FROM payment
WHERE cast(payment_date AS date) BETWEEN '2007-02-07' AND '2007-02-15';
-- 위와 같은 결과지만 다른 방법
SELECT customer_id, payment_id, amount, payment_date
FROM payment
WHERE to_char(payment_date,'yyyy-mm-dd') BETWEEN '2007-02-07' AND '2007-02-15';




-- LIKE 연산자: 컬럼값이 특정 패턴과 유사한 집합 출력
-- 특정패턴에서 '%'는 어떤 문자 혹은 문자열이든지 매칭되었다 판단
-- 특정패턴에서 '_'는 한개의 문자가 어떤 문자이든지 매칭되었다고 판단한다.
-- Like 연산의 결과가 true일 때 결과가 출력됨.
SELECT first_name, last_name
FROM customer
WHERE first_name LIKE 'Jen%';
-- '%', '_' 연산결과 sample
SELECT 
	'FOO' LIKE 'FOO',
	'FOO' LIKE 'F%',
	'FOO' LIKE '_O_',
	'BAR' LIKE 'B_%',
	'BAR' LIKE 'B_';

	
-- IS NULL (IS NOT NULL)
-- 특정 컬럼 혹은 값이 널 값인지 아닌지를 판단하는 연산자. 
-- 새로 데이터 넣고 실습(isNull파일 참조)
SELECT * 
FROM table_name
WHERE column_nmae IS NULL;

