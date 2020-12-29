for t in range(1, 1+int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    DP = [0 for _ in range(N)]
    DP[0] = arr[0]

    for i in range(1, N):
        DP[i] = max(DP[i-1] + arr[i], arr[i])

    print("#{} {}".format(t, max(DP)))
