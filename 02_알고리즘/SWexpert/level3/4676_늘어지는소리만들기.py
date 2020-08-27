for t in range(1, 1+int(input())):
    S = [''] + list(input())
    H = int(input())
    position = sorted(map(int, input().split()))

    cnt = dict()
    for p in position:
        if p not in cnt.keys():
            cnt[p] = 1
        else:
            cnt[p] += 1

    for k, v in cnt.items():
        S[k] += ('-'*v)

    print("#{} {}".format(t, ''.join(S)))
