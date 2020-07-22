def findRow(arr):
    for i in arr:
        if len(set(i)) != 9:
            return False
        else:
            continue
    return True


def findCol(arr):
    for i in range(9):
        ck = [0] * 10
        for j in range(9):
            ck[arr[j][i]] = arr[j][i]
        if len(set(ck)) != 10:
            return False
    return True


def findRect(arr):
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            if cycle(i, j, arr):
                continue
            else:
                return False
    return True


def cycle(x, y, arr):
    ck = [0] * 9
    for i in range(9):
        ii = i//3
        j = i % 3
        ck[i] = arr[y+j][x+ii]
    if len(set(ck)) != 9:
        return False
    else:
        return True


for t in range(1, 1+int(input())):
    arr = [list(map(int, input().split())) for i in range(9)]

    if findRow(arr) and findCol(arr) and findRect(arr):
        print("#{} {}".format(t, 1))
    else:
        print("#{} {}".format(t, 0))
