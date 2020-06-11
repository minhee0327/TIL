'''
try:
    시도할 코드
except 처리할 에러 as 에러메세지 변수:
    에러 발생시 실행코드
    관습적으로 에러메세지 변수 e 많이 사용
    # print(e)
else:
    에러 발생 안했을 때 실행 코드
finally:
    예외 발생 여부와 상관없이 무조건 실행하는 코드
    DB connection 이나 열린 파일등을 닫아야 할 때 close()를 해서 리소스 회수 해야할때 주로 사용

Class MyCustomError(Exception):
    def __str__(self):
        return "나만의 특별한 에러 처"
'''

