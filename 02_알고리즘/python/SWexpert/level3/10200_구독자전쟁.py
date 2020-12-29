for t in range(1, 1+int(input())):
    n, a, b = map(int, input().split())
    max_v, min_v = 0,  0
    if a+b <= n:
        max_v, min_v = min(a, b), 0
    else:
        max_v, min_v = min(a, b), a+b-n

    print("#{} {} {}".format(t, max_v, min_v))
