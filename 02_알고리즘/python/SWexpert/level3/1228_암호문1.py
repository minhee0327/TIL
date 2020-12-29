for t in range(1, 1+10):
    n = int(input())
    ori = list(map(int, input().split()))
    m = int(input())
    mori = list(map(str, input().split('I ')))

    for i in range(1, m+1):
        i_lst = list(map(int, mori[i].split()))
        x, y, s = i_lst[0], i_lst[1], i_lst[2:]

        for j in range(y-1, -1, -1):
            ori.insert(x, s[j])

    print("#{}".format(t), end=" ")
    print(' '.join(map(str, ori[:10])))
