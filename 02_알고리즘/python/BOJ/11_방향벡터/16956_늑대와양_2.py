R, C = map(int, input().split())

M = [list(input()) for _ in range(R)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

ck = False
for i in range(R):
    for j in range(C):
        if M[i][j] == 'W':
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue
                else:
                    if M[nx][ny] == 'S':
                        ck = True

if ck:
    print(0)
else:
    print(1)
    for i in range(R):
        for j in range(C):
            if M[i][j] not in 'SW':
                M[i][j] = 'D'

    for i in M:
        print(''.join(i))
