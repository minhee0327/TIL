-- payment테이블에서 단일 거래의 amount 액수가 가장 많은 고객들의 customer_id를 추출하라. 
-- 단, customer_id의 값은 유일해야한다.

-- 내가 푼 sql문
SELECT DISTINCT CUSTOMER_ID
FROM PAYMENT
WHERE AMOUNT IN (SELECT MAX(AMOUNT) FROM PAYMENT);

-- 선생님이 푼 sql문
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
	


-- 고객들에게 단체 이메일 전송한다. customer 테이블에서 고객의 email주소를 추출하고 이메일 형식에 맞지 않는 이메일 주소는 제외시켜라.
--  email형식은 '@'가 존재해야 하고 '@'로 시작하지 말아야하고 '@'로 끝나지 말아야한다.


-- 내가 푼거 (답안과 동일)
 SELECT
	email
FROM
	customer
WHERE
	email LIKE '%@%'
	AND email NOT LIKE '@%'
	AND email NOT LIKE '%@';



