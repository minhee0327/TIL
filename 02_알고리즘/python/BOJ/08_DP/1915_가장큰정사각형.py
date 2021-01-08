n, m = map(int, input().split())
arr = [[0 for _ in range(m+1)] for i in range(n+1)]
DP = [[0 for _ in range(m+1)] for i in range(n+1)]
ans = 0

for i in range(n):
    for idx, j in enumerate(list(map(int, list(input())))):
        arr[i+1][idx+1] = j

for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i][j]:
            DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1])+1
            ans = max(ans, DP[i][j])


print(ans**2)
