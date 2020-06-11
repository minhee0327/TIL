'''
1. open(파일이 존재하는 경로와 파일명, 모드, 인코딩)

- 모드: 파일이 열릴 때, 작업하고자 하는 모드로 열어줘야한다.
   - 당연히 작업하고자 하는 모드와 맞지 않는 작업을 하려하면 에러발생
   - 모드 종류
        - r: 읽기모드 (default)
        - w: 쓰기모드
        - x: 쓰기 전용
        - a: 추가모드
    - 모드 advanced
        - +: 갱신모드
        - t: text type
        - b: 이진데이터 타입

- f.close()
    - 파일을 닺지 않고 계속 프로그램 진행하면, 파일 연채로 다른 작업하는 것과 동일
    - 쓰지 않는 파일을 계속 열어두면, 메모리 잡아먹음 ㅠ3ㅠ

    - with라는 예약어를 통해 리소스를 쉽게 회수 할 수 있다. (example05에)
        - context menager
        - f.close 대신 사용
'''
f = open("some.txt",'w')
for i in range(1, 9+1):
    data = "5 *{} = {}\n".format(i,5*i)
    f.write(data)
f.close()