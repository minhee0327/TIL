-- dvd ��Ż �ý����� �����ڴ� ���� ���� ������ �˰�ʹ�.
-- �ű����̺��� �����ؼ� ���� ���� ������ �����ϰ� ������ �ű����̺��� �̸��� customer_rank�̰� ���̺� ������
-- customer_id, customer_rank�� ���ߴ�.
-- ctas����� �̿��Ͽ� �ű� ���̺��� �����ϸ鼭 �����͸� �Է��ض�.


-- ���� ��ü �����ݾ��� ����.
SELECT customer_id, sum(amount)
FROM payment 
GROUP BY customer_id ;

-- �� ���� �������� rank�� ����.
SELECT A.customer_id, ROW_NUMBER () OVER (order BY A.sum_amount desc) AS customer_rank
FROM (
	SELECT p.customer_id, sum(p.amount) AS sum_amount
	FROM payment p
	GROUP BY p.customer_id
) A
ORDER BY customer_rank;

-- CTAS�������
CREATE TABLE customer_rank AS
SELECT A.customer_id, ROW_NUMBER () OVER (order BY A.sum_amount desc) AS customer_rank
FROM (
	SELECT p.customer_id, sum(p.amount) AS sum_amount
	FROM payment p
	GROUP BY p.customer_id
) A
ORDER BY customer_rank;


SELECT * FROM customer_rank;