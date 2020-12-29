N = int(input())
A = set(map(int, input().split()))
M = int(input())
q = list(map(int, input().split()))

for i in q:
    if i in A:
        print(1)
    else:
        print(0)

# 주의 in 사용할 때, set 자료구조인지 꼭 확인할 것!
