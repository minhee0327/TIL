from itertools import combinations


def isTriplet(p):
    p = list(combinations(p, 3))
    ret = False
    for i in p:
        i = sorted(i)
        if i[0]+1 == i[1] and i[1]+1 == i[2]:
            ret = True
            break
    return ret


def isRun(p):
    p = list(combinations(p, 3))
    ret = False
    for i in p:
        if len(set(i)) == 1:
            ret = True
            break
    return ret


def isBabyGin(p):
    if isRun(p) or isTriplet(p):
        return True
    return False


for t in range(1, 1+int(input())):
    lst = list(map(int, input().split()))
    player1, player2 = [], []

    ans = 0

    for i in range(0, len(lst), 2):
        player1.append(lst[i])
        player2.append(lst[i+1])

        if len(player1) >= 3:
            player1_res = isBabyGin(player1)
            player2_res = isBabyGin(player2)

            if player1_res or player2_res:
                if player1_res:
                    ans = 1
                else:
                    ans = 2
                break

    print("#{} {}".format(t, ans))
