N = int(input())
A = list(map(int, input().split()))
cnt = 1
ans = 1

for i in range(1, N):
    if A[i] >= A[i-1]:
        cnt += 1
    else:
        cnt = 1
    if ans < cnt:
        ans = cnt

cnt = 1

for i in range(1, N):
    if A[i] <= A[i-1]:
        cnt += 1
    else:
        cnt = 1
    if ans < cnt:
        ans = cnt
print(ans)
