lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(1, int(input())+1):
    cnt = [0] * 8
    money = int(input())

    for i in range(8):
        cnt[i] = (money//lst[i])
        money %= lst[i]
    print('#{}'.format(t))
    for i in cnt:
        print(i, end=" ")
    print()
