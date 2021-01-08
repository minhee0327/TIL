import sys
sys.setrecursionlimit(10000)


def bfs(r, c):
    visited[r][c] = 1
    dx, dy = [0, 1, 0, -1, 1, 1, -1, -1], [1, 0, -1, 0, 1, -1, 1, -1]

    for i in range(8):
        nx, ny = r + dx[i], c + dy[i]
        if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and info[nx][ny]:
            bfs(nx, ny)


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    info = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    cnt = 0

    for i in range(h):
        for j in range(w):
            if info[i][j] and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)
