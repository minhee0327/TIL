for t in range(1, 1+int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    print("#{} {}".format(t, max(A)-min(A)))
