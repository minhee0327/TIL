R, C = map(int, input().split())

ground = [[i for i in input()] for _ in range(R)]


def findwolf(r, c):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue
        else:
            if ground[nx][ny] == 'W':
                return True
            elif ground[nx][ny] == '.':
                ground[nx][ny] = 'D'


for i in range(R):
    for j in range(C):
        if ground[i][j] == 'S':
            if findwolf(i, j):
                print(0)
                exit(0)

print(1)

for i in ground:
    print(''.join(i))

'''
[코드리뷰]
- ㅎ.. 1시간이 넘게 풀었는데 계속 틀려서 이상하다 싶었는데..
- 출력에 ' '로 띄어쓰기를 해서.. 계속 틀리게 채점됬다..ㅎ...
- 나는 양을 기준으로 늑대를 만나면, 0을 출력하고 프로그램이 종료되도록 했고
- 그게 아니라면 방어를 하는 방식으로 코드를 짰다..
- 출력에서 error인지 모르고 온갖 방법을 썼다..(왜인지 억울하다...한시간..후... 출력도 잘 보자!)
'''
