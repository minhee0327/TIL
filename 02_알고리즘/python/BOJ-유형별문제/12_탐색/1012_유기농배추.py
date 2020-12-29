import sys
sys.setrecursionlimit(10000)


def dfs(r, c):
    ck[r][c] = 1
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if ck[nx][ny] == 0 and ground[nx][ny]:
            dfs(nx, ny)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    ground = [[0]*m for _ in range(n)]

    for i in range(k):
        r, c = map(int, input().split())
        ground[c][r] = 1

    ck = [[0]*m for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if ck[i][j] == 0 and ground[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)
