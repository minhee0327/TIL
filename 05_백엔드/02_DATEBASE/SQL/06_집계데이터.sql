-- 기초 집계 데이터
-- group by절: 각 그룹에 대한 합계, 평균, 카운트 등을 계산할 수 있다.
-- group by절 기재, N개의 컬럼을 group by 하는 경우 ','으로 구분
-- group by절은 from 또는 where절 바로 뒤에 나타나야한다. 
SELECT * FROM payment;

SELECT customer_id FROM payment GROUP BY customer_id ORDER BY customer_id ;
SELECT DISTINCT  customer_id FROM payment;
-- 거래액이 가장 많은 고객순으로 출력
SELECT customer_id, sum(amount) AS amount_sum
FROM payment
GROUP BY customer_id
ORDER BY amount_sum DESC;

SELECT staff_id, count(payment_id) AS count
FROM payment
GROUP BY staff_id;

SELECT * FROM payment
WHERE staff_id =1;

-- Having절: group by 한 결과 중, 뽑을 정보만 뽑는다.
-- example03
SELECT customer_id, sum(amount) AS amount_sum
FROM payment
GROUP BY customer_id
HAVING sum(amount)> 200
ORDER BY amount_sum DESC;
-- example02
SELECT P.CUSTOMER_ID, C.EMAIL , SUM(P.AMOUNT) AS AMOUNT_SUM
FROM PAYMENT P, CUSTOMER C
WHERE P.CUSTOMER_ID = C.CUSTOMER_ID 
GROUP BY P.CUSTOMER_ID, C.EMAIL 
HAVING SUM(P.AMOUNT)> 200;
ORDER BY AMOUNT_SUM DESC;

-- example03
SELECT store_id, count(customer_id) AS count
FROM customer
GROUP BY store_id 
HAVING count(customer_id) > 300;

SELECT store_id, count(customer_id) FROM customer WHERE store_id =1 GROUP  BY store_id;

