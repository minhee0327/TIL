def order(n):
    # 왼쪽자식 확인하면서 비어있으면 다시순회, 마지막 지점부터 올라오면서 값합해주기
    if 2*n <= N:
        if lst[2*n] == 0:
            order(n*2)
        lst[n] += lst[2*n]
    # 오른쪽 확인하면서 비어있으면순회
    if 2*n + 1 <= N:
        if lst[2*n+1] == 0:
            order(n*2+1)
        lst[n] += lst[2*n+1]


for t in range(1, 1 + int(input())):
    # N: 노드개수, M: 리프노드개수, L: 출력할 노드번호
    N, M, L = map(int, input().split())
    lst = [0] * (N + 1)

    for _ in range(M):
        x, y = map(int, input().split())
        lst[x] = y

    order(1)
    print("#{} {}".format(t, lst[L]))
