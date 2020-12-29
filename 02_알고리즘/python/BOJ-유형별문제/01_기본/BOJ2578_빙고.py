def isBingo():
    res = 0
    # 가로 확인
    for i in range(5):
        if bingo[i][0] == bingo[i][1] == bingo[i][2] == bingo[i][3] == bingo[i][4] == 0:
            res += 1
    # 세로 확인
    for i in range(5):
        if bingo[0][i] == bingo[1][i] == bingo[2][i] == bingo[3][i] == bingo[4][i] == 0:
            res += 1
    # 대각선
    if (bingo[0][0] == bingo[1][1] == bingo[2][2] == bingo[3][3] == bingo[4][4] == 0):
        res += 1
    if (bingo[0][4] == bingo[1][3] == bingo[2][2] == bingo[3][1] == bingo[4][0] == 0):
        res += 1

    if res >= 3:
        return True
    return False


def removeBingo(num):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num:
                bingo[i][j] = 0
                return


bingo = [list(map(int, input().split())) for _ in range(5)]
speaker = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        removeBingo(speaker[i][j])

        if i*5 + j+1 >= 12 and isBingo():
            print(i*5 + j + 1)
            exit()
