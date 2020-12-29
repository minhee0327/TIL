for t in range(1, 1+int(input())):
    pivot = (11* 24*60) + (11* 60) + 11
    D, H, M = map(int, input().split())
    baram = (D*24*60) + (H*60) + M

    if baram - pivot <0:
        print('#{} {}'.format(t, -1))
    else:
        print('#{} {}'.format(t, baram-pivot))