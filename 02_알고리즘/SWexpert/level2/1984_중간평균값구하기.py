for t in range(1, int(input())+1):
    lst = sorted(map(int, input().split()))
    ans = round(sum(lst[1:9])/8)
    print("#{} {}".format(t, ans))
