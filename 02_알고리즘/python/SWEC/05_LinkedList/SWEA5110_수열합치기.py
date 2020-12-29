for t in range(1, 1+int(input())):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    for i in range(M-1):
        temp = list(map(int, input().split()))
        ck = 1
        for i in range(len(lst)):
            if temp[0] < lst[i]:
                ck = 0
                lst[i:i] = temp
                break
        if ck:
            lst += temp

    lst = lst[::-1]
    print("#{} {}".format(t, ' '.join(map(str, lst[:10]))))
