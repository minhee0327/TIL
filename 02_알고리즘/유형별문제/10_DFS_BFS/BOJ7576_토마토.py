from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx >= N or ny >= M or nx < 0 or ny < 0:
                continue
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y]+1
                queue.append((nx, ny))


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for i in range(N)]

queue = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))
bfs()

ck = False
result = -2

for i in tomato:
    for j in i:
        if j == 0:
            ck = True
        result = max(result, j)

# 0 이 남은 경우
if ck == True:
    print(-1)
# 통이 모두 비어있는 경우
elif result == -1:
    print(0)
else:
    print(result-1)

# print(tomato)
