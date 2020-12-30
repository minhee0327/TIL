-- �ǽ�����1

CREATE TABLE tb_movie_cust(
	customer_id varchar(10) PRIMARY KEY
	, customer_name varchar(50) NOT NULL 
	, sexual varchar(6) NOT NULL check(sexual = '����' OR sexual = '����')
	, birth_date date NOT NULL
	, address varchar(200) 
	, phone_number varchar(13) 
	, customer_grade char(1) check(customer_grade IN ('S','A','B','C','D') )
	, join_date date NOT NULL check(join_date <= exit_date)
	, exit_date date NOT NULL DEFAULT to_date('9999-12-31', 'yyyy-mm-dd')
)

INSERT INTO tb_movie_cust(customer_id, customer_name, sexual, birth_date, address, phone_number, customer_grade, join_date)
values('000000001', '������', '����', to_date('1982-06-12', 'yyyy-mm-dd'), '��⵵ ���ν� ������ ~~~', '010-6695-0102', 'S', to_date ('2017-01-01', 'yyyy-mm-dd'));

CREATE TABLE tb_movie_resv(
	reserve_num char(10) PRIMARY KEY
	, movie_id char(6) NOT NULL
	, theater_id char(6) NOT NULL
	, customer_id char(10) REFERENCES tb_movie_cust(customer_id) NOT NULL 
	, start_time timestamp NOT NULL CHECK (END_time > start_time)
	, end_time timestamp NOT NULL
	, seat_number varchar(4) NOT NULL 
)

INSERT INTO tb_movie_resv VALUES
	('9000000001', '000001', '000010', '000000001', to_timestamp('2019-05-01 14:00:00', 'yyyy-mm-dd hh24:mi:ss'), to_timestamp('2019-05-01 17:30:00', 'yyyy-mm-dd hh24:mi:ss'), 'A-01');
	
INSERT INTO tb_movie_cust(customer_id, customer_name, sexual, birth_date, address, phone_number, customer_grade, join_date)
VALUES
('0000000002', 'ȫ�浿', '����', to_date('1971-07-04', 'yyyy-mm-dd'), '��⵵ �Ⱦ�� ���ȱ� ��굿 1-2', '010-4321-4321', 'A', TO_date('2018-06-01', 'yyyy-mm-dd'));

INSERT INTO tb_movie_cust(customer_id, customer_name, sexual, birth_date, address, phone_number, customer_grade, join_date)
VALUES
('0000000003', '�̼���', '����', to_date('1971-07-04', 'yyyy-mm-dd'), '��⵵ �Ⱦ�� ���ȱ� ��굿 1-2', '010-4321-4321', 'B', TO_date('2019-12-01', 'yyyy-mm-dd')),
('0000000004', '�̽¿�', '����', to_date('1994-12-08', 'yyyy-mm-dd'), '��⵵ �Ⱦ�� ���ȱ� ��굿 1-2', '010-1234-4321', 'A', TO_date('2017-01-01', 'yyyy-mm-dd')),
('0000000005', '����ȯ', '����', to_date('1984-06-12', 'yyyy-mm-dd'), '��⵵ �Ⱦ�� ���ȱ� ��굿 2-2', '010-1111-4321', 'A', TO_date('2018-06-01', 'yyyy-mm-dd')),
('0000000006', '������', '����', to_date('1971-07-04', 'yyyy-mm-dd'), '��⵵ �Ⱦ�� ���ȱ� ��굿 3-2', '010-2222-4321', 'C', TO_date('2019-12-01', 'yyyy-mm-dd')),
('0000000007', '�⼺��', '����', to_date('1991-03-03', 'yyyy-mm-dd'), '��⵵ �Ⱦ�� ���ȱ� ��굿 1-3', '010-3333-4321', 'B', TO_date('2017-01-01', 'yyyy-mm-dd')),
('0000000008', '������', '����', to_date('1994-12-24', 'yyyy-mm-dd'), '��⵵ �Ⱦ�� ���ȱ� ��굿 3-3', '010-4444-4321', 'C', TO_date('2018-06-01', 'yyyy-mm-dd')),
('0000000009', '������', '����', to_date('1971-06-04', 'yyyy-mm-dd'), '��⵵ �Ⱦ�� ���ȱ� ��굿 3-1', '010-5555-4321', 'D', TO_date('2019-12-01', 'yyyy-mm-dd'));


SELECT count(*) AS ��ü����, count(DISTINCT customer_grade) AS ����ǰ���
FROM tb_movie_cust;



SELECT count(*) AS ��ü����, count(DISTINCT customer_grade) AS "����� ����", round(max(AVG_BY_GRADE),2) AS "��޺� ��� ����", 
		max(MAX_BY_GRADE) AS "��� �� �ִ� ����", min(MIN_BY_GRADE) AS "��� �� �ּ� ����", MAX(GRADE_BY_MIN_EMP_COUNT) AS "�ּ� ������ ���", MAX(GRADE_BY_MAX_EMP_COUNT) AS "�ִ� ������ ���"
FROM tb_movie_cust, (
	SELECT AVG(cnt) AVG_BY_GRADE, MAX(cnt) MAX_BY_GRADE, Min(cnt) MIN_BY_GRADE
	FROM 
	(
		SELECT customer_grade, count(*) cnt
		FROM tb_movie_cust A
		GROUP BY customer_grade
	) B
) B, 
(
	SELECT customer_grade AS grade_by_min_emp_count 
	FROM 
	(
		SELECT customer_grade, count(*) cnt
		FROM tb_movie_cust
		GROUP BY customer_grade
		ORDER BY cnt
	) A
	LIMIT 1
)C,
(
	SELECT customer_grade AS grade_by_max_emp_count
	FROM 
	(
		SELECT customer_grade, count(*) cnt
		FROM tb_movie_cust
		GROUP BY customer_grade
		ORDER BY cnt desc
	) A
	LIMIT 1

)D