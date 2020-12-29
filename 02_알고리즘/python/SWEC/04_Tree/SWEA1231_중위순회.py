def inorder(n):
    global ans

    if n >= len(tree):
        return

    inorder(2*n)
    ans += tree[n]
    inorder(2*n+1)


for t in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    ans = ''
    for _ in range(N):
        info = list(input().split())
        tree[int(info[0])] = info[1]

    inorder(1)

    print("#{} {}".format(t, ans))
