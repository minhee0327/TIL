for t in range(1, 1+int(input())):
    arr = sorted(map(int, input().split()))
    print(arr)
    if arr[0] == arr[1]:
        print("#{} {}".format(t, arr[2]))
    elif arr[2] == arr[1]:
        print("#{} {}".format(t, arr[0]))