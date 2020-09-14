for t in range(1, 1+int(input())):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = -1

    for _ in range(M):
        # i: instruction
        i = list(input().split())
        # print(arr)

        if i[0] == 'I':
            arr[int(i[1]):int(i[1])] = [int(i[2])]
        elif i[0] == 'D':
            arr.pop(int(i[1]))
        elif i[0] == 'C':
            arr[int(i[1])] = int(i[2])

    if L < len(arr):
        ans = arr[L]

    print("#{} {}".format(t, ans))
