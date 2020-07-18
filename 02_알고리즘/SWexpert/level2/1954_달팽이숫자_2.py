for t in range(1, 1+int(input())):
    N = int(input())
    B = [[0 for i in range(N)]for i in range(N)]
    cnt = N
    r, c, num, dir = 0, -1, 0, 1

    while cnt:
        for i in range(cnt):
            num += 1
            c += dir
            B[r][c] = num

        cnt -= 1

        for i in range(cnt):
            num += 1
            r += dir
            B[r][c] = num

        dir *= -1

    # 출력
    print("#{}".format(t))
    for b in B:
        for i in b:
            print(i, end=" ")
        print()
