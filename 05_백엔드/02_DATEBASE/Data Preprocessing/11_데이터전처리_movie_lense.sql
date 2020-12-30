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





-- 참고 
-- data import 해올 때, 기존에 만든 테이블 컬럼을 사용하고 싶다면
-- tables mapping시 columns 탭에 들어가서 변경을 해줘야한다. 안그럼 새로운 column으로 insert되니까 주의!
-- 또한 data type도 원하는 data type으로 변경해줄 수 있다. 
-- dbeaver가 업데이트 되서 기존 강의와 조금 차이가 있어서 해결하는데 시간이 좀 많이 걸렸기 때문에 메모 남겨둔다.