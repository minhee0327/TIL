-- 데이터 조작 관련 실습 테이블 

-- 실습 준비(insert, update)
CREATE TABLE link (
	ID SERIAL PRIMARY KEY
	, URL varchar(255) NOT NULL
	, name varchar (255) NOT NULL
	, description varchar (255)
	, rel varchar(50)
);

INSERT into link (url, name) values('http://naver.com', 'Naver');



-- update-join
CREATE TABLE product_segment(
	ID SERIAL PRIMARY KEY
	, SEGMENT VARCHAR NOT NULL
	, DISCOUNT NUMERIC(4, 2)
);
INSERT INTO PRODUCT_SEGMENT (SEGMENT, DISCOUNT) VALUES ('Grand Luxury', 0.05), ('Luxury', 0.06), ('Mass' , 0.1);
SELECT * FROM product_segment;

DROP TABLE product;

CREATE TABLE product(
	ID SERIAL PRIMARY KEY
	, NAME VARCHAR NOT NULL
	, PRICE NUMERIC(10, 2)
	, NET_PRICE NUMERIC(10, 2)
	, SEGMENT_ID INT NOT NULL
	, FOREIGN KEY (SEGMENT_ID) REFERENCES PRODUCT_SEGMENT(ID)
);
INSERT INTO PRODUCT (NAME, PRICE, SEGMENT_ID) VALUES 
	('K5', 804.89, 1)
	, ('K7', 228.55, 3)
	, ('K9', 366.45, 2)
	, ('SONATA', 145.33, 3)
	, ('SPARK', 551.77 , 2)
	, ('AVANTE', 261.58, 3)
	, ('LOZTE', 519.62, 2)
	, ('SANTAGE', 843.31,1)
	,('TUSON', 254.18, 3)
	, ('TRAX', 427.78, 2)
	, ('ORANDO', 936.29, 1)
	, ('RAY', 910.34 ,1)
	, ('MORNONG', 208.33, 3)
	, ('VERNA', 985.45, 1)
	, ('K8', 841.26, 1)
	, ('TICO', 892.38, 1)
	, ('MATIZ', 575.74, 2)
	, ('SPORTAGE', 530.64, 2)
	, ('ACCENT', 892.43, 1)
	, ('TOSCA', 161.71, 3);
	


-- upsert 실습준비
CREATE TABLE customers (
	CUSTOMER_ID SERIAL PRIMARY KEY
	, NAME VARCHAR UNIQUE
	, EMAIL VARCHAR NOT NULL
	, ACTIVE BOOL NOT NULL DEFAULT TRUE
)

SELECT * FROM customers;

INSERT
	INTO
	customers (name, email)
VALUES 
	('IBM', 'contact@ibm.com'),
	('Microsoft', 'contact@microsoft.com'),
	('Intel', 'contact@intel.com');
	







-- import 실습준비
CREATE TABLE CATEGORY_IMPORT
(
	CATEGORY_ID serial NOT NULL
	, "name" varchar(25) NOT NULL
	, last_update timestamp NOT NULL DEFAULT now()
	, CONSTRAINT category_import_key PRIMARY KEY (category_id)
)