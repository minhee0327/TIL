import sys
sys.setrecursionlimit(100000)


def dfs(r, c, graph):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        elif graph[nx][ny] == 0:
            graph[nx][ny] = 1
            dfs(nx, ny, graph)


N = int(input())
height = [list(map(int, input().split())) for _ in range(N)]
max_height = max([max(h)for h in height])
ans = 1

for h in range(1, max_height+1):
    graph = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if height[i][j] <= h:
                graph[i][j] = 1

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                dfs(i, j, graph)
                cnt += 1
    ans = max(ans, cnt)

print(ans)


'''
[틀렸던 이유 분석]
1. 처음에 런타임 오류에 걸렸다. => BOJ에서 런타임이 나는 이유를 찾아서 정리함.(유형별 문제 README.md 에 정리하겠음)
2. 가장 의심이 간건, 재귀깊이랑 ans를 처음에 부등호로 나타낸것
3. 재귀깊이먼저 제한을 두었지만, 틀렸다고 떠서 부등호 표현에 잘못된 것 같아 max함수로 마지막에 ans를 구했다.
4. 부등호 사용하면서 등호를 제대로 사용하지 않아 틀렸었던 것으로 예측.

[문제 접근]
1. 일단 각 빌딩의 높이를 heigh배열에 담은후, 그 중 가장 높은 높이를 구했다.(max_height)
2. 비가 하나도 오지 않았을 경우에는 다 촉촉한(?)상태니까 ans의 초기값을 1로 설정했다. 
3. 그리고 비가 1만큼왔을때부터~ max_height만큼 왔을때까지 임시 그래프를 생성해서 비가 젖은곳을 체크하려고 했다.
4. 그래서 배열의 크기만큼 돌면서 3번에서 나온 비의 높이까지 젖은 곳을 graph에 체크(1)했다.
5. 그 후, 그 그래프를 돌면서 안젖은곳(0)을 dfs로 돌면서 1로 바꿔주었고, 안젖은 곳을 찾았을 때마다 cnt값을 한번씩 증가해주었다.
6. 마지막으로 ans와 cnt를 비교해서 큰값을 업데이트 해나감
'''
