for t in range(1, 1+int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0

    if N > M:
        for i in range(N-M+1):
            temp = 0
            for j in range(i, M+i):
                temp += A[j]*B[j-i]
            ans = max(ans, temp)

    elif N < M:
        for i in range(M-N+1):
            temp = 0
            for j in range(i, N+i):
                temp += A[j-i]*B[j]
            ans = max(ans, temp)
    else:
        for i in range(N):
            ans += A[i]*B[i]

    print("#{} {}".format(t, ans))
