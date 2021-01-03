A = input()
B = input()

DP = [[0] * (len(B)+1) for _ in range(len(A)+1)]  # 행을 A로, 열을 B로

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] != B[j-1]:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        elif A[i-1] == B[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1

print(DP[len(A)][len(B)])
