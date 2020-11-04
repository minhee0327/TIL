-- payment���̺��� ���� �ŷ��� amount �׼��� ���� ���� ������ customer_id�� �����϶�. 
-- ��, customer_id�� ���� �����ؾ��Ѵ�.

-- ���� Ǭ sql��
SELECT DISTINCT CUSTOMER_ID
FROM PAYMENT
WHERE AMOUNT IN (SELECT MAX(AMOUNT) FROM PAYMENT);

-- �������� Ǭ sql��
SELECT
	DISTINCT A.CUSTOMER_ID
FROM
	PAYMENT A
WHERE
	A.AMOUNT IN (
		SELECT
			K.AMOUNT
		FROM
			PAYMENT K
		ORDER BY
			K.AMOUNT DESC
		LIMIT 1
	);
	


-- ���鿡�� ��ü �̸��� �����Ѵ�. customer ���̺��� ���� email�ּҸ� �����ϰ� �̸��� ���Ŀ� ���� �ʴ� �̸��� �ּҴ� ���ܽ��Ѷ�.
--  email������ '@'�� �����ؾ� �ϰ� '@'�� �������� ���ƾ��ϰ� '@'�� ������ ���ƾ��Ѵ�.


-- ���� Ǭ�� (��Ȱ� ����)
 SELECT
	email
FROM
	customer
WHERE
	email LIKE '%@%'
	AND email NOT LIKE '@%'
	AND email NOT LIKE '%@';



