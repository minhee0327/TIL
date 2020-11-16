-- film ���̺��� �ѹ��� scan�ؼ� ������ ���� ������ ����� ���ϴ� sql�ۼ�
-- ��������
SELECT film_id, title, rental_rate
FROM film
WHERE rental_rate > (SELECT avg(rental_rate) FROM film);
-- �߰� ����
SELECT film_id, title, rental_rate, avg(rental_rate) OVER ()
FROM film;
-- �����غ���(�ζ��� �� ����)
SELECT A.film_id, A.title, A.rental_rate
FROM (
	SELECT film_id, title, rental_rate, avg(rental_rate) OVER () AS avg_rental_rate
	FROM film	
) A
WHERE A.rental_rate > A.avg_rental_rate;


-- �ǽ�����2
-- except������ ����Ͽ� ������ ��ȭ�� ���ߴµ�, �̸� except���� ���� ���� ����� �����غ���.
SELECT f.film_id, f.title
FROM film f
where
NOT EXISTS (
	SELECT 1
		FROM inventory i
		WHERE f.film_id  = i.film_id
)
ORDER BY title;
