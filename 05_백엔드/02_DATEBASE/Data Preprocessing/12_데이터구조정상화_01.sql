-- 00. ������ Ȯ��public int[][] solution(int[][] arr1, int[][] arr2) {


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


-- 01. �ĺ��� ã��
SELECT * FROM information_schema.COLUMNS c WHERE c.table_name = 'movie'; 

-- movie table column list ---> movieID, title_nm, genres_nm

-- �ƹ��͵� ��� �ȵ� => �ĺ������� ���߰���
SELECT movieid, count(*) cnt 
FROM movie m 
GROUP BY movieid
HAVING count(*) > 1;

-- �ƹ��͵� ����� �ȵǱ�� ������, name�� ������ ������ �ֱ� ������ �ĺ��ڰ� �ƴ� ���ɼ� ����
SELECT title_nm, count(*) cnt 
FROM movie m 
GROUP BY title_nm
HAVING count(*) > 1;

-- �ƹ��͵� ��µǸ� �ȵǴµ� ��µ�. => �ĺ��ڰ� �� �� ����
SELECT genres_nm , count(*) cnt 
FROM movie m 
GROUP BY genres_nm
HAVING count(*) > 1;

-- ��ü �÷�, �ߺ��� �������
SELECT movieid, title_nm, genres_nm, count(*) cnt
FROM movie m
GROUP BY movieid, title_nm, genres_nm 
HAVING count(*)>1;









-- users ���̺� Ȯ�� (pk: user_id)
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




-- rating�� �ĺ��ڴ� user_id, movieid���� �����Ҽ� �ִ�.
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

-- �� �ǵ� ������ ����. �� user�� �ѹ� �̻��� �򰡴� �Ұ������� �� �� �ִ�.
SELECT userid, movieid , count(*) cnt 
FROM rating
GROUP BY userid, movieid 
HAVING count(*) > 1;
