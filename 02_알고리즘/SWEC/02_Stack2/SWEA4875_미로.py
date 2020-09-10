def func(r, c):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    global ans

    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N or graph[nx][ny] == '1':
            continue

        if graph[nx][ny] == '0' and ck[nx][ny] == 0:
            ck[nx][ny] = 1
            func(nx, ny)

        if graph[nx][ny] == '3':
            ans = 1


for t in range(1, 1+int(input())):
    N = int(input())
    graph = [list(input()) for _ in range(N)]
    ck = [[0] * (N) for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] == '2':
                ck[i][j] = 1
                func(i, j)

    print("#{} {}".format(t, ans))
