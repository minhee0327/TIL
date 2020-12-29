for t in range(1, 1+int(input())):
    N = int(input())
    S1 = N * (N+1) //2
    S2 = N**2
    S3 = N* (N+1)

    print("#{} {} {} {}".format(t, S1, S2, S3))