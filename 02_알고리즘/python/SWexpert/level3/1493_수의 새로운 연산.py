for t in range(1, 1+int(input())):
    p, q = map(int, input().split())

    max_v = max(p, q) + 1
    cnt = 0
    px, py, qx, qy = 0, 0, 0, 0

    # a: 대각선 수
    for a in range(2*max_v - 1):
        # j: 열, i: 행 (우측위로 숫자 채워갔음)
        for j in range(max_v):
            i = a - j
            if i >= 0 and i < max_v:
                cnt += 1
                if cnt == p:
                    px, py = i, j
                if cnt == q:
                    qx, qy = i, j
                if px and py and qx and qy:
                    break

    cnt = 0
    for a in range(2*max_v - 1):
        for j in range(max_v):
            i = a - j
            if i >= 0 and i < max_v:
                cnt += 1
                if i == px+qx+2 and j == px+qy+1:
                    print("#{} {}".format(t, cnt + 1))

    # print(arr)
    # print(px, py, qx, qy)
    # print(arr[px+qx+1][py+qy])

'''
1. 시간초과 및 결과값이 이상해서 수정해야함.
'''
