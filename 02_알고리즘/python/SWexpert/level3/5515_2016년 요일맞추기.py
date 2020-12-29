for t in range(1, 1+int(input())):
    m, d = map(int, input().split())
    date = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_date = sum(date[:m]) + d

    ans = 0
    if total_date < 4:
        ans = total_date+3
    else:
        ans = (total_date - 4) % 7

    print("#{} {}".format(t, ans))
