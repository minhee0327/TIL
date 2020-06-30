N, M = map(int, input().split())
A, B = input().split()

alpha = {
    1: ['C', 'G', 'I', 'J', 'L', 'O', 'S', 'U', 'V', 'W', 'Z'],
    2: ['B', 'D', 'N', 'P', 'Q', 'R', 'T', 'X', 'Y'],
    3: ['A', 'F', 'H', 'K', 'M'],
    4: ['E']}

voca = ''
for i in range(min(N, M)):
    voca += A[i] + B[i]

if N < M:
    voca += B[N:]
elif N > M:
    voca += A[M:]

# print(voca)
score = []

for i in voca:
    for k, v in alpha.items():
        if i in v:
            score.append(k)

while True:
    if len(score) == 2:
        if score[0] == 0:
            print(str(score[1])+'%')
        else:
            print(str(score[0])+str(score[1])+'%')
        exit(0)

    for i in range(1, len(score)):
        if score[i-1] + score[i] >= 10:
            score[i-1] = (score[i-1] + score[i]) % 10
        else:
            score[i-1] = (score[i-1] + score[i])
    score.pop()

'''
1. 예전에 풀었을때보다 속도를 훨씬 줄일 수 있었다.
    - 일단, 되도록 append를 안쓰고 할수있는 방법을 생각했다.
    - dict도 같은값 끼리 묶어서 표현했다.
    - 10보다 큰 경우 빼기 연산말고 나머지 연산했다.
    - 결과값을 저장할때 새로 deepcopy를 하지 않고, 기존 배열에 담고 필요없는 것을 pop()해나갔다.

2. 출력은 format을 사용하는게 좀더 clean한 것 같다.
    - 예: print("{}%".format(score[0]*10 + score[1]))

3. ord()를 사용할 생각은 못했는데, 이 부분은 별도로 한번 더 구현해봐야할 것 같다.
'''
