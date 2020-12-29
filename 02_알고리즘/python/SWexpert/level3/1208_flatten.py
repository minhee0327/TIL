for t in range(1, 1+10):
    n = int(input())
    dump = sorted(map(int, input().split()))

    while n != 0:
        dump[0] += 1
        dump[-1] -= 1
        dump.sort()
        #dump = sorted(dump)
        n -= 1

    print("#{} {}".format(t, max(dump)-min(dump)))
