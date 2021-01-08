from collections import deque

N = int(input())
W = sorted(map(int, input().split()), reverse=True)
M = int(input())
B = sorted(map(int, input().split()), reverse=True)

B = deque(B)

container = []
temp = []
ans = 0

while B or temp:
    if max(B) > max(W):
        print(-1)
        exit(0)
    if not B and len(container) != N:
        container.clear()
        ans += 1
        B.extendleft(reversed(temp))
        temp.clear()
    if len(container) == N:
        container.clear()
        ans += 1
        B.extendleft(reversed(temp))
        temp.clear()
    if W[len(container)] >= B[0]:
        container.append(B.popleft())
    else:
        temp.append(B.popleft())

print(ans+1)
