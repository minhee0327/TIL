for t in range(1, 1+10):
    l = int(input())
    board = [input()for i in range(8)]

    ans = 0

    # 가로 검사
    for s in board:
        for j in range(8 - l+1):
            temp = s[j:j+l]
            if temp == temp[::-1]:
                ans += 1
    # 세로검사
    for i in range(8):
        for j in range(8-l+1):
            temp = ''
            for k in range(l):
                temp += board[j+k][i]

            if temp == temp[::-1]:
                ans += 1

    print("#{} {}".format(t, ans))
