for t in range(1, 1+int(input())):
    N = int(input())
    dumi = [int(input()) for _ in range(N)]

    avg = sum(dumi)//len(dumi)
    # 평균값보다 큰 더미의 경우에만 건초더미에서 평균값 제외한만큼의 값을 계속 더해감
    ans = sum(d - avg for d in dumi if d > avg)
    print("#{} {}".format(t, ans))
