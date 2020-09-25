N = int(input())
lst = list(map(int, input().split()))
ans = [1]

for i in range(1, N):
    ans[lst[i]:lst[i]] = [i+1]

ans.reverse()
print(' '.join(map(str, ans)))
