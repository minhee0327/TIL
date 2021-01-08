'''
텍스트 파일을 읽어들이는 방법은 다양하다
1. 전체를 읽어 들이기
2. 줄 단위로 읽기
3. 반복문을 사용하여 읽기
'''

# 2. 줄단위로 읽기
# readline() 함수를 통해 텍스트 파일을 한줄 씩 읽을 수 있다.
# readline() 함수는 더이상 읽을 줄이 없으면 None 을 반환!
# 조건문을 사용하여 while 문 탈출

f = open("some.txt","r")
while True:
    data = f.readline()
    if not data:
        break
    print(data, end="")
f.close()