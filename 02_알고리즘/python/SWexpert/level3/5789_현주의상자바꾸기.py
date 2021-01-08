for t in range(1, 1+int(input())):
    N, Q = map(int, input().split())
    arr = [0 for i in range(N+1)]

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            arr[j] = i

    print("#{} {}".format(t, ' '.join(map(str, arr[1:]))))
