for _ in range(10):
    t = int(input())
    q = input()
    string = input()

    idx, cnt = 0, 0

    while idx < len(string)-len(q):
        if q == string[idx:idx+len(q)]:
            cnt += 1
            idx += len(q)
        else:
            idx += 1

    print("#{} {}".format(t, cnt))
