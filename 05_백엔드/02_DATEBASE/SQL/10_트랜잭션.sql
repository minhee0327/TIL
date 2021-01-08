-- ���� ������
-- with��, Ʈ������

-- 01. case
-- if/else���� ���� ������ ������ �� �ִ�. 

-- case ǥ���� ����
SELECT 
	CASE WHEN ���ǽ�1 THEN ���1
	CASE WHEN ���ǽ�2 THEN ���2
		 ELSE ���3
 	END
 	
 	
-- ��
SELECT * FROM film;
-- ���� 1���� �������鼭 �÷� 3���� ���
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

-- ���� ���� ������� �ٸ� ǥ����� (�� => �� �� ��ȯ)
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




-- ���� 3���� ���
SELECT rental_rate, count(*) cnt
FROM film
GROUP BY rental_rate;











-- coalesce: �Է��� ���ڰ� �� null���� �ƴ� ù��° �� ��ȯ
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
-- ���꿡 null�� ���ԵǸ�, null�� �����Ե�. price- discount�� ���� �� ���ΰ��� null�� ��쿡�� �׳� price�� ����ϰ����! �̷���Ȳ���� ���
SELECT product , (price - discount) AS net_price FROM tb_item_coalesce_test;
-- coalesce�� Ȱ���Ͽ� null�� ��� �ι�° ���ڸ� ��ȯ�ϰ�, null�� �ƴ� ��� ù��° ���� �������ش�.
SELECT product,price, discount, COALESCE(discount, 0), (price - COALESCE (discount, 0)) AS net_price
FROM tb_item_coalesce_test;


-- case�� Ȱ���Ͽ� ���� ���� ǥ���غ���
SELECT product,(price - 
	CASE WHEN discount IS NULL THEN 0
	ELSE discount
	END ) AS net_price 
FROM tb_item_coalesce_test;










-- null if 
-- �Է��� �ΰ��� ������ ���� �����ϸ� null�����ϰ� �׷��� ������ ù��° ���� �����Ѵ�.
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


-- ���� ��� ���� ���� ���غ��� (��2/��1 * 100)
SELECT sum(CASE WHEN gender = 1 THEN 1 ELSE 0 end) / sum(CASE WHEN gender = 2 THEN 1 ELSE 0 end) * 100 AS "MALE/FEMALE RATIO"
FROM tb_member_nullif_test ;

-- 0���� ������ ��� error�� ���´�.
-- test ���� �Ѹ� �ִ� ���ڸ� ���ڷ� ����
UPDATE tb_member_nullif_test SET gender = 1 WHERE gender = 2;
SELECT * FROM tb_member_nullif_test;
-- error�߻� (���ڰ� 0���̹Ƿ�) 0���� ���� �� ���ٴ� error�� ����.
SELECT sum(CASE WHEN gender = 1 THEN 1 ELSE 0 end) / sum(CASE WHEN gender = 2 THEN 1 ELSE 0 end) * 100 AS "MALE/FEMALE RATIO"
FROM tb_member_nullif_test ;
-- ������ �հ谡 0�̸� null�� �����ϵ��� �Ѵ�. (����3 /null => null)
SELECT sum(CASE WHEN gender = 1 THEN 1 ELSE 0 end) / NULLIF(sum(CASE WHEN gender = 2 THEN 1 ELSE 0 end),0) * 100 AS "MALE/FEMALE RATIO"
FROM tb_member_nullif_test ;







-- cast: Ư�� ������ Ÿ������ ����ȯ�ϴ� ��.
-- ���� ������ ���� cast ǥ������ Ȱ���Ͽ� ������ ����ȯ�Ѵ�.
-- ���� => integer(������)
SELECT cast('100' AS integer);
SELECT '100'::integer;
-- ���� => dateŸ������
SELECT cast('2020-11-26' AS date);
SELECT '2020-11-26'::date;
-- ���ڿ��� �Ǽ�������
SELECT cast('10.2' AS double precision);
SELECT '10.2'::double PRECISION;








-- with���� Ȱ��
-- length���� short, medium, long���� ����
SELECT film_id, title,
	(CASE
		WHEN length < 30 THEN 'short'
		WHEN length >=30 AND length <90 THEN 'medium'
		WHEN length >=90 THEN 'long'
		END 
	)length 
FROM film;


-- with���� Ȱ���Ͽ� �ش� ������ tmp1�� �����ϰ� select������ tmp1�� ��ȸ�غ� �� �ִ�.
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












-- �������
-- with���� �̿��Ͽ� ��������� �ۼ��� �� �ִ�. ������ �� ���� �θ��ڽİ��� ���踦 ǥ���ϴ� sql�̴�.

CREATE TABLE tb_emp_recursive_test(
	employee_id serial PRIMARY KEY
	, full_name varchar NOT NULL
	, manager_id int
);

INSERT INTO tb_emp_recursive_test (employee_id, full_name, manager_id)
VALUES
	(1, '�̰��', null),
	(2, '������', 1),
	(3, '��¹�', 1),
	(4, '�ϼ���', 1),
	(5, '�۹鼱', 1),
	(6, '�̽���', 2),
	(7, 'ȫ�߼�', 2),
	(8, '��̼�', 2),
	(9, '�輱��', 2),
	(10, '�̼���', 3),
	(11, '�輱��', 3),
	(12, '�輱��', 3),
	(13, '�̿���', 3),
	(14, '����', 4),
	(15, '�̽ÿ�', 4),
	(16, '�ּ���', 7),
	(17, '������', 7),
	(18, '�ֹ���', 8),
	(19, '������', 8),
	(20, '�밡��', 8);
	
SELECT * FROM tb_emp_recursive_test;


-- �ְ� �����ں��� ~ ���������� depth
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











-- Ʈ������
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