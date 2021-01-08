from collections import deque


def dfs(x, y):
    visited[x][y] = 1
    dist[x][y] += 1
    q = deque()
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            elif visited[nx][ny] == 0 and int(graph[nx][ny]) == 1:
                dist[nx][ny] = dist[x][y]+1
                visited[nx][ny] = 1
                q.append((nx, ny))


N, M = map(int, input().split())
graph = [input() for i in range(N)]
visited = [[0] * (M)for i in range(N)]
dist = [[0] * (M)for i in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and int(graph[i][j]) == 1:
            dfs(i, j)

print(dist[N-1][M-1])
