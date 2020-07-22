for t in range(1, 1+int(input())):
    # 현재속도, 위치
    c, w = 0, 0
    for n in range(int(input())):
        arr = list(map(int, input().split()))
        if arr[0] == 0:
            w += c
        elif arr[0] == 1:
            c += arr[1]
            w += c
        elif arr[0] == 2:
            if c-arr[1] > 0:
                c -= arr[1]
            else:
                c = 0
            w += c
    print("#{} {}".format(t, w))
