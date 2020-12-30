-- 실습1
CREATE TABLE basket(
	id serial PRIMARY KEY,
	fruit varchar(50) NOT null
);

INSERT INTO basket(fruit) values('apple');
INSERT INTO basket(fruit) values('apple');
INSERT INTO basket(fruit) values('orange');
INSERT INTO basket(fruit) values('orange');
INSERT INTO basket(fruit) values('orange');
INSERT INTO basket(fruit) values('banana');

SELECT * FROM basket;


DELETE FROM basket WHERE id in(
SELECT id
FROM (
	SELECT id, fruit,(row_number() over(PARTITION BY fruit ORDER BY id)) AS row_num 
	FROM basket
) T
WHERE row_num > 1);
















-- 실습2
-- ROW_NUMBER를 사용하면 중복제거
-- rank를 사용하면 중복되도 뽑음

SELECT * FROM film;

SELECT film_id , title, rating, length, a.row_num
FROM (
	SELECT film_id, title, rating, length, row_number () over(PARTITION BY rating ORDER BY length desc) AS row_num
	FROM film
)a
WHERE a.row_num = 1;




WITH tmp1 as(
SELECT film_id , title, rating, length, row_number() OVER (PARTITION BY rating ORDER BY length desc) length_rank
FROM film) SELECT * FROM tmp1 WHERE length_rank = 1;




