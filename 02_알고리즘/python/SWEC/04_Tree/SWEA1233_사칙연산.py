def calc(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        if b == 0:
            b = 1
        return a/b


def order(n):
    if len(tree[n]) > 1:
        left_child, right_child = int(tree[n][1]), int(tree[n][2])
        # 자식 노드의 value가 연산자면 계속 더 들어가기
        if tree[left_child][0] in "+-*/":
            order(left_child)
        if tree[right_child][0] in "+-*/":
            order(right_child)
        # 자식이 더이상 연산자가 아닐경우 계산
        tree[n] = [calc(int(tree[left_child][0]), int(
            tree[right_child][0]), tree[n][0])]


for t in range(1, 11):
    node = int(input())
    tree = [0] * (node + 1)

    for _ in range(node):
        temp = list(input().split())
        tree[int(temp[0])] = temp[1:]

    order(1)

    print("#{} {}".format(t, int(tree[1][0])))
