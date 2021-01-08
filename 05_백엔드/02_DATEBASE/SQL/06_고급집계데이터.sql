-- ��� ���� ������: ������ �ƴϰ�, ���ݴ� ������, ���� ���� �� �ִ� ���赥����
-- �ǽ��غ�

CREATE TABLE SALES(
BRAND VARCHAR NOT NULL,
SEGMENT VARCHAR NOT NULL,
QUANTITY INT NOT NULL,
PRIMARY KEY(BRAND, SEGMENT)
)

INSERT INTO SALES (BRAND, SEGMENT, QUANTITY)
VALUES 
	('ABC', 'Premium', 100),
	('ABC', 'Basic', 200),
	('XYZ', 'Premium', 100), 
	('XYZ', 'Basic', 300);
	
COMMIT;
SELECT * FROM sales;

-- grouping set
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY brand, segment;
-- 
SELECT brand, sum(quantity)
FROM sales
GROUP BY brand;
-- 
SELECT segment, sum(quantity)
FROM sales
GROUP BY segment;
-- 
SELECT sum(quantity)
FROM sales;

-- �� 4���� ��츦 union all �� ��� ���غ���.
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY brand, segment
UNION ALL
SELECT brand, NULL, sum(quantity)
FROM sales
GROUP BY brand
UNION ALL
SELECT NULL, segment, sum(quantity)
FROM sales
GROUP BY segment
UNION ALL
SELECT NULL, NULL, sum(quantity)
FROM sales;
-- �� ���� ����: ������ ���̺��� 4�����̳� �о���Ѵ� => �������� ����
-- sql���� �������. => ���� => �������� ���� X

-- grouping set�� ������ ��.(�Ʒ� sample code)
SELECT c1, c2, �����Լ�(c3)
FROM table_name
GROUP BY 
GROUPING sets((c1, c2), (c1) , (c2), ());
-- 
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY
	GROUPING sets((brand, segment), (brand), (segment), ());
--
-- grouping �Լ��� ���迡 ��������� �˼��� �ִ�. (���ΰ�� 0 , �Ⱦ��ΰ�� 1)
SELECT 
	GROUPING(brand) grouping_brand,
	GROUPING(segment) grouping_segment,
	brand,
	segment, 
	sum(quantity)
FROM sales
GROUP BY
	GROUPING sets((brand, segment), (brand), (segment), ())
ORDER BY brand, segment;
-- ����
SELECT 
		CASE WHEN GROUPING(brand) = 0 AND grouping(segment) = 0 THEN '�귣�庰 + ��޺�'
			 WHEN GROUPING(brand) = 0 AND grouping(segment) = 1 THEN '�귣�庰'
			 WHEN GROUPING(brand) = 1 AND grouping(segment) = 0 THEN '��޺�'
			 WHEN GROUPING(brand) = 1 AND grouping(segment) = 1 THEN '��ü�հ�'
			 ELSE ''
			 END AS "�������",
	brand,
	segment, 
	sum(quantity)
FROM sales
GROUP BY
	GROUPING sets((brand, segment), (brand), (segment), ());


-- roll up
SELECT segment, sum(quantity)
FROM sales
GROUP BY segment;
-- 
SELECT segment, sum(quantity)
FROM sales
GROUP BY
	ROLLUP (segment) 
ORDER BY segment;
--
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY 
	brand, segment
ORDER BY 	
	brand, segment;

-- group by�� �հ�, rollup�� �Ǿտ� �� �÷� ������ �հ� + ��ü�հ�
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY 
	ROLLUP (brand, segment)
ORDER BY 	
	brand, segment;

-- �κ� rollup�� ��ü �հ�� ������ �ʴ´�. (������ group by ���� ���� �� ����)
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY segment,
	ROLLUP (brand)
ORDER BY 
	segment, brand;

-- �κ� rollup = group by �� �հ� + �Ǿտ� �� �÷��� �հ� + ��ü �հ�� ������ �ʴ´�.
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY brand,
	ROLLUP (segment)
ORDER BY 
	brand,segment;
	
-- cube�� (3���� �÷� c1, c2, c3�� ���� ���ü� �ִ� ��� ����� ��: 2��)
-- ������ grouping�÷��� ������ �Ұ踦 �����ϴµ� ���.
SELECT c1, c2, c3, �����Լ�(c4)
FROM table_name
GROUP BY
	cube(c1, c2, c3);
-- Ư�� �÷��� �и��Ͽ� cube ������ �� �� �ִ�.
SELECT c1, c2, c3, �����Լ�(c4)
FROM TABLE_name
GROUP BY c1, 
CUBE (c2, c3);
-- cube = group by�� �հ� + brand�� + segment�� + ��ü �հ�
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY 
	CUBE (brand, segment)
ORDER BY 
	brand, segment;
--roll up�� �ѹ� ���غ���.
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY 
	ROLLUP (brand, segment)
ORDER BY brand, segment;
-- �κ� ť��: group by �� �հ� + �� �տ� �� �÷��� �հ�
-- �ڿ� �� �÷��̶�, ��ü �հ�� �ȱ���
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY brand,
	CUBE (segment)
ORDER BY brand, segment;

