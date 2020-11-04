CREATE TABLE T1 (ID SERIAL NOT NULL PRIMARY KEY, BCOLOR VARCHAR, FCOLOR VARCHAR );
DROP TABLE T1;

-- COMMIT 필요 없음 (테이블 생성) => DDL => 치는 순간 바로 적용

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

-- DISTICT 컬럼 1개
SELECT 
	DISTINCT BCOLOR
FROM 
	T1
ORDER BY bcolor;

-- DISTINCT 컬럼 2개
SELECT 
	DISTINCT BCOLOR, FCOLOR
FROM 
	T1
ORDER BY
	BCOLOR, FCOLOR;
	
-- DISTICT ON: ON을 사용한 컬럼 기준 중복제거 후, 나머지 컬럼값은 단 한개의 값만 보여준다.
SELECT 
	DISTINCT ON(BCOLOR) BCOLOR, FCOLOR
FROM T1
ORDER BY BCOLOR, FCOLOR;


SELECT 
	DISTINCT ON(BCOLOR) BCOLOR, FCOLOR
FROM T1
ORDER BY BCOLOR, FCOLOR DESC;

-- 