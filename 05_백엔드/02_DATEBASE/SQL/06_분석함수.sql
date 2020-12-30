-- 분석함수란: 특정 집합 내에서 결과 건수의 변화 없이 해당 집합 안에서 합계 및 카운트 등을 계산할 수 있는 함수이다.
-- 실습준비
CREATE TABLE PRODUCT_GROUP (
	GROUP_ID SERIAL PRIMARY KEY,
	GROUP_NAME VARCHAR(255) NOT NULL
);
-- decimal: 소수
CREATE TABLE PRODUCT(
	PRODUCT_ID SERIAL PRIMARY KEY,
	PRODUCT_NAME VARCHAR(255) NOT NULL,
	PRICE DECIMAL(11,2),
	GROUP_ID INT NOT NULL,
	FOREIGN KEY (GROUP_ID)
	REFERENCES PRODUCT_GROUP (GROUP_ID)
);

INSERT INTO PRODUCT_GROUP(GROUP_NAME) VALUES ('Smartphon'), ('Laptop'), ('Tablet');
INSERT INTO PRODUCT(PRODUCT_NAME, GROUP_ID, PRICE) 
VALUES 
	('Microsoft Lumia', 1, 200), 
	('HTC One', 1, 400), 
	('Nexus', 1, 500), 
	('iPhone', 1, 900),
	('HP Elite', 2, 1200),
	('Lenovo Thnkpad', 2, 700),
	('Sony VAIO', 2, 700),
	('Dell Vostro', 2, 800),
	('iPad', 3, 700),
	('Kindle Fire', 3, 1500),
	('Samsung Galaxy Tab', 3, 200);
	
COMMIT;


SELECT * FROM PRODUCT_GROUP;
SELECT * FROM product;

-- 집계함수는 집계의 결과만을 보여준다.
SELECT count(*)
FROM product;
-- 분석함수는 집계의 결과 및 집합을 함께 출력한다.
SELECT count(*) over(), A.*
FROM product A;





-- 분석함수 avg
-- 분석함수 문법 간략
-- 사용하고자 하는 분석함수를 쓰고, 대상 컬럼을 기재후 partition by에서 값을 구하는 기준컬럼을 쓰고, order by에서 정렬컬럼을 기재
-- 예시
SELECT c1,분석함수(c2, c3, ...), OVER (PARTITION BY c4 ORDER BY c5)
FROM TABLE_NAE;
-- 집계avg함수: 집계의 결과만을 출력한다.
SELECT avg(price) FROM product;
-- 집계 avg + group by
SELECT B.group_name, avg(price)
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id)
GROUP BY B.group_name;
-- 분석 avg함수: 보여줄것 다 보여주면서, 평균 가격도 보고싶을때!
-- 분석함수를 사용하여 결과 집합을 그대로 출력하면서, group_name기준의 평균 출력
-- group_name을 기준으로 price의 평균값 출력
SELECT A.product_name, A.price, B.group_name, AVG(A.price) OVER (PARTITION BY B.group_name)
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);
-- 
SELECT A.product_name, A.price, B.group_name, AVG(A.price) OVER (PARTITION BY B.group_name ORDER BY B.group_name)
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);
-- 누적 평균을 구할 수 있다. 
SELECT A.product_name, A.price, B.group_name, AVG(A.price) OVER (PARTITION BY B.group_name ORDER BY A.price)
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);
-- 




-- row_number 특정 집합 내에서 결과 건수의 변화 없이 해당 집합안에서 특정 컬럼의 순위를 구하는 함수이다.
-- 동일 순위가 있어도, 무조건 순차적으로 순위 매긴다. (1,2,3,4,...)
SELECT * FROM product_group;
SELECT * FROM product;
-- 
SELECT 
	A.product_name, 
	B.group_name, 
	A.price, 
	ROW_NUMBER () OVER 
		(PARTITION BY B.group_name ORDER BY A.Price desc)
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);
-- rank: 같은 순위면 같은 순위면서 다음 순위 건너뜀 (1,1,3,4...)
SELECT 
	A.product_name, 
	B.group_name, 
	A.price, 
	RANK () OVER 
		(PARTITION BY B.group_name ORDER BY A.Price desc)
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);
-- dense_rank: 같은 순위면 같은 순위면서 다음 순위 건너뛰지 않음 (1,1,2,3,...)
SELECT 
	A.product_name,
	B.group_name,
	A.price,
	DENSE_RANK () OVER (PARTITION BY B.group_name ORDER BY A.price)	
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);






-- first_value, last_value
-- 특정 집합 내에서 결과 건수의 변화 없이, 해당 집합안에서 특정컬럼의 첫번째 값 혹은 마지막 값을 구하는 함수
-- example01: 
SELECT 
	A.product_name, 
	B.group_name,
	A.price,
	FIRST_VALUE (A.price) OVER (PARTITION BY B.group_name ORDER BY A.price) AS LOWEST_PRICE_PER_GROUP
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id)

-- last value
-- 가장 마지막에 나오는 price 값 출력, group_name컬럼 기준 price컬럼 정렬중, 파티션의 첫번째 row~ 마지막 row까지
-- last value에 range를 추가하는 이유는, default value가 ragne between unbounded preceding and current row이기 때문.
SELECT 
	A.product_name, 
	B.group_name,
	A.price,
	LAST_VALUE (A.price) OVER 
	(PARTITION BY B.group_name ORDER BY A.price
	RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
	) AS LOWEST_PRICE_PER_GROUP
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);


-- LAG: 이전 행의 값을 찾는다. LAG(이전 값 찾을 행, 몇번째 이전값)
SELECT
	A.product_name,
	B.group_name,
	A.price,
	LAG(A.price, 1) OVER(PARTITION BY B.group_name ORDER BY A.price) AS prev_price,
	A.price - LAG(A.price, 1) OVER (PARTITION BY B.group_name ORDER BY A.price) AS cur_prev_diff
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);

-- LEAD: 다음행의 값을 찾는다.
SELECT
	A.product_name,
	B.group_name,
	A.price,
	LEAD(A.price, 1) OVER(PARTITION BY B.group_name ORDER BY A.price) AS prev_price,
	A.price - LEAD(A.price, 1) OVER (PARTITION BY B.group_name ORDER BY A.price) AS cur_prev_diff
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);


