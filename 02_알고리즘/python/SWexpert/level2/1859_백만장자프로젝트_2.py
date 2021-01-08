
for t in range(1, int(input())+1):
    n = input()
    lst = list(map(int, input().split()))

    chk = lst[-1]
    profit = 0

    for i in range(len(lst)-1, -1, -1):
        if lst[i] >= chk:
            chk = lst[i]
        if lst[i] < chk:
            profit += chk - lst[i]

    print('#{} {}'.format(t, profit))
