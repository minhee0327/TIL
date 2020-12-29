def findEnd(r, c):
    # print(r, c)
    global ans
    visited[r][c] = 1
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(4):
        nx, ny = dx[i] + r, dy[i] + c
        if miro[nx][ny] == '3':
            ans = 1
            return
        if nx < 0 or ny < 0 or nx >= 16 or ny >= 16 or miro[nx][ny] == '1' or visited[nx][ny]:
            continue
        else:
            findEnd(nx, ny)


for _ in range(10):
    t = int(input())
    miro = [list(input()) for t in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    ans = 0
    # print(miro)

    for i in range(16):
        for j in range(16):
            if miro[i][j] == '2':
                findEnd(i, j)

    print("#{} {}".format(t, ans))
