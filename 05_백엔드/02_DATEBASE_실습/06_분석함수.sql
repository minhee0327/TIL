-- �м��Լ���: Ư�� ���� ������ ��� �Ǽ��� ��ȭ ���� �ش� ���� �ȿ��� �հ� �� ī��Ʈ ���� ����� �� �ִ� �Լ��̴�.
-- �ǽ��غ�
CREATE TABLE PRODUCT_GROUP (
	GROUP_ID SERIAL PRIMARY KEY,
	GROUP_NAME VARCHAR(255) NOT NULL
);
-- decimal: �Ҽ�
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

-- �����Լ��� ������ ������� �����ش�.
SELECT count(*)
FROM product;
-- �м��Լ��� ������ ��� �� ������ �Բ� ����Ѵ�.
SELECT count(*) over(), A.*
FROM product A;





-- �м��Լ� avg
-- �м��Լ� ���� ����
-- ����ϰ��� �ϴ� �м��Լ��� ����, ��� �÷��� ������ partition by���� ���� ���ϴ� �����÷��� ����, order by���� �����÷��� ����
-- ����
SELECT c1,�м��Լ�(c2, c3, ...), OVER (PARTITION BY c4 ORDER BY c5)
FROM TABLE_NAE;
-- ����avg�Լ�: ������ ������� ����Ѵ�.
SELECT avg(price) FROM product;
-- ���� avg + group by
SELECT B.group_name, avg(price)
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id)
GROUP BY B.group_name;
-- �м� avg�Լ�: �����ٰ� �� �����ָ鼭, ��� ���ݵ� ���������!
-- �м��Լ��� ����Ͽ� ��� ������ �״�� ����ϸ鼭, group_name������ ��� ���
-- group_name�� �������� price�� ��հ� ���
SELECT A.product_name, A.price, B.group_name, AVG(A.price) OVER (PARTITION BY B.group_name)
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);
-- 
SELECT A.product_name, A.price, B.group_name, AVG(A.price) OVER (PARTITION BY B.group_name ORDER BY B.group_name)
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);
-- ���� ����� ���� �� �ִ�. 
SELECT A.product_name, A.price, B.group_name, AVG(A.price) OVER (PARTITION BY B.group_name ORDER BY A.price)
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);
-- 




-- row_number Ư�� ���� ������ ��� �Ǽ��� ��ȭ ���� �ش� ���վȿ��� Ư�� �÷��� ������ ���ϴ� �Լ��̴�.
-- ���� ������ �־, ������ ���������� ���� �ű��. (1,2,3,4,...)
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
-- rank: ���� ������ ���� �����鼭 ���� ���� �ǳʶ� (1,1,3,4...)
SELECT 
	A.product_name, 
	B.group_name, 
	A.price, 
	RANK () OVER 
		(PARTITION BY B.group_name ORDER BY A.Price desc)
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);
-- dense_rank: ���� ������ ���� �����鼭 ���� ���� �ǳʶ��� ���� (1,1,2,3,...)
SELECT 
	A.product_name,
	B.group_name,
	A.price,
	DENSE_RANK () OVER (PARTITION BY B.group_name ORDER BY A.price)	
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);






-- first_value, last_value
-- Ư�� ���� ������ ��� �Ǽ��� ��ȭ ����, �ش� ���վȿ��� Ư���÷��� ù��° �� Ȥ�� ������ ���� ���ϴ� �Լ�
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
-- ���� �������� ������ price �� ���, group_name�÷� ���� price�÷� ������, ��Ƽ���� ù��° row~ ������ row����
-- last value�� range�� �߰��ϴ� ������, default value�� ragne between unbounded preceding and current row�̱� ����.
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


-- LAG: ���� ���� ���� ã�´�. LAG(���� �� ã�� ��, ���° ������)
SELECT
	A.product_name,
	B.group_name,
	A.price,
	LAG(A.price, 1) OVER(PARTITION BY B.group_name ORDER BY A.price) AS prev_price,
	A.price - LAG(A.price, 1) OVER (PARTITION BY B.group_name ORDER BY A.price) AS cur_prev_diff
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);

-- LEAD: �������� ���� ã�´�.
SELECT
	A.product_name,
	B.group_name,
	A.price,
	LEAD(A.price, 1) OVER(PARTITION BY B.group_name ORDER BY A.price) AS prev_price,
	A.price - LEAD(A.price, 1) OVER (PARTITION BY B.group_name ORDER BY A.price) AS cur_prev_diff
FROM product A
INNER JOIN product_group B
	ON (A.group_id = B.group_id);


