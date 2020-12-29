def isDanjo(n):
    n = str(n)
    for i in range(1, len(n)):
        if n[i-1] > n[i]:
            return False
    return True


for t in range(1, 1+int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    ret = -1

    for i in range(N-1):
        for j in range(i+1, N):
            temp = A[i] * A[j]
            if isDanjo(temp):
                ret = max(ret, temp)

    print("#{} {}".format(t, ret))
