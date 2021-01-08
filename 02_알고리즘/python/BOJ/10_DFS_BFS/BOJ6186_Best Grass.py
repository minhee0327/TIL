def bfs(r, c):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    visited[r][c] == 1

    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if nx < 0 or ny < 0 or nx >= R or ny >= C or visited[nx][ny] or matrix[nx][ny] == ".":
            continue
        else:
            matrix[nx][ny] = "."


R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

cnt = 0
for i in range(R):
    for j in range(C):
        if visited[i][j] == 0 and matrix[i][j] == "#":
            bfs(i, j)
            cnt += 1

print(cnt)
