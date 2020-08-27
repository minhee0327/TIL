for t in range(1, 1 + int(input())):
    s = list(input())
    total_len = 1 + len(s) * 4
    arr = [['.' for _ in range(total_len)] for _ in range(5)]

    for i in range(0, total_len, 2):
        arr[2][i] = '#'

    for i in range(2, total_len, 4):
        arr[0][i] = '#'
        arr[2][i] = s.pop(0)
        arr[4][i] = '#'

    for i in range(1, total_len, 2):
        arr[1][i] = '#'
        arr[3][i] = '#'

    for a in arr:
        print("".join(a))
