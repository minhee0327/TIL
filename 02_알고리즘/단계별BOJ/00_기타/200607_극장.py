n = int(input())
arr = list(map(int, input().split()))
ans = []

ans.append(arr[0])

for i in range(1, len(arr)):
    ans.append(ans[i-1]+arr[i])

print(ans)

max_num = n - max(ans)
min_num = min(ans)*(-1)

print(max_num - min_num)
