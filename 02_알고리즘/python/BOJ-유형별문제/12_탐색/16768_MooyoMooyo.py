import sys
sys.setrecursionlimit(10000)


def check_array(N):
    return [[False for _ in range(10)]for i in range(N)]


N, K = map(int, input().split())

board = [list(input()) for i in range(N)]

ck1 = check_array(N)
ck2 = check_array(N)
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def countDFS(x, y):
    ck1[x][y] = True
    ret = 1

    for i in range(4):
        nx, ny = x + dx[i], y+dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= 10:
            continue
        elif ck1[nx][ny] or board[x][y] != board[nx][ny]:
            continue
        ret += countDFS(nx, ny)
    return ret


def removeDFS(x, y, num):
    ck2[x][y] = True
    board[x][y] = '0'

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= 10:
            continue
        elif ck2[nx][ny] or num != board[nx][ny]:
            continue
        removeDFS(nx, ny, num)


def down():
    for i in range(10):
        temp = []
        for j in range(N):
            if board[j][i] != '0':
                temp.append(board[j][i])
        for j in range(N-len(temp)):
            board[j][i] = '0'
        for j in range(N-len(temp), N):
            board[j][i] = temp[j-(N-len(temp))]


while True:
    exit = False
    ck1 = check_array(N)
    ck2 = check_array(N)

    for i in range(N):
        for j in range(10):
            if board[i][j] == '0' or ck1[i][j]:
                continue
            res = countDFS(i, j)
            if res >= K:
                removeDFS(i, j, board[i][j])
                exit = True

    # 제거할게 False이면, 없는상태라는거니까, while문 종료
    if not exit:
        break

    # 그게아니면, 내려주고 다시 반복
    down()

for i in board:
    print(''.join(i))


'''
[code Review]
1. 반복문을 탈출할때, ck, exit등 존재유무, 방문여부 등을 체크하는 변수를 두고 탈출하는 것을 자꾸 잊는다.
2. 위 방법을 사용하면 꽤나 많은 문제가 풀렸음에도, 자꾸 안쓰는건 연습부족.
3. 다시 한번 연습차원에서 보지 않고, MooyoMooyo_2.py로 작성해보기!
'''
