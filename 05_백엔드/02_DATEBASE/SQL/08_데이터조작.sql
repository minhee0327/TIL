-- ������ ���� �� ���̺����
-- ������ ����, ����, ���� ��

-- 01. insert��
-- ���̺��� ��������� �� ������ ��������� ���̸�, ���̺� �ȿ� �����͸� insert�ϴ� ���� �ʿ��ϴ�.
-- 2���� ���, ���̺� �÷� ������� �Է� (����Է�) / ���̺� �÷��� �����ؼ� ����
INSERT INTO table_name VALUES (value1, value2, value3,...);
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
-- commit�� �ϴ°� �⺻�ε� dbeaver�� auto commit ������ �Ǿ��־ ����
SELECT * FROM link;
-- ���� ����ǥ �Է��ϰ� ���� ��.
INSERT into link (url, name) values('''http://naver.com''', '''Naver''');
-- ������ �Է��ϰ� ���� ��.
INSERT into link (url, name) values('http://google.com', 'Google'), ('http://daum.net', 'Daum'), ('http://yahoo.com', 'Yahoo');

-- CTS: create table select? => ���̺��� ��Ű��(������)�� �����ͼ�, ���̺��� �����Ѵ�. ������ ���̺��� ���� ������ ����, �����ʹ� 0���� ��Ű���� ���������.
CREATE TABLE link_tmp AS SELECT * FROM link WHERE 0 = 1;
SELECT * FROM link_tmp;
--
INSERT INTO link_tmp SELECT * FROM link;
SELECT * FROM link_tmp;
-- (link_tmp) - (link)
SELECT * FROM link_tmp
EXCEPT
SELECT * FROM link;
-- (link) - (link_tmp)
SELECT * FROM link
EXCEPT
SELECT * FROM link_tmp;









-- 02. update
-- ����, ���̺��� �����ϴ� �����͸� �����ϴ� �۾�. ���ü��� ����
-- ��� �࿡ ���� �ٸ� ����ڴ� �ش� �࿡ ���� �۾��� ���� ���ϵ��� ��(lock)�� �Ǵ�. 
-- �� update�� �� ��, �绡�� commit���� ������ rdbms�� ���ü��� ��������. (������ commit�� �� �ֵ��� �� ��)
-- rdbms�� ����ϴ� ����: �����͸� ����ҿ� �����صΰ�, �������� ����ڰ� ���ÿ� ���� �� �ְԲ��ϱ� ����.
UPDATE					-- uptdate�� ���̺� ����
	table_name 
SET 					-- ������ �÷� �� �� �Է�
	column1 = value1, 
	column2 = value2
WHERE					-- �������
	����;
	
-- �ǽ� �غ�
-- column�߰�
ALTER TABLE link ADD COLUMN last_update DATE;
ALTER TABLE link ALTER COLUMN last_update SET DEFAULT CURRENT_date; -- last_update �÷��� �⺻��: ���糯¥.
SELECT * FROM link;  
COMMIT;
-- ����(last_update�÷��� null�ΰ��� => default value�� ����)
UPDATE link SET last_update = DEFAULT WHERE last_update IS NULL;
SELECT * FROM link;
-- ���̺� rel�÷��� ��� 'NO DATA'�� ����
-- ���â: where�� ���� update �����Ϸ��ϴµ�, data�� �սǵ� �� �ִ�. => dangerous query (��ü�÷��� �ٲٴ� �Ǽ��� �����Ϸ��� �ߴ� �˸�â)
UPDATE link SET rel ='NO DATA';
UPDATE link SET description = name;









-- 03. update join��
-- update�� �ٸ� ���̺��� ������ �����ϰ� ���� �� ���. 
-- �⺻ ����
UPDATE target_table A				-- update�� ���̺� ����
SET A.column_1 = ǥ����				-- Ư�� �÷� update
FROM ref_table B					-- ���� ���̺� ����
WHERE A.column_1 = B.column_1; 		-- ���� ����
--��ȸ
SELECT * FROM product_segment;
SELECT * FROM product;
-- ����(price) * ���η�(discount) => net_price column�� ������Ʈ �غ���.
UPDATE product A
SET net_price =A.price - A.price * B.discount
FROM product_segment B
WHERE A.segment_id = B.id;






-- 04. delete
-- ���̺��� Ư�� �����͸� �����ϰų� ���̺� ���� �����ϴ� ��� �����͸� ������ �� �ִ�.
DELETE FROM ���̺��̸� WHERE ���ǽ�;

DELETE FROM link WHERE id = 5;
SELECT * FROM link;

-- delete join
-- �� ���̺��� matching�Ǵ� row���� ��� �����.  
DELETE FROM link_tmp USING link WHERE link_tmp.id = link.id;
SELECT * FROM link_tmp;

-- ��ü �� ����
DELETE FROM link;
SELECT count(*) FROM link;

DELETE FROM link_tmp;
SELECT count(*) FROM link;











-- 05. upsert��
-- insert �õ��� ����(��Ȳ)�� ���� update�� �� �ִ� ����.
-- ���� ����
 INSERT
	INTO
	TABLE name(column_1) 			-- insert �õ�
VALUES(value_1) ON
CONFLICT target ACTION;				-- �浹�� �ٸ� �׼�

-- do nothing: �浹�� �ƹ��͵� ���� ����.
-- name�� unique�����̹Ƿ�, �ߺ��� ���� ������ ��������.
INSERT INTO customers (name, email)
VALUES ('Microsoft', 'hotline@microsoft.com')
ON CONFLICT (name) DO NOTHING;

SELECT * FROM customers;

-- �浹�� �߻��� ��� do update + exclude(�����Ͽ� �����̾�� ���)
INSERT INTO customers(name, email)
VALUES ('Microsoft', 'hotline@microsoft')
ON CONFLICT (name) 
DO UPDATE SET email = EXCLUDED.email || ';' || customers.email;

SELECT * FROM customers;












-- 06. export 
-- ���̺��� �����͸� �ٸ������� �����ͷ� �����ϴ� �۾� (��ǥ: csv)
-- ��
SELECT * FROM category;
-- C:\tmp�� �־����
COPY category(category_id, name,last_update)
TO 'C:\tmp\DB_CATEGORY.csv'
DELIMITER ','
CSV HEADER;
-- text�������·� ���
COPY category(category_id, name,last_update)	-- �����ϰ����ϴ� ���̺�� �÷�
TO 'C:\tmp\DB_CATEGORY.txt'						-- ������ �����͸� ������ ���ϰ��\�����̸�
DELIMITER '|'									-- ������ '|'
CSV HEADER; 									-- ��������, �÷��� �߰�
-- 
COPY category(category_id ,name, last_update)
TO 'C:\tmp\DB_CATEGORY_2.csv'
DELIMITER ','
CSV;











-- 07. import 
-- file => table�� �ֱ�
-- import �ǽ��غ�
CREATE TABLE CATEGORY_IMPORT
(
	CATEGORY_ID serial NOT NULL
	, "name" varchar(25) NOT NULL
	, last_update timestamp NOT NULL DEFAULT now()
	, CONSTRAINT category_import_key PRIMARY KEY (category_id)
);

SELECT * FROM CATEGORY_IMPORT;

COPY category_import(category_id, "name", last_update)	-- ������ ���̺� �� �÷��� �����Ѵ�.
FROM 'C:\tmp\DB_category.csv'							-- ������ ���� ����
DELIMITER ','											-- ������ ������ �����ڸ� �˷��ش�.
CSV HEADER;												-- �������� ����, header �������

SELECT * FROM category_import;
DELETE FROM category_import;

COPY category_import (category_id, "name", last_update)
FROM 'C:\tmp\DB_category.txt'
DELIMITER '|'
CSV HEADER;

SELECT * FROM category_import;
DELETE FROM category_import;

COPY category_import(category_id, "name", last_update) 
FROM 'C:\tmp\DB_category_2.csv'
DELIMITER ','	
CSV ;													-- header�� ���� �����̹Ƿ�, headerŰ���� ����









