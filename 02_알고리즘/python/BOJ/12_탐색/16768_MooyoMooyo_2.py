import sys
sys.setrecursionlimit(10000)


def check_array(N):
    return [[False for _ in range(10)] for i in range(N)]


N, K = map(int, input().split())
B = [list(input()) for i in range(N)]

ck1 = check_array(N)
ck2 = check_array(N)

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def findDFS(x, y):
    ck1[x][y] = True
    ret = 1

    for i in range(4):
        nx, ny = dx[i]+x, dy[i]+y
        if nx < 0 or ny < 0 or nx >= N or ny >= 10:
            continue
        elif ck1[nx][ny] or B[x][y] != B[nx][ny]:
            continue
        ret += findDFS(nx, ny)
    return ret


def removeDFS(x, y, num):
    ck2[x][y] = True
    B[x][y] = '0'

    for i in range(4):
        nx, ny = dx[i]+x, dy[i]+y
        if nx < 0 or ny < 0 or nx >= N or ny >= 10:
            continue
        elif ck2[nx][ny] or num != B[nx][ny]:
            continue
        removeDFS(nx, ny, num)


def down():
    for i in range(10):
        temp = []
        for j in range(N):
            if B[j][i] != '0':
                temp.append(B[j][i])
        for j in range(N-len(temp)):
            B[j][i] = '0'
        for j in range(N-len(temp), N):
            B[j][i] = temp[j-(N-len(temp))]


while True:
    exit = False

    ck1 = check_array(N)
    ck2 = check_array(N)

    for i in range(N):
        for j in range(10):
            if ck1[i][j] or B[i][j] == '0':
                continue
            res = findDFS(i, j)
            if res >= K:
                removeDFS(i, j, B[i][j])
                exit = True

    if not exit:
        break

    down()

for i in B:
    print(''.join(i))
