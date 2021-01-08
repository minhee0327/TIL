for t in range(1, 1+int(input())):
    P, Q, R, S, W = map(int, input().split())
    a, b = P * W, 0

    if W <= R:
        b = Q
    else:
        b = Q + S * (W-R)

    print("#{} {}".format(t, min(a, b)))
