from itertools import combinations

for t in range(1, 1+int(input())):
    total = [i for i in range(1, 13)]
    N, K = map(int, input().split())
    combi = list(combinations(total, N))

    ans = 0

    for c in combi:
        if sum(c) == K:
            ans += 1

    print("#{} {}".format(t, ans))
