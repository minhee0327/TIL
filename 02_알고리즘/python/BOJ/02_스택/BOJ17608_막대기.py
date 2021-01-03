import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

pivot = arr[-1]
cnt = 1
for i in range(N-2, -1, -1):
    if pivot < arr[i]:
        cnt += 1
        pivot = arr[i]

print(cnt)

'''
- 시간초과 => sys.stdin.readline..
'''
