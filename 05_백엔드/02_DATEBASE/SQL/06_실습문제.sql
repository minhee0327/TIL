-- Q1. 조인과 집계 데이터
-- rental table을 이용하여, 연, 연월, 연월일, 전체 각각의 기준으로 rental_id 기준렌탈이 일어난 횟수를 출력하라.
-- 전체 데이터 기준으로 모든 행 출력
SELECT to_char(rental_date, 'yyyy') FROM rental;
SELECT 
	to_char(rental_date, 'yyyy') AS Y,
	to_char(rental_date, 'mm') AS M,
	to_char(rental_date, 'dd') AS D,
	count(*) 
FROM rental
GROUP BY 
	ROLLUP (to_char(rental_date ,'yyyy'),to_char(rental_date, 'mm') ,to_char(rental_date, 'dd') ) ;
	
--!Q2
-- rental과  customer 테이블을 이용하여 현재까지 가장 많이 rental한 고객의 id, 렌탈순위, 누적렌탈횟수, 이름출력
SELECT 
	A.customer_id 
	,ROW_NUMBER () over(ORDER BY count(A.rental_id) desc) AS rental_rank
	,count(*) rental_count
	,B.first_name 
	,B.last_name 
FROM rental A ,
	customer B
WHERE A.customer_id = B.customer_id 
GROUP BY A.customer_id, B.first_name , B.last_name 
ORDER BY rental_rank
LIMIT 1;

--
SELECT 
	A.customer_id 
	,ROW_NUMBER () over(ORDER BY count(A.rental_id) desc) AS rental_rank
	,count(*) rental_count
	,max(B.first_name) AS first_name
	,max(B.last_name) AS last_name
FROM rental A ,
	customer B
WHERE A.customer_id = B.customer_id 
GROUP BY A.customer_id
ORDER BY rental_rank
LIMIT 1;