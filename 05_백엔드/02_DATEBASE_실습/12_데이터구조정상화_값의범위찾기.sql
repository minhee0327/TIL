-- 03. 데이터 값의 범위 찾기
-- 영화명과 출시년도가 같이 담겨있음. 이를 분리해서 담아보자.
SELECT * 
FROM movie;

-- split_part 함수를 활용하여 분리하기 예제
SELECT col1
	   ,split_part(col1, ',',1) part1
	   ,split_part(col1, ',',2) part2
	   ,split_part(col1, ',',3) part3
FROM 
	(SELECT '1,2,3' col1)c;
	
-- right 함수를 활용하여 분리하기 예제 (우측으로부터 몇 개를 자를지)
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


