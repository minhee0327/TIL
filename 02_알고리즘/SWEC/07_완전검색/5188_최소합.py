def dfs(r, c):
    global ans, cnt
    dx, dy = [0, 1], [1, 0]

    if cnt > ans:
        return

    if r == (N-1) and c == (N-1):
        ans = min(ans, cnt)
        return

    for i in range(2):
        nx, ny = dx[i] + r, dy[i] + c
        if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny] == 1:
            continue
        else:
            visited[nx][ny] = 1
            cnt += board[nx][ny]
            dfs(nx, ny)
            visited[nx][ny] = 0
            cnt -= board[nx][ny]


for t in range(1, 1+int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # ans가 가능한 최대값
    ans = (2*N - 1) * 10
    cnt = board[0][0]
    visited[0][0] = 1

    dfs(0, 0)

    print("#{} {}".format(t, ans))
