for t in range(1, 1+int(input())):
    tc, n = map(str, input().split())
    num = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0,
           "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    arr = list(map(str, input().split()))

    for i in arr:
        num[i] += 1

    print("#{}".format(t))
    for k, v in num.items():
        print((k+" ")*v, end=" ")
