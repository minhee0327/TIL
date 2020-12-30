CREATE TABLE T1 (ID SERIAL NOT NULL PRIMARY KEY, BCOLOR VARCHAR, FCOLOR VARCHAR );
DROP TABLE T1;

-- COMMIT �ʿ� ���� (���̺� ����) => DDL => ġ�� ���� �ٷ� ����

INSERT 
	INTO T1(BCOLOR, FCOLOR)
VALUES
	('red', 'red'),
	('red', 'red'),
	('red', NULL),
	(NULL, 'red'),
	('red', 'green'),
	('red', 'blue'),
	('green', 'red'),
	('green', 'blue'),
	('green', 'green'),
	('blue', 'red'),
	('blue', 'green'),
	('blue', 'green'),
	('blue', 'blue');
	
COMMIT;

SELECT * FROM T1;

-- DISTICT �÷� 1��
SELECT 
	DISTINCT BCOLOR
FROM 
	T1
ORDER BY bcolor;

-- DISTINCT �÷� 2��
SELECT 
	DISTINCT BCOLOR, FCOLOR
FROM 
	T1
ORDER BY
	BCOLOR, FCOLOR;
	
-- DISTICT ON: ON�� ����� �÷� ���� �ߺ����� ��, ������ �÷����� �� �Ѱ��� ���� �����ش�.
SELECT 
	DISTINCT ON(BCOLOR) BCOLOR, FCOLOR
FROM T1
ORDER BY BCOLOR, FCOLOR;


SELECT 
	DISTINCT ON(BCOLOR) BCOLOR, FCOLOR
FROM T1
ORDER BY BCOLOR, FCOLOR DESC;

-- 