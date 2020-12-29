for t in range(1, 1+int(input())):
    str1 = input()
    str2 = input()
    ans = 0
    if str1 in str2:
        ans = 1

    print("#{} {}".format(t, ans))
