for t in range(1, int(input())+1):
    n = int(input())
    arr = [[1]*i for i in range(1, n+1)]

    if n > 2:
        for i in range(1, n):
            for j in range(1, i):
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print('#{}'.format(t))
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
