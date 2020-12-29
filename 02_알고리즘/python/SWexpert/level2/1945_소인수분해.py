soin = [2, 3, 5, 7, 11]

for t in range(1, int(input())+1):
    n = int(input())
    lst = [0] * 5
    for i in range(5):
        count = 0
        while True:
            if n % soin[i] == 0:
                n //= soin[i]
                count += 1
            else:
                break
        lst[i] = count

    print("#{}".format(t), end=" ")

    for i in lst:
        print(i, end=" ")
    print()
