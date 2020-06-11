'''
텍스트 파일을 읽어들이는 방법은 다양하다
1. 전체를 읽어 들이기
2. 줄 단위로 읽기
3. 반복문을 사용하여 읽기
'''

# 3. 반복문을 사용하여 읽기
# 텍스트 파일의 모든 라인을 읽어서, 줄 단위로 요소를 가지는 리스트로 반환
# 그 리스트를 반복문을 통해 읽음.

f = open("some.txt","r")
while True:
    data = f.readlines()
    f.close()
    for line in data:
        print(line, end="")