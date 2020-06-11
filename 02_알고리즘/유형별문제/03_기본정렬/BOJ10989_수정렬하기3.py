import sys

N = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(N):
    arr[int(sys.stdin.readline())] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)

'''
1. 또 똑같이 해서 틀림 ㅠㅠ 
2. 일단 메모리, 시간 관련된 문제는 import sys 하자.
3. 문제에 조건: 이 수는 10000 보다 작거나 같은 수!!! 큰 힌트를 그냥 넘겼음 ㅠㅠ
4. 문제 핵심: 
    4.1 내장함수 sort()쓰지 않고, 이미 선언한 배열에 해당값이 몇번 있었는지 count해두었다가,
    4.2 10000번만큼 돌면서 확인하기
'''
