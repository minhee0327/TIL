n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

# 꽃 a, b, c에 대한 최소 비용


def ck(lst):
    dx, dy = [0, 1, 0, -1, 0], [0, 0, 1, 0, -1]
    ret = 0
    ck = []

    for i in lst:
        x = i//n
        y = i % n

        if x == 0 or y == 0 or x == n-1 or y == n-1:
            return 10000

        for j in range(5):
            nx, ny = x + dx[j], y + dy[j]
            ck.append((nx, ny))
            ret += cost[nx][ny]
    if len(set(ck)) == 15:
        return ret
    return 10000


ans = 10000

for i in range(n*n):
    for j in range(n*n):
        for k in range(n*n):
            lst = [i, j, k]
            ans = min(ans, ck(lst))

print(ans)
