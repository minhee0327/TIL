import sys
sys.setrecursionlimit(10000)


def dfs(v):
    check[v] = 1

    for g in graph[v]:
        if not check[g]:
            dfs(g)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
check = [0 for _ in range(N+1)]
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, N+1):
    if not check[i]:
        dfs(i)
        cnt += 1

print(cnt)

'''
[문제]
- 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성

[입력]
- 정점의 개수 N과 간선의 개수 M((1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2))
-  M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어짐

[출력]
- 연결요소의 갯수?
'''
