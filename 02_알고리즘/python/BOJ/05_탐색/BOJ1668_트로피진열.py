N = int(input())
arr = [int(input()) for _ in range(N)]

lc, rc = 1, 1  # left_count, right_count
l_pivot = arr[0]
r_pivot = arr[-1]

for i in range(1, N):
    if l_pivot < arr[i]:
        lc += 1
        l_pivot = arr[i]
    else:
        continue

for j in range(N-2, -1, -1):
    if r_pivot < arr[j]:
        rc += 1
        r_pivot = arr[j]
    else:
        continue

print(lc)
print(rc)
