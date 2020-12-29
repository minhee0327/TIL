N, K = map(int, input().split())
arr = [[0]*2 for _ in range(6)]
ans = 0

for _ in range(N):
    S, Y = map(int, input().split())
    arr[Y-1][S] += 1

for i in range(6):
    for j in range(2):
        if arr[i][j] % K:
            ans += 1
        ans += arr[i][j] // K

print(ans)
