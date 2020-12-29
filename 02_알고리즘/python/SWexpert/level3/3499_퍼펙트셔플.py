for t in range(1, 1+ int(input())):
    N = int(input())
    arr = list(input().split())
    DP = [0] * N
    
    if N %2:
        for i in range(N//2):
            DP[i*2] = arr[i]
            DP[i*2+1] = arr[i + N//2+1]
        DP[-1] = arr[N//2]
    else:
        for i in range(N//2):
            DP[i*2] = arr[i]
            DP[i*2+1] = arr[i + N//2]

    print("#{} {}".format(t, ' '.join(DP)))
