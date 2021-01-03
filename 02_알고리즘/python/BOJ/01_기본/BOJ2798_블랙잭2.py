# 메모리는 덜잡고, 속도는 더 느려짐.
n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if arr[i]+arr[j]+arr[k] <= m:
                result = max(result, arr[i]+arr[j]+arr[k])

print(result)
