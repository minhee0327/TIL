for t in range(1, 1+int(input())):
    n, k = map(int, input().split())
    score = sorted(map(int, input().split()), reverse=True)

    print("#{} {}".format(t, sum(score[:k])))
