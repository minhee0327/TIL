for t in range(1, 1+int(input())):
    N, M = map(int, input().split())
    que = list(map(int, input().split()))

    print("#{} {}".format(t, que[M % N]))
