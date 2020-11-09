-- join실습 준비
CREATE TABLE BASKET_A (ID INT PRIMARY KEY, FRUIT VARCHAR (100) NOT NULL);
CREATE TABLE BASKET_B (ID INT PRIMARY KEY, FRUIT VARCHAR (100) NOT NULL);

-- data 삽입 및 갱신 => commit or rollback; (트랜잭션 처리)
INSERT INTO BASKET_A (ID, FRUIT) VALUES (1, 'Apple'), (2, 'Orange'), (3,'Banana'), (4, 'Cucumber');
INSERT INTO BASKET_B (ID, FRUIT) VALUES (1, 'Orange'), (2, 'Apple'), (3,'Watermelon'), (4, 'Pear');
COMMIT;


SELECT * FROM basket_a;
SELECT * FROM basket_b;


-- inner join example01
 SELECT
	A.ID ID_A,
	A.FRUIT FRUIT_A,
	B.ID ID_B,
	B.FRUIT FRUIT_B
FROM
	BASKET_A A
INNER JOIN BASKET_B B ON
	A.FRUIT = B.FRUIT;

-- inner join example02
SELECT 
	A.CUSTOMER_ID ,
	A.FIRST_NAME,
	A.LAST_NAME ,
	A.EMAIL ,
	B.AMOUNT,
	B.PAYMENT_DATE
FROM 
	CUSTOMER A
INNER JOIN 
	PAYMENT B
ON A.CUSTOMER_ID  = B.CUSTOMER_ID;


-- 1:M의 관계
SELECT count(*) FROM payment;


-- inner join example03
 SELECT
	A.CUSTOMER_ID ,
	A.FIRST_NAME,
	A.LAST_NAME ,
	A.EMAIL ,
	B.AMOUNT,
	B.PAYMENT_DATE
FROM
	CUSTOMER A
INNER JOIN PAYMENT B ON
	A.customer_id = B.customer_id
WHERE
	A.customer_id = 2;

-- 고객 1: 결제 m : 직원1
SELECT 
	A.customer_ID, A.FIRST_NAME,
	A.LAST_NAME, A.EMAIL,
	B.AMOUNT, B.PAYMENT_DATE,
	C.FIRST_NAME AS S_FIRST_NAME,
	C.LAST_NAME AS S_LAST_NAME
FROM CUSTOMER A
INNER JOIN PAYMENT B ON A.CUSTOMER_ID = B.CUSTOMER_ID 
INNER JOIN STAFF C ON B.STAFF_ID = C.STAFF_ID;



-- outer조인(left) : 한쪽은 무조건 다 보여주고, 나머지 한쪽은 일치할 때만 가져옴
-- 예: 기준집합 => 보고자하는 => 기준 집합 출력할 때 => 고객은 다 보고싶은데 => 계약했던 안했던 고객을 보고 싶다. => 그 중 계약을 보여주면 좋다.
-- A는 다 나오되, B는 일치하는 것 만 나옴
 SELECT
	A.ID AS ID_A,
	A.FRUIT AS FRUIT_A,
	B.ID AS ID_B,
	B.FRUIT AS FRUIT_B
FROM
	BASKET_A A
LEFT JOIN BASKET_B B ON
	A.FRUIT = B.FRUIT;

-- outer join(left only): 
-- A의 모든 값들 중, B와 일치 하지 않은 경우만 출력
SELECT
	A.ID AS ID_A,
	A.FRUIT AS FRUIT_A,
	B.ID AS ID_B,
	B.FRUIT AS FRUIT_B
FROM
	BASKET_A A
LEFT JOIN BASKET_B B ON
	A.FRUIT = B.FRUIT
WHERE B.ID IS NULL;

-- outer join(right only)
--  B는 다 나오되, A는 일치하는 것 만 나옴
 SELECT
	A.ID AS ID_A,
	A.FRUIT AS FRUIT_A,
	B.ID AS ID_B,
	B.FRUIT AS FRUIT_B
FROM
	BASKET_A A
RIGHT JOIN BASKET_B B ON
	A.FRUIT = B.FRUIT;
	
-- outer join(left only): 
-- B의 모든 값들 중, A와 일치 하지 않은 경우만 출력
SELECT
	A.ID AS ID_A,
	A.FRUIT AS FRUIT_A,
	B.ID AS ID_B,
	B.FRUIT AS FRUIT_B
FROM
	BASKET_A A
RIGHT JOIN BASKET_B B ON
	A.FRUIT = B.FRUIT
WHERE A.ID IS NULL;



-- self join
-- 실습환경
-- manager 도, 대표이사도 모두 직원
-- table 설정할 때, manager는 모두 employee id를 참조한다고 조건을 둠.
-- 동일한 테이블이지만, 각각의 다른 집합으로 구성해놓고 selfjoin => 그다음 그 안에서 원하는 정보 추출
CREATE TABLE EMPLOYEE 
(
	EMPLOYEE_ID INT PRIMARY KEY
	, FIRST_NAME VARCHAR (255) NOT NULL
	, LAST_NAME VARCHAR (255) NOT NULL
	, MANAGER_ID INT 
	, FOREIGN KEY (MANAGER_ID)
	 REFERENCES EMPLOYEE (EMPLOYEE_ID)
	 ON DELETE CASCADE
);

INSERT
	INTO
	EMPLOYEE (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, MANAGER_ID)
VALUES
(1, 'Windy', 'Hays', NULL),
(2, 'Ava', 'Christensen', 1),
(3, 'Hanssan', 'Conner' , 1),
(4, 'Anna', 'Reeves', 2),
(5, 'Sau', 'Norman', 2),
(6, 'Kelsie', 'Hays', 3),
(7, 'Tory', 'Goff', 3),
(8, 'Salley', 'Lester', 3);

COMMIT;
SELECT * FROM employee;
-- self join: 테이블이 하나더라도 하나안에서도 관계가 있다.
-- self join example01: 사원의 메니저 정보를 null제외하고 추출할 수 있음. (inner join)
SELECT 
	E.first_name || ' ' || E.last_name AS EMPLOYEE,
	M.first_name || ' ' || M.last_name AS MANAGER
FROM EMPLOYEE E
INNER JOIN EMPLOYEE M
ON M.employee_id = E.manager_id
ORDER BY MANAGER;

-- self join example02: 사원의 메니저 정보를 null포함해서 모두 출력 가능 (outer join)
SELECT
	E.first_name || ' ' || E.last_name AS employee,
	M.first_name || ' ' || M.last_name AS manager
FROM employee E
LEFT OUTER JOIN employee M
ON M.employee_id = E.manager_id
ORDER BY manager;
-- self join example03: 부정형조건
SELECT 
	F1.title,
	F2.title,
	F1.length
FROM 
	film F1
INNER JOIN film F2
ON F1.film_id <> F2.film_id 
AND F1.length = F2.length
;


-- Full outer join (inner, left outer, right outer)

-- example01: basic full outer join
SELECT
	A.ID ID_A ,
	A.FRUIT FRUIT_A ,
	B.ID ID_B ,
	B.FRUIT FRUIT_B
FROM
	basket_a A
FULL OUTER JOIN basket_b B ON
	A.fruit = B.fruit;

-- example02: full outer (only outer)
SELECT
	A.ID ID_A ,
	A.FRUIT FRUIT_A ,
	B.ID ID_B ,
	B.FRUIT FRUIT_B
FROM
	basket_a A
FULL OUTER JOIN basket_b B ON
	A.fruit = B.fruit
WHERE
	A.ID IS NULL
	OR B.ID IS NULL;
	
-- 추가 실습 준비
CREATE TABLE
IF NOT EXISTS DEPARTMENTS
(
	DEPARTMENT_ID SERIAL PRIMARY KEY,
	DEPARTMENT_NAME VARCHAR (255) NOT NULL
);

CREATE TABLE
IF NOT EXISTS EMPLOYEES
(
	EMPLOYEE_ID SERIAL PRIMARY KEY,
	EMPLOYEE_NAME VARCHAR (255),
	DEPARTMENT_ID INTEGER
)

INSERT
	INTO
	DEPARTMENTS(DEPARTMENT_NAME)
VALUES ('Sales'),
('Marketing'),
('HR'),
('IT'),
('Production');

INSERT
	INTO
	EMPLOYEES (employee_name, department_id)
VALUES ('Bette Nicholson', 1),
('Christian Cable', 1),
('Joe Swank', 2),
('Fred Costner', 3),
('Sandra Kilmer', 4),
('Julia Mcqueen', NULL );

COMMIT;

SELECT * FROM employees;
SELECT * FROM departments;

-- example03 full outer join 
SELECT E.employee_name , D.department_name 
FROM employees E
FULL OUTER JOIN departments D
ON E.department_id = D.department_id; 

-- example04 full outer join (right only)
-- left가 null인 거
SELECT E.employee_name , D.department_name 
FROM employees E
FULL OUTER JOIN departments D
ON E.department_id = D.department_id 
WHERE E.employee_name IS NULL;

-- 위 구문은 right outer + right only와 동일하다. 
SELECT E.employee_name , D.department_name 
FROM employees E
RIGHT OUTER JOIN departments D
ON E.department_id = D.department_id 
WHERE E.employee_name IS NULL;

-- example 05: full outer join(left only)
SELECT E.employee_name , D.department_name 
FROM employees E
FULL OUTER JOIN departments D
ON E.department_id = D.department_id 
WHERE D.department_name IS NULL;
-- 마찬가지로 위 구문은 left outer join + left only로 표현 가능
SELECT E.employee_name , D.department_name 
FROM employees E
LEFT OUTER JOIN departments D
ON E.department_id = D.department_id 
WHERE D.department_name IS NULL;




-- CROSS JOIN: 두개의 테이블의 catesian product 연산 결과 출력 (데이터 복제에 많이 쓰임)
-- 실습 준비
CREATE TABLE CROSS_T1
(
	LABEL CHAR(1) PRIMARY KEY
);
CREATE TABLE CROSS_T2
(
	SCORE INT PRIMARY KEY
);
INSERT INTO CROSS_T1 (LABEL) VALUES ('A'), ('B');
COMMIT;
SELECT * FROM CROSS_T1;

INSERT INTO CROSS_T2 (SCORE) VALUES (1), (2), (3);
COMMIT;
SELECT * FROM CROSS_T2;

-- example01 cross join (on이 없음),  추력가능한 모든 경우의 수를 뽑는다.
SELECT
	*
FROM CROSS_T1
CROSS JOIN CROSS_T2
ORDER BY LABEL;

-- 조건이 없는 경우 inner join 방법
SELECT * 
FROM cross_t1, cross_t2
ORDER BY LABEL ;
-- 위 2 sql문 결과 집합 동일함 => 같은 sql문이라고 한다.
-- sql문의 목적이 집합을 출력하는 것 => 정보가 같다면, sql문 자체가 다르더라도 동일한 sql문이라고 한다.

SELECT 
	CASE WHEN LABEL ='A' THEN sum(score)
		 WHEN LABEL ='B' THEN sum(score) * -1
		 ELSE 0
		 END AS calc
FROM cross_t1
CROSS JOIN cross_t2
GROUP BY LABEL 
ORDER BY LABEL ;

-- nutural 조인: 실무에 많이 쓰이지는 않지만, inner join을 더 깊게 이해해볼 수 있다.
-- 실습 준비
CREATE TABLE CATEGORIES
(
	CATEGORY_ID SERIAL PRIMARY KEY,
	CATEGORY_NAME VARCHAR(255) NOT NULL
);

CREATE TABLE PRODUCTS
(
	PRODUCT_ID SERIAL PRIMARY KEY,
	PRODUCT_NAME VARCHAR(255) NOT NULL,
	CATEGORY_ID INT NOT NULL,
	FOREIGN KEY (CATEGORY_ID)
	REFERENCES CATEGORIES(CATEGORY_ID)
)

INSERT INTO CATEGORIES (CATEGORY_NAME) VALUES ('Smart Phone'), ('Laptop'), ('Tablet');
INSERT
	INTO
	PRODUCTS (PRODUCT_NAME, CATEGORY_ID)
VALUES 
('iPhone', 1),
('Samsung Galaxy', 1),
('HP Elite', 2),
('Lenovo Thinkpad', 2),
('iPad', 3),
('Kindle Fire', 3);

COMMIT;
SELECT * FROM categories;
SELECT * FROM products;

-- natural join: A, B 테이블간 동일하게 가지고 있는 컬럼을 기준으로 inner join한다.
-- inner join 의 도다른 sql작성방식으로, join 컬럼을 명시하지 않아도 동일하게 작동한다.
-- 자동으로 만들어지지만, 안정성이 떨어질 수 있다. (아무리 9999번 잘해도 1번 잘못되면 안정성이 100프로를 보장받지 못한다.)
SELECT * 
FROM products A
NATURAL JOIN categories B;
-- 위와 같은 결과
SELECT A.category_id, A.product_id, A.product_name, B.category_name
FROM products A, categories B
WHERE A.category_id = B.category_id;
-- 위와 같은 결과
SELECT A.category_id, A.product_id, A.product_name, B.category_name
FROM products A
INNER JOIN categories B
ON A.category_id = B.category_id;

-- natural join 다른 예 (안되는 경우 보여줌)
-- city table 과 country table의 동일한 이름으로 존재하는 column이 country_id, last_update가 있다.
-- 따라서 두 컬럼이 inner join에 성공해야지만 결과값이 나온다. => 결과 건수가 없게 나온다. 
-- 자동으로 join해서, 결과가 의도치 않은 방향으로 나올 수 있기 때문에 inner join으로 join 컬럼을 명시해서 의도한 대로 데이터 출력을 할 수 있다.

-- natural join 결과
SELECT * FROM city A NATURAL JOIN country B;
-- inner join 결과
SELECT * FROM city A INNER JOIN country B ON (A.country_id= B.country_id);
