CREATE TABLE data_type_test_1
(
	A_BOOLEAN BOOLEAN
	, B_CHAR CHAR(10)
	, C_VARCHAR VARCHAR(10)
	, D_TEXT TEXT
	, E_INT INT
	, F_SMALLINT SMALLINT
	, G_FLOAT FLOAT
	, H_NUMERIC NUMERIC(15, 2)
);

INSERT INTO DATA_TYPE_TEST_1 VALUES (TRUE, 'ABCDE', 'ABCDE', 'TEXT', 1000, 10, 10.12345, 10.25);

SELECT * FROM DATA_TYPE_TEST_1;
SELECT * FROM DATA_TYPE_TEST_2;


CREATE TABLE data_type_test_2
(
	A_DATE DATE
	, B_TIME TIME
	, C_TIMESTAMP TIMESTAMP
	, D_ARRAY TEXT[]
	, E_JSON JSON
);

INSERT INTO DATA_TYPE_TEST_2 VALUES 
	(CURRENT_DATE, 
	LOCALTIME, 
	CURRENT_TIMESTAMP, 
	ARRAY['010-1234-1234', '010-9992-8888'], 
	'{"customer":"John Doe", "items":{"product":"Beer", "qty": 6}}'
	);
	
SELECT * FROM data_type_test_2;




-- ���̺� ���� �ǽ�
CREATE TABLE ACCOUNT (
	USER_ID SERIAL PRIMARY KEY
	, USERNAME VARCHAR(50) UNIQUE NOT NULL
	, PASSWORD VARCHAR(50) NOT NULL
	, EMAIL VARCHAR(355) UNIQUE NOT NULL
	, CREATED_ON TIMESTAMP NOT NULL
	, LAST_LOGIN TIMESTAMP
);

CREATE TABLE ROLE(
	ROLE_ID SERIAL PRIMARY KEY
	, ROLE_NAME VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE ACCOUNT_ROLE(
	USER_ID INTEGER NOT NULL
	, ROLE_ID INTEGER NOT NULL
	, GRANT_DATE TIMESTAMP WITHOUT TIME ZONE
	, PRIMARY KEY (USER_ID, ROLE_ID)
	, CONSTRAINT ACCOUNT_ROLE_ROLE_ID_FKEY FOREIGN KEY (ROLE_ID)   	-- ROLE_ID �÷��� ROLL ���̺��� ROLE_ID�÷��� ����
	REFERENCES ROLE(ROLE_ID) MATCH SIMPLE							-- ROLE_ID�÷��� ROLE���̺��� ROLE_ID�÷��� ���� ���� Ȥ�� ����� �ƹ��͵� ���� �ʴ´�.
	ON UPDATE NO ACTION ON DELETE NO ACTION
	, CONSTRAINT ACCOUNT_ROLE_USER_ID_FKEY FOREIGN KEY (USER_ID)
	REFERENCES ACCOUNT(USER_ID) MATCH SIMPLE
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

INSERT INTO account VALUES (1, '������', '1234', 'mini@naver.com', current_timestamp, null);
SELECT * FROM account;

INSERT INTO ROLE values(1, 'DBA');
SELECT * FROM ROLE;

INSERT INTO account_role values(1, 1, current_timestamp);
SELECT * FROM account_role;


-- error ����1 (���� ���Ἲ �������� ����)
INSERT INTO account_role values(2, 1 , current_timestamp);	-- user_id�� 2�� ���µ� ������ �ؼ� ���� error; �����ϴ� ���̺��� pk�� null�̰ų� �������� ���� �� ���¿���

-- error ����2 
INSERT INTO account_role VALUES (1, 2, current_timestamp); 	-- role_id�� 2�� ���µ� ������ �ؼ� ���� error;

-- error ����3
INSERT INTO account_role values(1, 1, current_timestamp); 	-- �ߺ��� Ű ���� �� �� ����. (primary key�ϱ�), ��ü���Ἲ pk�� �׻� �����ϸ� not null�����ؾ���.

-- error ���� 4
UPDATE account SET user_id = 2 WHERE user_id =1; 			-- account table�� user_id�� account_role���� �����ϴ� ��Ȳ�ε�, �����ع����� �ȵȴ�.




-- ���̺� ����
-- 03. CTAS: Create table as select 

select * FROM category WHERE category_id = 1;

-- ���� ���ϴ� ������ ����
SELECT a.film_id, a.title, a.release_year, a.length, a.rating
FROM film a, film_category b
WHERE a.film_id = b.film_id AND b.category_id = 1;

-- �ش� ����������� ���̺� action_film�� ����
CREATE TABLE action_film AS
SELECT a.film_id, a.title, a.release_year, a.length, a.rating
FROM film a, film_category b
WHERE a.film_id = b.film_id AND b.category_id = 1;

SELECT * FROM action_film;

-- not exists (�������� ������쿡�� ����, ������ ��� ���� �۾� ���� ����.(error����))
CREATE TABLE IF NOT EXISTS action_film AS
SELECT a.film_id, a.title, a.release_year, a.length, a.rating
FROM film a, film_category b
WHERE a.film_id = b.film_id AND b.category_id = 1;
-- 










-- ���̺� ���� ����ǽ�
-- �ѹ� ������� ���̺��̴���, ���̺� ������ ������ �� �ִ�. (���� ��ȭ�� �����ϰ� ��ó)
DROP TABLE LINKS;
CREATE TABLE LINKS (
	LINK_ID SERIAL PRIMARY KEY
	, TITLE VARCHAR(512) NOT NULL
	, URL VARCHAR(1024) NOT NULL UNIQUE
);

ALTER TABLE LINKS ADD COLUMN ACTIVE BOOLEAN;				-- ACTIVE COLUMN �߰�
ALTER TABLE LINKS DROP COLUMN ACTIVE;						-- ACTIVE COLUMN ����
ALTER TABLE LINKS RENAME COLUMN TITLE TO LINK_TITLE; 		-- TITLE COLUMN���� LINK_TITLE�� ����
ALTER TABLE LINKS ADD COLUMN TARGET VARCHAR(10);			-- TARGET COLUMN �߰�
ALTER TABLE LINKS ALTER COLUMN TARGET SET DEFAULT '_BLANK';	-- TARGET �÷��� DEFAULT�� "_BLANK"�� ���� 


SELECT * FROM LINKS;

INSERT INTO LINKS (LINK_TITLE, URL) VALUES ('PostgreSQL', 'http://www.postgresqltutorial.com/');

ALTER TABLE LINKS ADD CHECK (TARGET IN('_BLANK', '_SELF', '_PARENT', '_TOP'));	-- TARGET COLUMN�� ���� üũ �������� �߰�

-- ERROR: TARGET CHECK ������������ 4���� ������ �����.
INSERT INTO LINKS (LINK_TITLE, URL, TARGET) VALUES ('PostgreSQL', 'http://www.postgresqltutorial.net/', '_WHATEVER');

-- _self�� check�������� �ȿ� �����Ƿ� ��밡��.
INSERT INTO LINKS (LINK_TITLE, URL, TARGET) VALUES ('PostgreSQL', 'http://www.postgresqltutorial.org/', '_SELF');







-- ���̺� �̸� ����
CREATE TABLE VENDORS (
	ID SERIAL PRIMARY KEY
	, NAME VARCHAR NOT NULL
);
CREATE TABLE SUPPLIER_GROUPS(
	ID SERIAL PRIMARY KEY
	, NAME VARCHAR NOT NULL
);

ALTER TABLE VENDORS RENAME TO SUPPLIERS;
ALTER TABLE SUPPLIERS ADD COLUMN GROUP_ID INT NOT NULL;
ALTER TABLE SUPPLIERS ADD FOREIGN KEY (GROUP_ID) REFERENCES SUPPLIER_GROUPS(ID);

SELECT * FROM SUPPLIERS;
SELECT * FROM SUPPLIER_GROUPS;

-- �� (��ü�ϴ� �����Ͱ� �ƴ� ���� �뵵)
CREATE VIEW SUPPLIER_DATA AS
SELECT 
	S.ID
	, S.NAME
	, B.NAME "GROUP"
FROM SUPPLIERS S, SUPPLIER_GROUPS B
WHERE S.GROUP_ID = B.ID

SELECT * FROM SUPPLIER_DATA;

-- TABLE���� �ٲٰ� �Ǹ� ������ ���� ���Ἲ ���������̳� �� ���� �ڵ����� ���ŵȴ�.
ALTER TABLE supplier_groups RENAME TO GROUPS;






-- ����
-- �⺻������ ORACLE(�����ϴ� �ְ��� DBMS), Ư���� �˾Ƶδ°� ����.
-- CREATE, DROP, ALTER => ġ�¼��� COMMIT (DDL)
-- DELETTE, UPDATE, MERGE, INSERT => ���� COMMIT���־���Ѵ�.

-- �÷� �߰�
CREATE TABLE TB_CUST(
	CUST_ID SERIAL PRIMARY KEY
	, CUST_NAME VARCHAR(50) NOT NULL
)

ALTER TABLE TB_CUST ADD COLUMN PHONE_NUMBER VARCHAR(13);
ALTER TABLE TB_CUST 
	ADD COLUMN  FAX_NUMBER VARCHAR(13),
	ADD COLUMN EMAIL_ADDR VARCHAR(50);

SELECT * FROM TB_CUST;

INSERT INTO tb_cust VALUES ( 1, '�̴�', '010-2121-1212', '031-212-1231', 'test@naver.com');

-- ���� ���ڵ���� �ְ�, ���ο� �÷��� �߰��ϰ� �Ǹ� ������ �ִ� ���ڵ�鿡 null�� ����� ������ error�߻��Ѵ�.
ALTER TABLE tb_cust ADD COLUMN contact_nm varchar NOT NULL;
-- �� ���, �ذ�å�� null�������� �÷��� �߰��Ѵ�.
ALTER TABLE tb_cust ADD COLUMN contact_nm varchar NULL;
-- contact_nm�÷��� update���ش�.
UPDATE tb_cust SET contact_nm = 'ȫ�浿' WHERE cust_id = 1;
-- alter column���� not null ���������� �ش�.
ALTER TABLE tb_cust ALTER COLUMN contact_nm SET NOT NULL;
--





-- �÷� ����
CREATE TABLE PUBLISHERS (
	PUBLISHER_ID SERIAL PRIMARY KEY
	, NAME VARCHAR NOT NULL
);
DROP TABLE PRODUCTS CASCADE;
DROP TABLE categories;

CREATE TABLE CATEGORIES(
	CATEGORY_ID SERIAL PRIMARY KEY
	, NAME VARCHAR NOT NULL
);

CREATE TABLE BOOKS(
	BOOK_ID SERIAL PRIMARY KEY
	, TITLE VARCHAR NOT NULL
	, ISBN VARCHAR NOT NULL
	, PUBLISHED_DATE DATE NOT NULL
	, DESCRIPTION VARCHAR
	, CATEGORY_ID INT NOT NULL
	, PUBLISHER_ID INT NOT NULL
	, FOREIGN KEY (PUBLISHER_ID) REFERENCES PUBLISHERS (PUBLISHER_ID)
	, FOREIGN KEY (CATEGORY_ID) REFERENCES CATEGORIES (CATEGORY_ID)
);
CREATE VIEW BOOK_INFO AS SELECT
	B.BOOK_ID,
	B.TITLE,
	B.ISBN,
	B.PUBLISHED_DATE,
	P.NAME
FROM 
	BOOKS B
	,PUBLISHERS P
WHERE P.PUBLISHER_ID = B.PUBLISHER_ID
ORDER BY B.TITLE;

SELECT * FROM BOOK_INFO;
SELECT * FROM BOOKS;

ALTER TABLE BOOKS DROP COLUMN CATEGORY_ID;

-- VIEW���� PUBLISHER_ID�� �����ϰ��ֱ� ������ �Ʒ� ������ ERROR�߻�
ALTER TABLE BOOKS DROP COLUMN PUBLISHER_ID;

-- �̷����, CASCADE�ɼ��� �־� ����
-- ��� �����ϴ� ���鵵 ���� ������ �ȴ�.(����)
-- DBA�� �ƴϸ� CASCADE�� ����ذ��� �������� �ʵ���..!
ALTER TABLE BOOKS DROP COLUMN PUBLISHER_ID CASCADE;


-- ���ÿ� �ΰ� �÷� �����غ���
ALTER TABLE BOOKS 
	DROP COLUMN ISBN,
	DROP COLUMN DESCRIPTION;














-- �÷� ������ Ÿ�� ����
CREATE TABLE ASSETS(
	ID SERIAL PRIMARY KEY
	, NAME TEXT NOT NULL
	, ASSET_NO VARCHAR(10) NOT NULL
	, DESCRIPTION TEXT
	, LOCATION TEXT
	, AQUIRED_DATE DATE NOT NULL
);


INSERT INTO ASSETS (NAME, ASSET_NO, LOCATION, AQUIRED_DATE) 
VALUES 
	('Server', '10001', 'Server room', '2017-01-01')
	,('UPS', '10002', 'Server room', '2017-01-02');
	
SELECT * FROM assets;

ALTER TABLE assets ALTER COLUMN name TYPE varchar(50);
ALTER TABLE assets 
	ALTER column LOCATION TYPE varchar(100),
	ALTER COLUMN description TYPE varchar(500);
	
ALTER TABLE assets ALTER COLUMN asset_no TYPE int USING asset_no::integer;












-- �÷� �̸� ����
DROP TABLE customer_groups;
DROP TABLE customers;
DROP TABLE customer_data;

CREATE TABLE CUSTOMER_GROUPS(
	ID SERIAL PRIMARY KEY
	, NAME VARCHAR NOT NULL
);

CREATE TABLE CUSTOMERS(
	ID SERIAL PRIMARY KEY
	, NAME VARCHAR NOT NULL
	, PHONE VARCHAR NOT NULL
	, EMAIL VARCHAR
	, GROUP_ID INT
	, FOREIGN KEY (GROUP_ID) REFERENCES CUSTOMER_GROUPS(ID)
);

CREATE VIEW CUSTOMER_DATA
AS SELECT 
	C.ID, 
	C.NAME,
	C.NAME CUSTOMER_GROUP
FROM CUSTOMERS C, CUSTOMER_GROUPS G
WHERE G.ID = C.GROUP_ID;

SELECT * FROM CUSTOMER_DATA;

-- �÷����� �ٲ���� ��, ���� ���뵵 �ڵ����� �ٲ��. 
ALTER TABLE CUSTOMERS RENAME COLUMN EMAIL TO CONTACT_EMAIL;
ALTER TABLE CUSTOMERS RENAME COLUMN NAME TO GROUP_NAME;










-- ���̺� ����
-- ���̺� ���� �ô� �׻� �����ϰ�, fk���赵 �����Ұ�
DROP TABLE page;

CREATE TABLE AUTHOR(
	AUTHOR_ID INT NOT NULL PRIMARY KEY
	, FIRSTNAME VARCHAR(50)
	, LASTNAME VARCHAR(50)
);

CREATE TABLE PAGE(
	PAGE_ID SERIAL PRIMARY KEY
	, TITLE VARCHAR(255) NOT NULL
	, CONTENT TEXT
	, AUTHOR_ID INT NOT NULL
	, FOREIGN KEY (AUTHOR_ID) REFERENCES AUTHOR(AUTHOR_ID)
);

INSERT INTO AUTHOR VALUES (1, 'kyounhoh', 'Lee');
INSERT INTO page VALUES (1, 'SQL�� ������ ���̽�', 'drop table', 1);


-- fk ������������ ���� ���̺� ���� ����
DROP TABLE author;
-- cacade �ɼ����� ����
DROP TABLE author CASCADE;
-- page ���̺��� ���� ������ �� ����! �ڽ� ���̺��̱� ������ ���� ����
DROP TABLE page;














-- �ӽ����̺�
-- DB ���� ������ Ȱ�� �Ⱓ���� �����ϴ� ���̺� (������ ����Ǹ�, �ӽ� ���̺��� �ڵ� �Ҹ�)
CREATE TEMP TABLE TB_CUST_TEMP_TEST(CUST_ID INT);

INSERT INTO tb_cust_temp_test values(1);
SELECT * FROM tb_cust_temp_test;

-- ������ �����ϴ� ���̺�� ���� �̸����� �ӽ����̺� ������ �ӽ� ���� �غ���
DROP TABLE tb_cust_temp_test;
--�Ϲ����̺� ���� 
CREATE TABLE tb_cust_temp_test (
	cust_id serial PRIMARY KEY,
	cust_nm varchar NOT null
);
-- �ӽ� ���̺� ���� (������ �Ϲ� ���̺�� ����)
CREATE TEMP TABLE tb_cust_temp_test(
	cust_id int
);
-- ��ȸ ��, �ӽ� ���̺� ��ȸ��
SELECT * FROM tb_cust_temp_test;
-- ���̺� ����
DROP TABLE tb_cust_temp_test;
-- �ӽ� ���̺��� ���ư��� �Ϲ� ���̺� ����!
SELECT * FROM tb_cust_temp_test;

-- ������ �����ߴٰ� �����ϰ� �� ��� �ӽ����̺��� ���ư���, �Ϲ� ���̺��� �ٶ󺸰� �ȴ�.















-- truncate: ��뷮�� ���̺��� ������ ���� �� �ִ�. ���׸�Ʈ ��ü�� �ٷ� ����� ������ ������ ������ ��������.
CREATE TABLE truncate_test as
SELECT * FROM account;

SELECT * FROM truncate_test;

TRUNCATE TABLE truncate_test;

SELECT * FROM truncate_test;


