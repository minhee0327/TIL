from queue import deque


def bfs(p1, p2):
    cnt = 0
    need_visit = deque([[p1, cnt]])

    while need_visit:
        current = need_visit.popleft()
        p = current[0]
        cnt = current[1]

        if p == p2:
            return cnt
        if not visited[p]:
            cnt += 1
            visited[p] = 1

            for i in relative[p]:
                if not visited[i]:
                    need_visit.append([i, cnt])

    return -1


n = int(input())
p1, p2 = map(int, input().split())
relative = [[] for _ in range(n+1)]
visited = [0] * (n+1)

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    relative[x].append(y)
    relative[y].append(x)

print(bfs(p1, p2))

'''
- 촌수를 따지면서, 같은 level에 있는 촌수를 고려하기 위해서 2차원배열로 deque를 만들었다.
- 이를 고려하지 않으면 같은 촌수를 다 포함시킨 cnt값이 나와서 이걸 해결하는 것을 생각하는게 오래걸림
'''
