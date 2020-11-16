-- Q1. ���ΰ� ���� ������
-- rental table�� �̿��Ͽ�, ��, ����, ������, ��ü ������ �������� rental_id ���ط�Ż�� �Ͼ Ƚ���� ����϶�.
-- ��ü ������ �������� ��� �� ���
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
-- rental��  customer ���̺��� �̿��Ͽ� ������� ���� ���� rental�� ���� id, ��Ż����, ������ŻȽ��, �̸����
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