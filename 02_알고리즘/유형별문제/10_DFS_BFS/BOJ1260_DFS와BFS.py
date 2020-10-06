from collections import defaultdict


def bfs(graph, v):
    need_visit = []
    need_visit.append(v)
    while need_visit:
        node = need_visit.pop(0)
        if not (visited[node]):
            visited[node] = 1
            print(node, end=' ')
            for i in graph[node]:
                if not visited[i]:
                    need_visit.append(i)


def dfs(graph, v):
    print(v, end=' ')
    visited[v] = 1
    for i in graph[v]:
        if not(visited[i]):
            dfs(graph, i)


N, M, V = map(int, input().split())
graph = defaultdict(list)


for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in graph.values():
    i.sort()

visited = [0] * (N+1)
dfs(graph, V)
print()
visited = [0] * (N+1)
bfs(graph, V)


'''
[처음에 통과 못함 => 다른 코드 참조해가며 내 코드 개선]

1. 이미 방문한 노드를 방문하지 않도록 visited 배열(체크용) 을 두는 것을 고려하지 못했다.
2. 나는 list 형태 대신 dict()를 사용했다. [알고리즘 강의에서도 dict를 사용했기 때문에 이게 편했음]
3. dfs를 재귀적으로 사용하는 방법도 조금 새로웠다. 그동안 반복문으로 구현했어서
4. 또한 dfs를 기존에 내가 알던대로 구현했더니 다른 모양새로 나옴ㅠㅠ

[정리]
1. 방문 여부 check하는 배열을 만드는 것을 습관화 할것!
'''
