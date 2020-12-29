for t in range(1, 1+int(input())):
    baksu = input()

    # cur: 현재 박수 치고있는 사람수, goyoung: 고용해야하는 사람수
    cur = [0] * len(baksu)
    goyoung = [0] * len(baksu)

    cur[0] = int(baksu[0])

    for i in range(1, len(baksu)):
        if int(baksu[i]):
            if sum(cur[:i]) >= i:
                cur[i] = int(baksu[i])
            else:
                goyoung[i] = i - (sum(cur[:i]))
                cur[i] = int(baksu[i]) + i - (sum(cur[:i]))

    print("#{} {}".format(t, sum(goyoung)))
