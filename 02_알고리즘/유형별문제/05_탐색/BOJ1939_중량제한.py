import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
island = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, W = map(int, sys.stdin.readline().split())
    island[A].append((B, W))
    island[B].append((A, W))

S, E = map(int, sys.stdin.readline().split())

min_v, max_v = 1, 1000000000  # 문제에서 가중치의 최소값은 1, 최대값은 1000000000이라 나옴.


def bfs(c):
    queue = deque()
    queue.append(S)
    visited = set()
    visited.add(S)
    while queue:
        x = queue.popleft()
        for y, w in island[x]:
            if y not in visited and w >= c:
                visited.add(y)
                queue.append(y)

    if E in visited:
        return True
    else:
        return False


# 최대로 가능한 것 찾기 (이분탐색)
result = min_v
while min_v <= max_v:
    mid = (min_v+max_v) // 2
    if bfs(mid):
        result = mid
        min_v = mid + 1
    else:
        max_v = mid - 1


print(result)
