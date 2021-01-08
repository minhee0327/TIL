for t in range(1 , 1+int(input())):
    N, K = map(int, input().split())
    DP = [[0 for _ in range(K+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        V, C = map(int, input().split())
        for j in range(1,K+1):
            if j >= V:
                DP[i][j] = max(DP[i-1][j-V] + C , DP[i-1][j])
            else:
                DP[i][j] = DP[i-1][j]

    print("#{} {}".format(t, DP[-1][-1]))