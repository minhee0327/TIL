N, M = map(int, input().split())
B = [list(map(int, input().split())) for i in range(N)]
DP = [[0 for i in range(M+1)] for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + B[i-1][j-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[i-1][y] - DP[x][j-1] + DP[i-1][j-1])
