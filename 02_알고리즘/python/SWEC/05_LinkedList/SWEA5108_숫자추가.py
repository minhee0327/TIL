for t in range(1, 1+int(input())):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        x, y = map(int, input().split())
        arr = arr[:x] + [y] + arr[x:]

    print("#{} {}".format(t, arr[L]))
