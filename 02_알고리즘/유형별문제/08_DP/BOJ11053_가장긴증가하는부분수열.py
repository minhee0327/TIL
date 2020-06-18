import sys

A = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
DP = [1] * A

for i in range(1, len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            DP[i] = max(DP[i], DP[j]+1)
        else:
            continue
# print(DP)
print(max(DP))
