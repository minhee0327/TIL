def dfs(row):
    global ans, cnt

    if row >= N:
        if ans > cnt:
            ans = cnt
            return

    if ans < cnt:
        return

    for i in range(N):
        if not visited[i]:
            cnt += V[row][i]
            visited[i] = 1
            dfs(row+1)
            visited[i] = 0
            cnt -= V[row][i]


for t in range(1, 1+int(input())):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    ans = 99 * 15 * 15
    cnt = 0
    visited = [0] * N

    for i in range(N):
        visited[i] = 1
        cnt += V[0][i]
        dfs(1)
        cnt -= V[0][i]
        visited[i] = 0

    print("#{} {}".format(t, ans))
