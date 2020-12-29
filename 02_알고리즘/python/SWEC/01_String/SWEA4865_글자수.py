for t in range(1, 1+int(input())):
    str1 = input()
    str2 = input()
    ans = 0

    for s in str1:
        ans = max(ans, str2.count(s))

    print("#{} {}".format(t, ans))
