import sys
sys.setrecursionlimit(10000)


def dfs(r, c, rgb):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    visited[r][c] = 1

    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny] or matrix[nx][ny] != rgb:
            continue
        elif matrix[nx][ny] == rgb:
            dfs(nx, ny, rgb)


N = int(input())
matrix = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
# rgb_cnt: 적록색약 아닌사람, rb_cnt: 적록색약인사람 수
rgb_cnt, rb_cnt = 0, 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j, matrix[i][j])
            rgb_cnt += 1

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'G':
            matrix[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j, matrix[i][j])
            rb_cnt += 1
print(rgb_cnt, rb_cnt)

'''
- 런타임 에러가 잡혀서 예전에 정리해둔 런타임 오류이유를 참조했다. (https://bit.ly/3ix4NFh)
- 그중 가장 의심이 간건 dfs를 돌면서 재귀깊이가 깊어진것같아서, setrecursionlimit을 주어 해결하였다.
- 다른 로직은 기존의 dfs유형과 크게 다르지 않은 것 같다.
'''
