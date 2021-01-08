for t in range(1, 1+int(input())):
    A, B = input().split()
    DP = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]

    for i in range(1,len(B)+1):
        for j in range(1,len(A)+1):
            if B[i-1] == A[j-1]:
                DP[i][j] =  DP[i-1][j-1] + 1
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])
    # print(DP)
    print("#{} {}".format(t, DP[-1][-1]))