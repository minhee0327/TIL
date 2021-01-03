import sys
sys.setrecursionlimit(10000000)


def dfs(r, c, cnt):
    visited[r][c] = 1
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                cnt = dfs(nx, ny, cnt+1)
    return cnt


M, N, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for n in range(lx, rx):
        for m in range(ly, ry):
            graph[n][m] = 1

    # print(graph)

res = []
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and graph[i][j] == 0:
            res.append(dfs(i, j, 1))

print(len(res))
res = sorted(res)
print(" ".join(map(str, res)))

'''
[Code Review]
1. 주어진 배열이 왼쪽으로 90도 돌려진 상태라는걸 인지하는게 늦었다.
2. 그래서 오른쪽으로 90도 회전했다고 생각하고 graph를 받았다.
3. lx, ly, rx, ry도 마찬가지로 90도 오른쪽으로 돌아갔다고 생각해보면 어느 구간이 1이되어있는지 찾기 수월했다.
    3.1 lx ~rx가 row, ly, ry가 col이라고 생각하고 풀었음 (+ N이 row, M이 col이라고 생각함)
4. (개인적으로) 3번까지 생각하는게 가장 어려웠던것 같고, 나머지는 dfs 평상시 구현하던대로 구현을 했음.
5. 단지번호 붙이기(BOJ2667문제)와 비슷한 형태여서 금방 구현을 했는데, 문제는 재귀깊이에 걸렸는지, 런타임에러가 남.
6. 이럴 경우 반복문으로 구현해봤어도 좋았을 것 같은데, 일단 구현을 해둔게 있으니, setrecursivelimit을 걸어줘봄.
7. 통과가 가능했음.
'''
