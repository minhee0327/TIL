# import sys
# sys.setrecursionlimit(10000)
# 재귀 깊이 제한 두는 라이브러리인데, swea에서 제공되지 않는 라이브러리라고해서 제외.

def bfs(r, c, cnt):
    global ans
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    # print(r, c, cnt)
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N or graph[nx][ny] == '1':
            continue
        if graph[nx][ny] == '0' and ck[nx][ny] == 0:
            ck[nx][ny] = 1
            bfs(nx, ny, cnt+1)
        if graph[nx][ny] == '3':
            ans = cnt


for t in range(1, 1+int(input())):
    N = int(input())
    graph = [list(input()) for _ in range(N)]
    ck = [[0] * (N) for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] == '2':
                ck[i][j] = 1
                bfs(i, j, 0)
    print("#{} {}".format(t, ans))
