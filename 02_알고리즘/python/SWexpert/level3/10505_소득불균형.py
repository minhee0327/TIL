for t in range(1, 1+int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    avg = sum(arr)//N
    cnt = 0
    for i in arr:
        if i <= avg:
            cnt += 1
    print("#{} {}".format(t, cnt))
