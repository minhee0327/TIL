n = int(input())
a = list(map(int, input().split()))
dpp = [1 for i in range(n)]
dpm = [1 for i in range(n)]
dpb = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dpp[i] = max(dpp[i], dpp[j]+1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[i] > a[j]:
            dpm[i] = max(dpm[i], dpm[j]+1)

for i in range(n):
    dpb[i] = dpp[i] + dpm[i] - 1

print(max(dpb))
