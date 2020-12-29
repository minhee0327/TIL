for t in range(1, 10+1):
    tc = int(input())
    arr = list(map(int, input().split()))

    while arr[-1] != 0:
        for i in range(1, 1+5):
            if arr[0] - i <= 0:
                arr.pop(0)
                arr.append(0)
                break
            arr.append(arr.pop(0)-i)

    print("#{}".format(tc), end=" ")
    print(' '.join(map(str, arr)))
