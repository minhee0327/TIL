N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visitied = [[0]*M for _ in range(N)]
virus_pos = []                              # virus position
safe = -3                                   # 벽 3개 제외한 가능한 경우를 구하기 위한 변수
# 바이러스가 퍼질수 있는 최대개수(N*M = 64, 편의상 100으로)
virus = 100


def bfs(x, y):
    res = 1
    visitied[x][y] = 1
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if not visitied[nx][ny] and not matrix[nx][ny]:
            res += bfs(nx, ny)

    return res


def countWall(wall, x, y):
    global virus, visitied
    if wall == 3:
        cnt = 0
        visitied = [[0]*M for _ in range(N)]
        for i, j in virus_pos:
            cnt += bfs(i, j)
        virus = min(cnt, virus)
        return

    for i in range(x, N):
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k, M):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                countWall(wall+1, i, j+1)
                matrix[i][j] = 0


for i in range(N):
    for j in range(M):
        if matrix[i][j] != 1:
            safe += 1
        if matrix[i][j] == 2:
            virus_pos.append((i, j))

countWall(0, 0, 0)                            # 1. 첫번째로 할 일은 벽을 3개 세워보는것
print(safe - virus)
