for t in range(1, 1+10):
    N = int(input())
    arr = [list(map(str, input().split())) for i in range(N)]

    cnt = 0

    for i in range(N):
        temp = ''
        for j in range(N):
            if arr[j][i] != '0':
                temp += arr[j][i]
        cnt += temp.count('12')

    print("#{} {}".format(t, cnt))
