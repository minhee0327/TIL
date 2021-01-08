M = [[0] * 101 for _ in range(101)]
for i in range(4):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(lx, rx):
        for j in range(ly, ry):
            M[i][j] = 1

ans = 0
for i in range(101):
    for j in range(101):
        if M[i][j] == 1:
            ans += 1


print(ans)
