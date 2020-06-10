n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if arr[i]+arr[j]+arr[k] <= m:
                ans.append(arr[i]+arr[j]+arr[k])

print(max(ans))
