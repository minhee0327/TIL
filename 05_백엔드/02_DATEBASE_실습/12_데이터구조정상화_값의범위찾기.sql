-- 03. ������ ���� ���� ã��
-- ��ȭ��� ��ó⵵�� ���� �������. �̸� �и��ؼ� ��ƺ���.
SELECT * 
FROM movie;

-- split_part �Լ��� Ȱ���Ͽ� �и��ϱ� ����
SELECT col1
	   ,split_part(col1, ',',1) part1
	   ,split_part(col1, ',',2) part2
	   ,split_part(col1, ',',3) part3
FROM 
	(SELECT '1,2,3' col1)c;
	
-- right �Լ��� Ȱ���Ͽ� �и��ϱ� ���� (�������κ��� �� ���� �ڸ���)
SELECT right('1234556789', 3) right_result;
SELECT right('1234556789', 4) right_result;

CREATE TABLE movie2 as
SELECT m.movieid,
	CASE WHEN m.title_nm LIKE '%(1%' THEN split_part(m.title_nm, '(1', 1) 
		 WHEN m.title_nm LIKE '%(2%' THEN split_part(m.title_nm, '(2', 1)
		 END title_nm
	,REPLACE(REPLACE(right(m.title_nm, 6), ')' , ''), '(','') realse_year
	, m.genres_nm 
FROM movie m;


SELECT * FROM movie2;

ALTER TABLE movie RENAME TO move_old;
ALTER TABLE movie2 RENAME TO movie;

SELECT * FROM movie;


