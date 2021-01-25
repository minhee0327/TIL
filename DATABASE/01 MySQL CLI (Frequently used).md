# 01 MySQL CLI (Frequently used)



## 사용자 목록, 추가 , 제거 권한 부여

| 기능                          | 명령어                                                       | 사용예                                                       |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 서버 로그인 <br />(MySQL접속) | mysql -u [username] -p;                                      | • mysql –u root –p; <br />• password입력                     |
| 사용자 목록 조회              | use mysql;<br />select user, host from user;                 | •mysql기본 스키마 mysql안에<br />•mysql 기본스키마인 user table에서 확인가능. |
| 사용자 추가                   | create user {username}@{ip} identified by '{password}';      | •create user bit@localhost identified by 'bit';<br />•create user bit@123.456.% identified by 'bit'; |
| 사용자 제거                   | drop user {username};<br />drop user 'user'@'localhost';delete from user where user={username}; | •drop 추천                                                   |
| 권한 확인                     | show grants for {username}@{ip};                             | • show grants for bit@localhost;                             |
| 권한 부여                     | grant {권한} privileges on {스키마}.{테이블} to {username}@{ip}; | • grant all privileges on \*.\* to bit@localhost;            |
| 권한 제거                     | revoke {권한} privileges on {스키마}.{테이블} from {username}@{ip}; | • revoke all on bit.* from bit@localhost;                    |



## DATABASE 생성, 목록, 보기

| 기능              | 명령어                      | 사용 예                             |
| ----------------- | --------------------------- | ----------------------------------- |
| 데이터베이스 생성 | create database [database]; | • database 생성                     |
| 데이터베이스 선택 | use [database];             | • database 선택                     |
| 데이터베이스 보기 | show databases;             | • database 어떤 게 있는지 보여줌    |
| 테이블 보기       | show tables;                | • database 에 있는 테이블 보여준다. |



## Windows에서 Database 관리

* windows용 MySQL은 windows 재부팅시 자동 실행 된다. 윈도우 서비스를 통해 관리
* 윈도우 검색창에서는 services
* 실행창 (window + R) 에서는 services.msc 입력.

[참조](https://minhee0327.gitbook.io/mini-til/undefined/untitled)