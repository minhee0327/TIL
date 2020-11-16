-- ���� �����ڿ� ��������
-- 01 union����
-- �ΰ� �̻��� select������ ��� ������ ���� ��� �������� �����ϸ� ���� �� �ߺ��� �����ʹ� ���ŵȴ�.
-- �ΰ��� select������ �ߺ��Ǵ� ������ ���� �ִٸ� �ߺ��� ���ŵȴ�.

-- �ǽ��غ�
CREATE TABLE SALES2007_1(NAME VARCHAR(50), AMOUNT NUMERIC(15, 2));
CREATE TABLE SALES2007_2(NAME VARCHAR(50), AMOUNT NUMERIC(15, 2));

INSERT INTO SALES2007_1 VALUES ('Mike', 150000.25), ('Jon', 132000.75), ('Mary', 100000);
INSERT INTO SALES2007_2 VALUES ('Mike', 120000.25), ('Jon', 142000.75), ('Mary', 100000);

COMMIT;
SELECT * FROM SALES2007_1;
SELECT * FROM SALES2007_2;

-- �� ���̺� ��ü ���� ��ģ ��, �ߺ�����
SELECT * FROM SALES2007_1 
UNION
SELECT * FROM SALES2007_2;
-- amount�÷��� ��ģ��, �ߺ�����
SELECT amount FROM SALES2007_1 
UNION
SELECT amount FROM SALES2007_2;
-- ��ģ �� �����Ҷ�
SELECT * FROM SALES2007_1 
UNION
SELECT * FROM SALES2007_2
ORDER BY amount desc;


-- union all����
-- �ΰ� �̻��� select������ ��� ������ ���� ��� �������� �����ϸ� ���ս� �ߺ��� �����͵� ��� ����Ѵ�.
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


-- intersect ����
-- �ΰ��̻��� select ������ ��� ������ �ϳ��� ��� �������� �����Ѵ�.
-- ���� a�� ���� b�� ������
-- �ǽ��غ�
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

-- INTERSECT: inner join�� ����� �����Ͽ� ���� ���Ǵ� �����.. X
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



-- except������: �� ���� select���� ��� ���տ��� �� �Ʒ��� �ִ� select ���� ��� ������ ������ ��� ����
-- �Ʒ� ����: ��� O ����
-- �ʸ��� �κ��丮 1:m���� => �� ���̺� ���� => ��ȭ �ϳ��� �������� ���
SELECT 
	DISTINCT A.film_id
	,B.title 
	FROM inventory A
INNER JOIN 
	film B
ON A.film_id = B.film_id
ORDER BY B.title;
-- ��� ���� ����: ��ü - ��� �ִ� ����
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
