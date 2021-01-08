for t in range(1, 1+int(input())):
    n = float(input())
    ans = ''

    for i in range(1, 14):
        # 나눌값
        div = 1 / (2 ** i)
        # 13번째 자리 over flow
        if i == 13:
            ans = 'overflow'
            break
        # 0.0이 되었으면 값이 다 빠진것 더 돌면서 확인 필요 X
        if n == 0.0:
            break
        # 만약 n-div값이 0보다 크면 다음 자리수 확인하기
        if n - div > 0:
            ans += '1'
            n -= div
        # 0보다 작으면 해당 자리값에서는 뺄 수 없으니까 결과에 0만붙이기
        elif n - div < 0:
            ans += '0'
        # 0이 됬으면 마지막 자리에서 다 빠졌음
        elif n - div == 0:
            ans += '1'
            break

    print("#{} {}".format(t, ans))
