from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
adj = [[]for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[b].append(a)


def bfs(v):
    q = deque([v])
    visited = [0] * (n+1)
    visited[v] = 1
    count = 1

    while q:
        v = q.popleft()
        for i in adj[v]:
            if not visited[i]:
                q.append(i)
                count += 1
                visited[i] = True
    return count


result = []
max_val = -1

for i in range(1, n+1):
    c = bfs(i)
    if c > max_val:
        result = [i]
        max_val = c
    elif c == max_val:
        result.append(i)
        max_val = c

for i in result:
    print(i, end=" ")
