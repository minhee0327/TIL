from itertools import combinations

people = [int(input()) for _ in range(9)]
nanjan = list(combinations(people, 7))
res = []

for n in nanjan:
    if sum(n) == 100:
        res = list(n)
        break

for i in sorted(res):
    print(i)

'''
[Code Review]
- 가장 먼저 생각난 조합으로 푸는방법.
- 이번에도 거꾸로 생각해보는걸 하지 않고 바로 접근했다는 점이 조금 아쉽다.
- 예전에 사다리문제도 끝지점에서 시작지점으로 갔던 것처럼, 이번에도 총 합에서 안되는 2명을 거르는게 빠를 수 있다는것.
'''
