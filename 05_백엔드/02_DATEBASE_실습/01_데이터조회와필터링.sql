-- �⺻ data base ��ȸ
select * from customer;
SELECT  FIRST_NAME, LAST_NAME, EMAIL FROM customer;
select A.FIRST_NAME, A.LAST_NAME, A.EMAIL from customer a;


-- order by: ������ �����͸� ����, ���� ó���� �ſ� �߿� (ASC(������, default), DESC(������))
 SELECT
	FIRST_NAME,
	LAST_NAME
FROM
	customer
ORDER BY
	first_name ASC;


SELECT
	FIRST_NAME,
	LAST_NAME
FROM
	customer
ORDER BY
	first_name DESC;


SELECT
	first_name,
	last_name
FROM
	customer
ORDER BY
	first_name ASC,
	last_name DESC;


SELECT
	first_name,
	last_name
FROM
	customer
ORDER BY
	1 ASC,
	2 DESC;

-- select distict�� : �ߺ����� ������ ����� ��� (DISTINCT ���� ����)
 

-- ���͸�1: where��
 SELECT
	LAST_NAME,
	FIRST_NAME
FROM
	customer
WHERE
	first_name = 'Jamie';


-- ������ 2���϶� (and)
 SELECT
	LAST_NAME,
	FIRST_NAME
FROM
	CUSTOMER
WHERE
	first_name = 'Jamie'
	AND last_name = 'Rice';


-- ������ 2���϶� (or)
 SELECT
	CUSTOMER_Id,
	AMOUNT,
	PAYMENT_DATE
FROM
	payment
WHERE
	AMOUNT <= 1
	OR AMOUNT >= 8;
	
-- LIMIT��: Ư�� ���� ��½� ����ϴ� ���� ���� �����ϴ� ����. �κ� ���� ó��. (MySQL, PostgreSQL)
-- OFFSET: ���� ��ġ M+1 ���� (�� M:3 �̸� 0, 1, 2, 3, => 4��° �� 3+1��°)
SELECT 
	* 
FROM
	TABLE_NMAE
LIMIT N OFFSET M;
-- 
SELECT * FROM film ORDER BY film_id ;

SELECT
	FILM_ID,
	TITLE,
	RELEASE_YEAR
FROM
	FILM
ORDER BY
	film_id
LIMIT 5;

SELECT
	FILM_ID,
	TITLE,
	RELEASE_YEAR
FROM
	FILM
ORDER BY
	film_id
LIMIT 4 OFFSET 3;

SELECT
	FILM_ID,
	TITLE,
	RENTAL_RATE
FROM
	FILM
ORDER BY
	RENTAL_RATE DESC
LIMIT 10;


-- FETCH��: ���� �� ����, �κ� ���� ó���� ���
-- N�� �Է����� �ʰ�, ROW ONLY�� �Է��� ���, �� �ѰǸ� ���. (����ϴ� ���� �� ����)
SELECT
	*
FROM
	TABLE_NAME FETCH FIRST [N] ROW ONLY;
	

-- ����ϴ� ���� ���� �����ϸ鼭 ������ġ ����
 SELECT
	*
FROM
	TABLE_NAME OFFSET N ROWS FETCH FIRST [N] ROW ONLY;


-- ���� (���Լ����, ���� 1�Ǹ� �������� ��쿡 ���̴� ��찡 ����.)
SELECT
	film_id,
	title
FROM
	film
ORDER BY
	title FETCH FIRST ROW ONLY;
	
-- ����: ù����� ~ n��° �����
SELECT
	film_id,
	title
FROM
	film
ORDER BY
	title FETCH FIRST 3 ROW ONLY;



-- ����: ������ 6���� ~ 3���� ���� �������ڴ�.
 SELECT
	film_id,
	title
FROM
	film
ORDER BY
	title OFFSET 5 ROWS FETCH FIRST 3 ROW ONLY;


-- in ����: customer_id�� 1Ȥ�� 2 �� return_date�������� ����
-- ������, ��Ƽ�������� Ư����, IN������ where or ���Ǻ��� ���ɻ� ����ȭ�� ����.
 SELECT
	customer_id,
	rental_id,
	return_date
FROM
	rental
WHERE
	customer_id IN (1,2)
ORDER BY
	return_date DESC;


-- or�� �� ���� ���� ��� ������
 SELECT
	customer_id,
	rental_id,
	return_date
FROM
	rental
WHERE
	customer_id = 1
	OR customer_id = 2
ORDER BY
	return_date DESC; 
	

-- not in 
-- 1Ȥ�� 2�� ������ ������ ( 1Ȥ�� 2�� �ƴ� ��)
SELECT 
	customer_id,
	rental_id,
	return_date
FROM 
	rental
WHERE 
	customer_id NOT IN (1, 2)
ORDER BY 
	return_date DESC;

-- and�� �ۼ��غ���
SELECT 
	customer_id,
	rental_id,
	return_date
FROM 
	rental
WHERE 
	customer_id <> 1 
	AND customer_id != 2
ORDER BY 
	return_date DESC;

--

SELECT 
	customer_id
FROM 
	rental
WHERE
	cast(return_date AS date) = '2005-05-27';



--
SELECT
	first_name,
	last_name
FROM
	customer
WHERE
	customer_id IN(
	SELECT
		customer_id
	FROM
		rental
	WHERE
		CAST(return_date AS date) = '2005-05-27');
		
	
--between (sql�� ��������� �������� ���� ����ϴ� ���� ����)
SELECT customer_id, payment_id, amount
FROM payment
WHERE amount BETWEEN 8 AND 9;
-- and�� ����ϴ� ���
SELECT customer_id, payment_id, amount
FROM payment
WHERE amount >= 8 AND amount <= 9;
-- not between
SELECT customer_id, payment_id, amount
FROM payment
WHERE amount NOT BETWEEN 8 AND 9;
-- ���� ���� ���
SELECT customer_id, payment_id, amount
FROM payment  
WHERE amount <8 OR amount  > 9;
-- between date �� ������ handling�غ���
-- timestamp ���� date �� �ٲ��� charŸ������ cast(����ȯ)
SELECT customer_id, payment_id, amount, payment_date
FROM payment
WHERE cast(payment_date AS date) BETWEEN '2007-02-07' AND '2007-02-15';
-- ���� ���� ������� �ٸ� ���
SELECT customer_id, payment_id, amount, payment_date
FROM payment
WHERE to_char(payment_date,'yyyy-mm-dd') BETWEEN '2007-02-07' AND '2007-02-15';




-- LIKE ������: �÷����� Ư�� ���ϰ� ������ ���� ���
-- Ư�����Ͽ��� '%'�� � ���� Ȥ�� ���ڿ��̵��� ��Ī�Ǿ��� �Ǵ�
-- Ư�����Ͽ��� '_'�� �Ѱ��� ���ڰ� � �����̵��� ��Ī�Ǿ��ٰ� �Ǵ��Ѵ�.
-- Like ������ ����� true�� �� ����� ��µ�.
SELECT first_name, last_name
FROM customer
WHERE first_name LIKE 'Jen%';
-- '%', '_' ������ sample
SELECT 
	'FOO' LIKE 'FOO',
	'FOO' LIKE 'F%',
	'FOO' LIKE '_O_',
	'BAR' LIKE 'B_%',
	'BAR' LIKE 'B_';

	
-- IS NULL (IS NOT NULL)
-- Ư�� �÷� Ȥ�� ���� �� ������ �ƴ����� �Ǵ��ϴ� ������. 
-- ���� ������ �ְ� �ǽ�(isNull���� ����)
SELECT * 
FROM table_name
WHERE column_nmae IS NULL;

