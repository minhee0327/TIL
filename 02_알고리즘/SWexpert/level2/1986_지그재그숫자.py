for t in range(1, int(input())+1):
    n = int(input())
    ans = 0
    for i in range(1, n+1):

        if i % 2 == 0:
            ans -= i
        else:
            ans += i
    print("#{} {}".format(t, ans))
