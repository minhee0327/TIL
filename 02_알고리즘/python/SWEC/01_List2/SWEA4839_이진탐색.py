def binary_search(n):
    cnt = 0
    s, e = 1, P
    while True:
        mid = int((s+e)/2)
        cnt += 1
        if n == mid:
            break
        elif n > mid:
            s = mid
        else:
            e = mid
    return cnt


for t in range(1, 1+int(input())):
    P, A, B = map(int, input().split())

    if binary_search(A) == binary_search(B):
        print("#{} {}".format(t, 0))
    elif binary_search(A) > binary_search(B):
        print("#{} {}".format(t, 'B'))
    else:
        print("#{} {}".format(t, 'A'))
