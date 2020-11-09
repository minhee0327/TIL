-- ���� ���� ������
-- group by��: �� �׷쿡 ���� �հ�, ���, ī��Ʈ ���� ����� �� �ִ�.
-- group by�� ����, N���� �÷��� group by �ϴ� ��� ','���� ����
-- group by���� from �Ǵ� where�� �ٷ� �ڿ� ��Ÿ�����Ѵ�. 
SELECT * FROM payment;

SELECT customer_id FROM payment GROUP BY customer_id ORDER BY customer_id ;
SELECT DISTINCT  customer_id FROM payment;
-- �ŷ����� ���� ���� �������� ���
SELECT customer_id, sum(amount) AS amount_sum
FROM payment
GROUP BY customer_id
ORDER BY amount_sum DESC;

SELECT staff_id, count(payment_id) AS count
FROM payment
GROUP BY staff_id;

SELECT * FROM payment
WHERE staff_id =1;

-- Having��: group by �� ��� ��, ���� ������ �̴´�.
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

