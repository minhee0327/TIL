def dfs(idx, v):
    global ans

    visited[idx] = 0

    v +=1
    if ans <v:
        ans = v

    for i in graph[idx]:
        if visited[i]:
            dfs(i, v)

    visited[idx] = 1 
    


for t in range(1, 1+int(input())):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    
    ans = 0
    visited = [1] * (N+1)

    for i in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1,N+1):
        dfs(i, 0)

    print("#{} {}".format(t, ans))