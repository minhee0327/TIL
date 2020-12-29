def func(r, c, m, arr):
    ret = 0
    for i in range(m):
        for j in range(m):
            if r+i >= n or c+j >= n:
                continue
            ret += arr[r+i][c+j]
    return ret


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(n)]
    ans = 0

    for r in range(n):
        for c in range(n):
            ans = max(func(r, c, m, arr), ans)

    print("#{} {}".format(t, ans))
