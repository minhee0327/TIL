-- film 테이블을 한번만 scan해서 문제와 같은 동일한 결과를 구하는 sql작성
-- 문제쿼리
SELECT film_id, title, rental_rate
FROM film
WHERE rental_rate > (SELECT avg(rental_rate) FROM film);
-- 중간 쿼리
SELECT film_id, title, rental_rate, avg(rental_rate) OVER ()
FROM film;
-- 변경해보기(인라인 뷰 형태)
SELECT A.film_id, A.title, A.rental_rate
FROM (
	SELECT film_id, title, rental_rate, avg(rental_rate) OVER () AS avg_rental_rate
	FROM film	
) A
WHERE A.rental_rate > A.avg_rental_rate;


-- 실습문제2
-- except연산을 사용하여 재고없는 영화를 구했는데, 이를 except연산 없이 같은 결과를 도출해보기.
SELECT f.film_id, f.title
FROM film f
where
NOT EXISTS (
	SELECT 1
		FROM inventory i
		WHERE f.film_id  = i.film_id
)
ORDER BY title;
