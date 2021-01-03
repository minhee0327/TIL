from queue import deque


def dfs():
    q = deque()
    q.append(1)
    ret = {}
    visited = [0 for _ in range(N+1)]

    while q:
        n = q.pop()
        for i in tree[n]:
            if not visited[i]:
                ret[i] = n
                q.append(i)
                visited[i] = 1

    return ret


N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

ans = dfs()

for i in range(2, N+1):
    print(ans[i])
