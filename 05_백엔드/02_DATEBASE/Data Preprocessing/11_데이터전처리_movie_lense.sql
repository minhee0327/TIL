CREATE TABLE users
(
 userID     integer NOT NULL,
 Gender     varchar(1) NOT NULL,
 Age        integer NOT NULL,
 Occupation integer NOT NULL,
 Zip_code   varchar(10) NOT NULL
-- CONSTRAINT PK_users PRIMARY KEY ( userID )
);

DROP TABLE users;
SELECT * FROM users;

CREATE TABLE movie
(
 MovieID   integer NOT NULL,
 Title_nm  varchar(1024) NOT NULL,
 Genres_nm varchar(1024) NOT NULL
-- CONSTRAINT PK_movie PRIMARY KEY ( MovieID )
);

SELECT * FROM movie;
DROP TABLE movie;

CREATE TABLE rating
(
 MovieID    integer NOT NULL,
 userID     integer NOT NULL,
 Rating_pnt integer NOT NULL,
 Timestamp  varchar(10) NOT NULL
-- CONSTRAINT PK_rating PRIMARY KEY ( MovieID, userID ),
-- CONSTRAINT FK_18 FOREIGN KEY ( userID ) REFERENCES users ( userID ),
-- CONSTRAINT FK_22 FOREIGN KEY ( MovieID ) REFERENCES movie ( MovieID )
);

SELECT * FROM rating;


DROP TABLE rating;

CREATE UNIQUE INDEX PK_movie ON movie (MovieID);
CREATE UNIQUE INDEX PK_rating ON rating (UserId, MovieID);
CREATE UNIQUE INDEX PK_users ON users (UserID);





-- ���� 
-- data import �ؿ� ��, ������ ���� ���̺� �÷��� ����ϰ� �ʹٸ�
-- tables mapping�� columns �ǿ� ���� ������ ������Ѵ�. �ȱ׷� ���ο� column���� insert�Ǵϱ� ����!
-- ���� data type�� ���ϴ� data type���� �������� �� �ִ�. 
-- dbeaver�� ������Ʈ �Ǽ� ���� ���ǿ� ���� ���̰� �־ �ذ��ϴµ� �ð��� �� ���� �ɷȱ� ������ �޸� ���ܵд�.