for t in range(1, 1+int(input())):
    N, num = map(str, input().split(' '))
    ans = ''

    for i in range(int(N)):
        ans += "{:04b}".format(int(num[i], 16))

    print("#{} {}".format(t, ans))
