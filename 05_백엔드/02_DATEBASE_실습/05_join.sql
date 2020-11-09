-- join�ǽ� �غ�
CREATE TABLE BASKET_A (ID INT PRIMARY KEY, FRUIT VARCHAR (100) NOT NULL);
CREATE TABLE BASKET_B (ID INT PRIMARY KEY, FRUIT VARCHAR (100) NOT NULL);

-- data ���� �� ���� => commit or rollback; (Ʈ����� ó��)
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


-- 1:M�� ����
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

-- �� 1: ���� m : ����1
SELECT 
	A.customer_ID, A.FIRST_NAME,
	A.LAST_NAME, A.EMAIL,
	B.AMOUNT, B.PAYMENT_DATE,
	C.FIRST_NAME AS S_FIRST_NAME,
	C.LAST_NAME AS S_LAST_NAME
FROM CUSTOMER A
INNER JOIN PAYMENT B ON A.CUSTOMER_ID = B.CUSTOMER_ID 
INNER JOIN STAFF C ON B.STAFF_ID = C.STAFF_ID;



-- outer����(left) : ������ ������ �� �����ְ�, ������ ������ ��ġ�� ���� ������
-- ��: �������� => �������ϴ� => ���� ���� ����� �� => ���� �� ��������� => ����ߴ� ���ߴ� ���� ���� �ʹ�. => �� �� ����� �����ָ� ����.
-- A�� �� ������, B�� ��ġ�ϴ� �� �� ����
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
-- A�� ��� ���� ��, B�� ��ġ ���� ���� ��츸 ���
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
--  B�� �� ������, A�� ��ġ�ϴ� �� �� ����
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
-- B�� ��� ���� ��, A�� ��ġ ���� ���� ��츸 ���
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
-- �ǽ�ȯ��
-- manager ��, ��ǥ�̻絵 ��� ����
-- table ������ ��, manager�� ��� employee id�� �����Ѵٰ� ������ ��.
-- ������ ���̺�������, ������ �ٸ� �������� �����س��� selfjoin => �״��� �� �ȿ��� ���ϴ� ���� ����
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
-- self join: ���̺��� �ϳ����� �ϳ��ȿ����� ���谡 �ִ�.
-- self join example01: ����� �޴��� ������ null�����ϰ� ������ �� ����. (inner join)
SELECT 
	E.first_name || ' ' || E.last_name AS EMPLOYEE,
	M.first_name || ' ' || M.last_name AS MANAGER
FROM EMPLOYEE E
INNER JOIN EMPLOYEE M
ON M.employee_id = E.manager_id
ORDER BY MANAGER;

-- self join example02: ����� �޴��� ������ null�����ؼ� ��� ��� ���� (outer join)
SELECT
	E.first_name || ' ' || E.last_name AS employee,
	M.first_name || ' ' || M.last_name AS manager
FROM employee E
LEFT OUTER JOIN employee M
ON M.employee_id = E.manager_id
ORDER BY manager;
-- self join example03: ����������
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
	
-- �߰� �ǽ� �غ�
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
-- left�� null�� ��
SELECT E.employee_name , D.department_name 
FROM employees E
FULL OUTER JOIN departments D
ON E.department_id = D.department_id 
WHERE E.employee_name IS NULL;

-- �� ������ right outer + right only�� �����ϴ�. 
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
-- ���������� �� ������ left outer join + left only�� ǥ�� ����
SELECT E.employee_name , D.department_name 
FROM employees E
LEFT OUTER JOIN departments D
ON E.department_id = D.department_id 
WHERE D.department_name IS NULL;




-- CROSS JOIN: �ΰ��� ���̺��� catesian product ���� ��� ��� (������ ������ ���� ����)
-- �ǽ� �غ�
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

-- example01 cross join (on�� ����),  �߷°����� ��� ����� ���� �̴´�.
SELECT
	*
FROM CROSS_T1
CROSS JOIN CROSS_T2
ORDER BY LABEL;

-- ������ ���� ��� inner join ���
SELECT * 
FROM cross_t1, cross_t2
ORDER BY LABEL ;
-- �� 2 sql�� ��� ���� ������ => ���� sql���̶�� �Ѵ�.
-- sql���� ������ ������ ����ϴ� �� => ������ ���ٸ�, sql�� ��ü�� �ٸ����� ������ sql���̶�� �Ѵ�.

SELECT 
	CASE WHEN LABEL ='A' THEN sum(score)
		 WHEN LABEL ='B' THEN sum(score) * -1
		 ELSE 0
		 END AS calc
FROM cross_t1
CROSS JOIN cross_t2
GROUP BY LABEL 
ORDER BY LABEL ;

-- nutural ����: �ǹ��� ���� �������� ������, inner join�� �� ��� �����غ� �� �ִ�.
-- �ǽ� �غ�
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

-- natural join: A, B ���̺� �����ϰ� ������ �ִ� �÷��� �������� inner join�Ѵ�.
-- inner join �� ���ٸ� sql�ۼ��������, join �÷��� ������� �ʾƵ� �����ϰ� �۵��Ѵ�.
-- �ڵ����� �����������, �������� ������ �� �ִ�. (�ƹ��� 9999�� ���ص� 1�� �߸��Ǹ� �������� 100���θ� ������� ���Ѵ�.)
SELECT * 
FROM products A
NATURAL JOIN categories B;
-- ���� ���� ���
SELECT A.category_id, A.product_id, A.product_name, B.category_name
FROM products A, categories B
WHERE A.category_id = B.category_id;
-- ���� ���� ���
SELECT A.category_id, A.product_id, A.product_name, B.category_name
FROM products A
INNER JOIN categories B
ON A.category_id = B.category_id;

-- natural join �ٸ� �� (�ȵǴ� ��� ������)
-- city table �� country table�� ������ �̸����� �����ϴ� column�� country_id, last_update�� �ִ�.
-- ���� �� �÷��� inner join�� �����ؾ����� ������� ���´�. => ��� �Ǽ��� ���� ���´�. 
-- �ڵ����� join�ؼ�, ����� �ǵ�ġ ���� �������� ���� �� �ֱ� ������ inner join���� join �÷��� ����ؼ� �ǵ��� ��� ������ ����� �� �� �ִ�.

-- natural join ���
SELECT * FROM city A NATURAL JOIN country B;
-- inner join ���
SELECT * FROM city A INNER JOIN country B ON (A.country_id= B.country_id);
