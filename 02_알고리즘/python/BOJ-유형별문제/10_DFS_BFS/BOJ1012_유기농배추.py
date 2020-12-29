import sys
sys.setrecursionlimit(10000)


def dfs(x, y):
    visited[x][y] = 1
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if visited[nx][ny] == 0 and baechu[nx][ny]:
            dfs(nx, ny)


for _ in range(int(input())):
    M, N, K = map(int, input().split())
    baechu = [[0] * (M) for _ in range(N)]
    visited = [[0] * (M) for _ in range(N)]
    count = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        baechu[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and baechu[i][j]:
                dfs(i, j)
                count += 1
    print(count)


'''
1. import sys
2. syslsetrecusionlimit(10000)
'''
