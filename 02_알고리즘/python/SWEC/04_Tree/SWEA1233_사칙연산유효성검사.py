def inorder(n):
    if n >= len(tree):
        return

    inorder(2*n)
    calc.append(tree[n])
    inorder(2*n + 1)


for t in range(1, 11):
    node = int(input())
    tree = [0] * (node + 1)
    calc = []
    ck = 1

    for _ in range(node):
        temp = list(input().split())
        tree[int(temp[0])] = temp[1]

    inorder(1)

    for i in range(len(calc)):
        if i % 2:
            if calc[i] not in '+-*/':
                ck = 0
                break
        else:
            if not calc[i].isdigit():
                ck = 0
                break
    # print(calc)
    print("#{} {}".format(t, ck))
