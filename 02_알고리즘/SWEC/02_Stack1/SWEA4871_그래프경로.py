def dfs(s, e):
    visited, need_visit = [], []
    need_visit.append(s)

    while need_visit:
        node = need_visit.pop()
        if node == e:
            return 1
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return 0


for t in range(1, 1 + int(input())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)

    start, end = map(int, input().split())

    print("#{} {}".format(t, dfs(start, end)))
