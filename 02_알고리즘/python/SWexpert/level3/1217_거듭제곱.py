def recursive(n, m, ans):
    if m == 0:
        return ans
    else:
        ans *= n
        return recursive(n, m-1, ans)


for _ in range(10):
    t = int(input())
    n, m = map(int, input().split())

    print("#{} {}".format(t, recursive(n, m, 1)))
