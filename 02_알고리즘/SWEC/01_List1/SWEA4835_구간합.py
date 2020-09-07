for t in range(1, 1+int(input())):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    min_v, max_v = 10000 * N, 0

    for i in range(N-M+1):
        if sum(lst[i:i+M]) > max_v:
            max_v = sum(lst[i:i+M])
        if sum(lst[i:i+M]) < min_v:
            min_v = sum(lst[i:i+M])

    print("#{} {}".format(t, max_v - min_v))
