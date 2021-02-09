# Built in function

- Built in function : DBMS가 제공하는 내장함수
- 자주 사용했던 것들 mysql 공식문서에서 요약 정리

### [숫자 함수](https://dev.mysql.com/doc/refman/8.0/en/numeric-functions.html)

| 함수명       | 기능                                                      |
| ------------ | -------------------------------------------------- |
| `CEIL()`     | 인수보다 작지 않은 가장 작은 정수 값을 반환합니다. (올림) |
| `FLOOR()`    | 인수보다 크지 않은 가장 큰 정수 값을 반환합니다. (내림)   |
| `MOD()`      | 나머지 반환                                               |
| `POW()`      | 지정된 거듭 제곱으로 제기 된 인수를 반환합니다.           |
| `POWER()`    | 지정된 거듭 제곱으로 제기 된 인수를 반환합니다.           |
| `ROUND()`    | 반올림                                                    |
| `SIGN()` | 인수의 부호를 반환 |
| `SQRT()` | 인수의 제곱근을 반환합니다. |
| `TRUNCATE()` | 지정된 소수 자릿수로 자릅니다. |
| `ABS()` | 절댓값 |



### [문자 함수](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html)

| 함수명                                                       | 기능                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| [`CONCAT()`](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_concat) | 연결된 문자열 반환                                      |
| [`LOWER()`](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_lower) | 인수를 소문자로 반환                                    |
| [`LPAD()`](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_lpad) | 지정된 문자열로 왼쪽이 채워진 문자열 인수를 반환합니다. |
| [`REGEXP`](https://dev.mysql.com/doc/refman/8.0/en/regexp.html#operator_regexp) | 문자열이 정규식과 일치하는지 여부                       |
| [`REPEAT()`](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_repeat) | 지정된 횟수만큼 문자열 반복                             |
| [`REPLACE()`](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_replace) | 지정된 문자열의 항목 바꾸기                             |
| [`REVERSE()`](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_reverse) | 문자열의 문자 반전                                      |
| [`SUBSTR()`](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_substr) | 지정된 부분 문자열을 반환합니다.                        |
| [`TRIM()`](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_trim) | 선행 및 후행 공백 제거                                  |
| [`CHAR_LENGTH(`str`)`](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_char-length) | 문자열의 문자 수를 반환                                 |
| [`LENGTH(`str`)`](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_length) | 바이트 단위로 측정된 문자열의 길이 반환                 |





### [날짜 및 시간 함수](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html)

* 단순 문자열로 저장 관리 할수도 있겠지만, 날짜형 데이터로 저장하여 관리하면, 날짜 더하거나 차이를 구하는 등의 날짜만의 연산 손쉽게 처리 가능
* format: 날짜, 시간 함수에서 날짜와 시간 부분을 나타내는 인수 표기 (%Y, %m, %d,..)
* 날짜형 데이터를 가진 열을 대상으로 연산 수행
* 문자형 (char, varchar) 데이터와 날짜형 데이터간 연산 수행시에는 date_format, str_to_date함수로 데이터형 상호 변환하여 수행

| 함수명                                                       | 기능                                                  |
| ------------------------------------------------------------ | ----------------------------------------------------- |
| [`ADDDATE(date, interval)`](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_adddate) | 날짜 값에 시간 값 (간격, interval) 추가               |
| [`STR_TO_DATE()`](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_str-to-date) | 문자열 데이터를 날짜로 변환                           |
| [`DATE_FORMAT()`](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date-format) | 지정된 날짜 형식 (날짜형 데이터를 문자열로)           |
| [`DATE()`](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date) | 날짜 또는 datetime 식의 날짜 부분 추출 ('2020-02-09') |
| [`DATE_SUB()`](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date-sub) | 날짜에서 시간 값 (간격) 빼기                          |
| [`DATEDIFF()`](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_datediff) | 두 날짜 빼기                                          |







### NULL 값 처리

* 지정되지 않은 값
* 값을 알 수도 없고, 적용할 수도 없다. ('', ' ', '0'과는 다른 특별한 값)
* 비교 연산자로 비교 불가능 
* **NULL 값에 대한 연산과 집계함수**
  * NULL+숫자 연산의 결과는 NULL
  * 집계함수 계산시 NULL이 포함된 행은 집계에서 빠진다.
  * 해당 되는 행이 하나도 없을 경우, sum, avg함수 결과는 null이 되고, count함수의 결과는 0이다.

* **NULL 값을 확인하는 방법 (IS NULL, IS NOT NULL)**
  * NULL값 찾을 때는 '=' 가 아니라 IS NULL
  * NULL이 아닌 값을 찾을 때는 '<>'가 아니라 IS NOT NULL

* **IFNULL** : NULL 값을 다른 값으로 대치하여 연산하거나, 다른 값으로 출력하는 함수.





### 행번호 출력

* MySQL에서 변수를 사용하여 처리하는 방법 ([Programmers 참조](https://github.com/minhee0327/Algorithm/blob/master/SQL/Programmers/level4.md#2-%EC%9E%85%EC%96%91%EC%8B%9C%EA%B0%81-%EA%B5%AC%ED%95%98%EA%B8%B0-2) )

* 변수는 이름 앞에 @ 기호를 붙이며, 치환문에는 SET과 := 기호를 사용한다.

  ```sql
  set @seq:=0;
  
  select (@seq:=@seq+1)'순번', custid, name, phone
  from customer
  where @seq<2;
  ```

---

참조: mysql 공식문서



