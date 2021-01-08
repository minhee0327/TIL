-- 고급 집계 데이터: 어려운게 아니고, 조금더 강력한, 수고를 덜을 수 있는 집계데이터
-- 실습준비

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

-- 위 4가지 경우를 union all 로 모두 구해보자.
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
-- 위 구문 단점: 동일한 테이블을 4번식이나 읽어야한다 => 성능저하 가능
-- sql문이 길어진다. => 복잡 => 유지보수 용이 X

-- grouping set이 나오게 됨.(아래 sample code)
SELECT c1, c2, 집계함수(c3)
FROM table_name
GROUP BY 
GROUPING sets((c1, c2), (c1) , (c2), ());
-- 
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY
	GROUPING sets((brand, segment), (brand), (segment), ());
--
-- grouping 함수로 집계에 사용유무를 알수도 있다. (쓰인경우 0 , 안쓰인경우 1)
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
-- 응용
SELECT 
		CASE WHEN GROUPING(brand) = 0 AND grouping(segment) = 0 THEN '브랜드별 + 등급별'
			 WHEN GROUPING(brand) = 0 AND grouping(segment) = 1 THEN '브랜드별'
			 WHEN GROUPING(brand) = 1 AND grouping(segment) = 0 THEN '등급별'
			 WHEN GROUPING(brand) = 1 AND grouping(segment) = 1 THEN '전체합계'
			 ELSE ''
			 END AS "집계기준",
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

-- group by별 합계, rollup절 맨앞에 쓴 컬럼 기준의 합계 + 전체합계
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY 
	ROLLUP (brand, segment)
ORDER BY 	
	brand, segment;

-- 부분 rollup시 전체 합계는 구하지 않는다. (기준은 group by 절에 오는 값 기준)
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY segment,
	ROLLUP (brand)
ORDER BY 
	segment, brand;

-- 부분 rollup = group by 별 합계 + 맨앞에 쓴 컬럼별 합계 + 전체 합계는 구하지 않는다.
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY brand,
	ROLLUP (segment)
ORDER BY 
	brand,segment;
	
-- cube절 (3개의 컬럼 c1, c2, c3에 대해 나올수 있는 모든 경우의 수: 2³)
-- 지정된 grouping컬럼의 다차원 소계를 생성하는데 사용.
SELECT c1, c2, c3, 집계함수(c4)
FROM table_name
GROUP BY
	cube(c1, c2, c3);
-- 특정 컬럼만 분리하여 cube 지정을 할 수 있다.
SELECT c1, c2, c3, 집계함수(c4)
FROM TABLE_name
GROUP BY c1, 
CUBE (c2, c3);
-- cube = group by절 합계 + brand별 + segment별 + 전체 합계
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY 
	CUBE (brand, segment)
ORDER BY 
	brand, segment;
--roll up과 한번 비교해보자.
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY 
	ROLLUP (brand, segment)
ORDER BY brand, segment;
-- 부분 큐브: group by 별 합계 + 맨 앞에 쓴 컬럼별 합계
-- 뒤에 쓴 컬럼이랑, 전체 합계는 안구함
SELECT brand, segment, sum(quantity)
FROM sales
GROUP BY brand,
	CUBE (segment)
ORDER BY brand, segment;

