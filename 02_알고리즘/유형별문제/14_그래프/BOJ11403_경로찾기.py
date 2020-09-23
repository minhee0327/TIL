def isPossible(s, e):
    visited = []
    need_visit = []
    need_visit.append(s)

    while need_visit:
        v = need_visit.pop()
        visited.append(v)
        for w in graph[v]:
            if w == e:
                return True
            if w not in visited:
                need_visit.append(w)
    return False


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
graph = [[]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            graph[i].append(j)

for i in range(N):
    for j in range(N):
        if isPossible(i, j):
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0

for m in matrix:
    print(' '.join(map(str, m)))
