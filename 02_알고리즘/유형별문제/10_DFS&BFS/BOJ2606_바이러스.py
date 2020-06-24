def bfs(v):  # v: start_node
    need_visit, visited = [], []
    need_visit.append(v)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return len(visited) - 1


vertext = int(input())
edge = int(input())
graph = [[] for _ in range(vertext+1)]

for i in range(edge):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(bfs(1))
