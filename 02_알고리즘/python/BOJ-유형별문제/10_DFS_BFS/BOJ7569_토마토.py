from collections import deque


def bfs():
    while queue:
        x, y, z = queue.popleft()
        visited[z][x][y] = 1
        dx, dy, dz = [1, -1, 0, 0, 0, 0], [0,
                                           0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if nx >= N or ny >= M or nz >= H or nx < 0 or ny < 0 or nz < 0:
                continue
            if tomato[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                queue.append((nx, ny, nz))
                tomato[nz][nx][ny] = tomato[z][x][y]+1
                visited[nz][nx][ny] = 1


M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for i in range(N)]
          for _ in range(H)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

queue = deque()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[h][i][j] == 1:
                queue.append((i, j, h))
bfs()

ck = False
result = -2

for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[z][y][x] == 0:
                ck = True
            result = max(result, tomato[z][y][x])

if ck == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)

# print(tomato)
