def order(num):
    global cnt
    if num > N:
        return

    order(num*2)
    tree[num] = cnt
    # print(tree, num, cnt)
    cnt += 1
    order(num*2+1)


for t in range(1, 1 + int(input())):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    order(1)

    print("#{} {} {}".format(t, tree[1], tree[N//2]))


'''
- 중위순회
- 노드 내부에 담긴 숫자들을 차례로 읽어보면 중위순회를 하고있음
- 중위순회의 순서는 기본적으로 Left - root - right 를 따름.
'''
