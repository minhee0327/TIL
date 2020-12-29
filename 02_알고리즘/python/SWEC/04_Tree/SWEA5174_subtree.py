def dfs(n):
    global cnt

    cnt += 1
    for i in tree[n]:
        # print(i, cnt)
        dfs(i)


for t in range(int(input())):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))

    tree = [[] for _ in range(E+2)]

    for i in range(0, E*2, 2):
        x = int(edge[i])
        y = int(edge[i+1])
        tree[x].append(y)

    # print(tree)
    cnt = 0
    dfs(N)

    print("#{} {}".format(t+1, cnt))

'''
- 어려운 문제가 아니였는데, 잘못 접근했던 문제.
- 그림에서 무뱡향 그래프로 표현되어 있어서, 나도 계속 무방향으로 생각해서 답이 안나왔다.
- 혹시 하고 방향그래프로 그려보니까.. 아차 싶었다.

- 방향그래프임을 인지한 다음 시작노드(N)에서 서브트리를 돌면서 지나가는 node 개수 세어주면된다.
'''
