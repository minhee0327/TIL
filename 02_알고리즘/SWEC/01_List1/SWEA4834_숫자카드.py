for t in range(1, 1+int(input())):
    n = int(input())
    card = input()
    lst = [0] * 10

    for i in range(10):
        lst[i] = card.count(str(i))

    print("#{} {} {}".format(t, len(lst) -
                             lst[::-1].index(max(lst))-1, max(lst)))
