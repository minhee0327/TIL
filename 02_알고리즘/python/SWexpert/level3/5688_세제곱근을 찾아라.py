arr = [i ** 3 for i in range(1000001)]
for t in range(1, 1+int(input())):
    N = int(input())

    for i in range(1, 10000001):
        if N == arr[i]:
            ans = i
            break
        if N < arr[i]:
            ans = -1
            break
    print("#{} {}".format(t, ans))
