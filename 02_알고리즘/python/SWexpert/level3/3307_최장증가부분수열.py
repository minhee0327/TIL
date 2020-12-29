for t in range(1, 1+int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    DP = [1] * N

    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                DP[i] = max(DP[i], DP[j]+1)

    print("#{} {}".format(t, max(DP)))

