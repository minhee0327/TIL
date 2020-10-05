import sys

N = int(sys.stdin.readline())
switch = [-1] + list(map(int, sys.stdin.readline().split()))

# 학생수만큼 반복해서, 성별과 스위치의 번호를 받음.
for _ in range(int(sys.stdin.readline())):
    S, num = map(int, sys.stdin.readline().split())
    # 성별 남
    if S == 1:
        for i in range(num, N, num):
            switch[i] = (switch[i] + 1) % 2

    # 성별 여
    elif S == 2:
        start, end = num, num
        while start > 0 and end < N:
            if switch[start] == switch[end]:
                start -= 1
                end += 1
        for i in range(start+1, end):
            switch[i] = (switch[i] + 1) % 2


for i in range(1, len(switch), 20):
    print(' '.join(map(str, switch[i:i+20])))

'''
- 시간초과;; 
- 내일 시간초과나는 문제들 모두 수정하겠음
'''
