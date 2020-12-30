-- ���� ������ sql�� ������ ���������� �ƴ� ������ �����ϴ� ������ ���Ѵ�.
-- 2���� sql�� �����Ͽ� �ϳ��� sql������ �������? => ��ø ��������, �ζ��� ��, ��Į�� ���� ����

-- ��ø ��������
SELECT film_id, title, rental_rate
FROM film
WHERE rental_rate > (SELECT avg(rental_rate) FROM film);

-- �ζ��� ��
-- from ���ȿ� subquery
SELECT A.film_id, A.title, A.rental_rate
FROM film A, (SELECT avg (rental_rate) AS avg_rental_rate FROM film) B
WHERE A.rental_rate > B.avg_rental_rate;


-- ��Į�� ��������
-- select ����Ʈ ���� �ִ� ����
 SELECT
	A.film_id ,
	A.title ,
	A.rental_rate
FROM
	(
	SELECT
		A.film_id, A.title, A.rental_rate, (
		SELECT
			avg(B.rental_rate)
		FROM
			film B ) AS avg_rental_rate
	FROM
		film A ) A
WHERE
	A.rental_rate > A.avg_rental_rate;
	


-- any������
-- ���� ������ ���� ��ȯ�� �� ���հ� ���Ѵ�. 
-- ���������� ���� ��� ���̴��� �����ϸ� ������ �����Ѵ�.
SELECT title, length
FROM film
WHERE length >= any(
	SELECT max(length)
	FROM film A, film_category B
	WHERE A.film_id = B.film_id
	GROUP BY B.category_id
);
-- =Any�� in�� �����ϴ�.
SELECT title, length
FROM film
WHERE length = any(
	SELECT max(length)
	FROM film A, film_category B
	WHERE A.film_id = B.film_id
	GROUP BY B.category_id
);


-- all ������
-- ���������� ���� ��ȯ�� �� ���հ� ��. ��� ���� ������ �ؾ߸� ������ ������.
-- �Ʒ� ���ÿ� ����, �󿵽ð��� ���� �� ��ȭ�� 185�� �� ���� �� �� �ִ�.
SELECT title, length
FROM film
WHERE length >= all(
	SELECT max(length)
	FROM film A, film_category B
	WHERE A.film_id = B.film_id
	GROUP BY B.category_id
);

--
SELECT rating, round(avg(length), 2) 
FROM film
GROUP BY rating;
--
SELECT film_id, title, length
FROM film
WHERE length > all(
	SELECT round(avg(length), 2) 
	FROM film
	GROUP BY rating
)ORDER BY length;


-- exists������: �������� ���� ������ �����ϴ��� ���θ� �Ǵ�. 
-- ���迩�θ� �Ǵ��ϱ� ������, ����� ���ϰ� �پ���. �ش� ������ �����ϱ⸸ �ϸ� ���̻� ������ X.(���� good)
SELECT first_name, last_name 
	FROM customer c
WHERE
EXISTS (
	SELECT 1 
		FROM payment p 
		WHERE p.customer_id = c.customer_id 
		AND p.amount > 11
)
ORDER BY first_name, last_name;
--
SELECT first_name, last_name 
	FROM customer c
WHERE
NOT EXISTS (
	SELECT 1 
		FROM payment p 
		WHERE p.customer_id = c.customer_id 
		AND p.amount > 11
)
ORDER BY first_name, last_name;
--
SELECT payment.payment_id ,1 FROM payment WHERE payment.amount >11;