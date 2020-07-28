for t in range(1, 1+10):
    n = int(input())
    ori = list(map(str, input().split()))
    m = int(input())
    mori = list(map(str, input().split()))

    idx = 0
    for i in range(m):
        if mori[idx] == 'I':
            x, y = int(mori[idx+1]), int(mori[idx+2])
            for j in range(y+3+idx - 1, 3+idx-1, -1):
                ori.insert(x, mori[j])
            idx += y + 3
        elif mori[idx] == 'D':
            x, y = int(mori[idx+1]), int(mori[idx+2])
            for j in range(y):
                del ori[x]
            idx += 3
        elif mori[idx] == 'A':
            y = int(mori[idx+1])
            for j in range(y):
                ori.append(mori[idx+2+j])
            idx += y+2

    print("#{}".format(t), end=" ")
    print(' '.join(map(str, ori[:10])))
