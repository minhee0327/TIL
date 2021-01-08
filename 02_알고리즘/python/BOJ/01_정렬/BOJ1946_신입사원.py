import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    score = sorted([list((map(int, sys.stdin.readline().split())))
                    for _ in range(N)], key=lambda x: x[0])
    cnt = 1
    min = score[0][1]

    for i in range(1, N):
        if score[i][1] < min:
            min = score[i][1]
            cnt += 1

    print(cnt)

'''
1 4
2 3
3 2
4 1
5 5

1 4
2 5
3 6
4 2
5 7
6 1
7 3
'''
