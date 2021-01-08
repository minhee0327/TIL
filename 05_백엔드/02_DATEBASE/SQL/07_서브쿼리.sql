-- 서브 쿼리는 sql문 내에서 메인쿼리가 아닌 하위에 존재하는 쿼리를 뜻한다.
-- 2개의 sql을 결합하여 하나의 sql문으로 결과도출? => 중첩 서브쿼리, 인라인 뷰, 스칼라 서브 쿼리

-- 중첩 서브쿼리
SELECT film_id, title, rental_rate
FROM film
WHERE rental_rate > (SELECT avg(rental_rate) FROM film);

-- 인라인 뷰
-- from 절안에 subquery
SELECT A.film_id, A.title, A.rental_rate
FROM film A, (SELECT avg (rental_rate) AS avg_rental_rate FROM film) B
WHERE A.rental_rate > B.avg_rental_rate;


-- 스칼라 서브쿼리
-- select 리스트 절에 있는 쿼리
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
	


-- any연산자
-- 서브 쿼리에 의해 반환된 값 집합과 비교한다. 
-- 서브쿼리의 값이 어떠한 값이더라도 만족하면 조건이 성립한다.
SELECT title, length
FROM film
WHERE length >= any(
	SELECT max(length)
	FROM film A, film_category B
	WHERE A.film_id = B.film_id
	GROUP BY B.category_id
);
-- =Any는 in과 동일하다.
SELECT title, length
FROM film
WHERE length = any(
	SELECT max(length)
	FROM film A, film_category B
	WHERE A.film_id = B.film_id
	GROUP BY B.category_id
);


-- all 연산자
-- 서브쿼리에 의해 반환된 값 집합과 비교. 모든 값이 만족을 해야만 조건이 성립됨.
-- 아래 예시에 의해, 상영시간이 가장 긴 영화가 185분 인 것을 알 수 있다.
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


-- exists연산자: 서브쿼리 내에 집합이 존재하는지 여부만 판단. 
-- 존배여부만 판단하기 때문에, 연산시 부하가 줄어든다. 해당 집합이 존재하기만 하면 더이상 연산을 X.(성능 good)
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