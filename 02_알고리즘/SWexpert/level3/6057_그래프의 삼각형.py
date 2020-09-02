# BFS로
def findTri(graph, start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)

    while need_visit:

        node = need_visit.pop(0)

        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


for t in range(1, 1+int(input())):
    N, M = map(int, input().split())

    graph = [[] for _ in range(M+1)]
    tri = []
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, 1+N):
        temp = sorted(findTri(graph, i))

        if temp not in tri:
            tri.append(temp)

    print("#{} {}".format(t, len(tri)))

'''
내일 다시 풀어볼것... 뭔가 접근이 잘못된건지..
'''
