for t in range(1, 1 + int(input())):
    N = int(input())
    board = [[0] * (11) for _ in range(11)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                board[i][j] += 1

    ans = 0
    for b in board:
        ans += b.count(2)
    print("#{} {}".format(t, ans))
