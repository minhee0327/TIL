def dfs(n):
    global ans
    global cnt

    if cnt < ans:
        visited[n] = 1

        if len(set(visited)) == 1 and visited[0]:
            cnt += e[n][0]
            if cnt < ans:
                ans = cnt
            cnt -= e[n][0]
        else:
            for i in range(N):
                if visited[i] == 0:
                    cnt += e[n][i]
                    dfs(i)
                    cnt -= e[n][i]

        visited[n] = 0


for t in range(1, 1 + int(input())):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 100 * 3
    cnt = 0

    dfs(0)

    print("#{} {}".format(t, ans))
