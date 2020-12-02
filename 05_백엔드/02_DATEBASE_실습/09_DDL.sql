-- ������ Ÿ�� �� ��������
-- 01. boolean
-- TRUE ('t', 'true', 'y', 'yes', '1')
-- FALSE ('f', 'false', 'n', 'no', '0')



-- �ǽ��غ�
CREATE TABLE STOCK_AVAILABILITY (
	PRODUCT_ID INT NOT NULL PRIMARY KEY,
	AVAILABLE BOOLEAN NOT NULL
);

-- ���� ���� �پ��ϰ� ǥ�� ���� (�� 5����)
INSERT INTO STOCK_AVAILABILITY (PRODUCT_ID, AVAILABLE) VALUES
	(100, TRUE),
	(200, FALSE),
	(300, 't'),
	(400, '1'),
	(500, 'y'),
	(600, 'yes'),
	(700, 'no'),
	(800, '0')
	
-- ��½ÿ��� TRUE / FALSE �θ� ǥ����
SELECT * FROM stock_availability;

-- �� �� ��� ����
SELECT * FROM stock_availability WHERE available;
SELECT * FROM stock_availability WHERE available ='YES';
SELECT * FROM stock_availability WHERE available ='1';

-- ������ ��� ����
SELECT * FROM stock_availability WHERE available ='NO';
SELECT * FROM stock_availability WHERE available ='0';










-- char, varchar, textŸ��
-- char(): ������ ����, ���� ���� ��� �������� �е�
-- varchar(): ������ ����, ���� ������ ���� �е� X
-- text: ���Ѵ� ���� ����
-- varchar: text�� ����
CREATE TABLE CHARACTER_TESTS(
	ID SERIAL PRIMARY KEY,
	X CHAR(3),
	Y VARCHAR(10), 
	Z TEXT
);

INSERT INTO CHARACTER_TESTS VALUES (1, 'Y', 'YES', 'YESYESYESASDFASDF');
SELECT * FROM CHARACTER_TESTS;

-- ���� ������ ������ �����ϰ� ���Ѵ�.(POSTGRESQL������!)
INSERT INTO CHARACTER_TESTS VALUES (2, 'Y', 'Y', 'ASDFASDF');
SELECT * FROM CHARACTER_TESTS WHERE X = Y;

















-- NUMERIC
-- ���� ~ �Ǽ������� ���� ǥ��
CREATE TABLE PRODUCTS(
	ID SERIAL PRIMARY KEY
	, NAME VARCHAR NOT NULL
	, PRICE NUMERIC(5,2)
);

-- �Ʒ��� ���� �Է��ϸ鼭 �Ҽ��� 3��° �ڸ� data�� ���ư� �� ����
INSERT INTO PRODUCTS(NAME, PRICE) VALUES
	('Phone', 500.215),
	('Tablet', 500.214);

SELECT * FROM products;

CREATE TABLE PRODUCTS_2(
	ID SERIAL PRIMARY KEY
	, NAME VARCHAR NOT NULL
	, PRICE NUMERIC(6,3)
);

DROP TABLE products_2;

INSERT INTO PRODUCTS_2(NAME, PRICE) VALUES
	('Phone', 500.215),
	('Tablet', 500.214);

SELECT * FROM products_2;











-- Integer
-- smallint, integer, bigint�� ������ ������ ����� ���� ��밡���� �ִ밪�� �ٸ�
-- å�� �������� ����� 32,767�� ���� �ʴ´ٰ� ���� ��, smallint�� �����ϴ°� ������ �뷮 ȿ���� ����
-- ��
CREATE TABLE books(
	book_id serial PRIMARY KEY
	, title varchar(255) NOT NULL
	, pages SMALLINT NOT NULL check(pages > 0)
);

-- integer: �����α����� ���� 2,147,483,647���� ���� �ʴ´ٰ� ���� ��, integer�� �����ϴ°� ������ ���� ȿ��
CREATE TABLE cities(
	city_id serial PRIMARY KEY
	, city_name varchar(255) NOT NULL
	, population int NOT NULL check( population >= 0)
);


DROP TABLE books;








--serial: integer�������� ������ sequential�� �����͸� ���Ѵ�. ���ϼ��� �����ϴ� pk�� ���� ���ȴ�.

-- serial data Ÿ���� ���
CREATE TABLE table_name(
	id serial
);

INSERT INTO table_name values(default);


-- �������� �̿��� �÷� ����
DROP SEQUENCE table_name_id_seq;
CREATE SEQUENCE table_name_id_seq;

CREATE TABLE table_name(
	id integer NOT NULL DEFAULT nextval('table_name_id_seq')
);

ALTER SEQUENCE table_name_id_seq OWNED BY table_name.id;
INSERT INTO table_name values(default);

SELECT * FROM table_name;






-- serial �ǽ�1
CREATE TABLE fruits(
	id serial PRIMARY KEY
	, name varchar NOT null
)

INSERT INTO fruits(name) values('orange');
INSERT INTO fruits(id, name) values(DEFAULT, 'apple');

SELECT * FROM fruits;

-- ���� ������ ���� �˰������.(postgresql���� ����)
SELECT currval (pg_get_serial_sequence('fruits', 'id'));









 -- date(����), time(�ð�), timestamp(����, �ð�)
 -- ���� �� �ð��� �����ϴ� �ֿ� ������ Ÿ��
 SELECT now()::date;
SELECT current_date;
SELECT to_char(now()::date, 'dd/mm/yyyy');
SELECT to_char(now()::date, 'Mon dd,yyyy');

SELECT first_name, last_name, create_date, now() - create_date AS diff FROM customer;
SELECT first_name, last_name, age(create_date) AS diff FROM customer;


-- Ư�� ����, ��, ���� ����
SELECT 
	first_name, 
	last_name, 
	extract(YEAR FROM create_date) AS YEAR,
	extract(MONTH FROM create_date) AS MONTH,
	EXTRACT(DAY FROM create_date) AS DAY
	FROM 
		customer;

-- 
SELECT current_time;
SELECT LOCALTIME;

SELECT 
	LOCALTIME, 
	EXTRACT (HOUR FROM localtime) AS hour,
	EXTRACT (minute FROM localtime) AS minute,
	EXTRACT (second FROM localtime) AS second,
	EXTRACT (milliseconds FROM localtime) AS milliseconds;
	


-- time�� Ȱ���Ͽ� �ð����
SELECT time '10:00' - time '02:00' AS diff;
SELECT time '10:59' - time '02:01' AS diff;
SELECT time '10:59:59' - time '02:01:01' AS diff;
SELECT 
	LOCALTIME
	, LOCALTIME + INTERVAL '2 hours' AS plus_2_hours
	, LOCALTIME - INTERVAL '2 hours' AS minus_2_hours;
	


-- timestamp
SELECT now();
SELECT current_timestamp;
SELECT timeofday();

SELECT
	to_char(current_timestamp, 'yyyy')
	, to_char(current_timestamp, 'yyyy-mm')
	, to_char(current_timestamp, 'yyyy-mm-dd')
	, to_char(current_timestamp, 'yyyy-mm-dd hh24')
	, to_char(current_timestamp, 'yyyy-mm-dd hh24:mi')
	, to_char(current_timestamp, 'yyyy-mm-dd hh24:mi:ss')
	, to_char(current_timestamp, 'yyyy-mm-dd hh24:mi:ss.ms')
	, to_char(current_timestamp, 'yyyy-mm-dd hh24:mi:ss.us')
;


-- �⺻Ű: ���̺� ������ ������ ���̾�� �ϰ�, not null�̾�� �Ѵ�.
-- �� ���̺� ������ �ݵ�� �����ؾ��ϴ� ��ü ���Ἲ�� ���� �����̴�.
CREATE TABLE tb_product_pk_test(
	product_no integer
	, description TEXT
	, product_cost numeric
);
ALTER TABLE tb_product_pk_test ADD PRIMARY KEY (product_no);


-- auto increment
CREATE TABLE tb_product_pk_test2(
	name varchar(255)
);
INSERT INTO tb_product_pk_test2 values('microsoft'), ('ibm'), ('apple'), ('samsung');

SELECT * FROM tb_product_pk_test2;
ALTER TABLE tb_product_pk_test2 ADD COLUMN id serial PRIMARY KEY;
SELECT * FROM tb_product_pk_test2;
INSERT INTO tb_product_pk_test2 VALUES ('lg');

ALTER TABLE tb_product_pk_test DROP CONSTRAINT tb_product_pk_test_pkey;
ALTER TABLE tb_product_pk_test2 DROP CONSTRAINT tb_product_pk_test2_pkey;









-- �ܷ�Ű

CREATE TABLE so_headers(
	id serial PRIMARY KEY,
	customer_id integer,
	ship_to varchar(255)
);

CREATE TABLE so_items(
	item_id integer NOT NULL
	,so_id integer
	, product_id integer
	, qty integer
	, net_price integer
	, PRIMARY key(item_id, so_id)
);
-- �ܷ�Ű �߰�
ALTER TABLE so_items ADD CONSTRAINT fk_so_headers_id FOREIGN KEY (so_id) REFERENCES so_headers(id);

INSERT INTO so_headers(customer_id, ship_to) VALUES
	(10, '4000 North First Street, CA 95134, USA')
	,(20, '1900 North First Street, CA 95134, USA')
	,(10, '4000 North First Street, CA 95134, USA');

INSERT INTO so_items (item_id, so_id, product_id, qty, net_price) 
VALUES
	(1, 1, 1001, 2, 1000)
	, (2, 1, 1000, 3, 1500)
	, (3, 2, 1000, 4, 1500)
	, (1, 2, 1001, 5, 1000)
	, (2, 3, 1002, 2, 1700)
	, (3, 3, 1003, 1, 2000)
;

SELECT * FROM so_items;
SELECT * FROM so_headers;

SELECT si.item_id, si.so_id, si.product_id, si.qty, si.net_price, sh.customer_id, sh.ship_to
FROM so_items si, so_headers sh
WHERE si.so_id = sh.id;

-- �ܷ�Ű ����
ALTER TABLE so_items DROP CONSTRAINT fk_so_headers_id;

DROP TABLE so_items;

-- ���̺� ������ ���ÿ� �ܷ�Ű ����
CREATE TABLE so_items(
	item_id integer NOT NULL
	, so_id integer REFERENCES so_headers(id)
	, product_id integer
	, qty integer
	, net_price NUMERIC
	, PRIMARY KEY (item_id, so_id)
)


-- ���� �ܷ�Ű ����
CREATE TABLE child_table(
	c1 integer PRIMARY KEY,
	c2 integer,
	c3 integer,
	FOREIGN KEY (c2, c3) REFERENCES parent_tables(p1, p2)
)
-- c2 + c3 �� p1, p2�� �����ؾ��Ѵ�.










-- üũ��������: Ư�� �÷��� ���� ���� ���� ������ ���ϴ� ��. (���������� ���� �� �� ���� ���� �����ܿ��� ���� ���°�)

-- ������ �ݵ�� 1900�� 1�� 1�� ����
-- �Ի����ڴ� ���Ϻ��� �ݵ�� Ŀ���Ѵ�
-- ������ 0���� �ݵ�� Ŀ���Ѵ�.

CREATE TABLE tb_emp_check_test(
	id serial PRIMARY KEY
	, first_name varchar(50)
	, last_name varchar(50)
	, birth_date date CHECK (birth_date > '1900-01-01')
	, joined_date date CHECK (joined_date > birth_date)
	, salary NUMERIC check(salary > 0)
);

INSERT INTO tb_emp_check_test (first_name, last_name, birth_date, joined_date, salary) VALUES
(
	'Minhee'
	,'Kang'
	, '1972-01-01'
	, '2015-07-01'
	, -100000
	)
	
ALTER TABLE tb_emp_check_test ADD CONSTRAINT salary_range_check check(salary > 0 AND salary <= 10000000000);
ALTER TABLE tb_emp_check_test ADD CONSTRAINT name_check check(length(first_name) > 0 AND length(last_name) > 0 );









-- unique ���� ����
-- Ư�� �÷��� ���� �� ���̺� ������ ������ ������ �����ϴ� ��
CREATE TABLE person(
	id serial PRIMARY KEY
	, first_name varchar(50)
	, last_name varchar(50)
	, email varchar(50)
	, UNIQUE (email)
);

INSERT INTO person(first_name, last_name, email) VALUES (
	'John',
	'Doe',
	'j.doe@postgresqltutorial.com'
);

CREATE TABLE person_unique_index_test(
	id serial PRIMARY KEY
	, first_name varchar(50)
	, last_name varchar(50)
	, email varchar(50)
);

-- ��뷮 �����Ϳ��� ������ ������ ã�� �� indexȰ��
CREATE UNIQUE INDEX ix_person_unique_index_test_01 ON person_unique_index_test(email);














-- not null��������: Ư�� �÷��� �� ���� ���� �����ϴ� ����

CREATE TABLE invoice(
	id serial PRIMARY KEY
	, product_id int NOT NULL
	, qty NUMERIC NOT NULL check(qty>0)
	, net_price NUMERIC CHECK (net_price > 0)
);

INSERT INTO invoice (product_id, qty, net_price) VALUES (NULL, 1, 1);

CREATE TABLE invoice_update_test(
	id serial PRIMARY KEY
	, product_id int NOT NULL
	, qty NUMERIC NOT NULL check(qty>0)
	, net_price NUMERIC CHECK (net_price > 0)
);

INSERT INTO invoice_update_test (product_id, qty, net_price) values(1,1,1);

-- error: product_id ���������� not null�̱� ������ �ȵȴ�.
UPDATE invoice_update_test
SET product_id = NULL
WHERE product_id =1;









