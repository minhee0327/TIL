def binary_searcy(num):
    l, r = 0, N-1
    left, right = 0, 0
    ans = 0

    while True:
        m = (l+r) // 2
        # 찾는 값이 오른쪽일 경우
        if num > A[m]:
            l = m+1
            if right == 1:
                break
            right = 1
            left = 0
        # 찾는 값이 왼쪽일 경우
        elif num < A[m]:
            r = m-1
            if left == 1:
                break
            right = 0
            left = 1
        # 무사히 찾는 값을 찾은 경우
        elif num == A[m]:
            ans = 1
            break
    return ans


for t in range(1, 1+int(input())):
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0

    for i in range(M):
        cnt += binary_searcy(B[i])

    print("#{} {}".format(t, cnt))
