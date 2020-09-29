M = [[0] * 101 for _ in range(101)]
N = int(input())

for n in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        for j in range(y, y+h):
            M[i][j] = n

for i in range(1, N+1):
    cnt = 0
    for j in range(101):
        for k in range(101):
            if M[j][k] == i:
                cnt += 1
    print(cnt)
