for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    W = sorted(map(int, input().split()), reverse=True)
    T = sorted(map(int, input().split()), reverse=True)
    move = [0] * N

    ans = 0

    for t in T:
        for i in range(N):
            if W[i] <= t and move[i] == 0:
                move[i] = 1
                ans += W[i]
                break

    print("#{} {}".format(tc, ans))
