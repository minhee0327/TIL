def dfs(x, y, d_count):
    visited[x][y] = 1

    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        elif visited[nx][ny] == 0 and int(graph[nx][ny]) == 1:
            d_count = dfs(nx, ny, d_count+1)
    return d_count


N = int(input())
graph = [input() for _ in range(N)]
visited = [[0]*N for i in range(N)]


danji = []

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and int(graph[i][j]) == 1:
            danji.append(dfs(i, j, 1))

print(len(danji))
danji.sort()
for i in danji:
    print(i)


'''
문제 잘읽자...!
오름차순 정렬해서 출력하기!
(testcase는 sort()안해도 값이 오름차순이었던 testcase...ㅠㅠ)
'''
