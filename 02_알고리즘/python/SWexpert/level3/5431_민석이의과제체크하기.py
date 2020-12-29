for t in range(1, 1+int(input())):
    N, K = map(int, input().split())
    submission = list(map(int, input().split()))
    q = [i for i in range(1, 1+N)]

    print("#{}".format(t), end=" ")
    for i in q:
        if i not in submission:
            print(i, end=" ")
    print()
