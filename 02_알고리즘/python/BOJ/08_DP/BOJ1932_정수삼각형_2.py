n = int(input())
# A[i][j] : i, j까지 도착했을 때 최댓값.
# DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + A[i][j]
A = [[0 for _ in range(n+1)] for i in range(n+1)]
DP = [[0 for _ in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    for j in range(1, i+1):
        A[i][j] = temp[j-1]

for i in range(1, n+1):
    for j in range(1, i+1):
        DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + A[i][j]

print(max(DP[-1]))


'''
[Code Review]
- DP를 안쓴다면, 2의 500승 정도의 경우를 모두 계산을 해야하기때문에 시간과 공간을 많이 차지하게됨.
- DP 사용할때엔 맨 앞에 0을 깔아주는게 좋다.
'''
