def check(N, candy):
    for i in range(N):
        if candy[i] % 2 == 1:
            candy[i] += 1
    return len(set(candy)) == 1


def teacher(N, candy):
    temp = [0 for i in range(N)]
    for idx in range(N):
        if candy[idx] % 2:
            candy[idx] += 1
        candy[idx] //= 2
        temp[(idx+1) % N] = candy[idx]

    for idx in range(N):
        candy[idx] += temp[idx]

    return candy


def process():
    N, candy = int(input()), list(map(int, input().split()))
    cnt = 0

    while not check(N, candy):
        cnt += 1
        candy = teacher(N, candy)
    print(cnt)


for _ in range(int(input())):
    process()

'''
[Code Review]
- 내가 구현한것을 함수로 나눈것과 유사하다고 생각한다.
- 문제가 만약 더 커진다면 이렇게 구조화하는게 나중에 구조화된 단위로 끊어 생각하기 좋을것같다.
- 아직 초보자라 선뜻 바로 함수로 구현을 잘 못한다 생각하지 말고 지금부터 조금씩 연습하자.
'''
