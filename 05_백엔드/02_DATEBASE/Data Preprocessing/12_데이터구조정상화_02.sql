-- 02. 참조키찾기
-- users <---> rating

/* Step 1 : 참조키 유무 알아보기 */
SELECT count(*) cnt
FROM TABLE1 T1
INNER JOIN TABLE2 t2
ON t1.x = t2.x
LIMIT 1;
 
SELECT count(*) cnt
FROM users
INNER JOIN rating 
ON users.userid = rating.userid
LIMIT 1;

SELECT *
FROM users
INNER JOIN rating 
ON users.userid = rating.userid
LIMIT 1;

-----------------------------------------------
/* Step 2 : 참조했을 때, 카디널리티(1:1, 1:N, N:M ?)*/
-- 1. D_x1 >= X2  -- 1:1
-- 2. D_x1 < X2   -- 1:N
-- 3. D_x1 = D_x2 -- 필수 
-- 4. D_x1 > D_x2 -- 선택 

SELECT count(DISTINCT t1.x) D_x1,
	   count(DISTINCT t2.x) D_x2,
	   count(t2.x) x2
FROM Table1 t1
	 LEFT OUTER JOIN Table2 t2
ON t1.x = t2.x

SELECT count(DISTINCT t1.userid) D_x1,
	   count(DISTINCT t2.userid) D_x2,
	   count(t2.userid) x2
FROM users t1
LEFT OUTER JOIN rating t2
ON t1.userid = t2.userid;


------------------------------------------------------
-- movie <---> rating

/* Step1 */
SELECT count(*) cnt
FROM movie
INNER JOIN rating 
ON movie.movieid = rating.movieid 
LIMIT 1;

/* Step2 */
SELECT count(DISTINCT t1.movieid) D_x1,
	   count(DISTINCT t2.movieid) D_x2,
	   count(t2.movieid) x2
FROM movie t1
LEFT OUTER JOIN rating t2
ON t1.movieid = t2.movieid;







