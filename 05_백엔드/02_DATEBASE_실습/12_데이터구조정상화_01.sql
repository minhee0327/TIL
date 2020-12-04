-- 00. 데이터 확인public int[][] solution(int[][] arr1, int[][] arr2) {


        int row = arr1[0].length;
        int col = arr1.length ;

        int[][] answer = new int[col][row];

        for(int i =0; i< col;i++ ) {
            for(int j=0; j< row;j++) {
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }

        return answer;
    }
SELECT * FROM movie;
SELECT * FROM users;
SELECT * FROM rating;


-- 01. 식별자 찾기
SELECT * FROM information_schema.COLUMNS c WHERE c.table_name = 'movie'; 

-- movie table column list ---> movieID, title_nm, genres_nm

-- 아무것도 출력 안됨 => 식별자임을 유추가능
SELECT movieid, count(*) cnt 
FROM movie m 
GROUP BY movieid
HAVING count(*) > 1;

-- 아무것도 출력이 안되기는 하지만, name은 변경의 여지가 있기 때문에 식별자가 아닐 가능성 있음
SELECT title_nm, count(*) cnt 
FROM movie m 
GROUP BY title_nm
HAVING count(*) > 1;

-- 아무것도 출력되면 안되는데 출력됨. => 식별자가 될 수 없음
SELECT genres_nm , count(*) cnt 
FROM movie m 
GROUP BY genres_nm
HAVING count(*) > 1;

-- 전체 컬럼, 중복이 없어야함
SELECT movieid, title_nm, genres_nm, count(*) cnt
FROM movie m
GROUP BY movieid, title_nm, genres_nm 
HAVING count(*)>1;









-- users 테이블 확인 (pk: user_id)
SELECT * FROM information_schema.COLUMNS c WHERE c.table_name = 'users';
-- userid, gender, age, occupation, zip_code

SELECT userid , count(*) cnt 
FROM users u 
GROUP BY userid
HAVING count(*) > 1;

SELECT gender , count(*) cnt 
FROM users u 
GROUP BY gender
HAVING count(*) > 1;

SELECT age , count(*) cnt 
FROM users u 
GROUP BY age
HAVING count(*) > 1;

SELECT occupation , count(*) cnt 
FROM users u 
GROUP BY occupation
HAVING count(*) > 1;




-- rating의 식별자는 user_id, movieid임을 유추할수 있다.
SELECT * FROM information_schema.COLUMNS c WHERE c.table_name = 'rating';
-- movieid, userid, rating_pnt, timestamp

SELECT movieid , count(*) cnt 
FROM rating
GROUP BY movieid
HAVING count(*) > 1;

SELECT userid , count(*) cnt 
FROM rating
GROUP BY userid
HAVING count(*) > 1;

SELECT rating_pnt , count(*) cnt 
FROM rating
GROUP BY rating_pnt
HAVING count(*) > 1;

SELECT timestamp , count(*) cnt 
FROM rating
GROUP BY timestamp
HAVING count(*) > 1;

-- 한 건도 나오지 않음. 한 user가 한번 이상의 평가는 불가능함을 알 수 있다.
SELECT userid, movieid , count(*) cnt 
FROM rating
GROUP BY userid, movieid 
HAVING count(*) > 1;
