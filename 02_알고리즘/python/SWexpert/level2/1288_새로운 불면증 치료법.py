for t in range(1, 1+int(input())):
    N = int(input())
    total = set()
    cnt = 1

    while True:
        if len(total) == 10:
            break

        temp = N * cnt

        while temp:
            total.add(temp % 10)
            temp //= 10

        cnt += 1
    print("#{} {}".format(t, (cnt-1) * N))
