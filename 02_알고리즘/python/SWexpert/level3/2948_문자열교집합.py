for t in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    N_arr = set(list(map(str, input().split(' '))))
    M_arr = set(list(map(str, input().split(' '))))

    cnt = len(N_arr & M_arr)

    print("#{} {}".format(t, cnt))
