
N, M = map(int, input().split())

group = dict()

for _ in range(N):
    team = input()
    num = int(input())
    member = []
    for i in range(num):
        member.append(input())
    group[team] = sorted(member)

for _ in range(M):
    q = input()
    kind = int(input())
    for k, v in group.items():
        if kind == 1:
            if q in v:
                print(k)
        elif kind == 0:
            if q == k:
                for i in v:
                    print(i)
