-- dvd 렌탈 시스템의 관리자는 고객별 매출 순위를 알고싶다.
-- 신규테이블을 생성해서 고객의 매출 순위를 관리하고 싶으며 신규테이블의 이름은 customer_rank이고 테이블 구성은
-- customer_id, customer_rank로 정했다.
-- ctas기법을 이용하여 신규 테이블을 생성하면서 데이터를 입력해라.


-- 고객별 전체 결제금액을 구함.
SELECT customer_id, sum(amount)
FROM payment 
GROUP BY customer_id ;

-- 이 값을 기준으로 rank를 구함.
SELECT A.customer_id, ROW_NUMBER () OVER (order BY A.sum_amount desc) AS customer_rank
FROM (
	SELECT p.customer_id, sum(p.amount) AS sum_amount
	FROM payment p
	GROUP BY p.customer_id
) A
ORDER BY customer_rank;

-- CTAS기법적용
CREATE TABLE customer_rank AS
SELECT A.customer_id, ROW_NUMBER () OVER (order BY A.sum_amount desc) AS customer_rank
FROM (
	SELECT p.customer_id, sum(p.amount) AS sum_amount
	FROM payment p
	GROUP BY p.customer_id
) A
ORDER BY customer_rank;


SELECT * FROM customer_rank;